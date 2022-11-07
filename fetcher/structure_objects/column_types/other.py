"""tbd"""
from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class OtherColumnType(ColumnType):
    """Base class for other column types"""
