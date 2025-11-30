import math
from typing import Literal
from dataclasses import dataclass
from decimal import Decimal

from .coordinates_system import (
    DescartesCoordinate,
    AngleDegrees
)


@dataclass
class DeviceType:
    name: Literal["water", "soap", "brush"]


class Device:
    def __init__(self, device_type: DeviceType):
        self.device_type = device_type
        self.is_started = False

    def start(self) -> None:
        self.is_started = True

    def stop(self) -> None:
        self.is_started = False

    def is_started(self) -> bool:
        return self.is_started
    
    def __str__(self):
        return f"{self.device_type}"

    def __repr__(self):
        return f"{self.device_type}"


class Robot:
    def __init__(self, coordinate: DescartesCoordinate, angle: AngleDegrees):
        self.coordinate = coordinate
        self.angle = angle
        self.device = None

    def move(self, distance_meters: int) -> None:
        if distance_meters < 0:
            raise ValueError("Distance must be >= 0")
        print(f"Initial POS {self.coordinate.x} {self.coordinate.y}")
        self.coordinate.x += round(distance_meters * math.cos(math.radians(self.angle.value)), 6)
        self.coordinate.y += round(distance_meters * math.sin(math.radians(self.angle.value)), 6)
        print(f"POS {self.coordinate.x} {self.coordinate.y}")
        
    def turn(self, angle_degree: float) -> None:
        self.angle += AngleDegrees(angle_degree)
        print(f"ANGLE {self.angle}")

    def set(self, device_type: str) -> None:
        self.device = Device(device_type)
        print(f"STATE: {device_type}")

    def start(self) -> None:
        if self.device is None:
            raise AssertionError("Device is not set. You can set the device with 'set' command")
        self.device.start()
        print(f"START WITH {self.device}")

    def stop(self) -> None:
        if self.device is None:
            raise AssertionError("Device is not set. You can set the device with 'set' command")
        self.device.stop()
        print(f"STOP: {self.device}")


class RobotCommandsRunner:
    def __init__(self, robot: Robot):
        self.robot = robot

    def run(self, command: str) -> None:
        components = command.split()
        if len(components) == 1:
            if components[0] == "start":
                self.robot.start()
            if components[0] == "stop":
                self.robot.stop()
        elif len(components) == 2:
            if components[0] == "move":
                param = int(components[1])
                self.robot.move(param)
            if components[0] == "turn":
                param = int(components[1])
                self.robot.turn(param)
            if components[0] == "set":
                param = str(components[1])
                self.robot.set(param)
        else:
            raise NotImplementedError("Can't parse unknown command")