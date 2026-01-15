from dataclasses import dataclass

from src.robot.state import CleaningMode


@dataclass(frozen=True)
class MoveCommand:
    distance: float


@dataclass(frozen=True)
class TurnCommand:
    angle: float


@dataclass(frozen=True)
class SetStateCommand:
    new_state: CleaningMode


@dataclass(frozen=True)
class StartCommand:
    pass


@dataclass(frozen=True)
class StopCommand:
    pass
