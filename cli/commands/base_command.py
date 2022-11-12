"""Abstract base class for all CLI commands."""
import argparse
from abc import ABC, abstractmethod

from cli.command_output import CommandResult, CommandResultStatus
from connection.database import DataBaseConnection
from factory import Factory


class BaseCommand(ABC):
    """Abstract base class for all CLI commands."""

    # pylint: disable=protected-access

    def __init__(self) -> None:
        self._factory = Factory()

    @property
    @staticmethod
    @abstractmethod
    def command_name() -> str:
        """Returns the name of the command."""

    @staticmethod
    @abstractmethod
    def parser_sub_parser(sub_parsers: argparse._SubParsersAction) -> None:
        """Register the sub parser for this command"""

    @abstractmethod
    def handle(
        self, connection: DataBaseConnection, args: argparse.Namespace
    ) -> CommandResult:
        """Handle the command."""

    @staticmethod
    def _add_table_arguments_to_sub_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--table",
            nargs="?",
            const=None,
            type=str,
            help="name of the table, containing the schema",
        )


# TODO: check types for mypy
def _requires_table(func):  # type: ignore
    """Decorator to check if a table name is provided in arguments."""

    def decorator(self, *args, **kwargs):  # type: ignore
        for i in args:
            if isinstance(i, argparse.Namespace):
                if i.table is None or i.table == "":
                    return CommandResult(
                        CommandResultStatus.ERROR, "No table name provided."
                    )
        return func(self, *args, **kwargs)

    return decorator
