# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ActionLoadVariable()
    ACT0001 = nodes.ActionLoadVariable()
    PAR0002 = nodes.ParameterVector3Split()
    ACT0003 = nodes.AppendListItem()
    ACT0004 = nodes.ActionSaveVariable()
    ACT0005 = nodes.ActionSaveVariable()
    ACT0006 = nodes.AppendListItem()
    CON0007 = nodes.GE_OnInit()
    ACT0008 = nodes.InitEmptyList()
    ACT0009 = nodes.ActionSaveVariable()
    ACT0010 = nodes.ActionSaveVariable()
    ACT0011 = nodes.InitEmptyList()
    CON0012 = nodes.ConditionMouseTargeting()
    CON0013 = nodes.ConditionKeyPressed()
    PAR0014 = nodes.ParameterObjectProperty()
    PAR0015 = nodes.ParameterSwitchValue()
    ACT0016 = nodes.ActionToggleGameObjectGameProperty()
    ACT0017 = nodes.ActionStopAnimation()
    ACT0018 = nodes.ActionSetMaterialNodeValue()
    CON0019 = nodes.ConditionKeyPressed()
    ACT0020 = nodes.ActionSetMaterialNodeValue()
    CON0021 = nodes.ConditionKeyPressed()
    ACT0022 = nodes.ActionSetAnimationFrame()
    CON0023 = nodes.ConditionKeyPressed()
    ACT0024 = nodes.ActionSetMaterialNodeValue()
    CON0025 = nodes.ConditionKeyPressed()
    ACT0026 = nodes.ActionApplyRotation()
    CON0027 = nodes.ConditionKeyPressed()
    CON0028 = nodes.ConditionKeyPressed()
    ACT0029 = nodes.ActionApplyRotation()
    PAR0030 = nodes.ParameterSimpleValue()
    ACT0031 = nodes.ActionSetMouseCursorVisibility()
    PAR0032 = nodes.ParameterActiveCamera()
    ACT0033 = nodes.ActionMousePick()
    ACT0034 = nodes.InitEmptyList()
    ACT0035 = nodes.ActionSaveVariable()
    ACT0036 = nodes.ActionSaveVariable()
    ACT0037 = nodes.ActionClearVariables()
    ACT0038 = nodes.InitEmptyList()
    PAR0039 = nodes.ParameterActiveCamera()
    ACT0040 = nodes.ActionMousePick()
    ACT0041 = nodes.ActionSetMaterialNodeValue()
    ACT0042 = nodes.InitEmptyList()
    ACT0043 = nodes.ActionSaveVariable()
    ACT0044 = nodes.ActionSaveVariable()
    ACT0045 = nodes.InitEmptyList()
    ACT0046 = nodes.ActionClearVariables()
    ACT0047 = nodes.ActionTimeDelay()
    CON0048 = nodes.ConditionMousePressed()
    ACT0049 = nodes.SetCurvePoints()
    ACT0050 = nodes.ParameterPythonModuleFunction()
    ACT0051 = nodes.ParameterPythonModuleFunction()
    ACT0052 = nodes.ParameterPythonModuleFunction()
    ACT0053 = nodes.ParameterPythonModuleFunction()
    CON0054 = nodes.ConditionKeyPressed()
    CON0055 = nodes.ConditionMouseTargeting()
    PAR0056 = nodes.ParameterVector3Split()
    ACT0057 = nodes.ActionSetObjectAttribute()
    PAR0058 = nodes.ParameterVector3Simple()
    ACT0059 = nodes.ActionTimeFilter()
    CON0060 = nodes.ConditionAnd()
    CON0061 = nodes.ConditionKeyPressed()
    ACT0062 = nodes.ActionApplyRotation()
    ACT0063 = nodes.ActionApplyRotation()
    CON0064 = nodes.ConditionMouseReleased()
    CON0065 = nodes.ConditionMousePressed()
    ACT0066 = nodes.ActionSetGameObjectGameProperty()
    PAR0067 = nodes.ParameterObjectProperty()
    CON0068 = nodes.GE_OnInit()
    ACT0069 = nodes.ActionMousePick()
    CON0070 = nodes.ConditionKeyPressed()
    CON0071 = nodes.ConditionMousePressedOn()
    ACT0072 = nodes.ActionSetGameObjectGameProperty()
    ACT0073 = nodes.ActionSetGameObjectGameProperty()
    ACT0074 = nodes.ActionSetGameObjectGameProperty()
    CON0075 = nodes.ConditionAnd()
    PAR0076 = nodes.ParameterObjectProperty()
    PAR0077 = nodes.ParameterObjectProperty()
    CON0078 = nodes.ConditionAnd()
    PAR0079 = nodes.ParameterMouseData()
    PAR0080 = nodes.ParameterArithmeticOp()
    PAR0081 = nodes.ParameterVector3Simple()
    ACT0082 = nodes.ActionApplyRotation()
    ACT0083 = nodes.ActionApplyRotation()
    ACT0084 = nodes.ActionTimeFilter()
    CON0085 = nodes.ConditionAnd()
    CON0086 = nodes.ConditionMousePressed()
    ACT0087 = nodes.ActionSetGameObjectGameProperty()
    CON0088 = nodes.ConditionMousePressedOn()
    PAR0089 = nodes.ParameterObjectProperty()
    ACT0090 = nodes.ActionApplyRotation()
    ACT0091 = nodes.ActionApplyRotation()
    PAR0092 = nodes.ParameterArithmeticOp()
    PAR0093 = nodes.ParameterVector3Simple()
    PAR0094 = nodes.ParameterVector3Split()
    PAR0095 = nodes.ParameterArithmeticOp()
    ACT0096 = nodes.ActionSetObjectAttribute()
    PAR0097 = nodes.ParameterArithmeticOp()
    PAR0098 = nodes.ParameterArithmeticOp()
    PAR0099 = nodes.ParameterVector3Simple()
    PAR0100 = nodes.ParameterVector3Split()
    CON0101 = nodes.ConditionAnd()
    CON0102 = nodes.ConditionMousePressed()
    ACT0103 = nodes.ActionTimeFilter()
    CON0104 = nodes.ConditionMouseTargeting()
    PAR0105 = nodes.ParameterObjectAttribute()
    PAR0106 = nodes.ParameterArithmeticOp()
    PAR0107 = nodes.ParameterArithmeticOp()
    PAR0108 = nodes.ParameterArithmeticOp()
    PAR0109 = nodes.ParameterArithmeticOp()
    PAR0110 = nodes.ParameterArithmeticOp()
    PAR0111 = nodes.ParameterArithmeticOp()
    PAR0112 = nodes.ParameterArithmeticOp()
    ACT0113 = nodes.ActionSetObjectAttribute()
    CON0114 = nodes.ConditionMousePressedOn()
    CON0115 = nodes.ConditionMouseTargeting()
    PAR0116 = nodes.ParameterVector3Simple()
    ACT0117 = nodes.ActionSetMaterialNodeValue()
    ACT0118 = nodes.ActionPrint()
    PAR0119 = nodes.ParameterArithmeticOp()
    CON0120 = nodes.ConditionAnd()
    ACT0121 = nodes.ActionTimeFilter()
    PAR0122 = nodes.ParameterObjectAttribute()
    PAR0123 = nodes.ParameterArithmeticOp()
    CON0124 = nodes.ConditionMouseTargeting()
    CON0125 = nodes.ConditionMousePressed()
    PAR0126 = nodes.ParameterVector3Simple()
    PAR0127 = nodes.ParameterVector3Split()
    ACT0128 = nodes.ActionSetMaterialNodeValue()
    ACT0129 = nodes.ActionSetObjectAttribute()
    PAR0130 = nodes.ParameterVector3Split()
    PAR0131 = nodes.ParameterArithmeticOp()
    PAR0132 = nodes.ParameterArithmeticOp()
    PAR0133 = nodes.ParameterArithmeticOp()
    PAR0134 = nodes.ParameterObjectProperty()
    ACT0135 = nodes.ActionSetGameObjectGameProperty()
    ACT0136 = nodes.ActionPlayAction()
    ACT0137 = nodes.ActionPrint()
    ACT0138 = nodes.ActionSetGameObjectGameProperty()
    ACT0139 = nodes.ActionSetGameObjectGameProperty()
    ACT0140 = nodes.ActionSetGameObjectGameProperty()
    CON0141 = nodes.GE_OnInit()
    PAR0142 = nodes.ParameterActionStatus()
    ACT0143 = nodes.ActionClearVariables()
    ACT0144 = nodes.ActionSetActiveCamera()
    ACT0000.path = ''
    ACT0000.file_name = 'variables'
    ACT0000.condition = ACT0033
    ACT0000.name = "y"
    ACT0001.path = ''
    ACT0001.file_name = 'variables'
    ACT0001.condition = ACT0033
    ACT0001.name = "x"
    PAR0002.input_v = ACT0033.OUTPOINT
    ACT0003.condition = ACT0000.OUT
    ACT0003.items = ACT0000.VAR
    ACT0003.val = PAR0002.OUTY
    ACT0004.path = ''
    ACT0004.file_name = 'variables'
    ACT0004.condition = ACT0006.OUT
    ACT0004.name = "x"
    ACT0004.val = ACT0006.LIST
    ACT0005.path = ''
    ACT0005.file_name = 'variables'
    ACT0005.condition = ACT0003.OUT
    ACT0005.name = "y"
    ACT0005.val = ACT0003.LIST
    ACT0006.condition = ACT0001.OUT
    ACT0006.items = ACT0001.VAR
    ACT0006.val = PAR0002.OUTX
    ACT0008.condition = ACT0143.OUT
    ACT0008.length = 0
    ACT0009.path = ''
    ACT0009.file_name = 'variables'
    ACT0009.condition = ACT0008.OUT
    ACT0009.name = "y"
    ACT0009.val = ACT0008.LIST
    ACT0010.path = ''
    ACT0010.file_name = 'variables'
    ACT0010.condition = ACT0011.OUT
    ACT0010.name = "x"
    ACT0010.val = ACT0011.LIST
    ACT0011.condition = ACT0143.OUT
    ACT0011.length = 0
    CON0012.game_object = "NLO:U_O"
    CON0013.key_code = bge.events.SPACEKEY
    CON0013.pulse = False
    PAR0014.game_object = "NLO:U_O"
    PAR0014.property_name = "animate"
    PAR0015.state = PAR0014
    ACT0016.condition = CON0013
    ACT0016.game_object = "NLO:U_O"
    ACT0016.property_name = "animate"
    ACT0017.condition = PAR0015.FALSE
    ACT0017.game_object = "NLO:U_O"
    ACT0017.action_layer = 0
    ACT0018.condition = CON0019
    ACT0018.mat_name = "FlavoTool 2.0"
    ACT0018.node_name = "Flavo Control"
    ACT0018.input_slot = 1
    ACT0018.value = 0.5
    CON0019.key_code = bge.events.TWOKEY
    CON0019.pulse = False
    ACT0020.condition = CON0021
    ACT0020.mat_name = "FlavoTool 2.0"
    ACT0020.node_name = "Flavo Control"
    ACT0020.input_slot = 1
    ACT0020.value = 1.0
    CON0021.key_code = bge.events.THREEKEY
    CON0021.pulse = False
    ACT0022.condition = CON0054
    ACT0022.game_object = "NLO:U_O"
    ACT0022.action_name = "Shader NodetreeAction.004"
    ACT0022.action_layer = 0
    ACT0022.action_frame = 0.0
    ACT0022.freeze = True
    ACT0022.layer_weight = 1.0
    CON0023.key_code = bge.events.LEFTCTRLKEY
    CON0023.pulse = False
    ACT0024.condition = CON0023
    ACT0024.mat_name = "FlavoTool 2.0"
    ACT0024.node_name = "Flavo Control"
    ACT0024.input_slot = 4
    ACT0024.value = 0.0
    CON0025.key_code = bge.events.SKEY
    CON0025.pulse = True
    ACT0026.local = True
    ACT0026.condition = CON0025
    ACT0026.game_object = "NLO:Camera Rotate"
    ACT0026.rotation = mathutils.Vector((0.03490658476948738, 0.0, 0.0))
    CON0027.key_code = bge.events.AKEY
    CON0027.pulse = True
    CON0028.key_code = bge.events.DKEY
    CON0028.pulse = True
    ACT0029.local = True
    ACT0029.condition = CON0028
    ACT0029.game_object = "NLO:Camera Rotate"
    ACT0029.rotation = mathutils.Vector((0.0, 0.0, 0.05235987901687622))
    PAR0030.value = True
    ACT0031.condition = PAR0030
    ACT0031.visibility_status = True
    ACT0033.condition = CON0060
    ACT0033.camera = PAR0032
    ACT0033.property = ""
    ACT0033.xray = False
    ACT0033.distance = 100.0
    ACT0034.condition = ACT0037.OUT
    ACT0034.length = 0
    ACT0035.path = ''
    ACT0035.file_name = 'variables'
    ACT0035.condition = ACT0034.OUT
    ACT0035.name = "x"
    ACT0035.val = ACT0034.LIST
    ACT0036.path = ''
    ACT0036.file_name = 'variables'
    ACT0036.condition = ACT0038.OUT
    ACT0036.name = "y"
    ACT0036.val = ACT0038.LIST
    ACT0037.path = ''
    ACT0037.file_name = 'variables'
    ACT0037.condition = CON0007
    ACT0038.condition = ACT0037.OUT
    ACT0038.length = 0
    ACT0040.condition = CON0048
    ACT0040.camera = PAR0039
    ACT0040.property = ""
    ACT0040.xray = False
    ACT0040.distance = 100.0
    ACT0041.condition = ACT0040
    ACT0041.mat_name = "FlavoTool 2.0"
    ACT0041.node_name = "Flavo Control"
    ACT0041.input_slot = 4
    ACT0041.value = 1.0
    ACT0042.condition = ACT0046.OUT
    ACT0042.length = 0
    ACT0043.path = ''
    ACT0043.file_name = 'variables'
    ACT0043.condition = ACT0042.OUT
    ACT0043.name = "x"
    ACT0043.val = ACT0042.LIST
    ACT0044.path = ''
    ACT0044.file_name = 'variables'
    ACT0044.condition = ACT0045.OUT
    ACT0044.name = "y"
    ACT0044.val = ACT0045.LIST
    ACT0045.condition = ACT0046.OUT
    ACT0045.length = 0
    ACT0046.path = ''
    ACT0046.file_name = 'variables'
    ACT0046.condition = ACT0047
    ACT0047.condition = CON0075
    ACT0047.delay = 0.10000000149011612
    CON0048.mouse_button_code = bge.events.LEFTMOUSE
    CON0048.pulse = False
    ACT0049.condition = None
    ACT0049.curve_object = "NLO:BezierCurve"
    ACT0049.points = None
    ACT0050.condition = ACT0004.OUT
    ACT0050.module_name = "vectors"
    ACT0050.module_func = "function"
    ACT0050.arg = "//Data\variables.json"
    ACT0051.condition = ACT0050.OUT
    ACT0051.module_name = "makecurve"
    ACT0051.module_func = "function"
    ACT0051.arg = ACT0050.VAL
    ACT0052.condition = False
    ACT0052.module_name = "Initcurve"
    ACT0052.module_func = "function"
    ACT0052.arg = 0.0
    ACT0053.condition = CON0023
    ACT0053.module_name = "clearcurve"
    ACT0053.module_func = "function"
    ACT0053.arg = 0.0
    CON0054.key_code = bge.events.LEFTALTKEY
    CON0054.pulse = False
    CON0055.game_object = "NLO:U_O"
    PAR0056.input_v = CON0055.POINT
    ACT0057.condition = CON0055.MOUSE_OVER
    ACT0057.xyz = {'x': True, 'y': True, 'z': True}
    ACT0057.game_object = "NLO:Mouse Cursor"
    ACT0057.attribute_value = PAR0058.OUTV
    ACT0057.value_type = 'worldPosition'
    PAR0058.input_x = PAR0056.OUTX
    PAR0058.input_y = PAR0056.OUTY
    PAR0058.input_z = 0.009999999776482582
    ACT0059.condition = CON0078
    ACT0059.delay = 0.10000000149011612
    CON0060.condition_a = ACT0059
    CON0060.condition_b = CON0012.MOUSE_OVER
    CON0061.key_code = bge.events.WKEY
    CON0061.pulse = True
    ACT0062.local = True
    ACT0062.condition = CON0061
    ACT0062.game_object = "NLO:Camera Rotate"
    ACT0062.rotation = mathutils.Vector((-0.03490658476948738, 0.0, 0.0))
    ACT0063.local = True
    ACT0063.condition = CON0027
    ACT0063.game_object = "NLO:Camera Rotate"
    ACT0063.rotation = mathutils.Vector((0.0, 0.0, -0.05235987901687622))
    CON0064.mouse_button_code = bge.events.LEFTMOUSE
    CON0064.pulse = False
    CON0065.mouse_button_code = bge.events.LEFTMOUSE
    CON0065.pulse = True
    ACT0066.condition = None
    ACT0066.game_object = "NLO:U_O"
    ACT0066.property_name = ""
    ACT0066.property_value = ""
    PAR0067.game_object = None
    PAR0067.property_name = ""
    ACT0069.condition = None
    ACT0069.camera = "NLO:HUD Camera"
    ACT0069.property = ""
    ACT0069.xray = False
    ACT0069.distance = 100.0
    CON0070.key_code = bge.events.ONEKEY
    CON0070.pulse = False
    CON0071.mouse_button = bge.events.LEFTMOUSE
    CON0071.game_object = "NLO:Innouculate Button"
    ACT0072.condition = CON0071
    ACT0072.game_object = "NLO:U_O"
    ACT0072.property_name = "inno"
    ACT0072.property_value = True
    ACT0073.condition = CON0071
    ACT0073.game_object = "NLO:U_O"
    ACT0073.property_name = "rot"
    ACT0073.property_value = False
    ACT0074.condition = CON0088
    ACT0074.game_object = "NLO:U_O"
    ACT0074.property_name = "inno"
    ACT0074.property_value = False
    CON0075.condition_a = CON0064
    CON0075.condition_b = PAR0076
    PAR0076.game_object = "NLO:U_O"
    PAR0076.property_name = "inno"
    PAR0077.game_object = "NLO:U_O"
    PAR0077.property_name = "inno"
    CON0078.condition_a = CON0065
    CON0078.condition_b = PAR0077
    PAR0080.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0080.operand_a = PAR0079.MDY
    PAR0080.operand_b = -2.0
    PAR0081.input_x = 0.0
    PAR0081.input_y = 0.0
    PAR0081.input_z = PAR0092
    ACT0082.local = True
    ACT0082.condition = ACT0084
    ACT0082.game_object = "NLO:Camera Rotate"
    ACT0082.rotation = PAR0093.OUTV
    ACT0083.local = False
    ACT0083.condition = ACT0084
    ACT0083.game_object = "NLO:Light Rotation Master"
    ACT0083.rotation = PAR0081.OUTV
    ACT0084.condition = CON0085
    ACT0084.delay = 0.10000000149011612
    CON0085.condition_a = PAR0089
    CON0085.condition_b = CON0086
    CON0086.mouse_button_code = bge.events.LEFTMOUSE
    CON0086.pulse = True
    ACT0087.condition = CON0088
    ACT0087.game_object = "NLO:U_O"
    ACT0087.property_name = "rot"
    ACT0087.property_value = True
    CON0088.mouse_button = bge.events.LEFTMOUSE
    CON0088.game_object = "NLO:Rotate Button.001"
    PAR0089.game_object = "NLO:U_O"
    PAR0089.property_name = "rot"
    ACT0090.local = True
    ACT0090.condition = ACT0084
    ACT0090.game_object = "NLO:Light Rotation Master"
    ACT0090.rotation = PAR0093.OUTV
    ACT0091.local = False
    ACT0091.condition = ACT0084
    ACT0091.game_object = "NLO:Camera Rotate"
    ACT0091.rotation = PAR0081.OUTV
    PAR0092.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0092.operand_a = PAR0079.MDX
    PAR0092.operand_b = -3.0
    PAR0093.input_x = PAR0080
    PAR0093.input_y = 0.0
    PAR0093.input_z = 0.0
    PAR0094.input_v = CON0115.POINT
    PAR0095.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0095.operand_a = PAR0100.OUTY
    PAR0095.operand_b = 0.09600000083446503
    ACT0096.condition = ACT0113.OUT
    ACT0096.xyz = {'x': True, 'y': True, 'z': True}
    ACT0096.game_object = "NLO:Light Rotation Master"
    ACT0096.attribute_value = PAR0099.OUTV
    ACT0096.value_type = 'worldOrientation'
    PAR0097.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0097.operand_a = PAR0098
    PAR0097.operand_b = -149.0
    PAR0098.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0098.operand_a = PAR0111
    PAR0098.operand_b = 0.01745329238474369
    PAR0099.input_x = PAR0097
    PAR0099.input_y = PAR0107
    PAR0099.input_z = 0.0
    PAR0100.input_v = PAR0105
    CON0101.condition_a = ACT0103
    CON0101.condition_b = CON0115.MOUSE_OVER
    CON0102.mouse_button_code = bge.events.LEFTMOUSE
    CON0102.pulse = True
    ACT0103.condition = CON0102
    ACT0103.delay = 0.019999999552965164
    CON0104.game_object = "NLO:Camera UI"
    PAR0105.game_object = "NLO:Light UI"
    PAR0105.attribute_name = "localPosition"
    PAR0106.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0106.operand_a = PAR0107
    PAR0106.operand_b = -1.0
    PAR0107.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0107.operand_a = PAR0108
    PAR0107.operand_b = 0.01745329238474369
    PAR0108.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0108.operand_a = PAR0110
    PAR0108.operand_b = 90.0
    PAR0109.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0109.operand_a = PAR0100.OUTX
    PAR0109.operand_b = -0.8399999737739563
    PAR0110.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0110.operand_a = PAR0109
    PAR0110.operand_b = 367.0
    PAR0111.operator = nodes.ParameterArithmeticOp.op_by_code("SUB")
    PAR0111.operand_a = PAR0112
    PAR0111.operand_b = 90.0
    PAR0112.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0112.operand_a = PAR0095
    PAR0112.operand_b = -523.0
    ACT0113.condition = CON0101
    ACT0113.xyz = {'x': True, 'y': True, 'z': True}
    ACT0113.game_object = "NLO:Light UI"
    ACT0113.attribute_value = PAR0116.OUTV
    ACT0113.value_type = 'worldPosition'
    CON0114.mouse_button = bge.events.LEFTMOUSE
    CON0114.game_object = "NLO:Camera UI"
    CON0115.game_object = "NLO:Rotation Graph"
    PAR0116.input_x = PAR0094.OUTX
    PAR0116.input_y = PAR0094.OUTY
    PAR0116.input_z = PAR0094.OUTZ
    ACT0117.condition = CON0070
    ACT0117.mat_name = "FlavoTool 2.0"
    ACT0117.node_name = "Flavo Control"
    ACT0117.input_slot = 1
    ACT0117.value = 0.0
    ACT0118.condition = ACT0129.OUT
    ACT0118.value = PAR0133
    PAR0119.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0119.operand_a = PAR0130.OUTY
    PAR0119.operand_b = 1.159999966621399
    CON0120.condition_a = ACT0121
    CON0120.condition_b = CON0124.MOUSE_OVER
    ACT0121.condition = CON0125
    ACT0121.delay = 0.019999999552965164
    PAR0122.game_object = "NLO:Slider Bar"
    PAR0122.attribute_name = "localPosition"
    PAR0123.operator = nodes.ParameterArithmeticOp.op_by_code("MUL")
    PAR0123.operand_a = PAR0119
    PAR0123.operand_b = 1.0
    CON0124.game_object = "NLO:Slider Plane"
    CON0125.mouse_button_code = bge.events.LEFTMOUSE
    CON0125.pulse = True
    PAR0126.input_x = PAR0127.OUTX
    PAR0126.input_y = PAR0127.OUTY
    PAR0126.input_z = PAR0127.OUTZ
    PAR0127.input_v = CON0124.POINT
    ACT0128.condition = ACT0129.OUT
    ACT0128.mat_name = "FlavoTool 2.0"
    ACT0128.node_name = "Flavo Control"
    ACT0128.input_slot = 1
    ACT0128.value = PAR0133
    ACT0129.condition = CON0120
    ACT0129.xyz = {'x': False, 'y': True, 'z': True}
    ACT0129.game_object = "NLO:Slider Bar"
    ACT0129.attribute_value = PAR0126.OUTV
    ACT0129.value_type = 'worldPosition'
    PAR0130.input_v = PAR0122
    PAR0131.operator = nodes.ParameterArithmeticOp.op_by_code("DIV")
    PAR0131.operand_a = PAR0123
    PAR0131.operand_b = 0.27000001072883606
    PAR0132.operator = nodes.ParameterArithmeticOp.op_by_code("ADD")
    PAR0132.operand_a = PAR0131
    PAR0132.operand_b = 1.0
    PAR0133.operator = nodes.ParameterArithmeticOp.op_by_code("DIV")
    PAR0133.operand_a = PAR0132
    PAR0133.operand_b = 2.0
    PAR0134.game_object = "NLO:U_O"
    PAR0134.property_name = "frame"
    ACT0135.condition = ACT0136.RUNNING
    ACT0135.game_object = "NLO:U_O"
    ACT0135.property_name = "frame"
    ACT0135.property_value = ACT0136.FRAME
    ACT0136.condition = PAR0015.TRUE
    ACT0136.game_object = "NLO:U_O"
    ACT0136.action_name = "Shader NodetreeAction.004"
    ACT0136.start_frame = PAR0134
    ACT0136.end_frame = 500.0
    ACT0136.layer = 0
    ACT0136.priority = 0
    ACT0136.play_mode = bge.logic.KX_ACTION_MODE_PLAY
    ACT0136.stop = True
    ACT0136.layer_weight = 1.0
    ACT0136.speed = 1.2699997425079346
    ACT0136.blendin = 0.0
    ACT0136.blend_mode = bge.logic.KX_ACTION_BLEND_BLEND
    ACT0137.condition = CON0013
    ACT0137.value = PAR0134
    ACT0138.condition = CON0054
    ACT0138.game_object = "NLO:U_O"
    ACT0138.property_name = "animate"
    ACT0138.property_value = False
    ACT0139.condition = CON0054
    ACT0139.game_object = "NLO:U_O"
    ACT0139.property_name = "frame"
    ACT0139.property_value = 0.0
    ACT0140.condition = CON0141
    ACT0140.game_object = "NLO:U_O"
    ACT0140.property_name = "frame"
    ACT0140.property_value = PAR0142.ACTION_FRAME
    PAR0142.game_object = "NLO:U_O"
    PAR0142.action_layer = 0
    ACT0143.path = ''
    ACT0143.file_name = 'variables'
    ACT0143.condition = CON0023
    ACT0144.condition = None
    ACT0144.camera = "NLO:Game Camera"
    network.add_cell(CON0007)
    network.add_cell(CON0012)
    network.add_cell(PAR0014)
    network.add_cell(CON0019)
    network.add_cell(CON0021)
    network.add_cell(CON0023)
    network.add_cell(CON0025)
    network.add_cell(CON0027)
    network.add_cell(PAR0030)
    network.add_cell(PAR0032)
    network.add_cell(ACT0037)
    network.add_cell(PAR0039)
    network.add_cell(CON0048)
    network.add_cell(ACT0052)
    network.add_cell(CON0054)
    network.add_cell(CON0061)
    network.add_cell(ACT0063)
    network.add_cell(CON0065)
    network.add_cell(PAR0067)
    network.add_cell(ACT0069)
    network.add_cell(CON0071)
    network.add_cell(ACT0073)
    network.add_cell(PAR0076)
    network.add_cell(PAR0079)
    network.add_cell(CON0086)
    network.add_cell(CON0088)
    network.add_cell(PAR0092)
    network.add_cell(CON0102)
    network.add_cell(CON0104)
    network.add_cell(CON0114)
    network.add_cell(PAR0122)
    network.add_cell(CON0124)
    network.add_cell(PAR0127)
    network.add_cell(PAR0130)
    network.add_cell(PAR0134)
    network.add_cell(ACT0138)
    network.add_cell(CON0141)
    network.add_cell(ACT0143)
    network.add_cell(ACT0008)
    network.add_cell(ACT0011)
    network.add_cell(PAR0015)
    network.add_cell(ACT0017)
    network.add_cell(ACT0020)
    network.add_cell(ACT0024)
    network.add_cell(CON0028)
    network.add_cell(ACT0031)
    network.add_cell(ACT0034)
    network.add_cell(ACT0038)
    network.add_cell(ACT0049)
    network.add_cell(ACT0053)
    network.add_cell(ACT0062)
    network.add_cell(ACT0066)
    network.add_cell(CON0070)
    network.add_cell(ACT0074)
    network.add_cell(PAR0077)
    network.add_cell(PAR0080)
    network.add_cell(ACT0087)
    network.add_cell(PAR0093)
    network.add_cell(ACT0103)
    network.add_cell(CON0115)
    network.add_cell(ACT0117)
    network.add_cell(PAR0119)
    network.add_cell(PAR0123)
    network.add_cell(PAR0126)
    network.add_cell(PAR0131)
    network.add_cell(ACT0136)
    network.add_cell(ACT0139)
    network.add_cell(PAR0142)
    network.add_cell(ACT0009)
    network.add_cell(CON0013)
    network.add_cell(ACT0018)
    network.add_cell(ACT0026)
    network.add_cell(ACT0035)
    network.add_cell(ACT0040)
    network.add_cell(CON0055)
    network.add_cell(CON0064)
    network.add_cell(ACT0072)
    network.add_cell(CON0078)
    network.add_cell(PAR0089)
    network.add_cell(PAR0094)
    network.add_cell(CON0101)
    network.add_cell(PAR0116)
    network.add_cell(CON0125)
    network.add_cell(PAR0132)
    network.add_cell(ACT0135)
    network.add_cell(ACT0140)
    network.add_cell(ACT0010)
    network.add_cell(ACT0022)
    network.add_cell(ACT0036)
    network.add_cell(PAR0056)
    network.add_cell(PAR0058)
    network.add_cell(CON0068)
    network.add_cell(PAR0081)
    network.add_cell(CON0085)
    network.add_cell(PAR0105)
    network.add_cell(ACT0113)
    network.add_cell(ACT0121)
    network.add_cell(PAR0133)
    network.add_cell(ACT0144)
    network.add_cell(ACT0016)
    network.add_cell(ACT0041)
    network.add_cell(ACT0057)
    network.add_cell(CON0075)
    network.add_cell(ACT0084)
    network.add_cell(ACT0091)
    network.add_cell(PAR0100)
    network.add_cell(PAR0109)
    network.add_cell(CON0120)
    network.add_cell(ACT0129)
    network.add_cell(ACT0029)
    network.add_cell(ACT0047)
    network.add_cell(ACT0059)
    network.add_cell(ACT0082)
    network.add_cell(ACT0090)
    network.add_cell(PAR0110)
    network.add_cell(ACT0118)
    network.add_cell(ACT0137)
    network.add_cell(ACT0046)
    network.add_cell(CON0060)
    network.add_cell(PAR0095)
    network.add_cell(PAR0108)
    network.add_cell(PAR0112)
    network.add_cell(ACT0033)
    network.add_cell(ACT0045)
    network.add_cell(ACT0083)
    network.add_cell(PAR0107)
    network.add_cell(ACT0128)
    network.add_cell(ACT0000)
    network.add_cell(PAR0002)
    network.add_cell(ACT0042)
    network.add_cell(ACT0044)
    network.add_cell(PAR0106)
    network.add_cell(ACT0001)
    network.add_cell(ACT0006)
    network.add_cell(PAR0111)
    network.add_cell(ACT0003)
    network.add_cell(ACT0005)
    network.add_cell(PAR0098)
    network.add_cell(ACT0004)
    network.add_cell(ACT0050)
    network.add_cell(PAR0097)
    network.add_cell(ACT0043)
    network.add_cell(PAR0099)
    network.add_cell(ACT0051)
    network.add_cell(ACT0096)
    owner["IGNLTree_FlavoTool2.0"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__FlavoTool2.0')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_FlavoTool2.0")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
