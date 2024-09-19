# stdlib
import logging
import os
from typing import Any

# relative
from . import trace_decorator
from .. import __version__
from .util import str_to_bool

__all__ = [
    "TRACING_ENABLED",
    "instrument",
    "instrument_fastapi",
    "instrument_botocore",
]

TRACING_ENABLED = str_to_bool(os.environ.get("TRACING", "False"))
logger = logging.getLogger(__name__)


def setup_instrumenter() -> Any:
    if not TRACING_ENABLED:
        return trace_decorator.no_instrument

    try:
        # third party
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
            OTLPSpanExporter,
        )
        from opentelemetry.sdk.resources import OTELResourceDetector
        from opentelemetry.sdk.resources import ProcessResourceDetector
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        # create a resource
        resource = Resource({"syft.version": __version__})
        resource = resource.merge(OTELResourceDetector().detect())
        resource = resource.merge(ProcessResourceDetector().detect())
        logger.debug(f"OTEL resource : {resource.__dict__}")

        # create a trace provider from the resource
        provider = TracerProvider(resource=resource)

        # create a span processor
        otlp_exporter = OTLPSpanExporter()
        span_processor = BatchSpanProcessor(otlp_exporter)
        provider.add_span_processor(span_processor)

        # set the global trace provider
        trace.set_tracer_provider(provider)

        logger.info("Added TracerProvider with BatchSpanProcessor")
        return trace_decorator.instrument
    except Exception as e:
        logger.error("Failed to import opentelemetry", exc_info=e)
        return trace_decorator.no_instrument


def instrument_fastapi(app: Any) -> None:
    if not TRACING_ENABLED:
        return

    try:
        # third party
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

        FastAPIInstrumentor().instrument_app(app)
        logger.info("Added OTEL FastAPIInstrumentor")
    except Exception as e:
        logger.error(f"Failed to load FastAPIInstrumentor. {e}")



def instrument_botocore() -> None:
    if not TRACING_ENABLED:
        return

    try:
        # third party
        from opentelemetry.instrumentation.botocore import BotocoreInstrumentor

        BotocoreInstrumentor().instrument()
        logger.info("Added OTEL BotocoreInstrumentor")
    except Exception as e:
        logger.error(f"Failed to load BotocoreInstrumentor. {e}")


instrument = setup_instrumenter()
