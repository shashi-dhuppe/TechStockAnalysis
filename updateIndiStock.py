# Importing the libraries

import pymysql

import stock as s
import config_stockAnalysis as csa

from datetime import date

def main():

	# rds settings
	rds_host = csa.rds_host
	db_name = csa.db_name
	name = csa.name
	password = csa.password

	try:
		conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name,connect_timeout=5)
		print("SUCCESS: Connection to RDS MySQL instance succeeded")
	except pymysql.MySQLError as e:
		print("ERROR: Unexpected error: Could not connect to MySQL instance.")
		print(e)

	with conn.cursor() as cur:
	
		temp = "Select stock_symbol from Stock"
		cur.execute(temp)
		conn.commit()
        
		for row in cur:
			cur.execute(s.createStockTable(row[0]))
			cur.execute(s.insert(row[0]))
			conn.commit()
		
		conn.commit()
	
	f = open("log_updateStock.txt", "a")
	today = date.today()
	f.write("\nToday's date: " + str(today))
	f.close()


	return

if __name__ == "__main__":
	main()
