import sqlite3

connection = sqlite3.connect('test.db')
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS category(
id INTEGER PRIMARY KEY,
name TEXT,
money INTEGER,
date TEXT
);
""")

connection.commit()
