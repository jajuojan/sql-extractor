"""TBD"""

import argparse
from typing import List, Type

from cli.command_output import CommandResult, CommandResultStatus
from cli.commands.base_command import BaseCommand
from cli.commands.print_create_table import PrintCreateTableCommand
from cli.commands.print_insert import PrintInsertCommand
from cli.commands.print_table_structure import PrintTableStructureCommand
from factory import Factory

_commands: List[Type[BaseCommand]] = [
    PrintCreateTableCommand,
    PrintInsertCommand,
    PrintTableStructureCommand,
]


class CommandHandler:
    """Handler for the command line interface."""

    def __init__(self) -> None:
        self._factory = Factory()

    def handle(self) -> CommandResult:
        """Parse the command line arguments and execute the command."""
        args = self._parse_args()

        connection = self._factory.get_connection(args.dialect, args.connection_string)

        for c in _commands:
            if c.command_name() == args.command:
                return c().handle(connection, args)

        return CommandResult(CommandResultStatus.ERROR, "Unknown command.")

    def _parse_args(self) -> argparse.Namespace:
        """Parse the command line arguments."""
        parser = argparse.ArgumentParser(description="My string.")
        # TODO: could this be derived from connection-string?
        parser.add_argument(
            "--dialect",
            nargs="?",
            default="tsql",
            type=str,
            choices=self._factory.allowed_dialects(),
        )
        parser.add_argument("--connection-string", nargs="?", default="local", type=str)

        sub_parsers = parser.add_subparsers(dest="command", required=True)
        for c in _commands:
            c.parser_sub_parser(sub_parsers)

        args = parser.parse_args()
        return args
