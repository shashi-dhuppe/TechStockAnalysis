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

def main():

	# This stockName should be read from some file
	stockName = "aapl"
	
	print(etl(stockName))
	return

if __name__ == "__main__":
	main()
