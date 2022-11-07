"""tbd"""
from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class NumericColumnType(ColumnType):
    """Base class for numeric column types"""
