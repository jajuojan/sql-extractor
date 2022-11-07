"""TBD"""
import typing
from abc import ABC
from dataclasses import dataclass, field

from fetcher.structure_objects.column import Column


@dataclass
class Table(ABC):
    """Database agnostic table"""

    name: str
    schema_name: str
    object_id: int
    columns: typing.List[Column] = field(default_factory=lambda: [])

    """
        def __init__(
            self,
            name: str,
            schema_name: str,
            object_id: int = -1,
            columns: typing.Union[typing.List[Column], None] = None,
        ) -> None:
            super().__init__()
            self.name: str = name
            self.schema_name: str = schema_name
            self.object_id: int = object_id
            self.columns: typing.List[Column] = columns if columns else []
    """
