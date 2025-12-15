from . import pure_robot as pr
from .base_robot import (
    BaseRobot
)


class RobotCleaner(BaseRobot):
    def __init__(self, state, transfer):
        super().__init__(state, transfer)  # вызов конструктора абстрактного класса

    def move(self, distance: int):
        self.state = pr.move(self.transfer, distance, self.state)
        return self

    def turn(self, angle: int):
        self.state = pr.turn(self.transfer, angle, self.state)
        return self
    
    def set_mode(self, mode: str):
        self.state = pr.set_state(self.transfer, mode, self.state)
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


