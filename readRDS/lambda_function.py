# Importing Libraries
import json
import os
import logging
import sys
import pymysql

# rds settings
rds_host = os.environ['rds_instance_endpoint']
name = os.environ['name']
password = os.environ['password']
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
    
    with conn.cursor() as cur:
        
        cur.execute("select * from AAPL")
        conn.commit()
        
        for row in cur:
            logger.info(row)
    conn.commit()
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Query Executed Successfully')
    }