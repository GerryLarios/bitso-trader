import os
import sqlalchemy
from schema import set_tables

def connect():
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(
        os.environ['POSTGRES_USER'],
        os.environ['POSTGRES_PASSWORD'],
        os.environ['HOST'],
        os.environ['PORT'],
        os.environ['POSTGRES_DB'])
    engine = sqlalchemy.create_engine(url, echo=True)
    meta = sqlalchemy.MetaData(bind=engine, reflect=True)
    return engine, meta

def database_is_empty(engine):
    tables = sqlalchemy.inspect(engine).get_table_names()
    return tables == []

def setup():
    engine, meta = connect()
    if database_is_empty(engine):
        set_tables(meta)
        meta.create_all(engine, checkfirst=True)
