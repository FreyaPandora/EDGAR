
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
        prices['1daily_return'] = (prices['open'] - prices['close'])/prices['open']
        prices['2daily_return'] = (prices['open'].shift(1) - prices['close'])/prices['open'].shift(1)
        prices['3daily_return'] = (prices['open'].shift(2) - prices['close'])/prices['open'].shift(2)
        prices['5daily_return'] = (prices['open'].shift(4) - prices['close'])/prices['open'].shift(4)
        prices['10daily_return'] = (prices['open'].shift(9) - prices['close'])/prices['open'].shift(9)
        prices.drop(columns = ['date','adjclose','open','close'],inplace=True)
        return prices


#part 3c
df1 = pd.read_csv('LM-dictionary-2021.csv')
sentiment_words = ['Negative', 'Positive', 'Uncertainty', 'Litigious', 'Strong_Modal', 'Weak_Modal', 'Constraining']

def get_sentiment_word_dict():
    sentiment_dict = {}
    for n in sentiment_words:
        sentiment_dict[n] = []
        for i in range(0, len(df1.index)):
            if df1.loc[i, n] != 0:
                sentiment_dict[n].append(df1.loc[i, 'Word'])

    return sentiment_dict

get_sentiment_word_dict()['Positive']