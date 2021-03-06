# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enemy_skills.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='enemy_skills.proto',
    package='dadguide_proto',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x12\x65nemy_skills.proto\x12\x0e\x64\x61\x64guide_proto\"\xbf\x02\n\x1cMonsterBehaviorWithOverrides\x12\x12\n\nmonster_id\x18\x01 \x01(\x05\x12-\n\x06levels\x18\x02 \x03(\x0b\x32\x1d.dadguide_proto.LevelBehavior\x12\x36\n\x0flevel_overrides\x18\x03 \x03(\x0b\x32\x1d.dadguide_proto.LevelBehavior\x12\x43\n\x06status\x18\x04 \x01(\x0e\x32\x33.dadguide_proto.MonsterBehaviorWithOverrides.Status\"_\n\x06Status\x12\x10\n\x0cNOT_APPROVED\x10\x00\x12\x12\n\x0e\x41PPROVED_AS_IS\x10\x01\x12\x14\n\x10NEEDS_REAPPROVAL\x10\x02\x12\x19\n\x15\x41PPROVED_WITH_CHANGES\x10\x03\"f\n\x0fMonsterBehavior\x12\x12\n\nmonster_id\x18\x01 \x01(\x05\x12-\n\x06levels\x18\x02 \x03(\x0b\x32\x1d.dadguide_proto.LevelBehavior\x12\x10\n\x08\x61pproved\x18\x03 \x01(\x08\"M\n\rLevelBehavior\x12\r\n\x05level\x18\x01 \x01(\x05\x12-\n\x06groups\x18\x02 \x03(\x0b\x32\x1d.dadguide_proto.BehaviorGroup\"\xd9\x02\n\rBehaviorGroup\x12;\n\ngroup_type\x18\x01 \x01(\x0e\x32\'.dadguide_proto.BehaviorGroup.GroupType\x12,\n\tcondition\x18\x02 \x01(\x0b\x32\x19.dadguide_proto.Condition\x12.\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x1c.dadguide_proto.BehaviorItem\"\xac\x01\n\tGroupType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07PASSIVE\x10\x01\x12\x0b\n\x07PREEMPT\x10\x02\x12\x11\n\rDISPEL_PLAYER\x10\x03\x12\x12\n\x0eMONSTER_STATUS\x10\x04\x12\r\n\tREMAINING\x10\x05\x12\x0c\n\x08STANDARD\x10\x06\x12\t\n\x05\x44\x45\x41TH\x10\x07\x12\x0f\n\x0bUNKNOWN_USE\x10\x08\x12\x14\n\x10HIGHEST_PRIORITY\x10\t\"u\n\x0c\x42\x65haviorItem\x12.\n\x05group\x18\x02 \x01(\x0b\x32\x1d.dadguide_proto.BehaviorGroupH\x00\x12,\n\x08\x62\x65havior\x18\x03 \x01(\x0b\x32\x18.dadguide_proto.BehaviorH\x00\x42\x07\n\x05value\"c\n\x08\x42\x65havior\x12,\n\tcondition\x18\x01 \x01(\x0b\x32\x19.dadguide_proto.Condition\x12\x16\n\x0e\x65nemy_skill_id\x18\x02 \x01(\x05\x12\x11\n\tchild_ids\x18\x03 \x03(\x05\"\x80\x04\n\tCondition\x12\x14\n\x0chp_threshold\x18\x01 \x01(\x05\x12\x12\n\nuse_chance\x18\x02 \x01(\x05\x12\x15\n\rrepeats_every\x18\x03 \x01(\x05\x12\x17\n\x0fglobal_one_time\x18\x04 \x01(\x08\x12\x19\n\x11limited_execution\x18\r \x01(\x05\x12!\n\x19trigger_enemies_remaining\x18\x05 \x01(\x05\x12\x13\n\x0bif_defeated\x18\x06 \x01(\x08\x12\x1f\n\x17if_attributes_available\x18\x07 \x01(\x08\x12\x18\n\x10trigger_monsters\x18\x08 \x03(\x05\x12\x16\n\x0etrigger_combos\x18\t \x01(\x05\x12\x1a\n\x12if_nothing_matched\x18\n \x01(\x08\x12\x14\n\x0ctrigger_turn\x18\x0b \x01(\x05\x12\x18\n\x10trigger_turn_end\x18\x0c \x01(\x05\x12\x1c\n\x14\x61lways_trigger_above\x18\x0e \x01(\x05\x12\x14\n\x0c\x61lways_after\x18\x0f \x01(\x05\x12\x11\n\tskill_set\x18\x10 \x01(\x05\x12\x19\n\x11\x65rased_attributes\x18\x11 \x03(\x05\x12\x13\n\x0b\x64\x61mage_done\x18\x12 \x01(\x05\x12\x1b\n\x13\x61ttributes_attacked\x18\x13 \x03(\x05\x12\x13\n\x0bskills_used\x18\x14 \x01(\x05\x62\x06proto3'
)

