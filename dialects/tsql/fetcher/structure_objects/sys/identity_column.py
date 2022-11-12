"""TBD"""

from dataclasses import dataclass


@dataclass
class IdentityColumn:
    # pylint: disable=too-many-instance-attributes
    """sys.identity_columns"""

    object_id: int
    name: str
    column_id: int
    system_type_id: int
    user_type_id: int
    max_length: int
    precision: int
    scale: int
    collation_name: str
    is_nullable: int
    is_ansi_padded: int
    is_rowguidcol: int
    is_identity: int
    is_filestream: int
    is_replicated: int
    is_non_sql_subscribed: int
    is_merge_published: int
    is_dts_replicated: int
    is_xml_document: int
    xml_collection_id: int
    default_object_id: int
    rule_object_id: int
    seed_value: str
    increment_value: str
    last_value: int
    is_not_for_replication: int
    is_computed: int
    is_sparse: int
    is_column_set: int
    generated_always_type: int
    generated_always_type_desc: str
    encryption_type: int
    encryption_type_desc: int
    encryption_algorithm_name: int
    column_encryption_key_id: int
    column_encryption_key_database_name: int
    is_hidden: int
    is_masked: int
    graph_type: int
    graph_type_desc: int
