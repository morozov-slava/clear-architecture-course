from .pure_robot import RobotState
from .robot_commands import make


def is_possible_to_run_command(state: RobotState, command) -> bool:
    # TODO: потенциальное расширение функционала с проверкой
    return True


class EventStore:
    def __init__(self):
        self.events = []

    def add(self, new_events: list) -> None:
        self.events.extend(new_events)

    def get_events(self) -> list:
        return self.events


class CommandHandler:
    def __init__(self, event_store: EventStore, initial_state: RobotState, transfer):
        self.event_store = event_store
        self.initial_state = initial_state
        self.transfer = transfer

    def run(self, new_command) -> RobotState:
        # 1. Get all events
        events = self.event_store.get_events()
        # 2. Run all added commands and get current state
        current_state = make(self.transfer, events, self.initial_state)
        # 3. Check posibility to run command
        if not is_possible_to_run_command(current_state, new_command):
            raise AssertionError("Impossible to run command")
        # 4. Add new command to Event Store
        self.event_store.add([new_command])







