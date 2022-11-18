"""TBD"""

from abc import ABC, abstractmethod

from connection.database import DataBaseConnection
from fetcher.structure_objects.database import DatabaseStructure


class StructureFetcher(ABC):
    """Fetcher for database structure"""

    def __init__(self, data_base: DataBaseConnection) -> None:
        self.data_base = data_base

    @abstractmethod
    def fetch(self) -> DatabaseStructure:
        """Fetches the database structure"""
