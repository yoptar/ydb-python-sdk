# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/protos/ydb_rate_limiter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/protos/ydb_rate_limiter.proto',
  package='Ydb.RateLimiter',
  syntax='proto3',
  serialized_pb=_b('\n/kikimr/public/api/protos/ydb_rate_limiter.proto\x12\x0fYdb.RateLimiter\x1a,kikimr/public/api/protos/ydb_operation.proto\"[\n\x17HierarchicalDrrSettings\x12\x1c\n\x14max_units_per_second\x18\x01 \x01(\x01\x12\"\n\x1amax_burst_size_coefficient\x18\x02 \x01(\x01\"o\n\x08Resource\x12\x15\n\rresource_path\x18\x01 \x01(\t\x12\x44\n\x10hierarchical_drr\x18\x02 \x01(\x0b\x32(.Ydb.RateLimiter.HierarchicalDrrSettingsH\x00\x42\x06\n\x04type\"\x9f\x01\n\x15\x43reateResourceRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x1e\n\x16\x63oordination_node_path\x18\x02 \x01(\t\x12+\n\x08resource\x18\x03 \x01(\x0b\x32\x19.Ydb.RateLimiter.Resource\"F\n\x16\x43reateResourceResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x16\n\x14\x43reateResourceResult\"\x9e\x01\n\x14\x41lterResourceRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x1e\n\x16\x63oordination_node_path\x18\x02 \x01(\t\x12+\n\x08resource\x18\x03 \x01(\x0b\x32\x19.Ydb.RateLimiter.Resource\"E\n\x15\x41lterResourceResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x15\n\x13\x41lterResourceResult\"\x87\x01\n\x13\x44ropResourceRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x1e\n\x16\x63oordination_node_path\x18\x02 \x01(\t\x12\x15\n\rresource_path\x18\x03 \x01(\t\"D\n\x14\x44ropResourceResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\x14\n\x12\x44ropResourceResult\"\x9b\x01\n\x14ListResourcesRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x1e\n\x16\x63oordination_node_path\x18\x02 \x01(\t\x12\x15\n\rresource_path\x18\x03 \x01(\t\x12\x11\n\trecursive\x18\x04 \x01(\x08\"E\n\x15ListResourcesResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"-\n\x13ListResourcesResult\x12\x16\n\x0eresource_paths\x18\x01 \x03(\t\"\x8b\x01\n\x17\x44\x65scribeResourceRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x1e\n\x16\x63oordination_node_path\x18\x02 \x01(\t\x12\x15\n\rresource_path\x18\x03 \x01(\t\"H\n\x18\x44\x65scribeResourceResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"E\n\x16\x44\x65scribeResourceResult\x12+\n\x08resource\x18\x01 \x01(\x0b\x32\x19.Ydb.RateLimiter.ResourceB5\n\x1b\x63om.yandex.ydb.rate_limiterB\x11RateLimiterProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,])




_HIERARCHICALDRRSETTINGS = _descriptor.Descriptor(
  name='HierarchicalDrrSettings',
  full_name='Ydb.RateLimiter.HierarchicalDrrSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_units_per_second', full_name='Ydb.RateLimiter.HierarchicalDrrSettings.max_units_per_second', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_burst_size_coefficient', full_name='Ydb.RateLimiter.HierarchicalDrrSettings.max_burst_size_coefficient', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=205,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='Ydb.RateLimiter.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_path', full_name='Ydb.RateLimiter.Resource.resource_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hierarchical_drr', full_name='Ydb.RateLimiter.Resource.hierarchical_drr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='Ydb.RateLimiter.Resource.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=207,
  serialized_end=318,
)


_CREATERESOURCEREQUEST = _descriptor.Descriptor(
  name='CreateResourceRequest',
  full_name='Ydb.RateLimiter.CreateResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.RateLimiter.CreateResourceRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordination_node_path', full_name='Ydb.RateLimiter.CreateResourceRequest.coordination_node_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='Ydb.RateLimiter.CreateResourceRequest.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=480,
)


_CREATERESOURCERESPONSE = _descriptor.Descriptor(
  name='CreateResourceResponse',
  full_name='Ydb.RateLimiter.CreateResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.RateLimiter.CreateResourceResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=552,
)


_CREATERESOURCERESULT = _descriptor.Descriptor(
  name='CreateResourceResult',
  full_name='Ydb.RateLimiter.CreateResourceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=576,
)


_ALTERRESOURCEREQUEST = _descriptor.Descriptor(
  name='AlterResourceRequest',
  full_name='Ydb.RateLimiter.AlterResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.RateLimiter.AlterResourceRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordination_node_path', full_name='Ydb.RateLimiter.AlterResourceRequest.coordination_node_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='Ydb.RateLimiter.AlterResourceRequest.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=737,
)


_ALTERRESOURCERESPONSE = _descriptor.Descriptor(
  name='AlterResourceResponse',
  full_name='Ydb.RateLimiter.AlterResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.RateLimiter.AlterResourceResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=808,
)


_ALTERRESOURCERESULT = _descriptor.Descriptor(
  name='AlterResourceResult',
  full_name='Ydb.RateLimiter.AlterResourceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=831,
)


_DROPRESOURCEREQUEST = _descriptor.Descriptor(
  name='DropResourceRequest',
  full_name='Ydb.RateLimiter.DropResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.RateLimiter.DropResourceRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordination_node_path', full_name='Ydb.RateLimiter.DropResourceRequest.coordination_node_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_path', full_name='Ydb.RateLimiter.DropResourceRequest.resource_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=969,
)


_DROPRESOURCERESPONSE = _descriptor.Descriptor(
  name='DropResourceResponse',
  full_name='Ydb.RateLimiter.DropResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.RateLimiter.DropResourceResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=971,
  serialized_end=1039,
)


_DROPRESOURCERESULT = _descriptor.Descriptor(
  name='DropResourceResult',
  full_name='Ydb.RateLimiter.DropResourceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1041,
  serialized_end=1061,
)


_LISTRESOURCESREQUEST = _descriptor.Descriptor(
  name='ListResourcesRequest',
  full_name='Ydb.RateLimiter.ListResourcesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.RateLimiter.ListResourcesRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordination_node_path', full_name='Ydb.RateLimiter.ListResourcesRequest.coordination_node_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_path', full_name='Ydb.RateLimiter.ListResourcesRequest.resource_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive', full_name='Ydb.RateLimiter.ListResourcesRequest.recursive', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1064,
  serialized_end=1219,
)


_LISTRESOURCESRESPONSE = _descriptor.Descriptor(
  name='ListResourcesResponse',
  full_name='Ydb.RateLimiter.ListResourcesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.RateLimiter.ListResourcesResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1221,
  serialized_end=1290,
)


_LISTRESOURCESRESULT = _descriptor.Descriptor(
  name='ListResourcesResult',
  full_name='Ydb.RateLimiter.ListResourcesResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_paths', full_name='Ydb.RateLimiter.ListResourcesResult.resource_paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1292,
  serialized_end=1337,
)


_DESCRIBERESOURCEREQUEST = _descriptor.Descriptor(
  name='DescribeResourceRequest',
  full_name='Ydb.RateLimiter.DescribeResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.RateLimiter.DescribeResourceRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordination_node_path', full_name='Ydb.RateLimiter.DescribeResourceRequest.coordination_node_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_path', full_name='Ydb.RateLimiter.DescribeResourceRequest.resource_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1340,
  serialized_end=1479,
)


_DESCRIBERESOURCERESPONSE = _descriptor.Descriptor(
  name='DescribeResourceResponse',
  full_name='Ydb.RateLimiter.DescribeResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.RateLimiter.DescribeResourceResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1481,
  serialized_end=1553,
)


_DESCRIBERESOURCERESULT = _descriptor.Descriptor(
  name='DescribeResourceResult',
  full_name='Ydb.RateLimiter.DescribeResourceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='Ydb.RateLimiter.DescribeResourceResult.resource', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1555,
  serialized_end=1624,
)

_RESOURCE.fields_by_name['hierarchical_drr'].message_type = _HIERARCHICALDRRSETTINGS
_RESOURCE.oneofs_by_name['type'].fields.append(
  _RESOURCE.fields_by_name['hierarchical_drr'])
_RESOURCE.fields_by_name['hierarchical_drr'].containing_oneof = _RESOURCE.oneofs_by_name['type']
_CREATERESOURCEREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_CREATERESOURCEREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_CREATERESOURCERESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_ALTERRESOURCEREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_ALTERRESOURCEREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_ALTERRESOURCERESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_DROPRESOURCEREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_DROPRESOURCERESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_LISTRESOURCESREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_LISTRESOURCESRESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_DESCRIBERESOURCEREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_DESCRIBERESOURCERESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_DESCRIBERESOURCERESULT.fields_by_name['resource'].message_type = _RESOURCE
DESCRIPTOR.message_types_by_name['HierarchicalDrrSettings'] = _HIERARCHICALDRRSETTINGS
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['CreateResourceRequest'] = _CREATERESOURCEREQUEST
DESCRIPTOR.message_types_by_name['CreateResourceResponse'] = _CREATERESOURCERESPONSE
DESCRIPTOR.message_types_by_name['CreateResourceResult'] = _CREATERESOURCERESULT
DESCRIPTOR.message_types_by_name['AlterResourceRequest'] = _ALTERRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['AlterResourceResponse'] = _ALTERRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['AlterResourceResult'] = _ALTERRESOURCERESULT
DESCRIPTOR.message_types_by_name['DropResourceRequest'] = _DROPRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['DropResourceResponse'] = _DROPRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['DropResourceResult'] = _DROPRESOURCERESULT
DESCRIPTOR.message_types_by_name['ListResourcesRequest'] = _LISTRESOURCESREQUEST
DESCRIPTOR.message_types_by_name['ListResourcesResponse'] = _LISTRESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['ListResourcesResult'] = _LISTRESOURCESRESULT
DESCRIPTOR.message_types_by_name['DescribeResourceRequest'] = _DESCRIBERESOURCEREQUEST
DESCRIPTOR.message_types_by_name['DescribeResourceResponse'] = _DESCRIBERESOURCERESPONSE
DESCRIPTOR.message_types_by_name['DescribeResourceResult'] = _DESCRIBERESOURCERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HierarchicalDrrSettings = _reflection.GeneratedProtocolMessageType('HierarchicalDrrSettings', (_message.Message,), dict(
  DESCRIPTOR = _HIERARCHICALDRRSETTINGS,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.HierarchicalDrrSettings)
  ))
