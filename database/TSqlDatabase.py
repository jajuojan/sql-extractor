from typing import Any, List
import typing
import pyodbc
from database.Database import DataBase
from database.SqlRow import SqlRow, SqlRowItem

# from database.Database import DataBase
# from helpers import get_local_server_name


class TSqlDataBase(DataBase):
    def __init__(self):
        super().__init__()
        self._connection = None

    @staticmethod
    def _get_local_connection(
        server_name: str, database_name: str
    ) -> pyodbc.Connection:
        return pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            f"Server={server_name};"
            f"Database={database_name};"
            "Trusted_Connection=yes;"
        )

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
            # print([column[0] for column in cursor.description])
            values.append(row)
            row = cursor.fetchone()
        return values

    def _sql_row_item_from_description(self, description: tuple) -> SqlRowItem:
        a = SqlRowItem()
        # (name, type_code, display_size, internal_size, precision, scale, null_ok).
        #for i in description:
        #    print(i)
        return a

    def _sql_row_from_description(self, description: tuple) -> SqlRow:
        return SqlRow([self._sql_row_item_from_description(i) for i in description])

    def get_version(self) -> str:
        return str(self._fetch_raw_single_row("SELECT @@version;")[0])

    def fetch_raw_sql_rows(self, sql: str) -> List[Any]:
        return self._fetch_raw_rows(sql)

    def fetch_sql_rows(self, sql: str) -> typing.List[SqlRow]:
        cursor = self._connection.cursor()
        cursor.execute(sql)
        values = []
        row = cursor.fetchone()
        # (name, type_code, display_size, internal_size, precision, scale, null_ok).
        print(type(cursor.description))
        print(cursor.description)
        description_row = self._sql_row_from_description(cursor.description)
        # for i in row:
        #    print(i)
        # print([column[0] for column in cursor.description])
        while row:
            sql_row = SqlRow()

            values.append(sql_row)
            row = cursor.fetchone()
        return values


def with_local_connection(database_name: str) -> DataBase:
    db = TSqlDataBase()
    from database.tsql.helpers import get_local_server_name

    server_name = get_local_server_name()
    db._connection = db._get_local_connection(server_name, database_name)
    return db
