"""TBD"""

from typing import cast

from dialects.tsql.fetcher.structure_objects.tsql_table import TsqlTable
from fetcher.structure_objects.table import Table
from formatters.base_formatter import BaseFormatter

SQL_HEADER = """SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

"""


class TableCreationFormatter(BaseFormatter):
    """Formatter for table creation SQL"""

    def format(self, table: Table) -> str:
        """Format a SQL for table creation"""
        assert isinstance(table, TsqlTable)
        tsql_table = cast(TsqlTable, table)

        ret = SQL_HEADER
        ret += f"CREATE TABLE [{tsql_table.schema_name}].[{tsql_table.name}](\n"
        col_count = len(tsql_table.columns)
        for idx, column in enumerate(tsql_table.information_schema_columns):
            identity = self._format_identity_column(tsql_table, column.column_name)
            nullable = " NOT NULL" if column.is_nullable == "NO" else ""
            comma = "" if idx == col_count - 1 else ","
            ret += f"    [{column.column_name}] [{column.data_type}]{identity}{nullable}{comma}\n"

        ret += ") ON [PRIMARY]\nGO\n"

        return ret

    def _format_identity_column(self, table: TsqlTable, column_name: str) -> str:
        identity_column = table.identity_column_by_column_name(column_name)
        if not identity_column:
            return ""

        sections = []

        seed_value = identity_column.seed_value.strip()
        identity_value = identity_column.increment_value.strip()
        sections.append(
            f"IDENTITY({seed_value},{identity_value})"
        )

        if identity_column.is_not_for_replication:
            sections.append("NOT FOR REPLICATION")

        return f" {' '.join(sections)}" if len(sections) > 0 else ""


_INSERT_SQL = """
INSERT INTO [{}].[{}] ({})
     VALUES
    (
        {}
    )
GO
"""


class TableInsertFormatter(BaseFormatter):
    """Formatter for table insert SQL"""

    def format(self, table: Table) -> str:
        """Format a SQL for table insert"""
        column_names = ", ".join([f"[{i.name}]" for i in table.columns])
        column_values = "  -- " + "\n         ,-- ".join(
            f"{i.name}, {i.type.name}" for i in table.columns
        )

        return _INSERT_SQL.format(
            table.schema_name, table.name, column_names, column_values
        )
