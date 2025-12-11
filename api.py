import src.robot.pure_robot as pr


class RobotCleaner:
    def __init__(self):
        self.state = pr.RobotState(0, 0, 0, pr.WATER)
        self.transfer = pr.transfer_to_cleaner

    def move(self, distance: int):
        self.state = pr.move(self.transfer, distance, self.state)
        return self

    def turn(self, angle: int):
        self.state = pr.turn(self.transfer, angle, self.state)
        return self

    def set_water_mode(self):
        self.state = pr.set_state(self.transfer, "water", self.state)
        return self

    def set_soap_mode(self):
        self.state = pr.set_state(self.transfer, "soap", self.state)
        return self

    def set_brush_mode(self):
        self.state = pr.set_state(self.transfer, "brush", self.state)
        return self

    def start(self):
        self.state = pr.start(self.transfer, self.state)
        return self

    def stop(self):
        self.state = pr.stop(self.transfer, self.state)
        return self

    def run_script(self, code: list[str]):
        self.state = pr.make(self.transfer, code, self.state)
        return self

    def get_position(self) -> tuple[float, float, int]:
        return self.state.x, self.state.y, self.state.angle
    
    def get_mode(self) -> str:
        return self.state.state



if __name__ == "__main__":
    robot = RobotCleaner()
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