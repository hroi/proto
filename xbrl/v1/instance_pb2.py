# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbrl/v1/instance.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from types import date_pb2 as types_dot_date__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xbrl/v1/instance.proto',
  package='asdf.xbrl.v1',
  syntax='proto3',
  serialized_options=b'Z\035github.com/hroi/proto/xbrl/v1',
  serialized_pb=b'\n\x16xbrl/v1/instance.proto\x12\x0c\x61sdf.xbrl.v1\x1a\x10types/date.proto\",\n\x06\x45ntity\x12\x0e\n\x06scheme\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\"\x1f\n\x08Instance\x12\x13\n\x0binstance_id\x18\x01 \x01(\x03\"\x8d\x01\n\x07\x43ontext\x12\x12\n\ncontext_id\x18\x01 \x01(\x03\x12\x13\n\x0binstance_id\x18\x02 \x01(\x03\x12$\n\x06\x65ntity\x18\x03 \x01(\x0b\x32\x14.asdf.xbrl.v1.Entity\x12%\n\x06period\x18\x04 \x01(\x0b\x32\x15.asdf.types.Daterange\x12\x0c\n\x04name\x18\x05 \x01(\t\"K\n\x04Unit\x12\x0f\n\x07unit_id\x18\x01 \x01(\x03\x12\x13\n\x0binstance_id\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07measure\x18\x04 \x01(\t\"\xe2\x01\n\x04\x46\x61\x63t\x12\x0f\n\x07\x66\x61\x63t_id\x18\x01 \x01(\x03\x12\x12\n\ncontext_id\x18\x02 \x01(\x03\x12\x0f\n\x07unit_id\x18\x03 \x01(\x03\x12\x12\n\nconcept_id\x18\x04 \x01(\x03\x12\x11\n\x07numeric\x18\x05 \x01(\x02H\x00\x12\x0e\n\x04text\x18\x06 \x01(\tH\x00\x12\x0e\n\x04\x64\x61te\x18\x07 \x01(\tH\x00\x12\x0e\n\x04\x62ool\x18\x08 \x01(\x08H\x00\x12\x11\n\x07\x65num_id\x18\t \x01(\x05H\x00\x12\x0c\n\x04lang\x18\n \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x0b \x01(\x05\x12\x11\n\tprecision\x18\x0c \x01(\x05\x42\x07\n\x05valueB\x1fZ\x1dgithub.com/hroi/proto/xbrl/v1b\x06proto3'
  ,
  dependencies=[types_dot_date__pb2.DESCRIPTOR,])




_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='asdf.xbrl.v1.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheme', full_name='asdf.xbrl.v1.Entity.scheme', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='asdf.xbrl.v1.Entity.identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=102,
)


_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='asdf.xbrl.v1.Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='asdf.xbrl.v1.Instance.instance_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=104,
  serialized_end=135,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='asdf.xbrl.v1.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context_id', full_name='asdf.xbrl.v1.Context.context_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='asdf.xbrl.v1.Context.instance_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity', full_name='asdf.xbrl.v1.Context.entity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='asdf.xbrl.v1.Context.period', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='asdf.xbrl.v1.Context.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=138,
  serialized_end=279,
)


_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='asdf.xbrl.v1.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='asdf.xbrl.v1.Unit.unit_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='asdf.xbrl.v1.Unit.instance_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='asdf.xbrl.v1.Unit.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure', full_name='asdf.xbrl.v1.Unit.measure', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=281,
  serialized_end=356,
)


_FACT = _descriptor.Descriptor(
  name='Fact',
  full_name='asdf.xbrl.v1.Fact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fact_id', full_name='asdf.xbrl.v1.Fact.fact_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context_id', full_name='asdf.xbrl.v1.Fact.context_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='asdf.xbrl.v1.Fact.unit_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concept_id', full_name='asdf.xbrl.v1.Fact.concept_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='asdf.xbrl.v1.Fact.numeric', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='asdf.xbrl.v1.Fact.text', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='asdf.xbrl.v1.Fact.date', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='asdf.xbrl.v1.Fact.bool', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_id', full_name='asdf.xbrl.v1.Fact.enum_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='asdf.xbrl.v1.Fact.lang', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decimals', full_name='asdf.xbrl.v1.Fact.decimals', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precision', full_name='asdf.xbrl.v1.Fact.precision', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='value', full_name='asdf.xbrl.v1.Fact.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=359,
  serialized_end=585,
)

_CONTEXT.fields_by_name['entity'].message_type = _ENTITY
_CONTEXT.fields_by_name['period'].message_type = types_dot_date__pb2._DATERANGE
_FACT.oneofs_by_name['value'].fields.append(
  _FACT.fields_by_name['numeric'])
_FACT.fields_by_name['numeric'].containing_oneof = _FACT.oneofs_by_name['value']
_FACT.oneofs_by_name['value'].fields.append(
  _FACT.fields_by_name['text'])
_FACT.fields_by_name['text'].containing_oneof = _FACT.oneofs_by_name['value']
_FACT.oneofs_by_name['value'].fields.append(
  _FACT.fields_by_name['date'])
_FACT.fields_by_name['date'].containing_oneof = _FACT.oneofs_by_name['value']
_FACT.oneofs_by_name['value'].fields.append(
  _FACT.fields_by_name['bool'])
_FACT.fields_by_name['bool'].containing_oneof = _FACT.oneofs_by_name['value']
_FACT.oneofs_by_name['value'].fields.append(
  _FACT.fields_by_name['enum_id'])
_FACT.fields_by_name['enum_id'].containing_oneof = _FACT.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['Unit'] = _UNIT
DESCRIPTOR.message_types_by_name['Fact'] = _FACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'xbrl.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:asdf.xbrl.v1.Entity)
  })
_sym_db.RegisterMessage(Entity)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCE,
  '__module__' : 'xbrl.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:asdf.xbrl.v1.Instance)
  })
_sym_db.RegisterMessage(Instance)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXT,
  '__module__' : 'xbrl.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:asdf.xbrl.v1.Context)
  })
_sym_db.RegisterMessage(Context)

Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), {
  'DESCRIPTOR' : _UNIT,
  '__module__' : 'xbrl.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:asdf.xbrl.v1.Unit)
  })
_sym_db.RegisterMessage(Unit)

Fact = _reflection.GeneratedProtocolMessageType('Fact', (_message.Message,), {
  'DESCRIPTOR' : _FACT,
  '__module__' : 'xbrl.v1.instance_pb2'
  # @@protoc_insertion_point(class_scope:asdf.xbrl.v1.Fact)
  })
_sym_db.RegisterMessage(Fact)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)