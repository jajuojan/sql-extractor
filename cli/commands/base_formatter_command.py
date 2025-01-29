"""tbd"""

import argparse
from abc import ABCMeta, abstractmethod

from cli.command_output import CommandResult, CommandResultStatus
from cli.commands.base_command import BaseCommand, _requires_table
from connection.database import DataBaseConnection
from formatters.base_formatter import FormatterType


class BaseFormatterCommand(BaseCommand, metaclass=ABCMeta):
    """Abstract base class for formatter commands."""

    @abstractmethod
    def _get_formatter_type(self) -> FormatterType:
        """Returns the formatter type."""

    @_requires_table
    def handle(
        self, connection: DataBaseConnection, args: argparse.Namespace
    ) -> CommandResult:
        """Prints the create table statement for the given table."""
        fetcher = self._factory.get_table_fetcher(connection)
        table = fetcher.fetch_table_with_name(args.table)
        sql = self._factory.get_formatter(
            args.dialect, self._get_formatter_type()
        ).format(table)
        print(sql)
        return CommandResult(CommandResultStatus.SUCCESS)
