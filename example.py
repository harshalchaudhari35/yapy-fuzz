
from yapyfuzz.core import Fuzzy
from yapyfuzz.handler import ListHandler, SQLiteHandler, PostgresHandler
import os

root_dir = os.path.abspath(__file__)

terms = ["hello", "world", "foo", "bar"]
list_handler = ListHandler()
list_handler.reader(terms)

name = f"{root_dir}/yapy/fuzzy.db"
query = "select * from albums"
db_handler = SQLiteHandler()
db_handler.reader(name, query)

db_settings = {
    "user":"postgres",
    "password":"postgres",
    "host":"localhost",
    "port":"5432",
    "dbname":"dellstore",
}

pg_handler = PostgresHandler()
# pg_handler.reader(query="select table_schema, table_name from information_schema.tables")
pg_handler.reader(query="select * from categories", **db_settings)
pg_handler.reader(query="select * from inventory", **db_settings)

fp = Fuzzy(pg_handler)
fp.get_selection()

fp = Fuzzy(list_handler)
fp.get_selection()

fp = Fuzzy(db_handler)
fp.get_selection()


# output = os.popen(
#     "sqlite3 /home/harshal/Works/oss_projects/pyfuzzy/pyfuzzy/fuzzy.db \"select * from albums\""
# ).read().encode("utf-8")
# type(output)