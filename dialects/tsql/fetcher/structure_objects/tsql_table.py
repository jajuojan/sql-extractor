"""TBD"""
import typing
from dataclasses import dataclass, field

from dialects.tsql.fetcher.structure_objects.information_schema.column import (
    InformationSchemaColumn,
)
from dialects.tsql.fetcher.structure_objects.sys.identity_column import IdentityColumn
from dialects.tsql.fetcher.structure_objects.sys.sys_object import SysObject
from fetcher.structure_objects.table import Table


@dataclass
class TsqlTable(Table):
    """Table for TSQL"""

    information_schema_columns: typing.List[InformationSchemaColumn] = field(
        default_factory=lambda: []
    )
    table_sys_object: SysObject = field(init=False)
    child_sys_objects: typing.List[SysObject] = field(init=False)
    identity_columns: typing.List[IdentityColumn] = field(init=False)

    """
    @property
    def columns(self) -> typing.List[Column]:
        columns = []
        for i in self.information_schema_columns:
            columns.append(Column(i.column_name, ColumnType(i.data_type)))
        return columns
    """

    def identity_column_by_column_name(
        self, column_name: str
    ) -> typing.Union[IdentityColumn, None]:
        """TBD"""
        for column in self.identity_columns:
            if column.name == column_name:
                return column
        return None
