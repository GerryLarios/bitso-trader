import os
import logging
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from schema import create_all_tables


def connect():
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(os.environ['POSTGRES_USER'],
                     os.environ['POSTGRES_PASSWORD'],
                     os.environ['HOST'],
                     os.environ['PORT'],
                     os.environ['POSTGRES_DB'])
    return create_engine(url, echo=True)

# SqlAlchemy instances
Base = declarative_base()
engine = connect()
session = sessionmaker(bind=engine)()


def database_is_empty():
    tables = inspect(engine).get_table_names()
    return tables == []

def setup():
    if database_is_empty():
        create_all_tables(engine)
    return session 

def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            session.commit()
            logging.info("success calling db func: " + func.__name__)
            return True
        except SQLAlchemyError as e:
            logging.error(e.args)
            session.rollback()
            return False
    return persist

@db_persist
def insert_or_update(model):
    return session.merge(model)

