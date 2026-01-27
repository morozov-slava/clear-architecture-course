from .robot_management import RobotMonade
from . import pure_robot as pr


class IdleCaps:
    def __init__(self, transfer):
        self._transfer = transfer

    def move(self, dist):
        return RobotMonade(
            lambda s: (IdleCaps(self._transfer),
                       pr.move(self._transfer, dist, s))
        )

    def turn(self, angle):
        return RobotMonade(
            lambda s: (IdleCaps(self._transfer),
                       pr.turn(self._transfer, angle, s))
        )

    def set_mode(self, mode):
        return RobotMonade(
            lambda s: (ReadyCaps(self._transfer),
                       pr.set_mode(self._transfer, mode, s))
        )



class ReadyCaps:
    def __init__(self, transfer):
        self._transfer = transfer

    def set_mode(self, mode):
        return RobotMonade(
            lambda s: (ReadyCaps(self._transfer),
                       pr.set_mode(self._transfer, mode, s))
        )

    def start(self):
        return RobotMonade(
            lambda s: (CleaningCaps(self._transfer),
                       pr.start(self._transfer, s))
        )



class CleaningCaps:
    def __init__(self, transfer):
        self._transfer = transfer

    def stop(self):
        return RobotMonade(
            lambda s: (IdleCaps(self._transfer),
                       pr.stop(self._transfer, s))
        )
