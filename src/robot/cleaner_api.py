from typing import Callable

from . import pure_robot as pr


def get_robot_command_by_name(command_name: str) -> Callable:
    commands = {
        "move": pr.move,
        "turn": pr.turn,
        "set": pr.set_state,
        "start": pr.start,
        "stop": pr.stop
    }
    return commands.get(command_name)


class RobotApi:

    def setup(self, robot_commands, f_transfer):
        self.robot_commands = robot_commands
        self.f_transfer = f_transfer

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pr.RobotState(0.0, 0.0, 0, pr.WATER)

        cmd = command.split(' ')
        command_func = self.robot_commands(cmd[0])
        if cmd[0] == 'move':
            self.cleaner_state = command_func(
                 self.f_transfer, int(cmd[1]), self.cleaner_state
            ) 
        elif cmd[0] == 'turn':
            self.cleaner_state = command_func(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == 'set':
            self.cleaner_state = command_func(
                self.f_transfer, cmd[1], self.cleaner_state
            ) 
        elif cmd[0] == 'start':
            self.cleaner_state = command_func(
                self.f_transfer, self.cleaner_state
            )
        elif cmd[0] == 'stop':
            self.cleaner_state = command_func(
                self.f_transfer, self.cleaner_state
            )
        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print (message)


def double_move(transfer,dist,state):
    return pr.move(transfer,dist*2,state)



api = RobotApi()    
api.setup(get_robot_command_by_name, transfer_to_cleaner)
