import math
from abc import ABC, abstractmethod

from .state import (
    CleaningMode,
    RobotState
)


def transfer_to_cleaner(message):
    print(message)


class RobotCommand(ABC):

    @abstractmethod
    def execute(self, transfer, state: RobotState) -> RobotState:
        raise NotImplementedError("Method must be implemented in child class")


class Move(RobotCommand):
    def __init__(self, dist):
        self.dist = dist

    def execute(self, transfer, state):
        angle_rads = state.angle * (math.pi/180.0)   
        new_state = RobotState(
            state.x + self.dist * math.cos(angle_rads),
            state.y + self.dist * math.sin(angle_rads),
            state.angle,
            state.state
        )  
        transfer(('POS(',new_state.x,',',new_state.y,')'))
        return new_state


class Turn(RobotCommand):
    def __init__(self, angle):
        self.angle = angle

    def execute(self, transfer, state):
        new_state = RobotState(
            state.x,
            state.y,
            state.angle + self.angle,
            state.state
        )
        transfer(("ANGLE", state.angle))
        return new_state


class SetState(RobotCommand):
    def __init__(self, mode):
        self.mode = mode

    def execute(self, transfer, state):
        if self.mode == 'water':
            new_mode = CleaningMode.WATER  
        elif self.mode == 'soap':
            new_mode = CleaningMode.SOAP
        elif self.mode == 'brush':
            new_mode = CleaningMode.BRUSH
        else:
            return state
        new_state = RobotState(
            state.x,
            state.y,
            state.angle,
            new_mode
        )
        transfer(('STATE', new_mode))
        return new_state


class Start(RobotCommand):
    def execute(self, transfer, state):
        transfer(('START WITH', state.state))
        return state


class Stop(RobotCommand):
    def execute(self, transfer, state):
        transfer(('STOP',))
        return state





# @dataclass
# class ParsedCommand:
#     name: str
#     params: list[str]


# class CommandParser:

#     @staticmethod
#     def parse(command: str) -> ParsedCommand:
#         parsed_command = command.split()
#         if len(parsed_command) == 1:
#             return ParsedCommand(
#                 name=parsed_command[0],
#                 params=[]
#             )
#         elif len(parsed_command) > 1:
#             return ParsedCommand(
#                 name=parsed_command[0],
#                 params=parsed_command[1:]
#             )
#         else:
#             raise ValueError("Invalid input command")


# class Command(Protocol):
#     def execute(self, robot: Robot, params: list[str]) -> None:
#         raise NotImplementedError("Base command class to set signature")


# class StartCommand:
#     def execute(self, robot: Robot, params: list[str]):
#         robot.start()


# class StopCommand:
#     def execute(self, robot: Robot, params: list[str]):
#         robot.stop()


# class MoveCommand:
#     def execute(self, robot: Robot, params: list[str]):
#         robot.move(int(params[0]))


# class TurnCommand:
#     def execute(self, robot: Robot, params: list[str]):
#         robot.turn(int(params[0]))


# class SetCommand:
#     def execute(self, robot: Robot, params: list[str]):
#         robot.set(DeviceType(params[0]))


# class RobotCommandsRunner:
#     def __init__(self, robot: Robot):
#         self.robot = robot
#         self.commands: dict[str, Command] = {
#             "start": StartCommand(),
#             "stop": StopCommand(),
#             "move": MoveCommand(),
#             "turn": TurnCommand(),
#             "set": SetCommand(),
#         }

#     def run(self, command: str) -> None:
#         parsed_command = CommandParser.parse(command)
#         robot_command = self.commands.get(parsed_command.name)
#         if robot_command is None:
#             raise ValueError(f"Unknown command: {parsed_command.name}")
#         robot_command.execute(self.robot, parsed_command.params)




