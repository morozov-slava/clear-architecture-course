from .state import RobotState
from .commands import RobotCommand


class RobotCommandsRunner:
    def __init__(self, state: RobotState):
        self.state = state

    def run(self, commands: list[RobotCommand], transfer) -> RobotState:
        new_state = self.state
        for command in commands:
            new_state = command.execute(transfer, new_state)
        return new_state