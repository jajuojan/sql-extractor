"""Structure Fetchers"""
import typing

from connection.database import DataBaseConnection
from dialects.tsql.fetcher.structure_objects.information_schema.column import (
    InformationSchemaColumn,
)
from dialects.tsql.fetcher.structure_objects.information_schema.procedure import (
    Procedure,
)
from dialects.tsql.fetcher.structure_objects.information_schema.schema import Schema
from dialects.tsql.fetcher.structure_objects.information_schema.table_info import (
    TableInfo,
)
from dialects.tsql.fetcher.structure_objects.sys.database_info import DatabaseInfo
from dialects.tsql.fetcher.structure_objects.sys.function import Function
from dialects.tsql.fetcher.structure_objects.sys.identity_column import IdentityColumn
from dialects.tsql.fetcher.structure_objects.sys.principal import Principal
from dialects.tsql.fetcher.structure_objects.sys.sys_object import SysObject

_IDENTITY_COLUMN_BASE_SQL = """
SELECT
object_id, name, column_id, system_type_id, user_type_id, max_length, precision, scale,
collation_name, is_nullable, is_ansi_padded, is_rowguidcol, is_identity, is_filestream,
is_replicated, is_non_sql_subscribed, is_merge_published, is_dts_replicated, is_xml_document,
xml_collection_id, default_object_id, rule_object_id, convert(char, seed_value),
convert(char, increment_value), convert(char, last_value), is_not_for_replication,
is_computed, is_sparse, is_column_set, generated_always_type, generated_always_type_desc,
encryption_type, encryption_type_desc, encryption_algorithm_name, column_encryption_key_id,
column_encryption_key_database_name, is_hidden, is_masked, graph_type, graph_type_desc
FROM sys.identity_columns
"""

_FETCH_PRINCIPALS_SQL = """
SELECT
name, principal_id, type, type_desc, default_schema_name, create_date, modify_date,
owning_principal_id, sid, is_fixed_role, authentication_type, authentication_type_desc,
default_language_name, default_language_lcid, allow_encrypted_value_modifications
FROM sys.database_principals
"""

_FETCH_DATABASES_SQL = """
SELECT
name, database_id, create_date, compatibility_level, collation_name
FROM sys.databases
"""

_FETCH_SCHEMAS_SQL = """
SELECT
catalog_name, schema_name, schema_owner, default_character_set_catalog,
default_character_set_schema, default_character_set_name
FROM INFORMATION_SCHEMA.SCHEMATA
"""

_FETCH_TABLES_SQL = """
SELECT
TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, TABLE_TYPE
FROM INFORMATION_SCHEMA.TABLES
"""

_FETCH_PROCEDURES_SQL = """
SELECT 
ROUTINE_CATALOG, ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_DEFINITION, ROUTINE_BODY, CREATED, LAST_ALTERED
FROM INFORMATION_SCHEMA.ROUTINES
WHERE ROUTINE_TYPE = 'PROCEDURE'
"""

_FETCH_FUNCTIONS_SQL = """
SELECT
o.name, o.object_id, o.schema_id, o.create_date, o.modify_date, o.type_desc, m.definition
FROM sys.sql_modules m 
INNER JOIN sys.objects o ON m.object_id = o.object_id
WHERE type_desc like '%function%'
"""

_FETCH_SYS_OBJECTS_SQL = """
SELECT
name, object_id, principal_id, schema_id, SCHEMA_NAME(schema_id) as schema_name, parent_object_id,
type, type_desc, create_date, modify_date, is_ms_shipped, is_published, is_schema_published
FROM sys.objects
"""

_FETCH_COLUMNS_SQL = """
SELECT
table_catalog, table_schema, table_name, column_name, ordinal_position, column_default, is_nullable,
data_type, character_maximum_length, character_octet_length, numeric_precision,
numeric_precision_radix, numeric_scale, datetime_precision, character_set_catalog,
character_set_schema, character_set_name, collation_catalog, collation_schema, collation_name,
domain_catalog, domain_schema, domain_name, OBJECT_ID(table_schema+'.'+table_name) AS table_id
FROM INFORMATION_SCHEMA.COLUMNS
"""


class StructureFetcher:
    """Fetcher for database structure"""

    def __init__(self, data_base: DataBaseConnection) -> None:
        self.data_base = data_base

    def fetch_principals(self) -> typing.List[Principal]:
        """Fetch principals"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_PRINCIPALS_SQL)
        return [Principal(*i) for i in row_set]

    def fetch_databases(self) -> typing.List[DatabaseInfo]:
        """Return a list of the names of databases"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_DATABASES_SQL)
        return [DatabaseInfo(*i) for i in row_set]

    def fetch_schemas(self) -> typing.List[Schema]:
        """Return a list of schemas"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_SCHEMAS_SQL)
        return [Schema(*i) for i in row_set]

    def fetch_tables(self) -> typing.List[TableInfo]:
        """Fetch tables"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_TABLES_SQL)
        return [TableInfo(*i) for i in row_set]

    def fetch_procedures(self) -> typing.List[Procedure]:
        """Fetch procedures"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_PROCEDURES_SQL)
        return [Procedure(*i) for i in row_set]

    def fetch_functions(self) -> typing.List[Function]:
        """Fetch functions"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_FUNCTIONS_SQL)
        return [Function(*i) for i in row_set]

    def fetch_sys_objects(self) -> typing.List[SysObject]:
        """Fetch sys objects"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_SYS_OBJECTS_SQL)
        return [SysObject(*i) for i in row_set]

    def fetch_columns(self) -> typing.List[InformationSchemaColumn]:
        """Fetch columns"""
        row_set = self.data_base.fetch_raw_sql_rows(_FETCH_COLUMNS_SQL)
        return [InformationSchemaColumn(*i) for i in row_set]

    def fetch_identity_columns_by_object_id(
        self, object_id: int
    ) -> typing.List[IdentityColumn]:
        """Fetch identity columns by object id"""
        sql = f"{_IDENTITY_COLUMN_BASE_SQL} WHERE object_id={object_id}"
        row_set = self.data_base.fetch_raw_sql_rows(sql)
        return [IdentityColumn(*i) for i in row_set]
