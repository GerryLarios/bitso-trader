import database
import logging
import pandas
import time
from sqlalchemy.exc import SQLAlchemyError
import bitso_api
from datetime import datetime
from schema import Trade


session = database.setup() # create database schema if not exists.

response = bitso_api.fetch_trades()
dataframe = pandas.DataFrame(response['payload'])

def extract_trades():
    for idx, row in dataframe.iterrows():
        trade = Trade(id         = row.tid,
                      book       = row.book, 
                      maker_side = row.maker_side,
                      amount     = row.amount,        
                      price      = row.price, 
                      created_at = row.created_at)
        record = database.insert_or_update(trade)

while True:
    logging.info('######### UPDATING DATABASE AT {} #########'.format(datetime.today()))
    extract_trades()
    time.sleep(60)
