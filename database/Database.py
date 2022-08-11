import typing

from database.SqlRow import SqlRow


# Base class for all database classes
class DataBase:
    # def __init__(self, name, user, password, host, port):
    def __init__(self):
        pass
        # TBD
        # self.name = name
        # self.user = user
        # self.password = password
        # self.host = host
        # self.port = port

    def fetch_raw_sql_rows(self, sql: str) -> typing.Any:
        raise NotImplementedError

    def fetch_sql_rows(self, sql: str) -> typing.List[SqlRow]:
        raise NotImplementedError

    def get_version(self) -> str:
        raise NotImplementedError
