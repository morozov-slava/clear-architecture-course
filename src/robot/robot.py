import math
from typing import Literal
from dataclasses import dataclass

from src.coordinate_systems.angles import AngleDegrees
from src.coordinate_systems.descart_coordinate_system import DescartesCoordinate



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

