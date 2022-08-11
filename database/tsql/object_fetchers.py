import typing

from database.TSqlDatabase import TSqlDataBase


def fetch_principals(db: TSqlDataBase) -> typing.List[typing.Any]:
    sql = "SELECT * FROM sys.database_principals;"
    return db.fetch_raw_sql_rows(sql)
