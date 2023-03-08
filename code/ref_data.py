
import csv
import pandas as pd
import yahoofinancials
from yahoofinancials import YahooFinancials



csv_file = 'sp-100-index-03-07-2023.csv'
def get_sp100():
    # sp100 = []
    # with open(csv_file,newline='\n'):
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for row in csv_reader:
    #         sp100.append(row)
    #     return df, sp100
    df =pd.read_csv(csv_file)
    
    return list(df['Symbol'])



def get_yahoo_data(start_date,end_date,tickers):


    for ticker in tickers:
        data = YahooFinancials(ticker).get_historical_price_data(start_date, end_date, 'daily')
        prices = pd.DataFrame(data[ticker]['prices'])
        prices['1daily_return'] = prices['open'] - prices['close'].shift(1)
        return prices

