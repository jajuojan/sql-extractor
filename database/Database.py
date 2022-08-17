"""Base-class for databases"""
import abc
import typing
from abc import ABCMeta

from database.sql_row import SqlRow


# Base class for all database classes
class DataBase(metaclass=ABCMeta):
    """Base-class for databases"""

    def __init__(self) -> None:
        pass
        # TBD
        # self.name = name
        # self.user = user
        # self.password = password
        # self.host = host
        # self.port = port

    @abc.abstractmethod
    def fetch_raw_sql_rows(self, sql: str) -> typing.Any:
        """Fetch one or several SQL rows"""

    @abc.abstractmethod
    def fetch_sql_rows(self, sql: str) -> typing.List[SqlRow]:
        """Fetch a single SQL row"""

    @abc.abstractmethod
    def get_version(self) -> str:
        """Return the version fo the database"""
