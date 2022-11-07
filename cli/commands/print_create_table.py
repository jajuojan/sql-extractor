"""TBD"""

import argparse

from cli.command_output import CommandResult, CommandResultStatus
from cli.commands.base_command import BaseCommand, _requires_table
from connection.database import DataBaseConnection
from formatters.base_formatter import FormatterType

_COMMAND_NAME = "print-create-table"


class PrintCreateTableCommand(BaseCommand):
    """Prints the create table statement for the given table."""

    @staticmethod
    def command_name() -> str:
        return _COMMAND_NAME

    @staticmethod
    def parser_sub_parser(sub_parsers: argparse._SubParsersAction) -> None:
        parser = sub_parsers.add_parser(
            _COMMAND_NAME, help="Prints the create table statement for the given table."
        )
        BaseCommand._add_table_arguments_to_sub_parser(parser)

    @_requires_table
    def handle(
        self, connection: DataBaseConnection, args: argparse.Namespace
    ) -> CommandResult:
        """Prints the create table statement for the given table."""
        fetcher = self._factory.get_table_fetcher(connection)
        table = fetcher.fetch_table_with_name(args.table)
        sql = self._factory.get_formatter(
            args.dialect, FormatterType.SQL_CREATE_TABLE
        ).format(table)
        print(sql)
        return CommandResult(CommandResultStatus.SUCCESS)
