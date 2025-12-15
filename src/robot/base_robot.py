from abc import ABC, abstractmethod

from . import pure_robot as pr


class BaseRobot(ABC):
    def __init__(self, state: pr.RobotState, transfer):
        self.state = state
        self.transfer = transfer

    @abstractmethod
    def move(self, distance: int):
        raise NotImplementedError("Method must be implemented in child class")
    
    @abstractmethod
    def turn(self, angle: int):
        raise NotImplementedError("Method must be implemented in child class")
    
    @abstractmethod
    def set_mode(self, mode: str):
        raise NotImplementedError("Method must be implemented in child class")
    
    @abstractmethod
    def start(self):
        raise NotImplementedError("Method must be implemented in child class")
    
    @abstractmethod
    def stop(self):
        raise NotImplementedError("Method must be implemented in child class")
    
    @abstractmethod
    def run_script(self, code: list[str]):
        raise NotImplementedError("Method must be implemented in child class")

    def get_x(self) -> float:
        return self.state.x
    
    def get_y(self) -> float:
        return self.state.y
    
    def get_angle(self) -> int:
        return self.state.angle
    
    def get_mode(self) -> str:
        return self.state.state
