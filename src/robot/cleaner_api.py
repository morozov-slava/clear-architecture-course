from . import pure_robot as pr


class RobotApi:

    def setup(self, f_move, f_turn, f_set_state, f_start, f_stop, f_transfer):
        self.f_move = f_move
        self.f_turn = f_turn
        self.f_set_state = f_set_state
        self.f_start = f_start
        self.f_stop = f_stop
        self.f_transfer = f_transfer

    def make(self, command):
        if not hasattr(self, 'cleaner_state'):
            self.cleaner_state = pr.RobotState(0.0, 0.0, 0, pr.WATER)

        cmd = command.split(' ')
        if cmd[0] == 'move':
            self.cleaner_state = self.f_move(
                 self.f_transfer, int(cmd[1]), self.cleaner_state
            ) 
        elif cmd[0] == 'turn':
            self.cleaner_state = self.f_turn(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == 'set':
            self.cleaner_state = self.f_set_state(
                self.f_transfer, cmd[1], self.cleaner_state
            ) 
        elif cmd[0] == 'start':
            self.cleaner_state = self.f_start(
                self.f_transfer, self.cleaner_state
            )
        elif cmd[0] == 'stop':
            self.cleaner_state = self.f_stop(
                self.f_transfer, self.cleaner_state
            )
        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print (message)


def double_move(transfer,dist,state):
    return pr.move(transfer,dist*2,state)


if __name__ == "__main__":
    api = RobotApi()    
    api.setup(pr.move, pr.turn, pr.set_state, pr.start, pr.stop, transfer_to_cleaner)
