"""TBD"""

from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class Column:
    """Database agnostic column"""

    name: str
    type: ColumnType
