# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.Login.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IM import BaseDefine_pb2 as IM_dot_BaseDefine__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eIM.Login.proto\x12\x08IM.Login\x1a\x13IM.BaseDefine.proto\"\x0e\n\x0cIMMsgServReq\"q\n\x0cIMMsgServRsp\x12.\n\x0bresult_code\x18\x01 \x02(\x0e\x32\x19.IM.BaseDefine.ResultType\x12\x10\n\x08prior_ip\x18\x02 \x01(\t\x12\x11\n\tbackip_ip\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\r\"\xad\x01\n\nIMLoginReq\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x32\n\ronline_status\x18\x03 \x02(\x0e\x32\x1b.IM.BaseDefine.UserStatType\x12.\n\x0b\x63lient_type\x18\x04 \x02(\x0e\x32\x19.IM.BaseDefine.ClientType\x12\x16\n\x0e\x63lient_version\x18\x05 \x01(\t\"\xc8\x01\n\nIMLoginRes\x12\x13\n\x0bserver_time\x18\x01 \x02(\r\x12.\n\x0bresult_code\x18\x02 \x02(\x0e\x32\x19.IM.BaseDefine.ResultType\x12\x15\n\rresult_string\x18\x03 \x01(\t\x12\x32\n\ronline_status\x18\x04 \x01(\x0e\x32\x1b.IM.BaseDefine.UserStatType\x12*\n\tuser_info\x18\x05 \x01(\x0b\x32\x17.IM.BaseDefine.UserInfo\"\r\n\x0bIMLogoutReq\"\"\n\x0bIMLogoutRsp\x12\x13\n\x0bresult_code\x18\x01 \x02(\r\"Q\n\nIMKickUser\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x32\n\x0bkick_reason\x18\x02 \x02(\x0e\x32\x1d.IM.BaseDefine.KickReasonType\"~\n\x10IMDeviceTokenReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x14\n\x0c\x64\x65vice_token\x18\x02 \x02(\t\x12.\n\x0b\x63lient_type\x18\x03 \x01(\x0e\x32\x19.IM.BaseDefine.ClientType\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"8\n\x10IMDeviceTokenRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"$\n\x11IMKickPCClientReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\"9\n\x11IMKickPCClientRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\"N\n\x0fIMPushShieldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x15\n\rshield_status\x18\x02 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"c\n\x0fIMPushShieldRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x15\n\rshield_status\x18\x03 \x01(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"<\n\x14IMQueryPushShieldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"h\n\x14IMQueryPushShieldRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x15\n\rshield_status\x18\x03 \x01(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x90\x01\n\x0bIMRegistReq\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x0b\n\x03sex\x18\x03 \x01(\r\x12\x0c\n\x04nick\x18\x04 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x05 \x01(\t\x12\r\n\x05phone\x18\x06 \x01(\t\x12\r\n\x05\x65mail\x18\x07 \x01(\t\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x8d\x01\n\x0bIMRegistRes\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12.\n\x0bresult_code\x18\x02 \x02(\x0e\x32\x19.IM.BaseDefine.ResultType\x12\x15\n\rresult_string\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\x42\x1b\n\x17\x63om.mogujie.tt.protobufH\x03')



