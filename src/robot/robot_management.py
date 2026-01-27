

class RobotMonade:
    def __init__(self, run):
        self._run = run

    def run(self, state):
        return self._run(state)

    def bind(self, f):
        def chained(state):
            cap, new_state = self._run(state)
            return f(cap).run(new_state)
        return RobotMonade(chained)