_MONSTERBEHAVIORWITHOVERRIDES_STATUS = _descriptor.EnumDescriptor(
    name='Status',
    full_name='dadguide_proto.MonsterBehaviorWithOverrides.Status',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NOT_APPROVED', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='APPROVED_AS_IS', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='NEEDS_REAPPROVAL', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='APPROVED_WITH_CHANGES', index=3, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=263,
    serialized_end=358,
)
_sym_db.RegisterEnumDescriptor(_MONSTERBEHAVIORWITHOVERRIDES_STATUS)

_BEHAVIORGROUP_GROUPTYPE = _descriptor.EnumDescriptor(
    name='GroupType',
    full_name='dadguide_proto.BehaviorGroup.GroupType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSPECIFIED', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='PASSIVE', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='PREEMPT', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='DISPEL_PLAYER', index=3, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='MONSTER_STATUS', index=4, number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='REMAINING', index=5, number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STANDARD', index=6, number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='DEATH', index=7, number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN_USE', index=8, number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='HIGHEST_PRIORITY', index=9, number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=717,
    serialized_end=889,
)
_sym_db.RegisterEnumDescriptor(_BEHAVIORGROUP_GROUPTYPE)

_MONSTERBEHAVIORWITHOVERRIDES = _descriptor.Descriptor(
    name='MonsterBehaviorWithOverrides',
    full_name='dadguide_proto.MonsterBehaviorWithOverrides',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='monster_id', full_name='dadguide_proto.MonsterBehaviorWithOverrides.monster_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='levels', full_name='dadguide_proto.MonsterBehaviorWithOverrides.levels', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='level_overrides', full_name='dadguide_proto.MonsterBehaviorWithOverrides.level_overrides', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='status', full_name='dadguide_proto.MonsterBehaviorWithOverrides.status', index=3,
            number=4, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _MONSTERBEHAVIORWITHOVERRIDES_STATUS,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=39,
    serialized_end=358,
)

_MONSTERBEHAVIOR = _descriptor.Descriptor(
    name='MonsterBehavior',
    full_name='dadguide_proto.MonsterBehavior',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='monster_id', full_name='dadguide_proto.MonsterBehavior.monster_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='levels', full_name='dadguide_proto.MonsterBehavior.levels', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='approved', full_name='dadguide_proto.MonsterBehavior.approved', index=2,
            number=3, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=360,
    serialized_end=462,
)

_LEVELBEHAVIOR = _descriptor.Descriptor(
    name='LevelBehavior',
    full_name='dadguide_proto.LevelBehavior',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='level', full_name='dadguide_proto.LevelBehavior.level', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='groups', full_name='dadguide_proto.LevelBehavior.groups', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=464,
    serialized_end=541,
)

_BEHAVIORGROUP = _descriptor.Descriptor(
    name='BehaviorGroup',
    full_name='dadguide_proto.BehaviorGroup',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='group_type', full_name='dadguide_proto.BehaviorGroup.group_type', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='condition', full_name='dadguide_proto.BehaviorGroup.condition', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='children', full_name='dadguide_proto.BehaviorGroup.children', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _BEHAVIORGROUP_GROUPTYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=544,
    serialized_end=889,
)

