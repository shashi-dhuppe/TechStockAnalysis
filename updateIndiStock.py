# Importing the libraries

import pymysql

import stock as s
import config_stockAnalysis as csa

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
        
		# for row in cur:
		# 	cur.execute(s.createStockTable(row[0]))
		# 	cur.execute(s.insert(row[0]))
		# 	conn.commit()
		
		# conn.commit()

		t2 = "Select * from Stock"
		cur.execute(t2)

		for row in cur:
			print(row)

	# This stockName should be read from some file
	# stockName = "AAPL"
	
	# print(s.createStockTable(stockName))
	# print(s.insert(stockName))
	return

if __name__ == "__main__":
	main()
