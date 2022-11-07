"""TBD"""

import datetime
from dataclasses import dataclass


@dataclass
class Procedure:
    """INFORMATION_SCHEMA.ROUTINES"""

    routine_catalog: str
    routine_schema: str
    routine_name: str
    routine_definition: str
    routine_body: str
    created: datetime.datetime
    last_altered: datetime.datetime
