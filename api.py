from dataclasses import dataclass
import src.robot.pure_robot as pr


@dataclass
class Result:
    status: int
    state: pr.RobotState | None
    error_info: str | None


class RobotCleanerApi:

    @staticmethod
    def move(state: pr.RobotState, distance: int) -> Result:
        try:
            new_state = pr.move(pr.transfer_to_cleaner, distance, state)
            return Result(200, new_state)
        except Exception as e:
            return Result(400, None, str(e))

    @staticmethod
    def turn(state: pr.RobotState, angle: int) -> Result:
        try:
            new_state = pr.turn(pr.transfer_to_cleaner, angle, state)
            return Result(200, new_state)
        except Exception as e:
            return Result(400, None, str(e))

    @staticmethod
    def set_mode(state: pr.RobotState, mode: str) -> Result:
        new_state = pr.set_state(pr.transfer_to_cleaner, mode, state)
        return Result(200, new_state)

    @staticmethod
    def start(state: pr.RobotState) -> Result:
        return Result(200, pr.start(pr.transfer_to_cleaner, state))

    @staticmethod
    def stop(state: pr.RobotState) -> Result:
        return Result(200, pr.stop(pr.transfer_to_cleaner, state))


def run_script(initial_state: pr.RobotState, code: list[str]) -> Result:
    state = initial_state
    for command in code:
        parts = command.split()
        if parts[0] == "move":
            result = RobotCleanerApi.move(state, int(parts[1]))
        elif parts[0] == "turn":
            result = RobotCleanerApi.turn(state, int(parts[1]))
        elif parts[0] == "set":
            result = RobotCleanerApi.set_mode(state, parts[1])
        elif parts[0] == "start":
            result = RobotCleanerApi.start(state)
        elif parts[0] == "stop":
            result = RobotCleanerApi.stop(state)
        if result.status == 400:
            return result
        state = result.state
    return Result(200, state)

