import src.robot.pure_robot as pr
from src.robot.interpretator import run_interpreter


code = "100 move -90 turn soap set start 50 move stop"
final_state = run_interpreter(code, pr.transfer_to_cleaner)
print(final_state)