_sym_db.RegisterMessage(HierarchicalDrrSettings)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.Resource)
  ))
_sym_db.RegisterMessage(Resource)

CreateResourceRequest = _reflection.GeneratedProtocolMessageType('CreateResourceRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESOURCEREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.CreateResourceRequest)
  ))
_sym_db.RegisterMessage(CreateResourceRequest)

CreateResourceResponse = _reflection.GeneratedProtocolMessageType('CreateResourceResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESOURCERESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.CreateResourceResponse)
  ))
_sym_db.RegisterMessage(CreateResourceResponse)

CreateResourceResult = _reflection.GeneratedProtocolMessageType('CreateResourceResult', (_message.Message,), dict(
  DESCRIPTOR = _CREATERESOURCERESULT,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.CreateResourceResult)
  ))
_sym_db.RegisterMessage(CreateResourceResult)

AlterResourceRequest = _reflection.GeneratedProtocolMessageType('AlterResourceRequest', (_message.Message,), dict(
  DESCRIPTOR = _ALTERRESOURCEREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.AlterResourceRequest)
  ))
_sym_db.RegisterMessage(AlterResourceRequest)

AlterResourceResponse = _reflection.GeneratedProtocolMessageType('AlterResourceResponse', (_message.Message,), dict(
  DESCRIPTOR = _ALTERRESOURCERESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.AlterResourceResponse)
  ))
