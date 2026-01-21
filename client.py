from src.robot.state import RobotState, CleaningMode
from src.robot.commands import (
    CommandNode,
    Move,
    Turn,
    SetState,
    Start,
    Stop,
    transfer_to_cleaner
)


def build_program():
    program = Move(100, 
            next_node=lambda t,s: Turn(-90, 
                next_node=lambda t,s: SetState('soap', 
                    next_node=lambda t,s: Move(50,
                        next_node=lambda t,s: Stop()
                    )
                )
            )
        )
    return program


def run_program(program: CommandNode, initial_state: RobotState, transfer,):
    return program.interpret(transfer, initial_state)


def main():
    initial_state = RobotState(0, 0 , 0, CleaningMode.WATER)
    ast_program = build_program()
    final_state = run_program(ast_program, initial_state, transfer_to_cleaner)
    print("Final state:", final_state)



if __name__ == "__main__":
    main()
