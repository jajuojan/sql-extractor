"""TBD"""

from dataclasses import dataclass, field
from typing import List

from fetcher.structure_objects.table import Table


@dataclass
class Schema:
    """Database agnostic schema"""

    name: str
    tables: List[Table] = field(default_factory=lambda: [])
