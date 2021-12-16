# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/pb/server_sensors.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server/pb/server_sensors.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eserver/pb/server_sensors.proto\"\x0e\n\x0cno_parameter\"?\n\x15\x62\x61se_operation_result\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\"y\n\x1fnew_sensor_reading_save_request\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\x1b\n\x13reading_location_id\x18\x02 \x01(\t\x12\x15\n\rreading_value\x18\x03 \x01(\x02\x12\x0f\n\x07read_at\x18\x04 \x01(\t\"^\n new_sensor_reading_save_response\x12\x12\n\nreading_id\x18\x01 \x01(\t\x12&\n\x06result\x18\x02 \x01(\x0b\x32\x16.base_operation_result\"\x9f\x02\n\x13sensor_reading_item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tsensor_id\x18\x02 \x01(\t\x12\x1b\n\x13reading_location_id\x18\x03 \x01(\t\x12\x15\n\rreading_value\x18\x04 \x01(\x02\x12\x17\n\x0ftrusted_reading\x18\x05 \x01(\x08\x12\x16\n\x0elocation_known\x18\x06 \x01(\x08\x12\x19\n\x11location_accurate\x18\x07 \x01(\x08\x12\x14\n\x0cis_processed\x18\x08 \x01(\x08\x12\x0f\n\x07read_at\x18\t \x01(\t\x12\x12\n\nupdated_at\x18\n \x01(\t\x12\x13\n\x0breceived_at\x18\x0b \x01(\t\x12\x19\n\x11overall_integrity\x18\x0c \x01(\x02\">\n(sensor_reading_fetch_single_item_request\x12\x12\n\nreading_id\x18\x01 \x01(\t\"w\n)sensor_reading_fetch_single_item_response\x12\"\n\x04item\x18\x01 \x01(\x0b\x32\x14.sensor_reading_item\x12&\n\x06result\x18\x02 \x01(\x0b\x32\x16.base_operation_result\"\x8b\x01\n(sensor_reading_fetch_multi_item_response\x12#\n\x05items\x18\x01 \x03(\x0b\x32\x14.sensor_reading_item\x12\x12\n\nitem_count\x18\x02 \x01(\x01\x12&\n\x06result\x18\x03 \x01(\x0b\x32\x16.base_operation_result2\x9a\x02\n\rSensorService\x12U\n\x0csave_reading\x12 .new_sensor_reading_save_request\x1a!.new_sensor_reading_save_response\"\x00\x12J\n\x0cget_readings\x12\r.no_parameter\x1a).sensor_reading_fetch_multi_item_response\"\x00\x12\x66\n\x0bget_reading\x12).sensor_reading_fetch_single_item_request\x1a*.sensor_reading_fetch_single_item_response\"\x00\x62\x06proto3'
)




_NO_PARAMETER = _descriptor.Descriptor(
  name='no_parameter',
  full_name='no_parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=34,
  serialized_end=48,
)


_BASE_OPERATION_RESULT = _descriptor.Descriptor(
  name='base_operation_result',
  full_name='base_operation_result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='base_operation_result.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='base_operation_result.error_message', index=1,
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
  serialized_start=50,
  serialized_end=113,
)


_NEW_SENSOR_READING_SAVE_REQUEST = _descriptor.Descriptor(
  name='new_sensor_reading_save_request',
  full_name='new_sensor_reading_save_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='new_sensor_reading_save_request.sensor_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reading_location_id', full_name='new_sensor_reading_save_request.reading_location_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reading_value', full_name='new_sensor_reading_save_request.reading_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_at', full_name='new_sensor_reading_save_request.read_at', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=115,
  serialized_end=236,
)


_NEW_SENSOR_READING_SAVE_RESPONSE = _descriptor.Descriptor(
  name='new_sensor_reading_save_response',
  full_name='new_sensor_reading_save_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reading_id', full_name='new_sensor_reading_save_response.reading_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='new_sensor_reading_save_response.result', index=1,
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
  serialized_start=238,
  serialized_end=332,
)


_SENSOR_READING_ITEM = _descriptor.Descriptor(
  name='sensor_reading_item',
  full_name='sensor_reading_item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sensor_reading_item.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='sensor_reading_item.sensor_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reading_location_id', full_name='sensor_reading_item.reading_location_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reading_value', full_name='sensor_reading_item.reading_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trusted_reading', full_name='sensor_reading_item.trusted_reading', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_known', full_name='sensor_reading_item.location_known', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_accurate', full_name='sensor_reading_item.location_accurate', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_processed', full_name='sensor_reading_item.is_processed', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_at', full_name='sensor_reading_item.read_at', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='sensor_reading_item.updated_at', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received_at', full_name='sensor_reading_item.received_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overall_integrity', full_name='sensor_reading_item.overall_integrity', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=335,
  serialized_end=622,
)


_SENSOR_READING_FETCH_SINGLE_ITEM_REQUEST = _descriptor.Descriptor(
  name='sensor_reading_fetch_single_item_request',
  full_name='sensor_reading_fetch_single_item_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reading_id', full_name='sensor_reading_fetch_single_item_request.reading_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=624,
  serialized_end=686,
)


_SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE = _descriptor.Descriptor(
  name='sensor_reading_fetch_single_item_response',
  full_name='sensor_reading_fetch_single_item_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='sensor_reading_fetch_single_item_response.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='sensor_reading_fetch_single_item_response.result', index=1,
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
  serialized_start=688,
  serialized_end=807,
)


_SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE = _descriptor.Descriptor(
  name='sensor_reading_fetch_multi_item_response',
  full_name='sensor_reading_fetch_multi_item_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='sensor_reading_fetch_multi_item_response.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_count', full_name='sensor_reading_fetch_multi_item_response.item_count', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='sensor_reading_fetch_multi_item_response.result', index=2,
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
  serialized_start=810,
  serialized_end=949,
)

_NEW_SENSOR_READING_SAVE_RESPONSE.fields_by_name['result'].message_type = _BASE_OPERATION_RESULT
_SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE.fields_by_name['item'].message_type = _SENSOR_READING_ITEM
_SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE.fields_by_name['result'].message_type = _BASE_OPERATION_RESULT
_SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE.fields_by_name['items'].message_type = _SENSOR_READING_ITEM
_SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE.fields_by_name['result'].message_type = _BASE_OPERATION_RESULT
DESCRIPTOR.message_types_by_name['no_parameter'] = _NO_PARAMETER
DESCRIPTOR.message_types_by_name['base_operation_result'] = _BASE_OPERATION_RESULT
DESCRIPTOR.message_types_by_name['new_sensor_reading_save_request'] = _NEW_SENSOR_READING_SAVE_REQUEST
DESCRIPTOR.message_types_by_name['new_sensor_reading_save_response'] = _NEW_SENSOR_READING_SAVE_RESPONSE
DESCRIPTOR.message_types_by_name['sensor_reading_item'] = _SENSOR_READING_ITEM
DESCRIPTOR.message_types_by_name['sensor_reading_fetch_single_item_request'] = _SENSOR_READING_FETCH_SINGLE_ITEM_REQUEST
DESCRIPTOR.message_types_by_name['sensor_reading_fetch_single_item_response'] = _SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE
DESCRIPTOR.message_types_by_name['sensor_reading_fetch_multi_item_response'] = _SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

no_parameter = _reflection.GeneratedProtocolMessageType('no_parameter', (_message.Message,), {
  'DESCRIPTOR' : _NO_PARAMETER,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:no_parameter)
  })
_sym_db.RegisterMessage(no_parameter)

base_operation_result = _reflection.GeneratedProtocolMessageType('base_operation_result', (_message.Message,), {
  'DESCRIPTOR' : _BASE_OPERATION_RESULT,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:base_operation_result)
  })
_sym_db.RegisterMessage(base_operation_result)

new_sensor_reading_save_request = _reflection.GeneratedProtocolMessageType('new_sensor_reading_save_request', (_message.Message,), {
  'DESCRIPTOR' : _NEW_SENSOR_READING_SAVE_REQUEST,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:new_sensor_reading_save_request)
  })
_sym_db.RegisterMessage(new_sensor_reading_save_request)

new_sensor_reading_save_response = _reflection.GeneratedProtocolMessageType('new_sensor_reading_save_response', (_message.Message,), {
  'DESCRIPTOR' : _NEW_SENSOR_READING_SAVE_RESPONSE,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:new_sensor_reading_save_response)
  })
_sym_db.RegisterMessage(new_sensor_reading_save_response)

sensor_reading_item = _reflection.GeneratedProtocolMessageType('sensor_reading_item', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR_READING_ITEM,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensor_reading_item)
  })
_sym_db.RegisterMessage(sensor_reading_item)

sensor_reading_fetch_single_item_request = _reflection.GeneratedProtocolMessageType('sensor_reading_fetch_single_item_request', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR_READING_FETCH_SINGLE_ITEM_REQUEST,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensor_reading_fetch_single_item_request)
  })
_sym_db.RegisterMessage(sensor_reading_fetch_single_item_request)

sensor_reading_fetch_single_item_response = _reflection.GeneratedProtocolMessageType('sensor_reading_fetch_single_item_response', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensor_reading_fetch_single_item_response)
  })
_sym_db.RegisterMessage(sensor_reading_fetch_single_item_response)

sensor_reading_fetch_multi_item_response = _reflection.GeneratedProtocolMessageType('sensor_reading_fetch_multi_item_response', (_message.Message,), {
  'DESCRIPTOR' : _SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE,
  '__module__' : 'server.pb.server_sensors_pb2'
  # @@protoc_insertion_point(class_scope:sensor_reading_fetch_multi_item_response)
  })
_sym_db.RegisterMessage(sensor_reading_fetch_multi_item_response)



_SENSORSERVICE = _descriptor.ServiceDescriptor(
  name='SensorService',
  full_name='SensorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=952,
  serialized_end=1234,
  methods=[
  _descriptor.MethodDescriptor(
    name='save_reading',
    full_name='SensorService.save_reading',
    index=0,
    containing_service=None,
    input_type=_NEW_SENSOR_READING_SAVE_REQUEST,
    output_type=_NEW_SENSOR_READING_SAVE_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_readings',
    full_name='SensorService.get_readings',
    index=1,
    containing_service=None,
    input_type=_NO_PARAMETER,
    output_type=_SENSOR_READING_FETCH_MULTI_ITEM_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_reading',
    full_name='SensorService.get_reading',
    index=2,
    containing_service=None,
    input_type=_SENSOR_READING_FETCH_SINGLE_ITEM_REQUEST,
    output_type=_SENSOR_READING_FETCH_SINGLE_ITEM_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENSORSERVICE)

DESCRIPTOR.services_by_name['SensorService'] = _SENSORSERVICE

# @@protoc_insertion_point(module_scope)
