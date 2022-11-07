# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

import os

from fetcher.structure_objects.column import Column
from fetcher.structure_objects.column_type import ColumnType
from fetcher.structure_objects.table import Table


def get_test_data(filename: str) -> str:
    """
    Returns the data from a test data file.
    """
    file_name = os.path.join("tests", "test_data", filename)
    with open(file_name, "r", encoding="utf-8") as file_handle:
        return file_handle.read()


def create_test_table() -> Table:
    """Create test table"""
    return Table(
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
    )
