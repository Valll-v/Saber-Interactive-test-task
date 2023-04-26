from commands import *
from exceptions import UndefinedCommandException


class CommandManager:

    def __init__(self):
        self.commands = {
            'help': HelpCommand().execute,
            'list': ListCommand().execute,
            'get': GetCommand().execute,
            'exit': ExitCommand().execute,
        }

    def execute_command(self, command, option=None, arg=None, data=None):
        command_for_execute = self.commands.get(command)
        if not command_for_execute:
            print(f'Команды {command} не найдено')
            return
        return command_for_execute(option, arg, data)
