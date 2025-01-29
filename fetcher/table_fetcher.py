"""Sys-object Fetcher"""

import typing
from abc import ABC, abstractmethod

from connection.database import DataBaseConnection
from fetcher.structure_objects.table import Table


class TableFetcher(ABC):
    """Fetcher for tables"""

    def __init__(self, data_base: DataBaseConnection) -> None:
        self.data_base = data_base

    @abstractmethod
    def fetch_tables(self) -> typing.Sequence[Table]:
        """Fetch all tables"""

    @abstractmethod
    def fetch_table_with_name(self, identifier: str) -> Table:
        """Fetch table with name"""
