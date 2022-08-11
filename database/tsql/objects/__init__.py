from database.TSqlDatabase import TSqlDataBase

# TODO
# db2
# mysql
# oracle
# postgres
# sqlite
# tsql
def get_database_type(database_type: str) -> TSqlDataBase:
    if database_type == "tsql":
        return TSqlDataBase()
    raise Exception("TBD")
