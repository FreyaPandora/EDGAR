
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



def get_yahoo_data(start_date,end_date,ticker):

        data = YahooFinancials(ticker).get_historical_price_data(start_date, end_date, 'daily')
        prices = pd.DataFrame(data[ticker]['prices'])
        prices['1daily_return'] = (prices['close'].shift(-1) - prices['close'])/prices['close']
        prices['2daily_return'] = (prices['close'].shift(-2) - prices['close'])/prices['close']
        prices['3daily_return'] = (prices['close'].shift(-3) - prices['close'])/prices['close']
        prices['5daily_return'] = (prices['close'].shift(-5) - prices['close'])/prices['close']
        prices['10daily_return'] = (prices['close'].shift(-10) - prices['close'])/prices['close']
        prices['Symbol'] = ticker
        prices.drop(columns = ['date','open','close'],inplace=True)
        prices.set_index('formatted_date',inplace=True)
        prices.rename(columns={'adjclose':'price','formatted_date':'date'},inplace=True)
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
                sentiment_dict[n].append(df1.loc[i, 'Word'].lower())

    return sentiment_dict
