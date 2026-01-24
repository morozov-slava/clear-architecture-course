from src.robot.state import (
    CleaningMode,
    RobotState
)
from src.robot.commands import (
    Move,
    Turn,
    SetState,
    Start,
    Stop,
    transfer_to_cleaner
)
from src.robot.commands_runner import RobotCommandsRunner


def main():
    robot = RobotState(x=0.0, y=0.0, angle=0, state=CleaningMode.WATER)
    robot_commands_runner = RobotCommandsRunner(robot)
    commands = [
        Move(30),
        Turn(90),
        Move(5),
        Start(),
        SetState("soap"),
        Move(10),
        Stop()
    ]
    new_state = robot_commands_runner.run(commands, transfer_to_cleaner)
    print(new_state)


if __name__ == "__main__":
    main()


