"""tbd"""
from connection.database import DataBaseConnection
from dialects.tsql.connection_handler import TsqlConnectonHandler
from dialects.tsql.fetcher.structure_fetcher import TsqlStructureFetcher
from dialects.tsql.fetcher.table_fetcher import TsqlTableFetcher
from dialects.tsql.formatter_handler import TsqlFormatterHandler
from fetcher.database_structure import DatabaseStructure
from fetcher.table_fetcher import TableFetcher
from formatters.base_formatter import BaseFormatter, FormatterType

_sql_dialects = ["postgres", "tsql"]


class Factory(object):
    """Factory for the database dialect specific classes"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def allowed_dialects() -> list[str]:
        """Returns the allowed dialects"""
        return _sql_dialects

    def get_connection(
        self, dialect: str, connection_string: str
    ) -> DataBaseConnection:
        """Returns the DB-connection based on the dialect and connection string"""
        if dialect == "tsql":
            return TsqlConnectonHandler().get_connection(dialect, connection_string)

        raise Exception("Unknown dialect")

    def get_structure(
        self, database_connection: DataBaseConnection
    ) -> DatabaseStructure:
        """Returns the structure fetcher based on the dialect and connection string"""
        if database_connection.dialect == "tsql":
            return TsqlStructureFetcher(database_connection).fetch()

        raise Exception("Unknown dialect")

    # TODO: Remove this and use tables via get_structure instead
    def get_table_fetcher(
        self, database_connection: DataBaseConnection
    ) -> TableFetcher:
        """Returns the table fetcher based on the dialect and connection string"""
        if database_connection.dialect == "tsql":
            return TsqlTableFetcher(database_connection)

        raise Exception("Unknown dialect")

    def get_formatter(
        self,
        dialect: str,
        formatter_type: FormatterType,
    ) -> BaseFormatter:
        """Returns the formatter based on the dialect and connection string"""
        if dialect == "tsql":
            return TsqlFormatterHandler().get_formatter(formatter_type)

        raise Exception("Unknown dialect")
