# Importing Libraries
import json
import os
import logging
import sys
import pymysql

import yfinance as yf

# rds settings
rds_host = os.environ['rds_instance_endpoint']
db_name = os.environ['db_name']
name = os.environ['db_username']
password = os.environ['db_password']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name,connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# This function takes stock name as an input and returns the INSERT Query string
def etl(ticker):
    # Getting the stock ticker from yahoo finance
    stock = yf.Ticker(ticker)

    # Getting the history of the stock for the last day
    # df = stock.history(period="1d")
    
    # return df
    # return str(stock)

    # Sorting it so that latest data is first and then calculating the percentage change
    # wrt to 1 day prior, 1 week prior and 1 month prior

    # df.sort_values(['Date'],ascending=False,inplace=True)

    # df['Rel Change(%) - 1 day']=round((df['Open']-df['Open'].shift(-1))/df['Open']*100,4)
    # df['Rel Change(%) - 7 day(1 week)']=round((df['Open']-df['Open'].shift(-7))/df['Open']*100,4)
    # df['Rel Change(%) - 30 day(1 month)']=round((df['Open']-df['Open'].shift(-30))/df['Open']*100,4)

    # df.to_csv(fname)

def lambda_handler(event, context):
    
    with conn.cursor() as cur:
        
        # cur.execute("select stock_symbol from Stock")
        # conn.commit()
        
        stockSymbols = ['absakshdiashdo']
        
        # for row in cur:
        #     stockSymbols.append(row[0])
            
        # for i in stockSymbols:
        #     print(etl(i))
        #     break
            
    print(etl(stockSymbols[0]))
        
    #     # cur.execute(insertQueryBuilder())
    #     # conn.commit()
        
    #     # cur.execute("select * from Stock")
    #     # conn.commit()
        
    #     for row in cur:
    #         logger.info(row)
    # conn.commit()
    
    return {
        "statusCode": 200,
        "body":json.dumps("Everything working fine")
    }