"""TBD"""

import datetime
from dataclasses import dataclass


@dataclass
class DatabaseInfo:
    """sys.databases"""

    name: str
    database_id: int
    create_date: datetime.datetime
    compatibility_level: int
    collation_name: str
