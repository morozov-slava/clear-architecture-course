import math
from typing import Callable, Optional

from .state import (
    RobotState, 
    CleaningMode
)


def transfer_to_cleaner(message):
    print(message)


class CommandNode:
    def __init__(self, next_node: Optional[Callable]=None):
        self.next_node = next_node

    def interpret(self, transfer, state: RobotState):
        raise NotImplementedError("Method must be implemented in child class")


class Move(CommandNode):
    def __init__(self, distance: float, next_node: Optional[Callable]=None):
        super().__init__(next_node)
        self.distance = distance

    def interpret(self, transfer, state: RobotState):
        angle_rads = state.angle * math.pi / 180.0
        new_state = RobotState(
            state.x + self.distance * math.cos(angle_rads),
            state.y + self.distance * math.sin(angle_rads),
            state.angle,
            state.state
        )
        transfer(('POS', new_state.x, new_state.y))
        if self.next_node:
            next_command = self.next_node(transfer, new_state)
            return next_command.interpret(transfer, new_state)
        return new_state


class Turn(CommandNode):
    def __init__(self, angle: float, next_node: Optional[Callable]=None):
        super().__init__(next_node)
        self.angle = angle

    def interpret(self, transfer, state: RobotState):
        new_state = RobotState(
            state.x,
            state.y,
            state.angle + self.angle,
            state.state
        )
        transfer(('ANGLE', new_state.angle))
        if self.next_node:
            next_command = self.next_node(transfer, new_state)
            return next_command.interpret(transfer, new_state)
        return new_state


class SetState(CommandNode):
    def __init__(self, mode: str, next_node: Optional[Callable]=None):
        super().__init__(next_node)
        self.mode = mode

    def interpret(self, transfer, state: RobotState):
        if self.mode.lower() == 'water':
            new_mode = CleaningMode.WATER
        elif self.mode.lower() == 'soap':
            new_mode = CleaningMode.SOAP
        elif self.mode.lower() == 'brush':
            new_mode = CleaningMode.BRUSH
        else:
            raise ValueError("Unknown state for robot")
        new_state = RobotState(state.x, state.y, state.angle, new_mode)
        transfer(('STATE', new_mode))
        if self.next_node:
            next_command = self.next_node(transfer, new_state)
            return next_command.interpret(transfer, new_state)
        return new_state


class Start(CommandNode):

    def interpret(self, transfer, state: RobotState):
        transfer(('START WITH', state.state))
        if self.next_node:
            next_command = self.next_node(transfer, state)
            return next_command.interpret(transfer, state)
        return state


class Stop(CommandNode):
    
    def interpret(self, transfer, state: RobotState):
        transfer(('STOP',))
        return state
