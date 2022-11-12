"""Low-level classes for SQL-DB access"""

import typing
from abc import ABCMeta
from typing import List, Union


class SqlRowItem(metaclass=ABCMeta):
    """Base class for all SqlRowItems"""


class SqlTypeRowItem(SqlRowItem):
    """Sql type row item"""

    def __init__(
        self,
        name: str,
        type_code: type,
        display_size: int,
        internal_size: int,
        precision: int,
        scale: int,
        null_ok: bool,
    ) -> None:
        # pylint: disable=too-many-arguments
        self.name = name
        self.type_code = type_code
        self.display_size = display_size
        self.internal_size = internal_size
        self.precision = precision
        self.scale = scale
        self.null_ok = null_ok

    def __str__(self) -> str:
        return f"{str(self.name)}, {str(self.type_code)}"


class SqlValueRowItem(SqlRowItem):
    """Sql value row item"""

    def __init__(self, value: typing.Any) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def as_str(self) -> str:
        """Return as string"""
        return str(self.value)

    def as_int(self) -> int:
        """Return as string"""
        return int(self.value)


class SqlRow:
    """Sql row"""

    def __init__(self, items: Union[List[SqlRowItem], None] = None) -> None:
        self.items = items if items else []

    def __str__(self) -> str:
        return ", ".join([str(i) for i in self.items])

    def __len__(self) -> int:
        return len(self.items)


class SqlRowSet:
    """Sql row set"""

    def __init__(
        self,
        type_row: SqlRow,
        value_rows: Union[List[SqlRow], None] = None,
        sql: Union[str, None] = None,
    ) -> None:
        self.type_row = type_row
        self.value_rows = value_rows if value_rows else []
        self.sql = sql

    def __str__(self) -> str:
        type_row_lenght = len(self.type_row.items)
        return f'RowSet: {type_row_lenght} columns, {len(self.value_rows)} rows. "{self.sql}"'
