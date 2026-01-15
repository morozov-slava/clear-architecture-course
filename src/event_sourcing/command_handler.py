from src.robot.commands import (
    MoveCommand,
    TurnCommand,
    SetStateCommand,
    StartCommand,
    StopCommand,
)
from src.robot.events import (
    MoveRequested,
    TurnRequested,
    SetStateRequested,
    StartRequested,
    StopRequested,
)
from .event_store import EventStore


class CommandHandler:
    def __init__(self, store: EventStore):
        self.store = store

    def handle(self, robot_id: str, command) -> None:
        if isinstance(command, MoveCommand):
            self.store.append(robot_id, MoveRequested(command.distance))

        elif isinstance(command, TurnCommand):
            self.store.append(robot_id, TurnRequested(command.angle))

        elif isinstance(command, SetStateCommand):
            self.store.append(robot_id, SetStateRequested(command.new_state))

        elif isinstance(command, StartCommand):
            self.store.append(robot_id, StartRequested())

        elif isinstance(command, StopCommand):
            self.store.append(robot_id, StopRequested())
