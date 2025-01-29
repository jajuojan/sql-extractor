"""Helpers for SqlServer"""

import subprocess

from dialects.tsql.tsql_exception import TSqlDataBaseException


def get_local_server_name() -> str:
    """Try to fetch the name of the local server"""
    res = subprocess.run(
        ["sqlcmd", "-Q", "select @@servername;"],
        stdout=subprocess.PIPE,
        text=True,
        check=False,
    )
    return _parse_local_server_name(res.stdout)


def _parse_local_server_name(cmd_output: str) -> str:
    header_end_found = False
    for i in cmd_output.splitlines():
        if header_end_found:
            return i.strip()
        if all(map(lambda x: x == "-", i)):
            header_end_found = True
    raise TSqlDataBaseException("Could not parse local server name from output.")
