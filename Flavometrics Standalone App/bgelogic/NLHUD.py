# MACHINE GENERATED
import bge, bpy, sys, importlib
import mathutils
from uplogic import nodes
import math

def _initialize(owner):
    network = nodes.LogicNetwork()
    CON0000 = nodes.GE_OnInit()
    PAR0001 = nodes.GESetOverlayCollection()
    ACT0002 = nodes.SetMaterial()
    CON0003 = nodes.ConditionMouseTargeting()
    PAR0001.condition = CON0000
    PAR0001.camera = "NLO:HUD Camera"
    PAR0001.collection = "HUD"
    ACT0002.condition = CON0003.MOUSE_ENTERED
    ACT0002.game_object = "NLO:Innoculate Button"
    ACT0002.slot = 1
    ACT0002.mat_name = "Color Letter"
    CON0003.game_object = "NLO:Innoculate Button"
    network.add_cell(CON0000)
    network.add_cell(CON0003)
    network.add_cell(PAR0001)
    network.add_cell(ACT0002)
    owner["IGNLTree_HUD"] = network
    network._owner = owner
    network.setup()
    network.stopped = not owner.get('NL__HUD')
    return network

def pulse_network(controller):
    owner = controller.owner
    network = owner.get("IGNLTree_HUD")
    if network is None:
        network = _initialize(owner)
    if network.stopped: return
    shutdown = network.evaluate()
    if shutdown is True:
        controller.sensors[0].repeat = False