_IMMSGSERVREQ = DESCRIPTOR.message_types_by_name['IMMsgServReq']
_IMMSGSERVRSP = DESCRIPTOR.message_types_by_name['IMMsgServRsp']
_IMLOGINREQ = DESCRIPTOR.message_types_by_name['IMLoginReq']
_IMLOGINRES = DESCRIPTOR.message_types_by_name['IMLoginRes']
_IMLOGOUTREQ = DESCRIPTOR.message_types_by_name['IMLogoutReq']
_IMLOGOUTRSP = DESCRIPTOR.message_types_by_name['IMLogoutRsp']
_IMKICKUSER = DESCRIPTOR.message_types_by_name['IMKickUser']
_IMDEVICETOKENREQ = DESCRIPTOR.message_types_by_name['IMDeviceTokenReq']
_IMDEVICETOKENRSP = DESCRIPTOR.message_types_by_name['IMDeviceTokenRsp']
_IMKICKPCCLIENTREQ = DESCRIPTOR.message_types_by_name['IMKickPCClientReq']
_IMKICKPCCLIENTRSP = DESCRIPTOR.message_types_by_name['IMKickPCClientRsp']
_IMPUSHSHIELDREQ = DESCRIPTOR.message_types_by_name['IMPushShieldReq']
_IMPUSHSHIELDRSP = DESCRIPTOR.message_types_by_name['IMPushShieldRsp']
_IMQUERYPUSHSHIELDREQ = DESCRIPTOR.message_types_by_name['IMQueryPushShieldReq']
_IMQUERYPUSHSHIELDRSP = DESCRIPTOR.message_types_by_name['IMQueryPushShieldRsp']
_IMREGISTREQ = DESCRIPTOR.message_types_by_name['IMRegistReq']
_IMREGISTRES = DESCRIPTOR.message_types_by_name['IMRegistRes']
IMMsgServReq = _reflection.GeneratedProtocolMessageType('IMMsgServReq', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGSERVREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMMsgServReq)
  })
_sym_db.RegisterMessage(IMMsgServReq)

IMMsgServRsp = _reflection.GeneratedProtocolMessageType('IMMsgServRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMMSGSERVRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMMsgServRsp)
  })
_sym_db.RegisterMessage(IMMsgServRsp)

IMLoginReq = _reflection.GeneratedProtocolMessageType('IMLoginReq', (_message.Message,), {
  'DESCRIPTOR' : _IMLOGINREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLoginReq)
  })
_sym_db.RegisterMessage(IMLoginReq)

IMLoginRes = _reflection.GeneratedProtocolMessageType('IMLoginRes', (_message.Message,), {
  'DESCRIPTOR' : _IMLOGINRES,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLoginRes)
  })
_sym_db.RegisterMessage(IMLoginRes)

IMLogoutReq = _reflection.GeneratedProtocolMessageType('IMLogoutReq', (_message.Message,), {
  'DESCRIPTOR' : _IMLOGOUTREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLogoutReq)
  })
_sym_db.RegisterMessage(IMLogoutReq)

IMLogoutRsp = _reflection.GeneratedProtocolMessageType('IMLogoutRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMLOGOUTRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMLogoutRsp)
  })
_sym_db.RegisterMessage(IMLogoutRsp)

IMKickUser = _reflection.GeneratedProtocolMessageType('IMKickUser', (_message.Message,), {
  'DESCRIPTOR' : _IMKICKUSER,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickUser)
  })
_sym_db.RegisterMessage(IMKickUser)

IMDeviceTokenReq = _reflection.GeneratedProtocolMessageType('IMDeviceTokenReq', (_message.Message,), {
  'DESCRIPTOR' : _IMDEVICETOKENREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMDeviceTokenReq)
  })
_sym_db.RegisterMessage(IMDeviceTokenReq)

IMDeviceTokenRsp = _reflection.GeneratedProtocolMessageType('IMDeviceTokenRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMDEVICETOKENRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMDeviceTokenRsp)
  })
_sym_db.RegisterMessage(IMDeviceTokenRsp)

IMKickPCClientReq = _reflection.GeneratedProtocolMessageType('IMKickPCClientReq', (_message.Message,), {
  'DESCRIPTOR' : _IMKICKPCCLIENTREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickPCClientReq)
  })
_sym_db.RegisterMessage(IMKickPCClientReq)

IMKickPCClientRsp = _reflection.GeneratedProtocolMessageType('IMKickPCClientRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMKICKPCCLIENTRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMKickPCClientRsp)
  })
_sym_db.RegisterMessage(IMKickPCClientRsp)

