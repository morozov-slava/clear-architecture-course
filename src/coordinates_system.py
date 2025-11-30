from dataclasses import dataclass
from decimal import Decimal


@dataclass
class DescartesCoordinate:
    x: float
    y: float

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return f"{self.x}, {self.y}"


@dataclass
class AngleDegrees:
    value: int

    def __post_init__(self):
        self.value = self.value % 360   # normalize angle

    def __add__(self, other):
        if isinstance(other, AngleDegrees):
            return AngleDegrees(self.value + other.value)
        raise NotImplementedError("Only available to sum for 'AngleDegrees' object types")
    

