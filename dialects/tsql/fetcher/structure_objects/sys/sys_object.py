"""TBD"""

from dataclasses import dataclass

_types = {
    "AF": "Aggregate function (CLR)",
    "C": "CHECK constraint",
    "D": "DEFAULT (constraint or stand-alone)",
    "F": "FOREIGN KEY constraint",
    "FN": "SQL scalar function",
    "FS": "Assembly (CLR) scalar-function",
    "FT": "Assembly (CLR) table-valued function",
    "IF": "SQL inline table-valued function",
    "IT": "Internal table",
    "P": "SQL Stored Procedure",
    "PC": "Assembly (CLR) stored-procedure",
    "PG": "Plan guide",
    "PK": "PRIMARY KEY constraint",
    "R": "Rule (old-style, stand-alone)",
    "RF": "Replication-filter-procedure",
    "S": "System base table",
    "SN": "Synonym",
    "SO": "Sequence object",
    "U": "Table (user-defined)",
    "V": "View",
    "EC": "Edge constraint",
    "SQ": "Service queue",
    "TA": "Assembly (CLR) DML trigger",
    "TF": "SQL table-valued-function",
    "TR": "SQL DML trigger",
    "TT": "Table type",
    "UQ": "UNIQUE constraint",
    "X": "Extended stored procedure",
    "ST": "STATS_TREE",
    "ET": "External Table",
}


@dataclass
class SysObject:
    """sys.objects"""

    name: str
    object_id: int
    principal_id: str
    schema_id: int
    schema_name: str
    parent_object_id: int
    type: str
    type_desc: str
    create_date: str
    modify_date: str
    is_ms_shipped: int
    is_published: int
    is_schema_published: int

    def type_as_str(self) -> str:
        """Return the description of type"""
        return _types[self.type]