IMPushShieldReq = _reflection.GeneratedProtocolMessageType('IMPushShieldReq', (_message.Message,), {
  'DESCRIPTOR' : _IMPUSHSHIELDREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMPushShieldReq)
  })
_sym_db.RegisterMessage(IMPushShieldReq)

IMPushShieldRsp = _reflection.GeneratedProtocolMessageType('IMPushShieldRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMPUSHSHIELDRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMPushShieldRsp)
  })
_sym_db.RegisterMessage(IMPushShieldRsp)

IMQueryPushShieldReq = _reflection.GeneratedProtocolMessageType('IMQueryPushShieldReq', (_message.Message,), {
  'DESCRIPTOR' : _IMQUERYPUSHSHIELDREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMQueryPushShieldReq)
  })
_sym_db.RegisterMessage(IMQueryPushShieldReq)

IMQueryPushShieldRsp = _reflection.GeneratedProtocolMessageType('IMQueryPushShieldRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMQUERYPUSHSHIELDRSP,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMQueryPushShieldRsp)
  })
_sym_db.RegisterMessage(IMQueryPushShieldRsp)

IMRegistReq = _reflection.GeneratedProtocolMessageType('IMRegistReq', (_message.Message,), {
  'DESCRIPTOR' : _IMREGISTREQ,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMRegistReq)
  })
_sym_db.RegisterMessage(IMRegistReq)

IMRegistRes = _reflection.GeneratedProtocolMessageType('IMRegistRes', (_message.Message,), {
  'DESCRIPTOR' : _IMREGISTRES,
  '__module__' : 'IM.Login_pb2'
  # @@protoc_insertion_point(class_scope:IM.Login.IMRegistRes)
  })
_sym_db.RegisterMessage(IMRegistRes)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.mogujie.tt.protobufH\003'
  _IMMSGSERVREQ._serialized_start=49
  _IMMSGSERVREQ._serialized_end=63
  _IMMSGSERVRSP._serialized_start=65
  _IMMSGSERVRSP._serialized_end=178
  _IMLOGINREQ._serialized_start=181
  _IMLOGINREQ._serialized_end=354
  _IMLOGINRES._serialized_start=357
  _IMLOGINRES._serialized_end=557
  _IMLOGOUTREQ._serialized_start=559
  _IMLOGOUTREQ._serialized_end=572
  _IMLOGOUTRSP._serialized_start=574
  _IMLOGOUTRSP._serialized_end=608
  _IMKICKUSER._serialized_start=610
  _IMKICKUSER._serialized_end=691
  _IMDEVICETOKENREQ._serialized_start=693
  _IMDEVICETOKENREQ._serialized_end=819
  _IMDEVICETOKENRSP._serialized_start=821
  _IMDEVICETOKENRSP._serialized_end=877
  _IMKICKPCCLIENTREQ._serialized_start=879
  _IMKICKPCCLIENTREQ._serialized_end=915
  _IMKICKPCCLIENTRSP._serialized_start=917
  _IMKICKPCCLIENTRSP._serialized_end=974
  _IMPUSHSHIELDREQ._serialized_start=976
  _IMPUSHSHIELDREQ._serialized_end=1054
  _IMPUSHSHIELDRSP._serialized_start=1056
  _IMPUSHSHIELDRSP._serialized_end=1155
  _IMQUERYPUSHSHIELDREQ._serialized_start=1157
  _IMQUERYPUSHSHIELDREQ._serialized_end=1217
  _IMQUERYPUSHSHIELDRSP._serialized_start=1219
  _IMQUERYPUSHSHIELDRSP._serialized_end=1323
  _IMREGISTREQ._serialized_start=1326
  _IMREGISTREQ._serialized_end=1470
  _IMREGISTRES._serialized_start=1473
  _IMREGISTRES._serialized_end=1614
# @@protoc_insertion_point(module_scope)
