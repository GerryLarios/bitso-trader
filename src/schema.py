from sqlalchemy import Table, Column, Integer, String, Date

def set_tables(meta):
    tradres = Table('trades', meta,
                    Column('id', Integer, primary_key=True),
                    Column('book', String),
                    Column('maker_side', String),
                    Column('amount', String),
                    Column('price', String),
                    Column('created_at', Date))
    return [trades]

