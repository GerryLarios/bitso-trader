from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Date, UniqueConstraint

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True, unique=True)
    book = Column(String)
    maker_side = Column(String)
    amount = Column(String)
    price = Column(String)
    created_at = Column(String)

    def __repr__(self):
        return f'{self.maker_side} : {self.amount} {self.book} * ${self.price} at {self.created_at}'

def create_all_tables(engine):
    Base.metadata.create_all(engine, checkfirst=True)

