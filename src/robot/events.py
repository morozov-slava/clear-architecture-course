from dataclasses import dataclass
from abc import ABC
from src.robot.state import CleaningMode


class Event(ABC):
    pass


@dataclass(frozen=True)
class MoveRequested(Event):
    distance: float


@dataclass(frozen=True)
class TurnRequested(Event):
    angle: float


@dataclass(frozen=True)
class SetStateRequested(Event):
    new_state: CleaningMode


@dataclass(frozen=True)
class StartRequested(Event):
    pass


@dataclass(frozen=True)
class StopRequested(Event):
    pass


@dataclass(frozen=True)
class RobotMoved(Event):
    distance: float


@dataclass(frozen=True)
class RobotTurned(Event):
    angle: float


@dataclass(frozen=True)
class RobotStateChanged(Event):
    new_state: CleaningMode


@dataclass(frozen=True)
class RobotStarted(Event):
    pass


@dataclass(frozen=True)
class RobotStopped(Event):
    pass
