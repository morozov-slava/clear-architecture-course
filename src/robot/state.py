from dataclasses import dataclass
from enum import Enum


class CleaningMode(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3


@dataclass(frozen=True)
class RobotState:
    x: float
    y: float
    angle: float
    state: int



