import math
from typing import Callable

# входная программа управления роботом
input_commands = (
    'move 100',
    'turn -90',
    'set soap',
    'start',
    'move 50',
    'stop'
)

# текущие позиция и угол (ориентация) робота
x = 0.0
y = 0.0
angle = 0
device = None
current_command = None


def parse_input_command(command: str) -> list[str]:
    return command.split(" ")


def move_robot(distance: str) -> None:
    global x
    global y
    dist = int(distance)
    angle_rads = angle * (math.pi/180.0)
    x += dist * math.cos(angle_rads)
    y += dist * math.sin(angle_rads)
    print(f"POS('{x}','{y}')")


def turn_robot(turn_angle: str) -> None:
    global angle
    angle += int(turn_angle)
    print ('ANGLE', angle)


def set_device(device_type: str) -> None:
    global device
    if device_type == "water":
        device = "water"  
    elif device_type == "soap":
        device = "soap"
    elif device_type== "brush":
        device = "brush"
    else:
        NotImplementedError(f"Unknown device type '{device_type}'")
    print('STATE', device)


def start_device() -> None:
    print('START WITH', device)


def stop_device() -> None:
    print('STOP')


def make_action_by_robot(parsed_command: list[str]) -> None:
    robot_actions_dict = {
        "move": move_robot,
        "turn": turn_robot,
        "set": set_device,
        "start": start_device,
        "stop": stop_device
    }
    func = robot_actions_dict.get(parsed_command[0])
    if func is None:
        raise NotImplementedError(f"Unknown command: '{current_command[0]}'")
    if len(parsed_command) == 1:
        func()
    elif len(parsed_command) == 2:
        func(parsed_command[1])
    else:
        raise NotImplementedError(f"Unknown parsed data format")


def main():
    for command in input_commands:
        current_command = parse_input_command(command)
        make_action_by_robot(current_command)


if __name__ == "__main__":
    main()


