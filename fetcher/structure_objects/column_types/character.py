"""tbd"""
from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class CharacterColumnType(ColumnType):
    """Base class for character column types"""
