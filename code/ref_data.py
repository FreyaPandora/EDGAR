import pandas as pd
from yahoofinancials import YahooFinancials

def get_sp100():
    """
    Returns a list of all the tickers in the S&P100 obtained from csv file. 

    Returns:
        "list(df['Symbol'])" (list): list of all the S&P100 tickers
    """    
    # Opens the csv containing companied from S&P100 
    csv_file = '../data/sp-100-index-03-07-2023.csv'
    
    # Creates a dataframe and return only the tickers as a list
    df =pd.read_csv(csv_file)
    return list(df['Symbol'])


def get_yahoo_data(start_date,end_date,tickers,freq):
    """
    Obtains yahoo financials data, stores it in a dataframe, calculates the daily returns
    and returns a dataframe containing financial data on all the tickers

    Args:
        start_date (str): start date to obtain data
        end_date (str): last data to obtain data
        tickers (list): list of all the ticker we are interested in
        freq (str): frequency at which data should be taken, i.e. 'daily', 'yearly', etc..

    Returns:
        final_df (dataframe): dataframe containing financial data on all tickers in S&P100
    """    
    list_comps = []
    
    # Goes through every ticker in the S&P100
    for ticker in tickers:
        
        # Tries to obtain yahoo financial data for the ticker, if the ticker has no available data
        #       for the ticker, skip it.
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
    
    # Joins the list of dataframes together into one big dataframe and return it.
    final_df=pd.concat(list_comps)   
    return final_df

def get_sentiment_word_dict():
    """
    Creates a dictionary containing all the positive words, negative words, etc... This 
    dictionary will be used to perform the sentimental analysis and categorise the words
    from the websites.

    Returns:
        sentimental_dict (dict): dictionary containing all relevant words categorised into
                                 their sentimental values.
    """
    
    # Obtains the LM-dictionary csv and imports it into dataframe.    
    df1 = pd.read_csv('../data/LM-dictionary-2021.csv')
    sentiment_words = ['Negative', 'Positive', 'Uncertainty', 'Litigious', 'Strong_Modal', 'Weak_Modal', 'Constraining']
    sentiment_dict = {}
    
    # Goes through every row in the dataframe, and if that word holds a sentimental value include it into the
    #       dictionary.
    for n in sentiment_words:
        sentiment_dict[n] = []
        for i in range(0, len(df1.index)):
            if df1.loc[i, n] != 0:
                sentiment_dict[n].append(df1.loc[i, 'Word'].lower())

    return sentiment_dict

