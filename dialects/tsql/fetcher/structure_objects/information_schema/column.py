"""TBD"""

from dataclasses import dataclass


@dataclass
class InformationSchemaColumn:
    # pylint: disable=too-many-instance-attributes
    """Column from INFORMATION_SCHEMA.COLUMNS"""

    table_catalog: str
    table_schema: str
    table_name: str
    column_name: str
    ordinal_position: int
    column_default: str
    is_nullable: str
    data_type: str
    character_maximum_length: int
    character_octet_length: int
    numeric_precision: int
    numeric_precision_radix: int
    numeric_scale: int
    datetime_precision: int
    character_set_catalog: str
    character_set_schema: str
    character_set_name: str
    collation_catalog: str
    collation_schema: str
    collation_name: str
    domain_catalog: str
    domain_schema: str
    domain_name: str
    table_id: int
