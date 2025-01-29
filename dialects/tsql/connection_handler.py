"""tbd"""

from connection.database import DataBaseConnection
from dialects.tsql.connection.tsql_database import (
    with_connection,
    with_local_connection,
)


class TsqlConnectonHandler:
    """Handles the connection to the database"""

    def __init__(self) -> None:
        pass

    def get_connection(
        self, dialect: str, connection_string: str
    ) -> DataBaseConnection:
        """Returns the DB-connection based on the dialect and connection string"""
        if dialect == "tsql":
            if connection_string.startswith("local:"):
                db_name = connection_string.split(":")[1]
                db_instance = with_local_connection(db_name)
            else:
                db_instance = with_connection(connection_string)
            return db_instance

        raise NotImplementedError("Unknown dialect")
