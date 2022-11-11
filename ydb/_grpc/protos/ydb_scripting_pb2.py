# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_scripting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2
from ydb._grpc.protos import ydb_value_pb2 as protos_dot_ydb__value__pb2
from ydb._grpc.protos import ydb_table_pb2 as protos_dot_ydb__table__pb2
from ydb._grpc.protos import ydb_query_stats_pb2 as protos_dot_ydb__query__stats__pb2
from ydb._grpc.protos import ydb_issue_message_pb2 as protos_dot_ydb__issue__message__pb2
from ydb._grpc.protos import ydb_status_codes_pb2 as protos_dot_ydb__status__codes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/ydb_scripting.proto',
  package='Ydb.Scripting',
  syntax='proto3',
  serialized_options=b'\n\022tech.ydb.scriptingB\017ScriptingProtosZ<github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Scripting\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aprotos/ydb_scripting.proto\x12\rYdb.Scripting\x1a\x1aprotos/ydb_operation.proto\x1a\x16protos/ydb_value.proto\x1a\x16protos/ydb_table.proto\x1a\x1cprotos/ydb_query_stats.proto\x1a\x1eprotos/ydb_issue_message.proto\x1a\x1dprotos/ydb_status_codes.proto\"\xa5\x02\n\x11\x45xecuteYqlRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x0e\n\x06script\x18\x02 \x01(\t\x12\x44\n\nparameters\x18\x03 \x03(\x0b\x32\x30.Ydb.Scripting.ExecuteYqlRequest.ParametersEntry\x12;\n\rcollect_stats\x18\x04 \x01(\x0e\x32$.Ydb.Table.QueryStatsCollection.Mode\x1a\x42\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.Ydb.TypedValue:\x02\x38\x01\"B\n\x12\x45xecuteYqlResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"h\n\x10\x45xecuteYqlResult\x12#\n\x0bresult_sets\x18\x01 \x03(\x0b\x32\x0e.Ydb.ResultSet\x12/\n\x0bquery_stats\x18\x02 \x01(\x0b\x32\x1a.Ydb.TableStats.QueryStats\"\xa7\x01\n\x19\x45xecuteYqlPartialResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.Ydb.StatusIds.StatusCode\x12\'\n\x06issues\x18\x02 \x03(\x0b\x32\x17.Ydb.Issue.IssueMessage\x12\x36\n\x06result\x18\x03 \x01(\x0b\x32&.Ydb.Scripting.ExecuteYqlPartialResult\"\x88\x01\n\x17\x45xecuteYqlPartialResult\x12\x18\n\x10result_set_index\x18\x01 \x01(\r\x12\"\n\nresult_set\x18\x02 \x01(\x0b\x32\x0e.Ydb.ResultSet\x12/\n\x0bquery_stats\x18\x03 \x01(\x0b\x32\x1a.Ydb.TableStats.QueryStats\"\xc9\x01\n\x11\x45xplainYqlRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x0e\n\x06script\x18\x02 \x01(\t\x12\x33\n\x04mode\x18\x03 \x01(\x0e\x32%.Ydb.Scripting.ExplainYqlRequest.Mode\"4\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08VALIDATE\x10\x02\x12\x08\n\x04PLAN\x10\x03\"B\n\x12\x45xplainYqlResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xb3\x01\n\x10\x45xplainYqlResult\x12N\n\x10parameters_types\x18\x01 \x03(\x0b\x32\x34.Ydb.Scripting.ExplainYqlResult.ParametersTypesEntry\x12\x0c\n\x04plan\x18\x02 \x01(\t\x1a\x41\n\x14ParametersTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.Ydb.Type:\x02\x38\x01\x42\x66\n\x12tech.ydb.scriptingB\x0fScriptingProtosZ<github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Scripting\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[protos_dot_ydb__operation__pb2.DESCRIPTOR,protos_dot_ydb__value__pb2.DESCRIPTOR,protos_dot_ydb__table__pb2.DESCRIPTOR,protos_dot_ydb__query__stats__pb2.DESCRIPTOR,protos_dot_ydb__issue__message__pb2.DESCRIPTOR,protos_dot_ydb__status__codes__pb2.DESCRIPTOR,])



_EXPLAINYQLREQUEST_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='Ydb.Scripting.ExplainYqlRequest.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1143,
  serialized_end=1195,
)
_sym_db.RegisterEnumDescriptor(_EXPLAINYQLREQUEST_MODE)


_EXECUTEYQLREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='Ydb.Scripting.ExecuteYqlRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.Scripting.ExecuteYqlRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.Scripting.ExecuteYqlRequest.ParametersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=508,
)

_EXECUTEYQLREQUEST = _descriptor.Descriptor(
  name='ExecuteYqlRequest',
  full_name='Ydb.Scripting.ExecuteYqlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Scripting.ExecuteYqlRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script', full_name='Ydb.Scripting.ExecuteYqlRequest.script', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='Ydb.Scripting.ExecuteYqlRequest.parameters', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collect_stats', full_name='Ydb.Scripting.ExecuteYqlRequest.collect_stats', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTEYQLREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=508,
)


