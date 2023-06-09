# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.Message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IM import BaseDefine_pb2 as IM_dot_BaseDefine__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10IM.Message.proto\x12\nIM.Message\x1a\x13IM.BaseDefine.proto\"\xae\x01\n\tIMMsgData\x12\x14\n\x0c\x66rom_user_id\x18\x01 \x02(\r\x12\x15\n\rto_session_id\x18\x02 \x02(\r\x12\x0e\n\x06msg_id\x18\x03 \x02(\r\x12\x13\n\x0b\x63reate_time\x18\x04 \x02(\r\x12(\n\x08msg_type\x18\x05 \x02(\x0e\x32\x16.IM.BaseDefine.MsgType\x12\x10\n\x08msg_data\x18\x06 \x02(\x0c\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"u\n\x0cIMMsgDataAck\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x12\n\nsession_id\x18\x02 \x02(\r\x12\x0e\n\x06msg_id\x18\x03 \x02(\r\x12\x30\n\x0csession_type\x18\x04 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\"y\n\x10IMMsgDataReadAck\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x12\n\nsession_id\x18\x02 \x02(\r\x12\x0e\n\x06msg_id\x18\x03 \x02(\r\x12\x30\n\x0csession_type\x18\x04 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\"|\n\x13IMMsgDataReadNotify\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x12\n\nsession_id\x18\x02 \x02(\r\x12\x0e\n\x06msg_id\x18\x03 \x02(\r\x12\x30\n\x0csession_type\x18\x04 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\"\x11\n\x0fIMClientTimeReq\"&\n\x0fIMClientTimeRsp\x12\x13\n\x0bserver_time\x18\x01 \x02(\r\"9\n\x11IMUnreadMsgCntReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x80\x01\n\x11IMUnreadMsgCntRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x11\n\ttotal_cnt\x18\x02 \x02(\r\x12\x32\n\x0funreadinfo_list\x18\x03 \x03(\x0b\x32\x19.IM.BaseDefine.UnreadInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xa4\x01\n\x0fIMGetMsgListReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12\x14\n\x0cmsg_id_begin\x18\x04 \x02(\r\x12\x0f\n\x07msg_cnt\x18\x05 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xbd\x01\n\x0fIMGetMsgListRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12\x14\n\x0cmsg_id_begin\x18\x04 \x02(\r\x12(\n\x08msg_list\x18\x05 \x03(\x0b\x32\x16.IM.BaseDefine.MsgInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x81\x01\n\x13IMGetLatestMsgIdReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x98\x01\n\x13IMGetLatestMsgIdRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12\x15\n\rlatest_msg_id\x18\x04 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x92\x01\n\x0fIMGetMsgByIdReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12\x13\n\x0bmsg_id_list\x18\x04 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xa7\x01\n\x0fIMGetMsgByIdRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x30\n\x0csession_type\x18\x02 \x02(\x0e\x32\x1a.IM.BaseDefine.SessionType\x12\x12\n\nsession_id\x18\x03 \x02(\r\x12(\n\x08msg_list\x18\x04 \x03(\x0b\x32\x16.IM.BaseDefine.MsgInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\x42\x1b\n\x17\x63om.mogujie.tt.protobufH\x03')



_IMMSGDATA = DESCRIPTOR.message_types_by_name['IMMsgData']
_IMMSGDATAACK = DESCRIPTOR.message_types_by_name['IMMsgDataAck']
_IMMSGDATAREADACK = DESCRIPTOR.message_types_by_name['IMMsgDataReadAck']
_IMMSGDATAREADNOTIFY = DESCRIPTOR.message_types_by_name['IMMsgDataReadNotify']
_IMCLIENTTIMEREQ = DESCRIPTOR.message_types_by_name['IMClientTimeReq']
_IMCLIENTTIMERSP = DESCRIPTOR.message_types_by_name['IMClientTimeRsp']
_IMUNREADMSGCNTREQ = DESCRIPTOR.message_types_by_name['IMUnreadMsgCntReq']
_IMUNREADMSGCNTRSP = DESCRIPTOR.message_types_by_name['IMUnreadMsgCntRsp']
_IMGETMSGLISTREQ = DESCRIPTOR.message_types_by_name['IMGetMsgListReq']
_IMGETMSGLISTRSP = DESCRIPTOR.message_types_by_name['IMGetMsgListRsp']
_IMGETLATESTMSGIDREQ = DESCRIPTOR.message_types_by_name['IMGetLatestMsgIdReq']
_IMGETLATESTMSGIDRSP = DESCRIPTOR.message_types_by_name['IMGetLatestMsgIdRsp']
_IMGETMSGBYIDREQ = DESCRIPTOR.message_types_by_name['IMGetMsgByIdReq']
_IMGETMSGBYIDRSP = DESCRIPTOR.message_types_by_name['IMGetMsgByIdRsp']
IMMsgData = _reflection.GeneratedProtocolMessageType('IMMsgData', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGDATA,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMMsgData)
  })
_sym_db.RegisterMessage(IMMsgData)

IMMsgDataAck = _reflection.GeneratedProtocolMessageType('IMMsgDataAck', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGDATAACK,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMMsgDataAck)
  })
