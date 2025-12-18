import src.robot.pure_robot as pr
from src.robot.interface import (
    set_robot,
    set_transfer
)


def run_robot_cleaner(code: list[str]):
    state = set_robot(x=0, y=0, angle=0, state=pr.WATER)
    transfer = set_transfer(pr.transfer_to_cleaner)
    pr.make(transfer, code, state)
    

if __name__ == "__main__":
    run_robot_cleaner(
        [
            'move 100',
            'turn -90',
            'set soap',
            'start',
            'move 50',
            'stop'
        ]
    )