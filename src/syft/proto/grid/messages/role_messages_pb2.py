# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/role_messages.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/grid/messages/role_messages.proto",
    package="syft.grid.messages",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\'proto/grid/messages/role_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\x8b\x01\n\x11\x43reateRoleMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"t\n\x12\x43reateRoleResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x88\x01\n\x0eGetRoleMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"q\n\x0fGetRoleResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8b\x01\n\x11GetAllRoleMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"t\n\x12GetAllRoleResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8b\x01\n\x11SearchRoleMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"t\n\x12SearchRoleResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8b\x01\n\x11UpdateRoleMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"t\n\x12UpdateRoleResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_CREATEROLEMESSAGE = _descriptor.Descriptor(
    name="CreateRoleMessage",
    full_name="syft.grid.messages.CreateRoleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.CreateRoleMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.CreateRoleMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.grid.messages.CreateRoleMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=132,
    serialized_end=271,
)


_CREATEROLERESPONSE = _descriptor.Descriptor(
    name="CreateRoleResponse",
    full_name="syft.grid.messages.CreateRoleResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.CreateRoleResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.CreateRoleResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.grid.messages.CreateRoleResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=273,
    serialized_end=389,
)


_GETROLEMESSAGE = _descriptor.Descriptor(
    name="GetRoleMessage",
    full_name="syft.grid.messages.GetRoleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetRoleMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.GetRoleMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.grid.messages.GetRoleMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=392,
    serialized_end=528,
)


_GETROLERESPONSE = _descriptor.Descriptor(
    name="GetRoleResponse",
    full_name="syft.grid.messages.GetRoleResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetRoleResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.GetRoleResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.grid.messages.GetRoleResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=530,
    serialized_end=643,
)


_GETALLROLEMESSAGE = _descriptor.Descriptor(
    name="GetAllRoleMessage",
    full_name="syft.grid.messages.GetAllRoleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetAllRoleMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.GetAllRoleMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.grid.messages.GetAllRoleMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=646,
    serialized_end=785,
)


_GETALLROLERESPONSE = _descriptor.Descriptor(
    name="GetAllRoleResponse",
    full_name="syft.grid.messages.GetAllRoleResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.GetAllRoleResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.GetAllRoleResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.grid.messages.GetAllRoleResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=787,
    serialized_end=903,
)


_SEARCHROLEMESSAGE = _descriptor.Descriptor(
    name="SearchRoleMessage",
    full_name="syft.grid.messages.SearchRoleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.SearchRoleMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.SearchRoleMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.grid.messages.SearchRoleMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=906,
    serialized_end=1045,
)


_SEARCHROLERESPONSE = _descriptor.Descriptor(
    name="SearchRoleResponse",
    full_name="syft.grid.messages.SearchRoleResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.SearchRoleResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.SearchRoleResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.grid.messages.SearchRoleResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1047,
    serialized_end=1163,
)


_UPDATEROLEMESSAGE = _descriptor.Descriptor(
    name="UpdateRoleMessage",
    full_name="syft.grid.messages.UpdateRoleMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.UpdateRoleMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.UpdateRoleMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.grid.messages.UpdateRoleMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1166,
    serialized_end=1305,
)


_UPDATEROLERESPONSE = _descriptor.Descriptor(
    name="UpdateRoleResponse",
    full_name="syft.grid.messages.UpdateRoleResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.grid.messages.UpdateRoleResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.grid.messages.UpdateRoleResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.grid.messages.UpdateRoleResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1307,
    serialized_end=1423,
)

_CREATEROLEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEROLEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEROLEMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEROLERESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEROLERESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETROLEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETROLEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETROLEMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETROLERESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETROLERESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLROLEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLROLEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLROLEMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLROLERESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLROLERESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHROLEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SEARCHROLEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHROLEMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SEARCHROLERESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SEARCHROLERESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEROLEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_UPDATEROLEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEROLEMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEROLERESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_UPDATEROLERESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["CreateRoleMessage"] = _CREATEROLEMESSAGE
DESCRIPTOR.message_types_by_name["CreateRoleResponse"] = _CREATEROLERESPONSE
DESCRIPTOR.message_types_by_name["GetRoleMessage"] = _GETROLEMESSAGE
DESCRIPTOR.message_types_by_name["GetRoleResponse"] = _GETROLERESPONSE
DESCRIPTOR.message_types_by_name["GetAllRoleMessage"] = _GETALLROLEMESSAGE
DESCRIPTOR.message_types_by_name["GetAllRoleResponse"] = _GETALLROLERESPONSE
DESCRIPTOR.message_types_by_name["SearchRoleMessage"] = _SEARCHROLEMESSAGE
DESCRIPTOR.message_types_by_name["SearchRoleResponse"] = _SEARCHROLERESPONSE
DESCRIPTOR.message_types_by_name["UpdateRoleMessage"] = _UPDATEROLEMESSAGE
DESCRIPTOR.message_types_by_name["UpdateRoleResponse"] = _UPDATEROLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRoleMessage = _reflection.GeneratedProtocolMessageType(
    "CreateRoleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEROLEMESSAGE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateRoleMessage)
    },
)
_sym_db.RegisterMessage(CreateRoleMessage)

CreateRoleResponse = _reflection.GeneratedProtocolMessageType(
    "CreateRoleResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEROLERESPONSE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateRoleResponse)
    },
)
_sym_db.RegisterMessage(CreateRoleResponse)

GetRoleMessage = _reflection.GeneratedProtocolMessageType(
    "GetRoleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROLEMESSAGE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRoleMessage)
    },
)
_sym_db.RegisterMessage(GetRoleMessage)

GetRoleResponse = _reflection.GeneratedProtocolMessageType(
    "GetRoleResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETROLERESPONSE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetRoleResponse)
    },
)
_sym_db.RegisterMessage(GetRoleResponse)

GetAllRoleMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllRoleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLROLEMESSAGE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllRoleMessage)
    },
)
_sym_db.RegisterMessage(GetAllRoleMessage)

GetAllRoleResponse = _reflection.GeneratedProtocolMessageType(
    "GetAllRoleResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLROLERESPONSE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetAllRoleResponse)
    },
)
_sym_db.RegisterMessage(GetAllRoleResponse)

SearchRoleMessage = _reflection.GeneratedProtocolMessageType(
    "SearchRoleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHROLEMESSAGE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchRoleMessage)
    },
)
_sym_db.RegisterMessage(SearchRoleMessage)

SearchRoleResponse = _reflection.GeneratedProtocolMessageType(
    "SearchRoleResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHROLERESPONSE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchRoleResponse)
    },
)
_sym_db.RegisterMessage(SearchRoleResponse)

UpdateRoleMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateRoleMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEROLEMESSAGE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateRoleMessage)
    },
)
_sym_db.RegisterMessage(UpdateRoleMessage)

UpdateRoleResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateRoleResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEROLERESPONSE,
        "__module__": "proto.grid.messages.role_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateRoleResponse)
    },
)
_sym_db.RegisterMessage(UpdateRoleResponse)


# @@protoc_insertion_point(module_scope)
