# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

from unittest import TestCase

from dialects.tsql.fetcher.structure_objects.information_schema.column import (
    InformationSchemaColumn,
)
from dialects.tsql.fetcher.structure_objects.sys.identity_column import IdentityColumn
from dialects.tsql.fetcher.structure_objects.tsql_table import TsqlTable
from dialects.tsql.formatter.table_sql_formatter import (
    TableCreationFormatter,
    TableInsertFormatter,
)
from fetcher.structure_objects.column import Column
from fetcher.structure_objects.column_type import ColumnType
from tests.helpers import get_test_data


class Test(TestCase):
    def test_sql_create_formatter(self) -> None:
        formatter = TableCreationFormatter()
        result = formatter.format(create_test_table())
        input_data = get_test_data("table_create_sql_tsql.txt")
        self.assertEqual(result, input_data)

    def test_sql_insert_formatter(self) -> None:
        formatter = TableInsertFormatter()
        result = formatter.format(create_test_table())
        input_data = get_test_data("table_insert_sql_tsql.txt")
        self.assertEqual(result, input_data)


def create_test_table() -> TsqlTable:
    """Create test table"""
    table = TsqlTable(
        name="test_table",
        schema_name="test_schema",
        object_id=1,
        columns=[
            Column(
                name="id",
                type=ColumnType(
                    name="int",
                ),
            ),
            Column(
                name="rowguid",
                type=ColumnType(
                    name="uniqueidentifier",
                ),
            ),
            Column(
                name="modifiedDate",
                type=ColumnType(
                    name="datetime",
                ),
            ),
        ],
        information_schema_columns=[
            create_information_schema_column("test_table", "test_schema", "id", "int"),
            create_information_schema_column(
                "test_table", "test_schema", "rowguid", "uniqueidentifier"
            ),
            create_information_schema_column(
                "test_table", "test_schema", "modifiedDate", "datetime"
            ),
        ],
    )
    table.identity_columns = [
        create_identity_column("id"),
        create_identity_column("rowguid"),
        create_identity_column("modifiedDate"),
    ]
    return table


def create_information_schema_column(
    table_name: str, table_schema: str, column_name: str, data_type: str
) -> InformationSchemaColumn:
    """Create test table"""
    return InformationSchemaColumn(
        table_catalog="xxx",
        table_schema=table_schema,
        table_name=table_name,
        column_name=column_name,
        ordinal_position=1,
        column_default="xxx",
        is_nullable="xxx",
        data_type=data_type,
        character_maximum_length=1,
        character_octet_length=1,
        numeric_precision=1,
        numeric_precision_radix=1,
        numeric_scale=1,
        datetime_precision=1,
        character_set_catalog="xxx",
        character_set_schema="xxx",
        character_set_name="xxx",
        collation_catalog="xxx",
        collation_schema="xxx",
        collation_name="xxx",
        domain_catalog="xxx",
        domain_schema="xxx",
        domain_name="xxx",
        table_id=1,
    )


def create_identity_column(name: str) -> IdentityColumn:
    return IdentityColumn(
        object_id=1,
        name=name,
        column_id=1,
        system_type_id=1,
        user_type_id=1,
        max_length=1,
        precision=1,
        scale=1,
        collation_name="xxx",
        is_nullable=1,
        is_ansi_padded=1,
        is_rowguidcol=1,
        is_identity=1,
        is_filestream=1,
        is_replicated=1,
        is_non_sql_subscribed=1,
        is_merge_published=1,
        is_dts_replicated=1,
        is_xml_document=1,
        xml_collection_id=1,
        default_object_id=1,
        rule_object_id=1,
        seed_value="xxx",
        increment_value="xxx",
        last_value=1,
        is_not_for_replication=1,
        is_computed=1,
        is_sparse=1,
        is_column_set=1,
        generated_always_type=1,
        generated_always_type_desc="xxx",
        encryption_type=1,
        encryption_type_desc=1,
        encryption_algorithm_name=1,
        column_encryption_key_id=1,
        column_encryption_key_database_name=1,
        is_hidden=1,
        is_masked=1,
        graph_type=1,
        graph_type_desc=1,
    )
