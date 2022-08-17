"""Entry-point"""
from database.tsql_database import with_local_connection


def _main() -> None:
    db_instance = with_local_connection("AdventureWorks")
    print(db_instance.get_version())
    # print(db.fetch_raw_sql("SELECT * FROM Person.BusinessEntity;"))
    # print(fetch_principals(db))
    print(db_instance.fetch_sql_rows("SELECT * FROM Person.BusinessEntity;"))


if __name__ == "__main__":
    _main()
