# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.File.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IM import BaseDefine_pb2 as IM_dot_BaseDefine__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rIM.File.proto\x12\x07IM.File\x1a\x13IM.BaseDefine.proto\"d\n\x0eIMFileLoginReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x0f\n\x07task_id\x18\x02 \x02(\t\x12\x30\n\tfile_role\x18\x03 \x02(\x0e\x32\x1d.IM.BaseDefine.ClientFileRole\"6\n\x0eIMFileLoginRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\x12\x0f\n\x07task_id\x18\x02 \x02(\t\"^\n\x0bIMFileState\x12-\n\x05state\x18\x01 \x02(\x0e\x32\x1e.IM.BaseDefine.ClientFileState\x12\x0f\n\x07task_id\x18\x02 \x02(\t\x12\x0f\n\x07user_id\x18\x03 \x02(\r\"\x8d\x01\n\x11IMFilePullDataReq\x12\x0f\n\x07task_id\x18\x01 \x02(\t\x12\x0f\n\x07user_id\x18\x02 \x02(\r\x12\x33\n\ntrans_mode\x18\x03 \x02(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\x12\x0e\n\x06offset\x18\x04 \x02(\r\x12\x11\n\tdata_size\x18\x05 \x02(\r\"m\n\x11IMFilePullDataRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\x12\x0f\n\x07task_id\x18\x02 \x02(\t\x12\x0f\n\x07user_id\x18\x03 \x02(\r\x12\x0e\n\x06offset\x18\x04 \x02(\r\x12\x11\n\tfile_data\x18\x05 \x02(\x0c\"\x90\x01\n\tIMFileReq\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x12\n\nto_user_id\x18\x02 \x02(\r\x12\x11\n\tfile_name\x18\x03 \x02(\t\x12\x11\n\tfile_size\x18\x04 \x02(\r\x12\x33\n\ntrans_mode\x18\x05 \x02(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\"\xd0\x01\n\tIMFileRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\x12\x14\n\x0c\x66rom_user_id\x18\x02 \x02(\r\x12\x12\n\nto_user_id\x18\x03 \x02(\r\x12\x11\n\tfile_name\x18\x04 \x02(\t\x12\x0f\n\x07task_id\x18\x05 \x02(\t\x12+\n\x0cip_addr_list\x18\x06 \x03(\x0b\x32\x15.IM.BaseDefine.IpAddr\x12\x33\n\ntrans_mode\x18\x07 \x02(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\"\xe8\x01\n\x0cIMFileNotify\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x12\n\nto_user_id\x18\x02 \x02(\r\x12\x11\n\tfile_name\x18\x03 \x02(\t\x12\x11\n\tfile_size\x18\x04 \x02(\r\x12\x0f\n\x07task_id\x18\x05 \x02(\t\x12+\n\x0cip_addr_list\x18\x06 \x03(\x0b\x32\x15.IM.BaseDefine.IpAddr\x12\x33\n\ntrans_mode\x18\x07 \x02(\x0e\x32\x1f.IM.BaseDefine.TransferFileType\x12\x15\n\roffline_ready\x18\x08 \x02(\r\";\n\x13IMFileHasOfflineReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xa3\x01\n\x13IMFileHasOfflineRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x39\n\x11offline_file_list\x18\x02 \x03(\x0b\x32\x1e.IM.BaseDefine.OfflineFileInfo\x12+\n\x0cip_addr_list\x18\x03 \x03(\x0b\x32\x15.IM.BaseDefine.IpAddr\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"v\n\x13IMFileAddOfflineReq\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x12\n\nto_user_id\x18\x02 \x02(\r\x12\x0f\n\x07task_id\x18\x03 \x02(\t\x12\x11\n\tfile_name\x18\x04 \x02(\t\x12\x11\n\tfile_size\x18\x05 \x02(\r\"P\n\x13IMFileDelOfflineReq\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x12\n\nto_user_id\x18\x02 \x02(\r\x12\x0f\n\x07task_id\x18\x03 \x02(\tB\x1b\n\x17\x63om.mogujie.tt.protobufH\x03')



_IMFILELOGINREQ = DESCRIPTOR.message_types_by_name['IMFileLoginReq']
_IMFILELOGINRSP = DESCRIPTOR.message_types_by_name['IMFileLoginRsp']
_IMFILESTATE = DESCRIPTOR.message_types_by_name['IMFileState']
_IMFILEPULLDATAREQ = DESCRIPTOR.message_types_by_name['IMFilePullDataReq']
_IMFILEPULLDATARSP = DESCRIPTOR.message_types_by_name['IMFilePullDataRsp']
_IMFILEREQ = DESCRIPTOR.message_types_by_name['IMFileReq']
_IMFILERSP = DESCRIPTOR.message_types_by_name['IMFileRsp']
_IMFILENOTIFY = DESCRIPTOR.message_types_by_name['IMFileNotify']
_IMFILEHASOFFLINEREQ = DESCRIPTOR.message_types_by_name['IMFileHasOfflineReq']
_IMFILEHASOFFLINERSP = DESCRIPTOR.message_types_by_name['IMFileHasOfflineRsp']
_IMFILEADDOFFLINEREQ = DESCRIPTOR.message_types_by_name['IMFileAddOfflineReq']
_IMFILEDELOFFLINEREQ = DESCRIPTOR.message_types_by_name['IMFileDelOfflineReq']
IMFileLoginReq = _reflection.GeneratedProtocolMessageType('IMFileLoginReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILELOGINREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileLoginReq)
  })
