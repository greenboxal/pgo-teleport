# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import holoholo_shared_pb2 as holoholo__shared__pb2
import remaining_pb2 as remaining__pb2
holoholo__shared__pb2 = remaining__pb2.holoholo__shared__pb2

from holoholo_shared_pb2 import *
from remaining_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='Holoholo.Rpc',
  syntax='proto3',
  serialized_pb=_b('\n\trpc.proto\x12\x0cHoloholo.Rpc\x1a\x15holoholo_shared.proto\x1a\x0fremaining.proto\"A\n\rMapFieldEntry\x12!\n\x03key\x18\x01 \x01(\x0e\x32\x14.Holoholo.Rpc.Method\x12\r\n\x05value\x18\x02 \x01(\x0c\"6\n\x05Thing\x12\r\n\x05start\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x0c\"\xb5\x03\n\x17RpcRequestEnvelopeProto\x12*\n\tdirection\x18\x01 \x01(\x0e\x32\x17.Holoholo.Rpc.Direction\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12.\n\tparameter\x18\x04 \x03(\x0b\x32\x1b.Holoholo.Rpc.MapFieldEntry\x12\x0e\n\x06\x66ooter\x18\x06 \x01(\x0c\x12\x0b\n\x03lat\x18\x07 \x01(\x01\x12\x0c\n\x04long\x18\x08 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\t \x01(\x01\x12<\n\x04\x61uth\x18\n \x01(\x0b\x32..Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo\x12\"\n\x05thing\x18\x0b \x01(\x0b\x32\x13.Holoholo.Rpc.Thing\x12\x11\n\tunknown12\x18\x0c \x01(\x05\x1ax\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x41\n\x05token\x18\x02 \x01(\x0b\x32\x32.Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.JWT\x1a\x17\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\"\xf9\x02\n\x18RpcResponseEnvelopeProto\x12*\n\tdirection\x18\x01 \x01(\x0e\x32\x17.Holoholo.Rpc.Direction\x12\x13\n\x0bresponse_id\x18\x02 \x01(\x04\x12\x0f\n\x07\x61pi_url\x18\x03 \x01(\t\x12\x0e\n\x06\x66ooter\x18\x06 \x01(\x0c\x12\x41\n\x08unknown7\x18\x07 \x01(\x0b\x32/.Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7\x12\x0b\n\x03lat\x18\x08 \x01(\x01\x12\x0c\n\x04long\x18\t \x01(\x01\x12\x10\n\x08\x61ltitude\x18\n \x01(\x01\x12\"\n\x05thing\x18\x0b \x01(\x0b\x32\x13.Holoholo.Rpc.Thing\x12\x11\n\tunknown12\x18\x0c \x01(\x05\x12\x0f\n\x07returns\x18\x64 \x03(\x0c\x1a\x43\n\x08Unknown7\x12\x11\n\tunknown71\x18\x01 \x01(\x0c\x12\x11\n\tunknown72\x18\x02 \x01(\x03\x12\x11\n\tunknown73\x18\x03 \x01(\x0c*3\n\tDirection\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08RESPONSE\x10\x01\x12\x0b\n\x07REQUEST\x10\x02P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[holoholo__shared__pb2.DESCRIPTOR,remaining__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='Holoholo.Rpc.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1010,
  serialized_end=1061,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
UNKNOWN = 0
RESPONSE = 1
REQUEST = 2



_MAPFIELDENTRY = _descriptor.Descriptor(
  name='MapFieldEntry',
  full_name='Holoholo.Rpc.MapFieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Holoholo.Rpc.MapFieldEntry.key', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Holoholo.Rpc.MapFieldEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=67,
  serialized_end=132,
)


_THING = _descriptor.Descriptor(
  name='Thing',
  full_name='Holoholo.Rpc.Thing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='Holoholo.Rpc.Thing.start', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Holoholo.Rpc.Thing.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='Holoholo.Rpc.Thing.end', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=134,
  serialized_end=188,
)


_RPCREQUESTENVELOPEPROTO_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=605,
  serialized_end=628,
)

_RPCREQUESTENVELOPEPROTO_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RPCREQUESTENVELOPEPROTO_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=628,
)

_RPCREQUESTENVELOPEPROTO = _descriptor.Descriptor(
  name='RpcRequestEnvelopeProto',
  full_name='Holoholo.Rpc.RpcRequestEnvelopeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direction', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.direction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.request_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.parameter', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='footer', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.footer', index=3,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.lat', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.long', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.altitude', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.auth', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thing', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.thing', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='Holoholo.Rpc.RpcRequestEnvelopeProto.unknown12', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RPCREQUESTENVELOPEPROTO_AUTHINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=628,
)


_RPCRESPONSEENVELOPEPROTO_UNKNOWN7 = _descriptor.Descriptor(
  name='Unknown7',
  full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown71', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7.unknown71', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown72', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7.unknown72', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown73', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7.unknown73', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=941,
  serialized_end=1008,
)

