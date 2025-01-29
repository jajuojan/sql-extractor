"""Sys-object Fetcher"""

import typing

from connection.database import DataBaseConnection
from dialects.tsql.fetcher.internal_structure_fetcher import StructureFetcher
from dialects.tsql.fetcher.structure_objects.tsql_table import TsqlTable
from dialects.tsql.fetcher.sys_object_fetcher import SysObjectFetcher
from dialects.tsql.tsql_exception import TSqlDataBaseException
from fetcher.structure_objects.column import Column
from fetcher.structure_objects.column_type import ColumnType
from fetcher.table_fetcher import TableFetcher


class TsqlTableFetcher(TableFetcher):
    """TSQL-specific Fetcher for tables"""

    def __init__(self, data_base: DataBaseConnection) -> None:
        super().__init__(data_base)
        self.struct_fetcher = StructureFetcher(self.data_base)
        self.sys_obj_fetcher = SysObjectFetcher(self.data_base)

    def fetch_tables(self) -> typing.Sequence[TsqlTable]:
        """Fetch all tables"""
        information_schema_columns_raw = self.struct_fetcher.fetch_columns()

        tables: typing.List[TsqlTable] = []
        schemas: typing.Dict[str, typing.Dict[str, TsqlTable]] = {}
        for column in information_schema_columns_raw:
            if column.table_schema not in schemas:
                schemas[column.table_schema] = {}
            col_tables = schemas[column.table_schema]
            if column.table_name not in col_tables:
                col_tables[column.table_name] = TsqlTable(
                    column.table_name, column.table_schema, column.table_id
                )
                tables.append(col_tables[column.table_name])
            col_tables[column.table_name].information_schema_columns.append(column)

        for i in tables:
            i.information_schema_columns = sorted(
                i.information_schema_columns, key=lambda x: x.ordinal_position
            )
            self._inject_with_tables(i)

        self._inject_columns(tables)
        return tables

    def fetch_table_with_name(self, identifier: str) -> TsqlTable:
        """Fetch table with name"""
        schema_name = None
        table_name = identifier
        if "." in identifier:
            splitted = identifier.split(".")
            if len(splitted) != 2:
                raise TSqlDataBaseException("Unable to parse table name")
            schema_name, table_name = splitted

        tables = self.fetch_tables()
        for table in tables:
            if table.name == table_name and (
                not schema_name or table.schema_name == schema_name
            ):
                return table

        raise TSqlDataBaseException("No such table found")

    def _inject_with_tables(self, table: TsqlTable) -> None:
        table.table_sys_object = self.sys_obj_fetcher.fetch_sys_object_by_id(
            table.object_id
        )
        table.child_sys_objects = self.sys_obj_fetcher.fetch_sys_object_by_parent_id(
            table.object_id
        )
        table.identity_columns = (
            self.struct_fetcher.fetch_identity_columns_by_object_id(table.object_id)
        )

    def _inject_columns(self, tables: typing.List[TsqlTable]) -> None:
        for table in tables:
            for info_column in table.information_schema_columns:
                table.columns.append(
                    Column(info_column.column_name, ColumnType(info_column.data_type))
                )
