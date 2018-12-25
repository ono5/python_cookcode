import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# memory
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

# sqlite
# engine = sqlalchemy.create_engine('sqlite:///:test_sqlite2:', echo=True)

# mysql
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root@localhost/test_mysql_database2', echo=True)


Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

# Create session to access Database
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# Add value to Database
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

# Update data
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# Delete data
p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

# Fetch data from database
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)