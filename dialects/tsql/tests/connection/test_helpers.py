# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

from unittest import TestCase

from dialects.tsql.connection.helpers import _parse_local_server_name
from tests.helpers import get_test_data


class Test(TestCase):
    def test_parse_local_server_name(self) -> None:
        input_data = get_test_data("local_server_name.txt")
        res = _parse_local_server_name(input_data)
        self.assertEqual(res, "DESKTOP-1V23A4B")

    def test_parse_local_server_name_invalid(self) -> None:
        with self.assertRaises(Exception) as context:
            _parse_local_server_name("empty\n--\n")
        self.assertTrue(
            "Could not parse local server name from output." in str(context.exception)
        )
