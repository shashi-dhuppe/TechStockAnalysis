# Importing the libraries

import yfinance as yf

# This function takes stock name as an input and saves the input.csv after transforming the input
def etl(ticker):
	# Getting the stock ticker from yahoo finance
	stock = yf.Ticker(ticker)

	# Getting the history of the stock for the last 32 days
	df = stock.history(period="32d")

	# Sorting it so that latest data is first and then calculating the percentage change
	# wrt to 1 day prior, 1 week prior and 1 month prior

	df.sort_values(['Date'],ascending=False,inplace=True)

	df['Rel Change(%) - 1 day']=round((df['Open']-df['Open'].shift(-1))/df['Open']*100,4)
	df['Rel Change(%) - 7 day(1 week)']=round((df['Open']-df['Open'].shift(-7))/df['Open']*100,4)
	df['Rel Change(%) - 30 day(1 month)']=round((df['Open']-df['Open'].shift(-30))/df['Open']*100,4)

	fname = ticker + ".csv"
	df.to_csv(fname)

def main():

	# This stockName should be read from some file
	stockName = "aapl"
	
	etl(stockName)
	print("Stock Data Saved Successfully")
	return

if __name__ == "__main__":
	main()
