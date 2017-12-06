import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base=declarative_base()

class Employee(Base):
    __tablename__='employee'
    firstName=Column(String(10),primary_key=True)
    lastName=Column(String(10),primary_key=True)
    qualification=Column(String(10))
    def __init__(self,firstName,lastName,qualification):
        self.firstName=firstName
        self.lastName=lastName
        self.qualification=qualification

    def __repr__(self):
        return "<Employee(First name='%s', Last name='%s', Qualification='%s')>" % (self.firstName, self.lastName,self.qualification)