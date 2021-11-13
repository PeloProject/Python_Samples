import sqlite3
import os

curdir = os.getcwd()
print(curdir)

dbname = "test.db"
conn = sqlite3.connect(dbname)
conn.close()
print("test")
