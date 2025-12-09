from src.coordinate_systems.angles import AngleDegrees
from src.coordinate_systems.descart_coordinate_system import DescartesCoordinate
from src.robot.robot import Robot
from src.robot.robot_controller import RobotController


def main():
    robot = Robot(
        coordinate=DescartesCoordinate(x=0.0, y=0.0), 
        angle=AngleDegrees(value=0)
    )
    robot_commands_runner = RobotController(robot)

    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop',
        'set water',
        'turn 45',
        'move 150',
        'start',
        'move 10',
        'stop'
    ]
    for command in commands:
        robot_commands_runner.execute(command)


if __name__ == "__main__":
    main()


