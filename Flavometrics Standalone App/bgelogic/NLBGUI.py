# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    ACT0000 = nodes.ParameterPythonModuleFunction()
    CON0001 = nodes.GE_OnInit()
    ACT0000.condition = CON0001
    ACT0000.module_name = "bguitest"
    ACT0000.module_func = ""
    ACT0000.arg = nodes.Invalid()
    network.add_cell(CON0001)
    network.add_cell(ACT0000)
    owner["IGNLTree_BGUI"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__BGUI')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_BGUI")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
