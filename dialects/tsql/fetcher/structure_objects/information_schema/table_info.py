"""TBD"""

from dataclasses import dataclass


@dataclass
class TableInfo:
    """INFORMATION_SCHEMA.TABLES"""

    table_catalog: str
    table_schema: str
    table_name: str
    table_type: str