_sym_db.RegisterMessage(IMMsgDataAck)

IMMsgDataReadAck = _reflection.GeneratedProtocolMessageType('IMMsgDataReadAck', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGDATAREADACK,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMMsgDataReadAck)
  })
_sym_db.RegisterMessage(IMMsgDataReadAck)

IMMsgDataReadNotify = _reflection.GeneratedProtocolMessageType('IMMsgDataReadNotify', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGDATAREADNOTIFY,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMMsgDataReadNotify)
  })
_sym_db.RegisterMessage(IMMsgDataReadNotify)

IMClientTimeReq = _reflection.GeneratedProtocolMessageType('IMClientTimeReq', (_message.Message,), {
  'DESCRIPTOR' : _IMCLIENTTIMEREQ,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMClientTimeReq)
  })
_sym_db.RegisterMessage(IMClientTimeReq)

IMClientTimeRsp = _reflection.GeneratedProtocolMessageType('IMClientTimeRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMCLIENTTIMERSP,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMClientTimeRsp)
  })
_sym_db.RegisterMessage(IMClientTimeRsp)

IMUnreadMsgCntReq = _reflection.GeneratedProtocolMessageType('IMUnreadMsgCntReq', (_message.Message,), {
  'DESCRIPTOR' : _IMUNREADMSGCNTREQ,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMUnreadMsgCntReq)
  })
_sym_db.RegisterMessage(IMUnreadMsgCntReq)

IMUnreadMsgCntRsp = _reflection.GeneratedProtocolMessageType('IMUnreadMsgCntRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMUNREADMSGCNTRSP,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMUnreadMsgCntRsp)
  })
_sym_db.RegisterMessage(IMUnreadMsgCntRsp)

IMGetMsgListReq = _reflection.GeneratedProtocolMessageType('IMGetMsgListReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGETMSGLISTREQ,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetMsgListReq)
  })
_sym_db.RegisterMessage(IMGetMsgListReq)

IMGetMsgListRsp = _reflection.GeneratedProtocolMessageType('IMGetMsgListRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGETMSGLISTRSP,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetMsgListRsp)
  })
_sym_db.RegisterMessage(IMGetMsgListRsp)

IMGetLatestMsgIdReq = _reflection.GeneratedProtocolMessageType('IMGetLatestMsgIdReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGETLATESTMSGIDREQ,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetLatestMsgIdReq)
  })
_sym_db.RegisterMessage(IMGetLatestMsgIdReq)

IMGetLatestMsgIdRsp = _reflection.GeneratedProtocolMessageType('IMGetLatestMsgIdRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGETLATESTMSGIDRSP,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetLatestMsgIdRsp)
  })
_sym_db.RegisterMessage(IMGetLatestMsgIdRsp)

IMGetMsgByIdReq = _reflection.GeneratedProtocolMessageType('IMGetMsgByIdReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGETMSGBYIDREQ,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetMsgByIdReq)
  })
_sym_db.RegisterMessage(IMGetMsgByIdReq)

IMGetMsgByIdRsp = _reflection.GeneratedProtocolMessageType('IMGetMsgByIdRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGETMSGBYIDRSP,
  '__module__' : 'IM.Message_pb2'
  # @@protoc_insertion_point(class_scope:IM.Message.IMGetMsgByIdRsp)
  })
_sym_db.RegisterMessage(IMGetMsgByIdRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.mogujie.tt.protobufH\003'
  _IMMSGDATA._serialized_start=54
  _IMMSGDATA._serialized_end=228
  _IMMSGDATAACK._serialized_start=230
  _IMMSGDATAACK._serialized_end=347
  _IMMSGDATAREADACK._serialized_start=349
  _IMMSGDATAREADACK._serialized_end=470
  _IMMSGDATAREADNOTIFY._serialized_start=472
  _IMMSGDATAREADNOTIFY._serialized_end=596
  _IMCLIENTTIMEREQ._serialized_start=598
  _IMCLIENTTIMEREQ._serialized_end=615
  _IMCLIENTTIMERSP._serialized_start=617
  _IMCLIENTTIMERSP._serialized_end=655
  _IMUNREADMSGCNTREQ._serialized_start=657
  _IMUNREADMSGCNTREQ._serialized_end=714
  _IMUNREADMSGCNTRSP._serialized_start=717
  _IMUNREADMSGCNTRSP._serialized_end=845
  _IMGETMSGLISTREQ._serialized_start=848
  _IMGETMSGLISTREQ._serialized_end=1012
  _IMGETMSGLISTRSP._serialized_start=1015
  _IMGETMSGLISTRSP._serialized_end=1204
  _IMGETLATESTMSGIDREQ._serialized_start=1207
  _IMGETLATESTMSGIDREQ._serialized_end=1336
  _IMGETLATESTMSGIDRSP._serialized_start=1339
  _IMGETLATESTMSGIDRSP._serialized_end=1491
  _IMGETMSGBYIDREQ._serialized_start=1494
  _IMGETMSGBYIDREQ._serialized_end=1640
  _IMGETMSGBYIDRSP._serialized_start=1643
  _IMGETMSGBYIDRSP._serialized_end=1810
# @@protoc_insertion_point(module_scope)
