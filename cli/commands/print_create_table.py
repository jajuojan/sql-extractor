"""TBD"""

import argparse

from cli.commands.base_command import BaseCommand
from cli.commands.base_formatter_command import BaseFormatterCommand
from formatters.base_formatter import FormatterType


class PrintCreateTableCommand(BaseFormatterCommand):
    """Prints the create table statement for the given table."""

    # pylint: disable=protected-access

    @property
    @staticmethod
    def command_name() -> str:
        return "print-create-table"

    @staticmethod
    def parser_sub_parser(sub_parsers: argparse._SubParsersAction) -> None:
        parser = sub_parsers.add_parser(
            PrintCreateTableCommand.command_name(),
            help="Prints the create table statement for the given table.",
        )
        BaseCommand._add_table_arguments_to_sub_parser(parser)

    def _get_formatter_type(self) -> FormatterType:
        return FormatterType.SQL_CREATE_TABLE
