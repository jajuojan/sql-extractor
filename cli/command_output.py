"""Command output classes."""
from dataclasses import dataclass
from enum import Enum
from typing import Union


class CommandResultStatus(Enum):
    """The result status of a command."""

    SUCCESS = 1
    ERROR = 2


@dataclass
class CommandResult:
    """Command result."""

    status: CommandResultStatus
    message: Union[str, None] = None


class CommandException(Exception):
    """Command exception."""

    def __init__(self, message: str):
        """Constructor."""
        super().__init__(message)
        self.message = message
