# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/annotations/validation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/annotations/validation.proto',
  package='Ydb',
  syntax='proto3',
  serialized_options=b'\n\010tech.ydbZ2github.com/ydb-platform/ydb-go-genproto/protos/Ydb\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#protos/annotations/validation.proto\x12\x03Ydb\x1a google/protobuf/descriptor.proto\"\x9b\x01\n\x05Limit\x12!\n\x05range\x18\x01 \x01(\x0b\x32\x10.Ydb.Limit.RangeH\x00\x12\x0c\n\x02lt\x18\x02 \x01(\rH\x00\x12\x0c\n\x02le\x18\x03 \x01(\rH\x00\x12\x0c\n\x02\x65q\x18\x04 \x01(\rH\x00\x12\x0c\n\x02ge\x18\x05 \x01(\rH\x00\x12\x0c\n\x02gt\x18\x06 \x01(\rH\x00\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\r\x12\x0b\n\x03max\x18\x02 \x01(\rB\x06\n\x04kind\"3\n\x06MapKey\x12\x1a\n\x06length\x18\x01 \x01(\x0b\x32\n.Ydb.Limit\x12\r\n\x05value\x18\x02 \x01(\t:1\n\x08required\x12\x1d.google.protobuf.FieldOptions\x18\xe2\xac\x05 \x01(\x08:9\n\x04size\x12\x1d.google.protobuf.FieldOptions\x18\xe3\xac\x05 \x01(\x0b\x32\n.Ydb.Limit:;\n\x06length\x12\x1d.google.protobuf.FieldOptions\x18\xe4\xac\x05 \x01(\x0b\x32\n.Ydb.Limit:=\n\x07map_key\x12\x1d.google.protobuf.FieldOptions\x18\xe5\xac\x05 \x01(\x0b\x32\x0b.Ydb.MapKey:.\n\x05value\x12\x1d.google.protobuf.FieldOptions\x18\xe6\xac\x05 \x01(\tBA\n\x08tech.ydbZ2github.com/ydb-platform/ydb-go-genproto/protos/Ydb\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


REQUIRED_FIELD_NUMBER = 87650
required = _descriptor.FieldDescriptor(
  name='required', full_name='Ydb.required', index=0,
  number=87650, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SIZE_FIELD_NUMBER = 87651
size = _descriptor.FieldDescriptor(
  name='size', full_name='Ydb.size', index=1,
  number=87651, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
LENGTH_FIELD_NUMBER = 87652
length = _descriptor.FieldDescriptor(
  name='length', full_name='Ydb.length', index=2,
  number=87652, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
MAP_KEY_FIELD_NUMBER = 87653
map_key = _descriptor.FieldDescriptor(
  name='map_key', full_name='Ydb.map_key', index=3,
  number=87653, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
VALUE_FIELD_NUMBER = 87654
value = _descriptor.FieldDescriptor(
  name='value', full_name='Ydb.value', index=4,
  number=87654, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_LIMIT_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='Ydb.Limit.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='Ydb.Limit.Range.min', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max', full_name='Ydb.Limit.Range.max', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=226,
)

_LIMIT = _descriptor.Descriptor(
  name='Limit',
  full_name='Ydb.Limit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='Ydb.Limit.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lt', full_name='Ydb.Limit.lt', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='le', full_name='Ydb.Limit.le', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eq', full_name='Ydb.Limit.eq', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ge', full_name='Ydb.Limit.ge', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gt', full_name='Ydb.Limit.gt', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LIMIT_RANGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='Ydb.Limit.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=79,
  serialized_end=234,
)


_MAPKEY = _descriptor.Descriptor(
  name='MapKey',
  full_name='Ydb.MapKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='Ydb.MapKey.length', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.MapKey.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=287,
)

_LIMIT_RANGE.containing_type = _LIMIT
_LIMIT.fields_by_name['range'].message_type = _LIMIT_RANGE
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['range'])
_LIMIT.fields_by_name['range'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['lt'])
_LIMIT.fields_by_name['lt'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['le'])
_LIMIT.fields_by_name['le'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['eq'])
_LIMIT.fields_by_name['eq'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['ge'])
_LIMIT.fields_by_name['ge'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_LIMIT.oneofs_by_name['kind'].fields.append(
  _LIMIT.fields_by_name['gt'])
_LIMIT.fields_by_name['gt'].containing_oneof = _LIMIT.oneofs_by_name['kind']
_MAPKEY.fields_by_name['length'].message_type = _LIMIT
DESCRIPTOR.message_types_by_name['Limit'] = _LIMIT
DESCRIPTOR.message_types_by_name['MapKey'] = _MAPKEY
DESCRIPTOR.extensions_by_name['required'] = required
DESCRIPTOR.extensions_by_name['size'] = size
DESCRIPTOR.extensions_by_name['length'] = length
DESCRIPTOR.extensions_by_name['map_key'] = map_key
DESCRIPTOR.extensions_by_name['value'] = value
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Limit = _reflection.GeneratedProtocolMessageType('Limit', (_message.Message,), {

  'Range' : _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {
    'DESCRIPTOR' : _LIMIT_RANGE,
    '__module__' : 'protos.annotations.validation_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Limit.Range)
    })
  ,
  'DESCRIPTOR' : _LIMIT,
  '__module__' : 'protos.annotations.validation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Limit)
  })
_sym_db.RegisterMessage(Limit)
_sym_db.RegisterMessage(Limit.Range)

MapKey = _reflection.GeneratedProtocolMessageType('MapKey', (_message.Message,), {
  'DESCRIPTOR' : _MAPKEY,
  '__module__' : 'protos.annotations.validation_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.MapKey)
  })
_sym_db.RegisterMessage(MapKey)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(required)
size.message_type = _LIMIT
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(size)
length.message_type = _LIMIT
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(length)
map_key.message_type = _MAPKEY
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(map_key)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(value)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
