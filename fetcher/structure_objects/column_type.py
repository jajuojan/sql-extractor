"""Base class for column types"""

from dataclasses import dataclass


@dataclass
class ColumnType:
    """Base class for column types"""

    name: str
