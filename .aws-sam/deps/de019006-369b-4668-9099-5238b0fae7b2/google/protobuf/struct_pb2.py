# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: google/protobuf/struct.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'google/protobuf/struct.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/protobuf/struct.proto\x12\x0fgoogle.protobuf\"\x98\x01\n\x06Struct\x12;\n\x06\x66ields\x18\x01 \x03(\x0b\x32#.google.protobuf.Struct.FieldsEntryR\x06\x66ields\x1aQ\n\x0b\x46ieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\"\xb2\x02\n\x05Value\x12;\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12#\n\x0cnumber_value\x18\x02 \x01(\x01H\x00R\x0bnumberValue\x12#\n\x0cstring_value\x18\x03 \x01(\tH\x00R\x0bstringValue\x12\x1f\n\nbool_value\x18\x04 \x01(\x08H\x00R\tboolValue\x12<\n\x0cstruct_value\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\x0bstructValue\x12;\n\nlist_value\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.ListValueH\x00R\tlistValueB\x06\n\x04kind\";\n\tListValue\x12.\n\x06values\x18\x01 \x03(\x0b\x32\x16.google.protobuf.ValueR\x06values*\x1b\n\tNullValue\x12\x0e\n\nNULL_VALUE\x10\x00\x42\x7f\n\x13\x63om.google.protobufB\x0bStructProtoP\x01Z/google.golang.org/protobuf/types/known/structpb\xf8\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.protobuf.struct_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.google.protobufB\013StructProtoP\001Z/google.golang.org/protobuf/types/known/structpb\370\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'
  _globals['_STRUCT_FIELDSENTRY']._loaded_options = None
  _globals['_STRUCT_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_NULLVALUE']._serialized_start=574
  _globals['_NULLVALUE']._serialized_end=601
  _globals['_STRUCT']._serialized_start=50
  _globals['_STRUCT']._serialized_end=202
  _globals['_STRUCT_FIELDSENTRY']._serialized_start=121
  _globals['_STRUCT_FIELDSENTRY']._serialized_end=202
  _globals['_VALUE']._serialized_start=205
  _globals['_VALUE']._serialized_end=511
  _globals['_LISTVALUE']._serialized_start=513
  _globals['_LISTVALUE']._serialized_end=572
# @@protoc_insertion_point(module_scope)
