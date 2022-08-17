"""TBD"""


from typing import List, Union


# (name, type_code, display_size, internal_size, precision, scale, null_ok).
class SqlRowItem:
    """TBD"""

    def __init__(self) -> None:
        """TBD"""
        self.column_name = None
        self.value = None
        self.type = None
        self.internal_size = None
        self.precision = None
        self.scale = None


class SqlRow:
    """TBD"""

    def __init__(self, items: Union[List[SqlRowItem], None] = None) -> None:
        """TBD"""
        self.items = items if items else []
