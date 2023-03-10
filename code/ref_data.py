import pandas as pd
from yahoofinancials import YahooFinancials

def get_sp100():
    """_summary_

    Returns:
        _type_: _description_
    """    
    csv_file = '../data/sp-100-index-03-07-2023.csv'
    df =pd.read_csv(csv_file)
    return list(df['Symbol'])


def get_yahoo_data(start_date,end_date,tickers,freq):
    list_comps = []
    for ticker in tickers:
        try:
            data = YahooFinancials(ticker).get_historical_price_data(start_date, end_date, freq)
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
            list_comps.append(prices)
        except:
            continue



    final_df=pd.concat(list_comps)   
    return final_df

#part 3c

def get_sentiment_word_dict():
    df1 = pd.read_csv('../data/LM-dictionary-2021.csv')
    sentiment_words = ['Negative', 'Positive', 'Uncertainty', 'Litigious', 'Strong_Modal', 'Weak_Modal', 'Constraining']
    sentiment_dict = {}
    for n in sentiment_words:
        sentiment_dict[n] = []
        for i in range(0, len(df1.index)):
            if df1.loc[i, n] != 0:
                sentiment_dict[n].append(df1.loc[i, 'Word'].lower())

    return sentiment_dict

