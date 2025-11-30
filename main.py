from src.coordinates_system import (
    DescartesCoordinate,
    AngleDegrees
)
from src.robot import (
    Robot,
    RobotCommandsRunner
)


def main():
    robot = Robot(
        coordinate=DescartesCoordinate(x=0.0, y=0.0), 
        angle=AngleDegrees(value=0)
    )
    robot_commands_runner = RobotCommandsRunner(robot)

    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]
    for command in commands:
        robot_commands_runner.run(command)


if __name__ == "__main__":
    main()


