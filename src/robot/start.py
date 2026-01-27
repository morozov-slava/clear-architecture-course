from .robot_management import RobotMonade
from .capabilities import IdleCaps
from .pure_robot import RobotState, WATER


def program_start(transfer):
    return RobotMonade(
        lambda s: (IdleCaps(transfer), s)
    )


def initial_state():
    return RobotState(0, 0, 0, WATER)
