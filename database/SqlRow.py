class SqlRow:
    def __init__(self, items=None):
        self.items = items if items else []


# (name, type_code, display_size, internal_size, precision, scale, null_ok).
class SqlRowItem:
    def __init__(self):
        self.column_name = None
        self.value = None
        self.type = None
        self.internal_size = None
        self.precision = None
        self.scale = None
