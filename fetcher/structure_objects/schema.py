"""TBD"""
from dataclasses import dataclass


@dataclass
class Schema:
    """Database agnostic schema"""

    name: str
