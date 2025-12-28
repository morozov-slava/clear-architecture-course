import src.robot.pure_robot as pr
import src.robot.robot_commands as rc


initial_state = pr.RobotState(0, 0, 0, pr.WATER)

program = [
    rc.Move(10),
    rc.Turn(90),
    rc.Move(5),
    rc.SetState('soap'),
    rc.Start(),
    rc.Stop()
]

final_state = rc.make(pr.transfer_to_cleaner, program, initial_state)
