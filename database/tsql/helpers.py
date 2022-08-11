import subprocess
from typing import Union


def get_local_server_name() -> str:
    res = subprocess.run(
        ["sqlcmd", "-Q", "select @@servername;"], stdout=subprocess.PIPE, text=True
    )
    return _parse_local_server_name(res.stdout)


def _parse_local_server_name(cmd_output: str) -> str:
    header_end_found = False
    for i in cmd_output.splitlines():
        if header_end_found:
            return i.strip()
        if all(map(lambda x: x == "-", i)):
            header_end_found = True
    raise Exception("Could not parse local server name from output.")
