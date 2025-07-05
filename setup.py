import sqlite3
def init_db():
    with sqlite3.connect('rbac.db') as conn:
        with open("data base/schema.sql", "r") as schema:
            conn.executescript(schema.read())
        print('DATABASE CREATED')
if __name__=='__main__':
    init_db()
