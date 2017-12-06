import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:password@localhost/test')
Base = declarative_base()

class Employee(Base):
    __tablename__='emp'

    empid=Column(Integer,primary_key=True)
    name=Column(String(10))

    def __repr__(self):
        return "<Employee(id='%s', name='%s')>" % (self.empid, self.name)

Session = sessionmaker(bind=engine)
session=Session()
emp=Employee(empid='456',name='Amit')
session.add(emp)
session.commit()