"""TBD"""

from dataclasses import dataclass, field
from typing import List

from fetcher.structure_objects.schema import Schema


@dataclass
class DatabaseStructure:
    """
    Represents the structure of a database.

    Attributes:
        schemas (List[Schema]): A list of schemas in the database.
    """

    schemas: List[Schema] = field(default_factory=lambda: [])
