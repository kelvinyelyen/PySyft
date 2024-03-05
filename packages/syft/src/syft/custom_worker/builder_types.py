# stdlib
from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Any
from typing import Optional

# third party
from pydantic import BaseModel

__all__ = [
    "BuilderBase",
    "ImageBuildResult",
    "ImagePushResult",
    "BUILD_IMAGE_TIMEOUT_SEC",
    "PUSH_IMAGE_TIMEOUT_SEC",
]


BUILD_IMAGE_TIMEOUT_SEC = 30 * 60
PUSH_IMAGE_TIMEOUT_SEC = 10 * 60


class ImageBuildResult(BaseModel):
    image_hash: str
    logs: str


class ImagePushResult(BaseModel):
    logs: str
    exit_code: int


class BuilderBase(ABC):
    @abstractmethod
    def build_image(
        self,
        tag: str,
        dockerfile: Optional[str] = None,
        dockerfile_path: Optional[Path] = None,
        buildargs: Optional[dict] = None,
        **kwargs: Any,
    ) -> ImageBuildResult:
        pass

    @abstractmethod
    def push_image(
        self,
        tag: str,
        username: str,
        password: str,
        registry_url: str,
        **kwargs: Any,
    ) -> ImagePushResult:
        pass