_BEHAVIORITEM = _descriptor.Descriptor(
    name='BehaviorItem',
    full_name='dadguide_proto.BehaviorItem',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='group', full_name='dadguide_proto.BehaviorItem.group', index=0,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='behavior', full_name='dadguide_proto.BehaviorItem.behavior', index=1,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
            name='value', full_name='dadguide_proto.BehaviorItem.value',
            index=0, containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[]),
    ],
    serialized_start=891,
    serialized_end=1008,
)

_BEHAVIOR = _descriptor.Descriptor(
    name='Behavior',
    full_name='dadguide_proto.Behavior',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='condition', full_name='dadguide_proto.Behavior.condition', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='enemy_skill_id', full_name='dadguide_proto.Behavior.enemy_skill_id', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='child_ids', full_name='dadguide_proto.Behavior.child_ids', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=1010,
    serialized_end=1109,
)

_CONDITION = _descriptor.Descriptor(
    name='Condition',
    full_name='dadguide_proto.Condition',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='hp_threshold', full_name='dadguide_proto.Condition.hp_threshold', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='use_chance', full_name='dadguide_proto.Condition.use_chance', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='repeats_every', full_name='dadguide_proto.Condition.repeats_every', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='global_one_time', full_name='dadguide_proto.Condition.global_one_time', index=3,
            number=4, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='limited_execution', full_name='dadguide_proto.Condition.limited_execution', index=4,
            number=13, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trigger_enemies_remaining', full_name='dadguide_proto.Condition.trigger_enemies_remaining', index=5,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='if_defeated', full_name='dadguide_proto.Condition.if_defeated', index=6,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='if_attributes_available', full_name='dadguide_proto.Condition.if_attributes_available', index=7,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trigger_monsters', full_name='dadguide_proto.Condition.trigger_monsters', index=8,
            number=8, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trigger_combos', full_name='dadguide_proto.Condition.trigger_combos', index=9,
            number=9, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='if_nothing_matched', full_name='dadguide_proto.Condition.if_nothing_matched', index=10,
            number=10, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trigger_turn', full_name='dadguide_proto.Condition.trigger_turn', index=11,
            number=11, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='trigger_turn_end', full_name='dadguide_proto.Condition.trigger_turn_end', index=12,
            number=12, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='always_trigger_above', full_name='dadguide_proto.Condition.always_trigger_above', index=13,
            number=14, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='always_after', full_name='dadguide_proto.Condition.always_after', index=14,
            number=15, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='skill_set', full_name='dadguide_proto.Condition.skill_set', index=15,
            number=16, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='erased_attributes', full_name='dadguide_proto.Condition.erased_attributes', index=16,
            number=17, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='damage_done', full_name='dadguide_proto.Condition.damage_done', index=17,
            number=18, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='attributes_attacked', full_name='dadguide_proto.Condition.attributes_attacked', index=18,
            number=19, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='skills_used', full_name='dadguide_proto.Condition.skills_used', index=19,
            number=20, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key),
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
    serialized_start=1112,
    serialized_end=1624,
)

_MONSTERBEHAVIORWITHOVERRIDES.fields_by_name['levels'].message_type = _LEVELBEHAVIOR
_MONSTERBEHAVIORWITHOVERRIDES.fields_by_name['level_overrides'].message_type = _LEVELBEHAVIOR
_MONSTERBEHAVIORWITHOVERRIDES.fields_by_name['status'].enum_type = _MONSTERBEHAVIORWITHOVERRIDES_STATUS
_MONSTERBEHAVIORWITHOVERRIDES_STATUS.containing_type = _MONSTERBEHAVIORWITHOVERRIDES
_MONSTERBEHAVIOR.fields_by_name['levels'].message_type = _LEVELBEHAVIOR
_LEVELBEHAVIOR.fields_by_name['groups'].message_type = _BEHAVIORGROUP
_BEHAVIORGROUP.fields_by_name['group_type'].enum_type = _BEHAVIORGROUP_GROUPTYPE
_BEHAVIORGROUP.fields_by_name['condition'].message_type = _CONDITION
_BEHAVIORGROUP.fields_by_name['children'].message_type = _BEHAVIORITEM
_BEHAVIORGROUP_GROUPTYPE.containing_type = _BEHAVIORGROUP
_BEHAVIORITEM.fields_by_name['group'].message_type = _BEHAVIORGROUP
_BEHAVIORITEM.fields_by_name['behavior'].message_type = _BEHAVIOR
_BEHAVIORITEM.oneofs_by_name['value'].fields.append(
    _BEHAVIORITEM.fields_by_name['group'])
