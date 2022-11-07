"""TBD"""

from typing import List, Optional

from fetcher.structure_objects.table import Table
from formatters.base_formatter import BaseFormatter

HTML_STYLE = """<style>
    table,
    th,
    td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    </style>"""
HTML_BASE = """<!DOCTYPE html> <html> <head>
{style}
</head> <body>
{body}
</body> </html>
"""

_DEFAULT_COLUMNS = ["column_name", "data_type"]


class HtmlTableStructureFormatter(BaseFormatter):
    """Formats a table structure to HTML"""

    def format(self, table: Table, columns: Optional[List[str]] = None) -> str:
        """Formats a table structure to HTML"""
        return HTML_BASE.format(
            style=HTML_STYLE, body=self._format_structure_html(table, columns)
        )

    def _format_structure_html(
        self, table: Table, columns: Optional[List[str]] = None
    ) -> str:
        if not columns:
            columns = _DEFAULT_COLUMNS

        ret = f"<h2>{table.name}</h2>\n"
        ret += "<table>\n"
        ret += "<tr> <th>Name</th> <th>Type</th> </tr>\n"

        for column in table.columns:
            ret += f"<tr> <th>{column.name}</th> <th>{column.type.name}</th> </tr>\n"
        ret += "</table>\n"

        return ret
