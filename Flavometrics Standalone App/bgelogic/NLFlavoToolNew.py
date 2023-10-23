# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.ConditionKeyPressed()
    CON0000.key_code = bge.events.SPACEKEY
    CON0000.pulse = False
    network.add_cell(CON0000)
    owner["IGNLTree_FlavoTool New"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__FlavoTool New')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_FlavoTool New")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
