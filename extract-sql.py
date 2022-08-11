import pyodbc
import subprocess


from database.TSqlDatabase import with_local_connection
from database.tsql.object_fetchers import fetch_principals


def main():
    db = with_local_connection("AdventureWorks")
    print(db.get_version())
    # print(db.fetch_raw_sql("SELECT * FROM Person.BusinessEntity;"))
    # print(fetch_principals(db))
    print(db.fetch_sql_rows("SELECT * FROM Person.BusinessEntity;"))

if __name__ == "__main__":
    main()
