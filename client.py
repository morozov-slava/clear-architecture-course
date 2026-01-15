from src.robot.state import RobotState, CleaningMode
from src.robot.commands import (
    MoveCommand,
    TurnCommand,
    SetStateCommand,
    StartCommand,
    StopCommand,
)
from src.event_sourcing.event_store import EventStore
from src.event_sourcing.projector import StateProjector
from src.event_sourcing.processors import RobotProcessor
from src.event_sourcing.command_handler import CommandHandler


def main():
    robot_id = "robot-001"

    event_store = EventStore()
    initial_state = RobotState(0.0, 0.0, 0.0, CleaningMode.WATER.value)
    projector = StateProjector(initial_state)

    processor = RobotProcessor(event_store, projector)
    event_store.subscribe(processor.handle)

    command_handler = CommandHandler(event_store)

    commands = [
        MoveCommand(100),
        TurnCommand(-90),
        SetStateCommand(CleaningMode.SOAP),
        StartCommand(),
        MoveCommand(50),
        StopCommand(),
    ]

    for cmd in commands:
        command_handler.handle(robot_id, cmd)

    final_state = projector.project(event_store.get_events(robot_id))
    print("Текущее положение робота:", final_state)

    print("История событий:")
    for i, event in enumerate(event_store.get_events(robot_id), 1):
        print(f"{i}. {event}")


if __name__ == "__main__":
    main()
