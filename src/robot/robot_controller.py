from typing import Protocol

from .robot import (
    Robot, 
    DeviceType
)
from .commands_parsing import CommandParser


class Command(Protocol):
    def execute(self, robot: Robot, params: list[str]) -> None:
        raise NotImplementedError("Base command class to set signature")


class StartCommand:
    def execute(self, robot: Robot, params: list[str]):
        robot.start()


class StopCommand:
    def execute(self, robot: Robot, params: list[str]):
        robot.stop()


class MoveCommand:
    def execute(self, robot: Robot, params: list[str]):
        robot.move(int(params[0]))


class TurnCommand:
    def execute(self, robot: Robot, params: list[str]):
        robot.turn(int(params[0]))


class SetCommand:
    def execute(self, robot: Robot, params: list[str]):
        robot.set(DeviceType(params[0]))


class RobotController:
    def __init__(self, robot: Robot):
        self.robot = robot
        self.commands: dict[str, Command] = {
            "start": StartCommand(),
            "stop": StopCommand(),
            "move": MoveCommand(),
            "turn": TurnCommand(),
            "set": SetCommand(),
        }

    def execute(self, command: str) -> None:
        parsed_command = CommandParser.parse(command)
        robot_command = self.commands.get(parsed_command.name)
        if robot_command is None:
            raise ValueError(f"Unknown command: {parsed_command.name}")
        robot_command.execute(self.robot, parsed_command.params)