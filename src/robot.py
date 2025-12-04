import math
from typing import Literal, Protocol
from dataclasses import dataclass

from .coordinates_system import (
    DescartesCoordinate,
    AngleDegrees
)


@dataclass
class DeviceType:
    name: Literal["water", "soap", "brush"]


class Robot:
    def __init__(self, coordinate: DescartesCoordinate, angle: AngleDegrees):
        self.coordinate = coordinate
        self.angle = angle
        self.device = None

    def move(self, distance_meters: int) -> None:
        if distance_meters < 0:
            raise ValueError("Distance must be >= 0")
        self.coordinate.x += round(distance_meters * math.cos(math.radians(self.angle.value)), 6)
        self.coordinate.y += round(distance_meters * math.sin(math.radians(self.angle.value)), 6)
        print(f"POS {self.coordinate.x} {self.coordinate.y}")
        
    def turn(self, angle_degree: float) -> None:
        self.angle += AngleDegrees(angle_degree)
        print(f"ANGLE {self.angle.value}")

    def set(self, device: DeviceType) -> None:
        self.device = device.name
        print(f"STATE: {self.device}")

    def start(self) -> None:
        if self.device is None:
            raise AssertionError("Device is not set. You can set the device with 'set' command")
        print(f"START WITH {self.device}")

    def stop(self) -> None:
        if self.device is None:
            raise AssertionError("Device is not set. You can set the device with 'set' command")
        print(f"STOP: {self.device}")


@dataclass
class ParsedCommand:
    name: str
    params: list[str]


class CommandParser:

    @staticmethod
    def parse(command: str) -> ParsedCommand:
        parsed_command = command.split()
        if len(parsed_command) == 1:
            return ParsedCommand(
                name=parsed_command[0],
                params=[]
            )
        elif len(parsed_command) > 1:
            return ParsedCommand(
                name=parsed_command[0],
                params=parsed_command[1:]
            )
        else:
            raise ValueError("Invalid input command")


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


class RobotCommandsRunner:
    def __init__(self, robot: Robot):
        self.robot = robot
        self.commands: dict[str, Command] = {
            "start": StartCommand(),
            "stop": StopCommand(),
            "move": MoveCommand(),
            "turn": TurnCommand(),
            "set": SetCommand(),
        }

    def run(self, command: str) -> None:
        parsed_command = CommandParser.parse(command)
        robot_command = self.commands.get(parsed_command.name)
        if robot_command is None:
            raise ValueError(f"Unknown command: {parsed_command.name}")
        robot_command.execute(self.robot, parsed_command.params)