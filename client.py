import src.robot.robot_commands as rc
import src.robot.pure_robot as pr
from src.robot.event_sourcing import (
    EventStore,
    CommandHandler 
)


def main():
    initial_state = pr.RobotState(0, 0, 0, pr.WATER)
    cleaner_transfer = pr.transfer_to_cleaner
    event_store = EventStore()
    command_handler = CommandHandler(
        event_store=event_store,
        initial_state=initial_state,
        transfer=cleaner_transfer
    )

    command_handler.run(rc.Move(10))
    command_handler.run(rc.Turn(90))
    command_handler.run(rc.Move(5))
    command_handler.run(rc.SetState('soap'))
    command_handler.run(rc.SetState('soap'))
    command_handler.run(rc.Start())
    command_handler.run(rc.Stop())

    current_state = rc.make(
        transfer=cleaner_transfer,
        commands=event_store.get_events(),
        initial_state=initial_state
    )
    print("Текущая позиция:", current_state)


if __name__ == "__main__":
    main()