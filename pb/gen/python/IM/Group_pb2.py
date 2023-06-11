# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IM.Group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IM import BaseDefine_pb2 as IM_dot_BaseDefine__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eIM.Group.proto\x12\x08IM.Group\x1a\x13IM.BaseDefine.proto\"<\n\x14IMNormalGroupListReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"y\n\x14IMNormalGroupListRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12;\n\x12group_version_list\x18\x02 \x03(\x0b\x32\x1f.IM.BaseDefine.GroupVersionInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"w\n\x12IMGroupInfoListReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12;\n\x12group_version_list\x18\x02 \x03(\x0b\x32\x1f.IM.BaseDefine.GroupVersionInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"m\n\x12IMGroupInfoListRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x31\n\x0fgroup_info_list\x18\x02 \x03(\x0b\x32\x18.IM.BaseDefine.GroupInfo\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xb8\x01\n\x10IMGroupCreateReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12<\n\ngroup_type\x18\x02 \x02(\x0e\x32\x18.IM.BaseDefine.GroupType:\x0eGROUP_TYPE_TMP\x12\x12\n\ngroup_name\x18\x03 \x02(\t\x12\x14\n\x0cgroup_avatar\x18\x04 \x02(\t\x12\x16\n\x0emember_id_list\x18\x05 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x89\x01\n\x10IMGroupCreateRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x13\n\x0bresult_code\x18\x02 \x02(\r\x12\x10\n\x08group_id\x18\x03 \x01(\r\x12\x12\n\ngroup_name\x18\x04 \x02(\t\x12\x14\n\x0cuser_id_list\x18\x05 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\x9d\x01\n\x16IMGroupChangeMemberReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x33\n\x0b\x63hange_type\x18\x02 \x02(\x0e\x32\x1e.IM.BaseDefine.GroupModifyType\x12\x10\n\x08group_id\x18\x03 \x02(\r\x12\x16\n\x0emember_id_list\x18\x04 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xce\x01\n\x16IMGroupChangeMemberRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x33\n\x0b\x63hange_type\x18\x02 \x02(\x0e\x32\x1e.IM.BaseDefine.GroupModifyType\x12\x13\n\x0bresult_code\x18\x03 \x02(\r\x12\x10\n\x08group_id\x18\x04 \x02(\r\x12\x18\n\x10\x63ur_user_id_list\x18\x05 \x03(\r\x12\x18\n\x10\x63hg_user_id_list\x18\x06 \x03(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"a\n\x10IMGroupShieldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x10\n\x08group_id\x18\x02 \x02(\r\x12\x15\n\rshield_status\x18\x03 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"_\n\x10IMGroupShieldRsp\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x10\n\x08group_id\x18\x02 \x02(\r\x12\x13\n\x0bresult_code\x18\x03 \x02(\r\x12\x13\n\x0b\x61ttach_data\x18\x14 \x01(\x0c\"\xa7\x01\n\x19IMGroupChangeMemberNotify\x12\x0f\n\x07user_id\x18\x01 \x02(\r\x12\x33\n\x0b\x63hange_type\x18\x02 \x02(\x0e\x32\x1e.IM.BaseDefine.GroupModifyType\x12\x10\n\x08group_id\x18\x03 \x02(\r\x12\x18\n\x10\x63ur_user_id_list\x18\x04 \x03(\r\x12\x18\n\x10\x63hg_user_id_list\x18\x05 \x03(\rB\x1b\n\x17\x63om.mogujie.tt.protobufH\x03')



_IMNORMALGROUPLISTREQ = DESCRIPTOR.message_types_by_name['IMNormalGroupListReq']
_IMNORMALGROUPLISTRSP = DESCRIPTOR.message_types_by_name['IMNormalGroupListRsp']
_IMGROUPINFOLISTREQ = DESCRIPTOR.message_types_by_name['IMGroupInfoListReq']
_IMGROUPINFOLISTRSP = DESCRIPTOR.message_types_by_name['IMGroupInfoListRsp']
_IMGROUPCREATEREQ = DESCRIPTOR.message_types_by_name['IMGroupCreateReq']
_IMGROUPCREATERSP = DESCRIPTOR.message_types_by_name['IMGroupCreateRsp']
_IMGROUPCHANGEMEMBERREQ = DESCRIPTOR.message_types_by_name['IMGroupChangeMemberReq']
_IMGROUPCHANGEMEMBERRSP = DESCRIPTOR.message_types_by_name['IMGroupChangeMemberRsp']
_IMGROUPSHIELDREQ = DESCRIPTOR.message_types_by_name['IMGroupShieldReq']
_IMGROUPSHIELDRSP = DESCRIPTOR.message_types_by_name['IMGroupShieldRsp']
_IMGROUPCHANGEMEMBERNOTIFY = DESCRIPTOR.message_types_by_name['IMGroupChangeMemberNotify']
IMNormalGroupListReq = _reflection.GeneratedProtocolMessageType('IMNormalGroupListReq', (_message.Message,), {
  'DESCRIPTOR' : _IMNORMALGROUPLISTREQ,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMNormalGroupListReq)
  })
