from src.robot.start import program_start, initial_state
import src.robot.pure_robot as pr

program = (
    program_start(pr.transfer_to_cleaner)
    .bind(lambda r: r.move(10))
    .bind(lambda r: r.turn(90))
    .bind(lambda r: r.move(5))
    .bind(lambda r: r.set_mode("water"))
    .bind(lambda r: r.start())
    .bind(lambda r: r.stop())
)

caps, final_state = program.run(initial_state())
print(final_state)