_sym_db.RegisterMessage(IMFileLoginReq)

IMFileLoginRsp = _reflection.GeneratedProtocolMessageType('IMFileLoginRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMFILELOGINRSP,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileLoginRsp)
  })
_sym_db.RegisterMessage(IMFileLoginRsp)

IMFileState = _reflection.GeneratedProtocolMessageType('IMFileState', (_message.Message,), {
  'DESCRIPTOR' : _IMFILESTATE,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileState)
  })
_sym_db.RegisterMessage(IMFileState)

IMFilePullDataReq = _reflection.GeneratedProtocolMessageType('IMFilePullDataReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEPULLDATAREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFilePullDataReq)
  })
_sym_db.RegisterMessage(IMFilePullDataReq)

IMFilePullDataRsp = _reflection.GeneratedProtocolMessageType('IMFilePullDataRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEPULLDATARSP,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFilePullDataRsp)
  })
_sym_db.RegisterMessage(IMFilePullDataRsp)

IMFileReq = _reflection.GeneratedProtocolMessageType('IMFileReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileReq)
  })
_sym_db.RegisterMessage(IMFileReq)

IMFileRsp = _reflection.GeneratedProtocolMessageType('IMFileRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMFILERSP,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileRsp)
  })
_sym_db.RegisterMessage(IMFileRsp)

IMFileNotify = _reflection.GeneratedProtocolMessageType('IMFileNotify', (_message.Message,), {
  'DESCRIPTOR' : _IMFILENOTIFY,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileNotify)
  })
_sym_db.RegisterMessage(IMFileNotify)

IMFileHasOfflineReq = _reflection.GeneratedProtocolMessageType('IMFileHasOfflineReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEHASOFFLINEREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileHasOfflineReq)
  })
_sym_db.RegisterMessage(IMFileHasOfflineReq)

IMFileHasOfflineRsp = _reflection.GeneratedProtocolMessageType('IMFileHasOfflineRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEHASOFFLINERSP,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileHasOfflineRsp)
  })
_sym_db.RegisterMessage(IMFileHasOfflineRsp)

IMFileAddOfflineReq = _reflection.GeneratedProtocolMessageType('IMFileAddOfflineReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEADDOFFLINEREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileAddOfflineReq)
  })
_sym_db.RegisterMessage(IMFileAddOfflineReq)

IMFileDelOfflineReq = _reflection.GeneratedProtocolMessageType('IMFileDelOfflineReq', (_message.Message,), {
  'DESCRIPTOR' : _IMFILEDELOFFLINEREQ,
  '__module__' : 'IM.File_pb2'
  # @@protoc_insertion_point(class_scope:IM.File.IMFileDelOfflineReq)
  })
_sym_db.RegisterMessage(IMFileDelOfflineReq)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.mogujie.tt.protobufH\003'
  _IMFILELOGINREQ._serialized_start=47
  _IMFILELOGINREQ._serialized_end=147
  _IMFILELOGINRSP._serialized_start=149
  _IMFILELOGINRSP._serialized_end=203
  _IMFILESTATE._serialized_start=205
  _IMFILESTATE._serialized_end=299
  _IMFILEPULLDATAREQ._serialized_start=302
  _IMFILEPULLDATAREQ._serialized_end=443
  _IMFILEPULLDATARSP._serialized_start=445
  _IMFILEPULLDATARSP._serialized_end=554
  _IMFILEREQ._serialized_start=557
  _IMFILEREQ._serialized_end=701
  _IMFILERSP._serialized_start=704
  _IMFILERSP._serialized_end=912
  _IMFILENOTIFY._serialized_start=915
  _IMFILENOTIFY._serialized_end=1147
  _IMFILEHASOFFLINEREQ._serialized_start=1149
  _IMFILEHASOFFLINEREQ._serialized_end=1208
  _IMFILEHASOFFLINERSP._serialized_start=1211
  _IMFILEHASOFFLINERSP._serialized_end=1374
  _IMFILEADDOFFLINEREQ._serialized_start=1376
  _IMFILEADDOFFLINEREQ._serialized_end=1494
  _IMFILEDELOFFLINEREQ._serialized_start=1496
  _IMFILEDELOFFLINEREQ._serialized_end=1576
# @@protoc_insertion_point(module_scope)
