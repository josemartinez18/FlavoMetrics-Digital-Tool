# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.GE_OnInit()
    ACT0001 = nodes.ActionListVariables()
    ACT0001.path = ''
    ACT0001.file_name = 'variables'
    ACT0001.condition = CON0000
    ACT0001.print_list = True
    network.add_cell(CON0000)
    network.add_cell(ACT0001)
    owner["IGNLTree_NodeTree.001"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__NodeTree.001')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_NodeTree.001")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
