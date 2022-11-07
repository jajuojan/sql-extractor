"""tbd"""
from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class DateTimeColumnType(ColumnType):
    """Base class for date and time column types"""
