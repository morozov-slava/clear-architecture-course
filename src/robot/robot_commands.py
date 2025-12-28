from . import pure_robot as pr


class RobotCommand:
    def execute(self, transfer, state: pr.RobotState):
        raise NotImplementedError("Method must be implemented in child class")


class Move(RobotCommand):
    def __init__(self, dist):
        self.dist = dist

    def execute(self, transfer, state):
        return pr.move(transfer, self.dist, state)


class Turn(RobotCommand):
    def __init__(self, angle):
        self.angle = angle

    def execute(self, transfer, state):
        return pr.turn(transfer, self.angle, state)


class SetState(RobotCommand):
    def __init__(self, mode):
        self.mode = mode

    def execute(self, transfer, state):
        return pr.set_state(transfer, self.mode, state)


class Start(RobotCommand):
    def execute(self, transfer, state):
        return pr.start(transfer, state)


class Stop(RobotCommand):
    def execute(self, transfer, state):
        return pr.stop(transfer, state)



def make(transfer, commands: list[RobotCommand], initial_state: pr.RobotState):
    current_state = initial_state
    for cmd in commands:
        current_state = cmd.execute(transfer, current_state)
    return current_state
