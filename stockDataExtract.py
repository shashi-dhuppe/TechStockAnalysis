# Importing the libraries

import yfinance as yf

# This function takes stock name as an input and saves the input.csv after transforming the input
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

def createStockTable(ticker):
	pre = "CREATE TABLE IF NOT EXISTS "
	post = """
		(DateEntry DATETIME PRIMARY KEY,
		Open FLOAT NOT NULL,
		High FLOAT NOT NULL,
		Low FLOAT NOT NULL,
		Close FLOAT NOT NULL,
		Volume FLOAT NOT NULL,
		OneDayChange FLOAT,
		OneWeekChange FLOAT,
		OneMonthChange FLOAT
		);
	"""

	return (pre + ticker + post)

def main():

	# This stockName should be read from some file
	stockName = "AAPL"
	
	print(createStockTable(stockName))
	print(etl(stockName))
	return

if __name__ == "__main__":
	main()
