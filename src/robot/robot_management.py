from . import pure_robot as pr


class StateMonad:
    def __init__(self, fn):
        self.fn = fn

    def run(self, state):
        return self.fn(state)

    def bind(self, f):
        def new_fn(state):
            result, new_state = self.fn(state)
            return f(result).run(new_state)
        return StateMonad(new_fn)
    

def moveM(transfer, dist):
    return StateMonad(
        lambda state: (None, pr.move(transfer, dist, state))
    )


def turnM(transfer, angle):
    return StateMonad(
        lambda state: (None, pr.turn(transfer, angle, state))
    )


def setStateM(transfer, mode):
    return StateMonad(
        lambda state: (None, pr.set_state(transfer, mode, state))
    )


def startM(transfer):
    return StateMonad(
        lambda state: (None, pr.start(transfer, state))
    )

def stopM(transfer):
    return StateMonad(
        lambda state: (None, pr.stop(transfer, state))
    )