_RPCRESPONSEENVELOPEPROTO = _descriptor.Descriptor(
  name='RpcResponseEnvelopeProto',
  full_name='Holoholo.Rpc.RpcResponseEnvelopeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direction', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.direction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_id', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.response_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_url', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.api_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='footer', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.footer', index=3,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown7', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.unknown7', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.lat', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.long', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.altitude', index=7,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thing', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.thing', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.unknown12', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='returns', full_name='Holoholo.Rpc.RpcResponseEnvelopeProto.returns', index=10,
      number=100, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RPCRESPONSEENVELOPEPROTO_UNKNOWN7, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=631,
  serialized_end=1008,
)

_MAPFIELDENTRY.fields_by_name['key'].enum_type = holoholo__shared__pb2._METHOD
_RPCREQUESTENVELOPEPROTO_AUTHINFO_JWT.containing_type = _RPCREQUESTENVELOPEPROTO_AUTHINFO
_RPCREQUESTENVELOPEPROTO_AUTHINFO.fields_by_name['token'].message_type = _RPCREQUESTENVELOPEPROTO_AUTHINFO_JWT
_RPCREQUESTENVELOPEPROTO_AUTHINFO.containing_type = _RPCREQUESTENVELOPEPROTO
_RPCREQUESTENVELOPEPROTO.fields_by_name['direction'].enum_type = _DIRECTION
_RPCREQUESTENVELOPEPROTO.fields_by_name['parameter'].message_type = _MAPFIELDENTRY
_RPCREQUESTENVELOPEPROTO.fields_by_name['auth'].message_type = _RPCREQUESTENVELOPEPROTO_AUTHINFO
_RPCREQUESTENVELOPEPROTO.fields_by_name['thing'].message_type = _THING
_RPCRESPONSEENVELOPEPROTO_UNKNOWN7.containing_type = _RPCRESPONSEENVELOPEPROTO
_RPCRESPONSEENVELOPEPROTO.fields_by_name['direction'].enum_type = _DIRECTION
_RPCRESPONSEENVELOPEPROTO.fields_by_name['unknown7'].message_type = _RPCRESPONSEENVELOPEPROTO_UNKNOWN7
_RPCRESPONSEENVELOPEPROTO.fields_by_name['thing'].message_type = _THING
DESCRIPTOR.message_types_by_name['MapFieldEntry'] = _MAPFIELDENTRY
DESCRIPTOR.message_types_by_name['Thing'] = _THING
DESCRIPTOR.message_types_by_name['RpcRequestEnvelopeProto'] = _RPCREQUESTENVELOPEPROTO
DESCRIPTOR.message_types_by_name['RpcResponseEnvelopeProto'] = _RPCRESPONSEENVELOPEPROTO
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION

MapFieldEntry = _reflection.GeneratedProtocolMessageType('MapFieldEntry', (_message.Message,), dict(
  DESCRIPTOR = _MAPFIELDENTRY,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:Holoholo.Rpc.MapFieldEntry)
  ))
_sym_db.RegisterMessage(MapFieldEntry)

Thing = _reflection.GeneratedProtocolMessageType('Thing', (_message.Message,), dict(
  DESCRIPTOR = _THING,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:Holoholo.Rpc.Thing)
  ))
_sym_db.RegisterMessage(Thing)

RpcRequestEnvelopeProto = _reflection.GeneratedProtocolMessageType('RpcRequestEnvelopeProto', (_message.Message,), dict(

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _RPCREQUESTENVELOPEPROTO_AUTHINFO_JWT,
      __module__ = 'rpc_pb2'
      # @@protoc_insertion_point(class_scope:Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _RPCREQUESTENVELOPEPROTO_AUTHINFO,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:Holoholo.Rpc.RpcRequestEnvelopeProto.AuthInfo)
    ))
  ,
  DESCRIPTOR = _RPCREQUESTENVELOPEPROTO,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:Holoholo.Rpc.RpcRequestEnvelopeProto)
  ))
_sym_db.RegisterMessage(RpcRequestEnvelopeProto)
_sym_db.RegisterMessage(RpcRequestEnvelopeProto.AuthInfo)
_sym_db.RegisterMessage(RpcRequestEnvelopeProto.AuthInfo.JWT)

RpcResponseEnvelopeProto = _reflection.GeneratedProtocolMessageType('RpcResponseEnvelopeProto', (_message.Message,), dict(

  Unknown7 = _reflection.GeneratedProtocolMessageType('Unknown7', (_message.Message,), dict(
    DESCRIPTOR = _RPCRESPONSEENVELOPEPROTO_UNKNOWN7,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:Holoholo.Rpc.RpcResponseEnvelopeProto.Unknown7)
    ))
  ,
  DESCRIPTOR = _RPCRESPONSEENVELOPEPROTO,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:Holoholo.Rpc.RpcResponseEnvelopeProto)
  ))
_sym_db.RegisterMessage(RpcResponseEnvelopeProto)
_sym_db.RegisterMessage(RpcResponseEnvelopeProto.Unknown7)


# @@protoc_insertion_point(module_scope)
