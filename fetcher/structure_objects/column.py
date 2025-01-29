"""Column structure object"""

from dataclasses import dataclass

from fetcher.structure_objects.column_type import ColumnType


@dataclass
class Column:
    """
    Database agnostic column.

    Attributes:
        name (str): The name of the column.
        type (ColumnType): The type of the column.
    """

    name: str
    type: ColumnType
