# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ParameterPythonModuleFunction()
    PAR0001 = nodes.ParameterSimpleValue()
    ACT0002 = nodes.ActionPrint()
    CON0003 = nodes.ConditionKeyPressed()
    ACT0000.condition = CON0003
    ACT0000.module_name = "text"
    ACT0000.module_func = "add"
    ACT0000.arg = PAR0001
    PAR0001.value = 1
    ACT0002.condition = ACT0000.OUT
    ACT0002.value = ACT0000.VAL
    CON0003.key_code = bge.events.SPACEKEY
    CON0003.pulse = False
    network.add_cell(PAR0001)
    network.add_cell(CON0003)
    network.add_cell(ACT0000)
    network.add_cell(ACT0002)
    owner["IGNLTree_NodeTree"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__NodeTree')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_NodeTree")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
