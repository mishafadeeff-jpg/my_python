from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:1606@localhost:5432/postgres"

Base = declarative_base()


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(20))
    company_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)


def get_engine():
    return create_engine(DATABASE_URL, echo=False)


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
