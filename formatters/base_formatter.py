"""Abstract base class for all formatters"""

from abc import ABC, abstractmethod
from enum import Enum

from fetcher.structure_objects.table import Table


class FormatterType(Enum):
    """Available formatter types"""

    SQL_CREATE_TABLE = 1
    SQL_CREATE_INSERT = 2
    HTML_TABLE_STRUCTURE = 3
    MD_TABLE_STRUCTURE = 4


class BaseFormatter(ABC):
    """Abstract base class for all formatters"""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def format(self, table: Table) -> str:
        """Returns a formatted string"""
