"""TBD"""
import argparse

from cli.command_output import CommandResult, CommandResultStatus
from cli.commands.base_command import BaseCommand, _requires_table
from connection.database import DataBaseConnection
from formatters.base_formatter import FormatterType

_FORMATS = ["html", "md"]


class PrintTableStructureCommand(BaseCommand):
    """Prints the create table statement for the given table."""

    # pylint: disable=protected-access

    @property
    @staticmethod
    def command_name() -> str:
        return "print-table-structure"

    @staticmethod
    def parser_sub_parser(sub_parsers: argparse._SubParsersAction) -> None:
        parser: argparse.ArgumentParser = sub_parsers.add_parser(
            PrintTableStructureCommand.command_name(),
            help="Prints the table structure.",
        )
        BaseCommand._add_table_arguments_to_sub_parser(parser)
        parser.add_argument(
            "--format",
            nargs="?",
            const=None,
            type=str,
            default="html",
            help="The format to print the table structure in.",
            choices=_FORMATS,
        )

    @_requires_table
    def handle(
        self, connection: DataBaseConnection, args: argparse.Namespace
    ) -> CommandResult:
        fetcher = self._factory.get_table_fetcher(connection)
        table = fetcher.fetch_table_with_name(args.table)

        if args.format == "html":
            sql = self._factory.get_formatter(
                args.dialect, FormatterType.HTML_TABLE_STRUCTURE
            ).format(table)
        elif args.format == "md":
            sql = self._factory.get_formatter(
                args.dialect, FormatterType.MD_TABLE_STRUCTURE
            ).format(table)
        else:
            return CommandResult(CommandResultStatus.ERROR, "Unknown format.")

        print(sql)
        return CommandResult(CommandResultStatus.SUCCESS)
