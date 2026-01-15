from typing import Callable
from src.robot.events import Event


class EventStore:
    def __init__(self):
        self.events: dict[str, list[Event]] = {}
        self.subscribers: list[Callable[[str, Event], None]] = []

    def subscribe(self, handler: Callable[[str, Event], None]) -> None:
        self.subscribers.append(handler)

    def append(self, robot_id: str, event: Event) -> None:
        self.events.setdefault(robot_id, []).append(event)
        for subscriber in self.subscribers:
            subscriber(robot_id, event)

    def get_events(self, robot_id: str) -> list[Event]:
        return self.events.get(robot_id, []).copy()
