from src.robot.cleaner_api import api


def main():
    api('move 100')
    api('turn -90')
    api('set soap')
    api('start')
    api('move 50')
    api('stop')


if __name__ == "__main__":
    main()