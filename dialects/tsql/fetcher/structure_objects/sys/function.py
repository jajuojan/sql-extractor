"""TBD"""

import datetime
from dataclasses import dataclass


@dataclass
class Function:
    """sys.sql_modules, sys.objects"""

    name: str
    object_id: str
    schema_id: int
    create_date: datetime.datetime
    modify_date: datetime.datetime
    type_desc: str
    definition: str
