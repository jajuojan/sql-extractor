# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

from unittest import TestCase

from formatters.table_md_formatter import MdTableStructureFormatter
from tests.helpers import create_test_table, get_test_data


class Test(TestCase):
    def test_md_formatter(self) -> None:
        formatter = MdTableStructureFormatter()
        result = formatter.format(create_test_table())
        input_data = get_test_data("table_structure_md.txt")
        self.assertEqual(result, input_data)
