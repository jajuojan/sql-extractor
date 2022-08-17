import typing

from database.tsql_database import TSqlDataBase


def fetch_principals(db: TSqlDataBase) -> typing.List[typing.Any]:
    """TBD"""
    sql = "SELECT * FROM sys.database_principals;"
    return db.fetch_raw_sql_rows(sql)