_BEHAVIORITEM.fields_by_name['group'].containing_oneof = _BEHAVIORITEM.oneofs_by_name['value']
_BEHAVIORITEM.oneofs_by_name['value'].fields.append(
    _BEHAVIORITEM.fields_by_name['behavior'])
_BEHAVIORITEM.fields_by_name['behavior'].containing_oneof = _BEHAVIORITEM.oneofs_by_name['value']
_BEHAVIOR.fields_by_name['condition'].message_type = _CONDITION
DESCRIPTOR.message_types_by_name['MonsterBehaviorWithOverrides'] = _MONSTERBEHAVIORWITHOVERRIDES
DESCRIPTOR.message_types_by_name['MonsterBehavior'] = _MONSTERBEHAVIOR
DESCRIPTOR.message_types_by_name['LevelBehavior'] = _LEVELBEHAVIOR
DESCRIPTOR.message_types_by_name['BehaviorGroup'] = _BEHAVIORGROUP
DESCRIPTOR.message_types_by_name['BehaviorItem'] = _BEHAVIORITEM
DESCRIPTOR.message_types_by_name['Behavior'] = _BEHAVIOR
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MonsterBehaviorWithOverrides = _reflection.GeneratedProtocolMessageType('MonsterBehaviorWithOverrides',
                                                                        (_message.Message,), {
                                                                            'DESCRIPTOR': _MONSTERBEHAVIORWITHOVERRIDES,
                                                                            '__module__': 'enemy_skills_pb2'
                                                                            # @@protoc_insertion_point(class_scope:dadguide_proto.MonsterBehaviorWithOverrides)
                                                                        })
_sym_db.RegisterMessage(MonsterBehaviorWithOverrides)

MonsterBehavior = _reflection.GeneratedProtocolMessageType('MonsterBehavior', (_message.Message,), {
    'DESCRIPTOR': _MONSTERBEHAVIOR,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.MonsterBehavior)
})
_sym_db.RegisterMessage(MonsterBehavior)

LevelBehavior = _reflection.GeneratedProtocolMessageType('LevelBehavior', (_message.Message,), {
    'DESCRIPTOR': _LEVELBEHAVIOR,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.LevelBehavior)
})
_sym_db.RegisterMessage(LevelBehavior)

BehaviorGroup = _reflection.GeneratedProtocolMessageType('BehaviorGroup', (_message.Message,), {
    'DESCRIPTOR': _BEHAVIORGROUP,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.BehaviorGroup)
})
_sym_db.RegisterMessage(BehaviorGroup)

BehaviorItem = _reflection.GeneratedProtocolMessageType('BehaviorItem', (_message.Message,), {
    'DESCRIPTOR': _BEHAVIORITEM,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.BehaviorItem)
})
_sym_db.RegisterMessage(BehaviorItem)

Behavior = _reflection.GeneratedProtocolMessageType('Behavior', (_message.Message,), {
    'DESCRIPTOR': _BEHAVIOR,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.Behavior)
})
_sym_db.RegisterMessage(Behavior)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
    'DESCRIPTOR': _CONDITION,
    '__module__': 'enemy_skills_pb2'
    # @@protoc_insertion_point(class_scope:dadguide_proto.Condition)
})
_sym_db.RegisterMessage(Condition)

# @@protoc_insertion_point(module_scope)
