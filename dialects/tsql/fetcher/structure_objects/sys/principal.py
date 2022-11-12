"""TBD"""

import datetime
from dataclasses import dataclass


@dataclass
class Principal:
   # pylint: disable=too-many-instance-attributes
    """sys.database_principals"""

    name: str
    principal_id: int
    type: str
    type_desc: str
    default_schema_name: str
    create_date: datetime.datetime
    modify_date: datetime.datetime
    owning_principal_id: int
    sid: str
    is_fixed_role: int
    authentication_type: int
    authentication_type_desc: str
    default_language_name: str
    default_language_lcid: str
    allow_encrypted_value_modifications: int
