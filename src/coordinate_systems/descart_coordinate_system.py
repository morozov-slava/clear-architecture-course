from dataclasses import dataclass


@dataclass
class DescartesCoordinate:
    x: float
    y: float

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return f"{self.x}, {self.y}"