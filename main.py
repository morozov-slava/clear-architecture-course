from src.robot.robot_management import (
    moveM,
    turnM,
    startM,
    stopM,
    setStateM,
)
import src.robot.pure_robot as pr


program = (
    setStateM(pr.transfer_to_cleaner, 'water')
    .bind(lambda _: moveM(pr.transfer_to_cleaner, 10))
    .bind(lambda _: turnM(pr.transfer_to_cleaner, 90))
    .bind(lambda _: moveM(pr.transfer_to_cleaner, 5))
    .bind(lambda _: startM(pr.transfer_to_cleaner))
    .bind(lambda _: stopM(pr.transfer_to_cleaner))
)

initial_state = pr.RobotState(0, 0, 0, pr.WATER)
_, final_state = program.run(initial_state)

print(final_state)
