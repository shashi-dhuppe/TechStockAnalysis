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

# try:
#     conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name,connect_timeout=5)
# except pymysql.MySQLError as e:
#     logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
#     logger.error(e)
#     sys.exit()

# logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

# This function takes stock name as an input and returns the INSERT Query string
def etl(ticker):
    # Getting the stock ticker from yahoo finance
    stock = yf.Ticker(ticker)

    # Get 1 day prior market data
    df = stock.history(period="1d").reset_index()

    # Converting and only choosing Date, Open, High, Low and Close Value
    dfl = list(df.iloc[0,:5])

    # Converting datetime to string and rounding all other values up to 4 precision points
    dfl[0] = str(dfl[0])
    for i in range(1,len(dfl)):
        dfl[i] = round(dfl[i],4)

    # Preparing insert string piece
    s = str(dfl).replace('[','').replace(']','')

    # Forming an INSERT Query
    insert = 'INSERT IGNORE INTO '+str(ticker)+ "("+s + ");"

    return insert

def lambda_handler(event, context):
    
    # with conn.cursor() as cur:
        
    #     # cur.execute("select stock_symbol from Stock")
    #     # conn.commit()
        
    #     stockSymbols = ['absakshdiashdo']
        
    #     # for row in cur:
    #     #     stockSymbols.append(row[0])
            
    #     # for i in stockSymbols:
    #     #     print(etl(i))
    #     #     break
            
    # print(etl(stockSymbols[0]))
    print(etl('AAPL'))
        
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