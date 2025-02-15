"""Handles the formatter-selection for the tsql dialect"""

from dialects.tsql.formatter.table_sql_formatter import (
    TableCreationFormatter,
    TableInsertFormatter,
)
from dialects.tsql.tsql_exception import TSqlDataBaseException
from formatters.base_formatter import BaseFormatter, FormatterType
from formatters.table_html_formatter import HtmlTableStructureFormatter
from formatters.table_md_formatter import MdTableStructureFormatter


class TsqlFormatterHandler:
    """Handles the formatter-selection for the tsql dialect"""

    def __init__(self) -> None:
        pass

    def get_formatter(
        self,
        formatter_type: FormatterType,
    ) -> BaseFormatter:
        """Returns the formatter based on formatter type"""
        if formatter_type == FormatterType.SQL_CREATE_TABLE:
            return TableCreationFormatter()
        if formatter_type == FormatterType.SQL_CREATE_INSERT:
            return TableInsertFormatter()
        if formatter_type == FormatterType.HTML_TABLE_STRUCTURE:
            return HtmlTableStructureFormatter()
        if formatter_type == FormatterType.MD_TABLE_STRUCTURE:
            return MdTableStructureFormatter()

        raise TSqlDataBaseException("Unknown formatter type")
