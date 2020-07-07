import database
import logging
import pandas
import time
from sqlalchemy.exc import SQLAlchemyError
from bitso_api import BitsoAPI
from datetime import datetime
from schema import Trade

def extract_trades(dataframe):
    logging.info('######### UPDATING DATABASE AT {} #########'.format(datetime.today()))
    for idx, row in dataframe.iterrows():
        trade = Trade(id         = row.tid,
                      book       = row.book, 
                      maker_side = row.maker_side,
                      amount     = row.amount,        
                      price      = row.price, 
                      created_at = row.created_at)
        record = database.insert_or_update(trade)
        if(record):
            logging.info('Trade inserted: {}'.format(trade.id))
    logging.info('###########################################')

def main():
    try:
        session = database.setup()
        api = BitsoAPI('eth_mxn')
        while True:
            logging.info('========= FETCH DATA =========')
            response = api.trades(25)
            dataframe = pandas.DataFrame(response['payload'])
            logging.info('==============================')
            extract_trades(dataframe)
            time.sleep(60)
    except:
        logging.error('Something went wrong with the system!')

if __name__ == '__main__':
    main()
