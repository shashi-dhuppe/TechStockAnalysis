# Importing the libraries
import yfinance as yf

# This py file contains various methods for Individual Stock
# All methods take stock symbol as input and return string query as output

# This function takes stock name as an input and saves the input.csv after transforming the input
def insert(ticker):
	# Getting the stock ticker from yahoo finance
	stock = yf.Ticker(ticker)

	# Get 1 day prior market data
	df = stock.history(period="1d").reset_index()

	# Converting and only choosing Date, Open, High, Low and Close Value
	dfl = list(df.iloc[0,:6])

	# Converting datetime to string and rounding all other values up to 4 precision points
	dfl[0] = str(dfl[0])
	for i in range(1,len(dfl)):
		dfl[i] = round(dfl[i],4)

    # Preparing insert string piece
	s = str(dfl).replace('[','').replace(']','')

	s2 = " , NULL, NULL, NULL"

    # Forming an INSERT Query
	insert = 'INSERT INTO '+str(ticker)+ " VALUES ("+s + s2 + ");"

	return insert

def createStockTable(ticker):
	pre = "CREATE TABLE IF NOT EXISTS "
	post = """
		( 
		DateEntry DATETIME PRIMARY KEY,
		Open DECIMAL(19,4) NOT NULL,
		High DECIMAL(19,4) NOT NULL,
		Low DECIMAL(19,4) NOT NULL,
		Close DECIMAL(19,4) NOT NULL,
		Volume DECIMAL(19,4) NOT NULL,
		OneDayChange DECIMAL(19,4),
		OneWeekChange DECIMAL(19,4),
		OneMonthChange DECIMAL(19,4)
		);
	"""

	return (pre + ticker + post)

def dropTable(ticker):
	pre = "DROP TABLE "
	return (pre + ticker + ";")