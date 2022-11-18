"""TBD"""

from dataclasses import dataclass, field
from typing import List

from fetcher.structure_objects.schema import Schema


@dataclass
class DatabaseStructure:
    """database structure for the database"""

    schemas: List[Schema] = field(default_factory=lambda: [])
