import math
from src.robot.state import RobotState
from src.robot.events import (
    Event,
    RobotMoved,
    RobotTurned,
    RobotStateChanged,
)


class StateProjector:
    def __init__(self, initial_state: RobotState):
        self.initial_state = initial_state

    def project(self, events: list[Event]) -> RobotState:
        state = self.initial_state
        for event in events:
            state = self._apply(state, event)
        return state

    def _apply(self, state: RobotState, event: Event) -> RobotState:
        if isinstance(event, RobotMoved):
            angle = math.radians(state.angle)
            return RobotState(
                x=state.x + event.distance * math.cos(angle),
                y=state.y + event.distance * math.sin(angle),
                angle=state.angle,
                state=state.state,
            )

        if isinstance(event, RobotTurned):
            return RobotState(
                x=state.x,
                y=state.y,
                angle=state.angle + event.angle,
                state=state.state,
            )

        if isinstance(event, RobotStateChanged):
            return RobotState(
                x=state.x,
                y=state.y,
                angle=state.angle,
                state=event.new_state.value,
            )

        return state
