import math
from collections import namedtuple

RobotState = namedtuple("RobotState", "x y angle mode")

WATER = 1
SOAP  = 2
BRUSH = 3


def transfer_to_cleaner(message):
    print(message)


def move(transfer, dist, state):
    angle_rads = state.angle * (math.pi / 180.0)
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.mode
    )
    transfer(("POS", new_state.x, new_state.y))
    return new_state


def turn(transfer, angle, state):
    new_state = RobotState(
        state.x,
        state.y,
        state.angle + angle,
        state.mode
    )
    transfer(("ANGLE", new_state.angle))
    return new_state


def set_mode(transfer, mode, state):
    mapping = {
        "water": WATER,
        "soap": SOAP,
        "brush": BRUSH,
    }
    if mode not in mapping:
        return state

    new_state = state._replace(mode=mapping[mode])
    transfer(("MODE", new_state.mode))
    return new_state


def start(transfer, state):
    transfer(("START", state.mode))
    return state


def stop(transfer, state):
    transfer(("STOP",))
    return state
