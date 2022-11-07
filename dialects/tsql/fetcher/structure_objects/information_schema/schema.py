"""TBD"""

from dataclasses import dataclass


@dataclass
class Schema:
    """INFORMATION_SCHEMA.SCHEMATA"""

    catalog_name: str
    schema_name: str
    schema_owner: str
    default_character_set_catalog: str
    default_character_set_schema: str
    default_character_set_name: str
