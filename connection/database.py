"""Base-class for databases"""

import abc
import typing
from abc import ABCMeta

from connection.sql_row import SqlRowSet


class DataBaseConnection(metaclass=ABCMeta):
    """Base-class for DataBaseConnections"""

    def __init__(self, dialect: str) -> None:
        self.dialect = dialect

    @abc.abstractmethod
    def fetch_raw_sql_rows(self, sql: str) -> typing.Any:
        """Fetch one or several SQL rows"""

    @abc.abstractmethod
    def fetch_sql_rows(self, sql: str) -> SqlRowSet:
        """Fetch a single SQL row"""