_EXECUTEYQLRESPONSE = _descriptor.Descriptor(
  name='ExecuteYqlResponse',
  full_name='Ydb.Scripting.ExecuteYqlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Scripting.ExecuteYqlResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=510,
  serialized_end=576,
)


_EXECUTEYQLRESULT = _descriptor.Descriptor(
  name='ExecuteYqlResult',
  full_name='Ydb.Scripting.ExecuteYqlResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_sets', full_name='Ydb.Scripting.ExecuteYqlResult.result_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_stats', full_name='Ydb.Scripting.ExecuteYqlResult.query_stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=578,
  serialized_end=682,
)


_EXECUTEYQLPARTIALRESPONSE = _descriptor.Descriptor(
  name='ExecuteYqlPartialResponse',
  full_name='Ydb.Scripting.ExecuteYqlPartialResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Ydb.Scripting.ExecuteYqlPartialResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issues', full_name='Ydb.Scripting.ExecuteYqlPartialResponse.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='Ydb.Scripting.ExecuteYqlPartialResponse.result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=685,
  serialized_end=852,
)


_EXECUTEYQLPARTIALRESULT = _descriptor.Descriptor(
  name='ExecuteYqlPartialResult',
  full_name='Ydb.Scripting.ExecuteYqlPartialResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_set_index', full_name='Ydb.Scripting.ExecuteYqlPartialResult.result_set_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_set', full_name='Ydb.Scripting.ExecuteYqlPartialResult.result_set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_stats', full_name='Ydb.Scripting.ExecuteYqlPartialResult.query_stats', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=855,
  serialized_end=991,
)


_EXPLAINYQLREQUEST = _descriptor.Descriptor(
  name='ExplainYqlRequest',
  full_name='Ydb.Scripting.ExplainYqlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Scripting.ExplainYqlRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script', full_name='Ydb.Scripting.ExplainYqlRequest.script', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='Ydb.Scripting.ExplainYqlRequest.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPLAINYQLREQUEST_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=994,
  serialized_end=1195,
)


_EXPLAINYQLRESPONSE = _descriptor.Descriptor(
  name='ExplainYqlResponse',
  full_name='Ydb.Scripting.ExplainYqlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Scripting.ExplainYqlResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1197,
  serialized_end=1263,
)


_EXPLAINYQLRESULT_PARAMETERSTYPESENTRY = _descriptor.Descriptor(
  name='ParametersTypesEntry',
  full_name='Ydb.Scripting.ExplainYqlResult.ParametersTypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Ydb.Scripting.ExplainYqlResult.ParametersTypesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Ydb.Scripting.ExplainYqlResult.ParametersTypesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1380,
  serialized_end=1445,
)

_EXPLAINYQLRESULT = _descriptor.Descriptor(
  name='ExplainYqlResult',
  full_name='Ydb.Scripting.ExplainYqlResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters_types', full_name='Ydb.Scripting.ExplainYqlResult.parameters_types', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plan', full_name='Ydb.Scripting.ExplainYqlResult.plan', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXPLAINYQLRESULT_PARAMETERSTYPESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1266,
  serialized_end=1445,
)

