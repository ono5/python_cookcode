import sqlite3


# Create DB
# conn = sqlite3.connect('test_sqlite.db')

conn = sqlite3.connect(':memory:')

# Create cursor
curs = conn.cursor()

curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)

curs.execute(
    'UPDATE persons set name="Hiroki" WHERE name = "Mike"'
)

curs.execute(
    'DELETE FROM persons WHERE name = "Hiroki"'
)

# Commit
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# Cursor close
curs.close()

# Connection close
conn.close()
