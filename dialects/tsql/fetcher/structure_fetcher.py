"""TBD"""


from fetcher.structure_fetcher import StructureFetcher
from fetcher.structure_objects.database import DatabaseStructure


class TsqlStructureFetcher(StructureFetcher):
    """Fetcher for database structure"""

    def fetch(self) -> DatabaseStructure:
        return DatabaseStructure()
