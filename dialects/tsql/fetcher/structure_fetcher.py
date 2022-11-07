"""TBD"""


from fetcher.database_structure import DatabaseStructure
from fetcher.structure_fetcher import StructureFetcher


class TsqlStructureFetcher(StructureFetcher):
    """Fetcher for database structure"""

    def fetch(self) -> DatabaseStructure:
        return DatabaseStructure()
