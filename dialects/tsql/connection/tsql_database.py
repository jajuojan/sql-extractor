"""Low-level connection to SqlServer"""
# pylint: disable=import-error

from typing import Any, List

import pyodbc

from connection.database import DataBaseConnection
from connection.sql_row import SqlRow, SqlRowSet, SqlTypeRowItem, SqlValueRowItem


class TSqlDataBaseConnection(DataBaseConnection):
    """Low-level access to SqlServer-DB"""

    def __init__(self, connection: pyodbc.Connection, dialect: str) -> None:
        super().__init__(dialect)
        self._connection = connection

    def _fetch_raw_single_row(self, sql: str, allow_multiple: bool = False) -> Any:
        rows = self._fetch_raw_rows(sql)
        if not allow_multiple and len(rows) > 1:
            raise Exception("More than one row returned.")
        return rows[0]

    # TODO: use fetchall() ??
    def _fetch_raw_rows(self, sql: str) -> List[Any]:
        cursor = self._connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        values = []
        while row:
            values.append(row)
            row = cursor.fetchone()
        return values

    def _sql_type_row_item_from_description(self, description: tuple) -> SqlTypeRowItem:
        """Fill SELECTs single columns type/meta-data into SqlTypeRowItem"""
        return SqlTypeRowItem(*description)

    def _sql_type_row_from_description(self, description: tuple) -> SqlRow:
        """Fill SELECTs type/meta-data from all columns into SqlRow"""
        return SqlRow(
            [self._sql_type_row_item_from_description(i) for i in description]
        )

    def _sql_value_row_from_cursor(self, cursor_row: tuple) -> SqlRow:
        """Fill SELECTs values from all columns into SqlRow"""
        return SqlRow([SqlValueRowItem(i) for i in cursor_row])

    def fetch_raw_sql_rows(self, sql: str) -> List[Any]:
        return self._fetch_raw_rows(sql)

    def fetch_sql_rows(self, sql: str) -> SqlRowSet:
        """Run a SELECT and return the SqlRowSet-result"""
        cursor = self._connection.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        description_row = self._sql_type_row_from_description(cursor.description)

        value_rows = []
        while row:
            value_rows.append(self._sql_value_row_from_cursor(row))
            row = cursor.fetchone()

        return SqlRowSet(description_row, value_rows, sql=sql)

    def get_version(self) -> str:
        """Return the version fo the database"""
        return str(self._fetch_raw_single_row("SELECT @@version;")[0])


def with_local_connection(database_name: str) -> DataBaseConnection:
    """TBD"""
    # pylint: disable=import-outside-toplevel
    from dialects.tsql.connection.helpers import get_local_server_name

    server_name = get_local_server_name()
    connection = _get_connection(server_name, database_name)
    return TSqlDataBaseConnection(connection, "tsql")


def _get_connection(server_name: str, database_name: str) -> pyodbc.Connection:
    return pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        f"Server={server_name};"
        f"Database={database_name};"
        "Trusted_Connection=yes;"
    )


def with_connection(connection_string: str) -> DataBaseConnection:
    """return a database connection from connection string"""
    connection_string = "Driver={SQL Server Native Client 11.0};" + connection_string
    connection = pyodbc.connect(connection_string)
    return TSqlDataBaseConnection(connection, "tsql")
