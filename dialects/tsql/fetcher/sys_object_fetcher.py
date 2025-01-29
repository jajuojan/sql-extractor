"""Structure Fetchers"""

import typing

from connection.database import DataBaseConnection
from dialects.tsql.fetcher.structure_objects.sys.sys_object import SysObject

_BASE_SQL = """
SELECT
name, object_id, principal_id, schema_id, SCHEMA_NAME(schema_id) as schema_name,
parent_object_id, type, type_desc, create_date, modify_date, is_ms_shipped,
is_published, is_schema_published
FROM
sys.objects
"""


class SysObjectFetcher:
    """Fetcher for sys.objects"""

    def __init__(self, data_base: DataBaseConnection) -> None:
        self.data_base = data_base

    def fetch_sys_objects(self) -> typing.List[SysObject]:
        """Fetch sys objects"""
        row_set = self.data_base.fetch_raw_sql_rows(_BASE_SQL)
        return [SysObject(*i) for i in row_set]

    def fetch_sys_object_by_id(self, object_id: int) -> SysObject:
        """Fetch sys object by id"""
        sql = f"{_BASE_SQL} WHERE object_id = {object_id}"
        row_set = self.data_base.fetch_raw_sql_rows(sql)
        return SysObject(*row_set[0])

    def fetch_sys_object_by_parent_id(self, parent_id: int) -> typing.List[SysObject]:
        """Fetch sys object by parent id"""
        sql = f"{_BASE_SQL} WHERE parent_object_id = {parent_id}"
        row_set = self.data_base.fetch_raw_sql_rows(sql)
        return [SysObject(*i) for i in row_set]