_sym_db.RegisterMessage(IMNormalGroupListReq)

IMNormalGroupListRsp = _reflection.GeneratedProtocolMessageType('IMNormalGroupListRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMNORMALGROUPLISTRSP,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMNormalGroupListRsp)
  })
_sym_db.RegisterMessage(IMNormalGroupListRsp)

IMGroupInfoListReq = _reflection.GeneratedProtocolMessageType('IMGroupInfoListReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPINFOLISTREQ,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupInfoListReq)
  })
_sym_db.RegisterMessage(IMGroupInfoListReq)

IMGroupInfoListRsp = _reflection.GeneratedProtocolMessageType('IMGroupInfoListRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPINFOLISTRSP,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupInfoListRsp)
  })
_sym_db.RegisterMessage(IMGroupInfoListRsp)

IMGroupCreateReq = _reflection.GeneratedProtocolMessageType('IMGroupCreateReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPCREATEREQ,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupCreateReq)
  })
_sym_db.RegisterMessage(IMGroupCreateReq)

IMGroupCreateRsp = _reflection.GeneratedProtocolMessageType('IMGroupCreateRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPCREATERSP,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupCreateRsp)
  })
_sym_db.RegisterMessage(IMGroupCreateRsp)

IMGroupChangeMemberReq = _reflection.GeneratedProtocolMessageType('IMGroupChangeMemberReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPCHANGEMEMBERREQ,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupChangeMemberReq)
  })
_sym_db.RegisterMessage(IMGroupChangeMemberReq)

IMGroupChangeMemberRsp = _reflection.GeneratedProtocolMessageType('IMGroupChangeMemberRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPCHANGEMEMBERRSP,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupChangeMemberRsp)
  })
_sym_db.RegisterMessage(IMGroupChangeMemberRsp)

IMGroupShieldReq = _reflection.GeneratedProtocolMessageType('IMGroupShieldReq', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPSHIELDREQ,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupShieldReq)
  })
_sym_db.RegisterMessage(IMGroupShieldReq)

IMGroupShieldRsp = _reflection.GeneratedProtocolMessageType('IMGroupShieldRsp', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPSHIELDRSP,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupShieldRsp)
  })
_sym_db.RegisterMessage(IMGroupShieldRsp)

IMGroupChangeMemberNotify = _reflection.GeneratedProtocolMessageType('IMGroupChangeMemberNotify', (_message.Message,), {
  'DESCRIPTOR' : _IMGROUPCHANGEMEMBERNOTIFY,
  '__module__' : 'IM.Group_pb2'
  # @@protoc_insertion_point(class_scope:IM.Group.IMGroupChangeMemberNotify)
  })
_sym_db.RegisterMessage(IMGroupChangeMemberNotify)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.mogujie.tt.protobufH\003'
  _IMNORMALGROUPLISTREQ._serialized_start=49
  _IMNORMALGROUPLISTREQ._serialized_end=109
  _IMNORMALGROUPLISTRSP._serialized_start=111
  _IMNORMALGROUPLISTRSP._serialized_end=232
  _IMGROUPINFOLISTREQ._serialized_start=234
  _IMGROUPINFOLISTREQ._serialized_end=353
  _IMGROUPINFOLISTRSP._serialized_start=355
  _IMGROUPINFOLISTRSP._serialized_end=464
  _IMGROUPCREATEREQ._serialized_start=467
  _IMGROUPCREATEREQ._serialized_end=651
  _IMGROUPCREATERSP._serialized_start=654
  _IMGROUPCREATERSP._serialized_end=791
  _IMGROUPCHANGEMEMBERREQ._serialized_start=794
  _IMGROUPCHANGEMEMBERREQ._serialized_end=951
  _IMGROUPCHANGEMEMBERRSP._serialized_start=954
  _IMGROUPCHANGEMEMBERRSP._serialized_end=1160
  _IMGROUPSHIELDREQ._serialized_start=1162
  _IMGROUPSHIELDREQ._serialized_end=1259
  _IMGROUPSHIELDRSP._serialized_start=1261
  _IMGROUPSHIELDRSP._serialized_end=1356
  _IMGROUPCHANGEMEMBERNOTIFY._serialized_start=1359
  _IMGROUPCHANGEMEMBERNOTIFY._serialized_end=1526
# @@protoc_insertion_point(module_scope)