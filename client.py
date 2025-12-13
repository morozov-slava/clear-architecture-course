from src.robot import pure_robot as pr
from api import run_script


initial = pr.RobotState(0, 0, 0, pr.WATER)

result = run_script(
    initial,
    [
        "move 100",
        "turn -90",
        "set soap",
        "start",
        "move 50",
        "stop"
    ]
)

print(result.state)
