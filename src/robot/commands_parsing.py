from dataclasses import dataclass


@dataclass
class ParsedCommand:
    name: str
    params: list[str]


class CommandParser:

    @staticmethod
    def parse(command: str) -> ParsedCommand:
        parsed_command = command.split()
        if len(parsed_command) == 1:
            return ParsedCommand(
                name=parsed_command[0],
                params=[]
            )
        elif len(parsed_command) > 1:
            return ParsedCommand(
                name=parsed_command[0],
                params=parsed_command[1:]
            )
        else:
            raise ValueError("Invalid input command")