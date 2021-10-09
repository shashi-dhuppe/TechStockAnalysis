# Importing Libraries
import json
import os
import logging
import sys
import pymysql


# rds settings
rds_host = os.environ['rds_instance_endpoint']
name = os.environ['db_username']
password = os.environ['db_password']
db_name = os.environ['db_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name,connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    
    param = event['queryStringParameters']
    
    # Function to build query which takes i/p from API about stockName and stockWeight(optional)
    def insertQueryBuilder():
        pre = "INSERT INTO Stock (stock_symbol"
        if 'sw' in param:
            w = ",weight) VALUES ("
            pre = pre + w
        else:
            pre = pre + ") VALUES("
        
        v1 = param['sname']
        
        if 'sw' in param:
            v2 = param['sw']
            post = "'"+v1 + "'," + str(v2) + ")"
        
        else:
            post = "'"+v1 + "')"
        
        q = pre + post
        
        return q
        
    with conn.cursor() as cur:
        
        # cur.execute("""
        #     CREATE TABLE IF NOT EXISTS Stock 
        #     ( 
        #         stock_id INT AUTO_INCREMENT PRIMARY KEY,
        #         stock_name varchar(255) NOT NULL, 
        #         stock_symbol varchar(10) NOT NULL,
        #         weight FLOAT
        #     )
        # """)
        # conn.commit()
        
        cur.execute(insertQueryBuilder())
        conn.commit()
        
        cur.execute("select * from Stock")
        conn.commit()
        
        for row in cur:
            logger.info(row)
    conn.commit()
    
    return {
        "statusCode": 200,
        "body":json.dumps("Everything working fine")
    }