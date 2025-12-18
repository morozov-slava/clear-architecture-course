from . import pure_robot as pr


def set_robot(x, y, angle, state) -> pr.RobotState:
    return pr.RobotState(x=x, y=y, angle=angle, state=state)


def set_transfer(transfer):
    return transfer
    