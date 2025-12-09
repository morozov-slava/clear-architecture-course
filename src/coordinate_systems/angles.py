from dataclasses import dataclass


@dataclass
class AngleDegrees:
    value: int

    def __post_init__(self):
        self.value = self.value % 360   # normalize angle

    def __add__(self, other):
        if isinstance(other, AngleDegrees):
            return AngleDegrees(self.value + other.value)
        raise NotImplementedError("Only available to sum for 'AngleDegrees' object types")