_sym_db.RegisterMessage(AlterResourceResponse)

AlterResourceResult = _reflection.GeneratedProtocolMessageType('AlterResourceResult', (_message.Message,), dict(
  DESCRIPTOR = _ALTERRESOURCERESULT,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.AlterResourceResult)
  ))
_sym_db.RegisterMessage(AlterResourceResult)

DropResourceRequest = _reflection.GeneratedProtocolMessageType('DropResourceRequest', (_message.Message,), dict(
  DESCRIPTOR = _DROPRESOURCEREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DropResourceRequest)
  ))
_sym_db.RegisterMessage(DropResourceRequest)

DropResourceResponse = _reflection.GeneratedProtocolMessageType('DropResourceResponse', (_message.Message,), dict(
  DESCRIPTOR = _DROPRESOURCERESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DropResourceResponse)
  ))
_sym_db.RegisterMessage(DropResourceResponse)

DropResourceResult = _reflection.GeneratedProtocolMessageType('DropResourceResult', (_message.Message,), dict(
  DESCRIPTOR = _DROPRESOURCERESULT,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DropResourceResult)
  ))
_sym_db.RegisterMessage(DropResourceResult)

ListResourcesRequest = _reflection.GeneratedProtocolMessageType('ListResourcesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESOURCESREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.ListResourcesRequest)
  ))
_sym_db.RegisterMessage(ListResourcesRequest)

ListResourcesResponse = _reflection.GeneratedProtocolMessageType('ListResourcesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESOURCESRESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.ListResourcesResponse)
  ))
_sym_db.RegisterMessage(ListResourcesResponse)

ListResourcesResult = _reflection.GeneratedProtocolMessageType('ListResourcesResult', (_message.Message,), dict(
  DESCRIPTOR = _LISTRESOURCESRESULT,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.ListResourcesResult)
  ))
_sym_db.RegisterMessage(ListResourcesResult)

DescribeResourceRequest = _reflection.GeneratedProtocolMessageType('DescribeResourceRequest', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIBERESOURCEREQUEST,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DescribeResourceRequest)
  ))
_sym_db.RegisterMessage(DescribeResourceRequest)

DescribeResourceResponse = _reflection.GeneratedProtocolMessageType('DescribeResourceResponse', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIBERESOURCERESPONSE,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DescribeResourceResponse)
  ))
_sym_db.RegisterMessage(DescribeResourceResponse)

DescribeResourceResult = _reflection.GeneratedProtocolMessageType('DescribeResourceResult', (_message.Message,), dict(
  DESCRIPTOR = _DESCRIBERESOURCERESULT,
  __module__ = 'kikimr.public.api.protos.ydb_rate_limiter_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.RateLimiter.DescribeResourceResult)
  ))
_sym_db.RegisterMessage(DescribeResourceResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.yandex.ydb.rate_limiterB\021RateLimiterProtosP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
