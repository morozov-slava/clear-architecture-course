from . import pure_robot as pr


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __repr__(self):
        return repr(self.stack)


def parse_token(token: str):
    try:
        return int(token)
    except ValueError:
        return token


def cmd_move(stack, transfer):
    dist = stack.pop()
    state = stack.pop()
    new_state = pr.move(transfer, dist, state)
    stack.push(new_state)


def cmd_turn(stack, transfer):
    angle = stack.pop()
    state = stack.pop()
    new_state = pr.turn(transfer, angle, state)
    stack.push(new_state)


def cmd_set(stack, transfer):
    mode = stack.pop()
    state = stack.pop()
    new_state = pr.set_state(transfer, mode, state)
    stack.push(new_state)


def cmd_start(stack, transfer):
    state = stack.pop()
    stack.push(pr.start(transfer, state))


def cmd_stop(stack, transfer):
    state = stack.pop()
    stack.push(pr.stop(transfer, state))


COMMANDS = {
    "move": cmd_move,
    "turn": cmd_turn,
    "set": cmd_set,
    "start": cmd_start,
    "stop": cmd_stop,
}


def run_interpreter(code: str, transfer):
    stack = Stack()
    stack.push(pr.RobotState(0, 0, 0, pr.WATER))
    tokens = code.split()
    for raw in tokens:
        token = parse_token(raw)
        if token in COMMANDS:
            COMMANDS[token](stack, transfer)
        else:
            stack.push(token)
    return stack.pop()