_EXECUTEYQLREQUEST_PARAMETERSENTRY.fields_by_name['value'].message_type = protos_dot_ydb__value__pb2._TYPEDVALUE
_EXECUTEYQLREQUEST_PARAMETERSENTRY.containing_type = _EXECUTEYQLREQUEST
_EXECUTEYQLREQUEST.fields_by_name['operation_params'].message_type = protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_EXECUTEYQLREQUEST.fields_by_name['parameters'].message_type = _EXECUTEYQLREQUEST_PARAMETERSENTRY
_EXECUTEYQLREQUEST.fields_by_name['collect_stats'].enum_type = protos_dot_ydb__table__pb2._QUERYSTATSCOLLECTION_MODE
_EXECUTEYQLRESPONSE.fields_by_name['operation'].message_type = protos_dot_ydb__operation__pb2._OPERATION
_EXECUTEYQLRESULT.fields_by_name['result_sets'].message_type = protos_dot_ydb__value__pb2._RESULTSET
_EXECUTEYQLRESULT.fields_by_name['query_stats'].message_type = protos_dot_ydb__query__stats__pb2._QUERYSTATS
_EXECUTEYQLPARTIALRESPONSE.fields_by_name['status'].enum_type = protos_dot_ydb__status__codes__pb2._STATUSIDS_STATUSCODE
_EXECUTEYQLPARTIALRESPONSE.fields_by_name['issues'].message_type = protos_dot_ydb__issue__message__pb2._ISSUEMESSAGE
_EXECUTEYQLPARTIALRESPONSE.fields_by_name['result'].message_type = _EXECUTEYQLPARTIALRESULT
_EXECUTEYQLPARTIALRESULT.fields_by_name['result_set'].message_type = protos_dot_ydb__value__pb2._RESULTSET
_EXECUTEYQLPARTIALRESULT.fields_by_name['query_stats'].message_type = protos_dot_ydb__query__stats__pb2._QUERYSTATS
_EXPLAINYQLREQUEST.fields_by_name['operation_params'].message_type = protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_EXPLAINYQLREQUEST.fields_by_name['mode'].enum_type = _EXPLAINYQLREQUEST_MODE
_EXPLAINYQLREQUEST_MODE.containing_type = _EXPLAINYQLREQUEST
_EXPLAINYQLRESPONSE.fields_by_name['operation'].message_type = protos_dot_ydb__operation__pb2._OPERATION
_EXPLAINYQLRESULT_PARAMETERSTYPESENTRY.fields_by_name['value'].message_type = protos_dot_ydb__value__pb2._TYPE
_EXPLAINYQLRESULT_PARAMETERSTYPESENTRY.containing_type = _EXPLAINYQLRESULT
_EXPLAINYQLRESULT.fields_by_name['parameters_types'].message_type = _EXPLAINYQLRESULT_PARAMETERSTYPESENTRY
DESCRIPTOR.message_types_by_name['ExecuteYqlRequest'] = _EXECUTEYQLREQUEST
DESCRIPTOR.message_types_by_name['ExecuteYqlResponse'] = _EXECUTEYQLRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteYqlResult'] = _EXECUTEYQLRESULT
DESCRIPTOR.message_types_by_name['ExecuteYqlPartialResponse'] = _EXECUTEYQLPARTIALRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteYqlPartialResult'] = _EXECUTEYQLPARTIALRESULT
DESCRIPTOR.message_types_by_name['ExplainYqlRequest'] = _EXPLAINYQLREQUEST
DESCRIPTOR.message_types_by_name['ExplainYqlResponse'] = _EXPLAINYQLRESPONSE
DESCRIPTOR.message_types_by_name['ExplainYqlResult'] = _EXPLAINYQLRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteYqlRequest = _reflection.GeneratedProtocolMessageType('ExecuteYqlRequest', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTEYQLREQUEST_PARAMETERSENTRY,
    '__module__' : 'protos.ydb_scripting_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlRequest.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _EXECUTEYQLREQUEST,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlRequest)
  })
_sym_db.RegisterMessage(ExecuteYqlRequest)
_sym_db.RegisterMessage(ExecuteYqlRequest.ParametersEntry)

ExecuteYqlResponse = _reflection.GeneratedProtocolMessageType('ExecuteYqlResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEYQLRESPONSE,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlResponse)
  })
_sym_db.RegisterMessage(ExecuteYqlResponse)

ExecuteYqlResult = _reflection.GeneratedProtocolMessageType('ExecuteYqlResult', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEYQLRESULT,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlResult)
  })
_sym_db.RegisterMessage(ExecuteYqlResult)

ExecuteYqlPartialResponse = _reflection.GeneratedProtocolMessageType('ExecuteYqlPartialResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEYQLPARTIALRESPONSE,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlPartialResponse)
  })
_sym_db.RegisterMessage(ExecuteYqlPartialResponse)

ExecuteYqlPartialResult = _reflection.GeneratedProtocolMessageType('ExecuteYqlPartialResult', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEYQLPARTIALRESULT,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExecuteYqlPartialResult)
  })
_sym_db.RegisterMessage(ExecuteYqlPartialResult)

ExplainYqlRequest = _reflection.GeneratedProtocolMessageType('ExplainYqlRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPLAINYQLREQUEST,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExplainYqlRequest)
  })
_sym_db.RegisterMessage(ExplainYqlRequest)

ExplainYqlResponse = _reflection.GeneratedProtocolMessageType('ExplainYqlResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPLAINYQLRESPONSE,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExplainYqlResponse)
  })
_sym_db.RegisterMessage(ExplainYqlResponse)

ExplainYqlResult = _reflection.GeneratedProtocolMessageType('ExplainYqlResult', (_message.Message,), {

  'ParametersTypesEntry' : _reflection.GeneratedProtocolMessageType('ParametersTypesEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXPLAINYQLRESULT_PARAMETERSTYPESENTRY,
    '__module__' : 'protos.ydb_scripting_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExplainYqlResult.ParametersTypesEntry)
    })
  ,
  'DESCRIPTOR' : _EXPLAINYQLRESULT,
  '__module__' : 'protos.ydb_scripting_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Scripting.ExplainYqlResult)
  })
_sym_db.RegisterMessage(ExplainYqlResult)
_sym_db.RegisterMessage(ExplainYqlResult.ParametersTypesEntry)


DESCRIPTOR._options = None
_EXECUTEYQLREQUEST_PARAMETERSENTRY._options = None
_EXPLAINYQLRESULT_PARAMETERSTYPESENTRY._options = None
# @@protoc_insertion_point(module_scope)
