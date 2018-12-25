import sqlite3

import memcache

db = memcache.Client(['127.0.0.1:11211'])

# SQLite3
conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
curs.execute(
    'CREATE TABLE persons('
    'employee_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()


# Retrieve data from database
def get_employ_id(name):
    employ_id = db.get(name)
    # if memcached archives data, it returns data
    if employ_id:
        return employ_id
    # No memcached data, so, access sqlite3 to retrieve data
    curs.execute(
        'SELECT * FROM persons WHERE name = "{}"'.format(name)
    )
    person = curs.fetchone()
    # Check data in sqlite3
    if not person:
        raise Exception('No employ')
    # unpacking data
    employ_id, name = person
    # set data into memcached
    db.set(name, employ_id, time=60)
    return employ_id


print(get_employ_id("Mike"))


curs.close()
conn.close()


