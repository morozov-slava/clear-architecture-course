import src.robot.pure_robot as pr
from src.robot.robot_cleaner import RobotCleaner


class RobotCleanerApi:
    def __init__(self):
        self.robot = RobotCleaner(
            state=pr.RobotState(0, 0, 0, pr.WATER),
            transfer=pr.transfer_to_cleaner
        )

    def move(self, distance: int):
        self.robot.move(distance)
        return self

    def turn(self, angle: int):
        self.robot.turn(angle)
        return self

    def set_water_mode(self):
        self.robot.set_mode("water")
        return self

    def set_soap_mode(self):
        self.robot.set_mode("soap")
        return self

    def set_brush_mode(self):
        self.robot.set_mode("brush")
        return self

    def start(self):
        self.robot.start()
        return self

    def stop(self):
        self.robot.stop()
        return self

    def run_script(self, code: list[str]):
        self.robot.run_script(code)
        return self

    def get_position(self) -> tuple[float, float, int]:
        return self.robot.get_x(), self.robot.get_y(), self.robot.get_angle()
    
    def get_mode(self) -> str:
        return self.robot.get_mode()



if __name__ == "__main__":
    robot = RobotCleanerApi()
    robot.run_script(
        [
            'move 100',
            'turn -90',
            'set soap',
            'start',
            'move 50',
            'stop'
        ]
    )
    print(robot.get_position())
    print(robot.get_mode())