from src.robot.events import (
    Event,
    MoveRequested,
    TurnRequested,
    SetStateRequested,
    StartRequested,
    StopRequested,
    RobotMoved,
    RobotTurned,
    RobotStateChanged,
    RobotStarted,
    RobotStopped,
)
from src.event_sourcing.event_store import EventStore
from src.event_sourcing.projector import StateProjector


class RobotProcessor:
    def __init__(self, store: EventStore, projector: StateProjector):
        self.store = store
        self.projector = projector

    def handle(self, robot_id: str, event: Event) -> None:
        events = self.store.get_events(robot_id)
        self.projector.project(events)

        if isinstance(event, MoveRequested):
            self.store.append(robot_id, RobotMoved(event.distance))
        elif isinstance(event, TurnRequested):
            self.store.append(robot_id, RobotTurned(event.angle))
        elif isinstance(event, SetStateRequested):
            self.store.append(robot_id, RobotStateChanged(event.new_state))
        elif isinstance(event, StartRequested):
            self.store.append(robot_id, RobotStarted())
        elif isinstance(event, StopRequested):
            self.store.append(robot_id, RobotStopped())
