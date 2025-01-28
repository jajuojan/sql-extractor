"""A markdown formatter for table structure"""

from fetcher.structure_objects.table import Table
from formatters.base_formatter import BaseFormatter


class MdTableStructureFormatter(BaseFormatter):
    """A markdown formatter for table structure"""

    def format(self, table: Table) -> str:
        """Formats a table structure to markdown"""
        ret = f"## {table.name}\n"

        ret += "| Name | Type |\n"
        ret += "| ------------- |:----- |\n"
        for column in table.columns:
            ret += f"| {column.name} | {column.type.name} |\n"

        return ret
