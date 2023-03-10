from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

def linear_regessor(predict_target, sentiment_list):
    
    df_sentiment = pd.read_csv(r'..\data\sentiment_factors.csv')
    df_returns = pd.read_csv(r'..\data\stock_returns_daily.csv')
    df_returns.rename(columns = {'formatted_date':'FilingDate'}, inplace = True)
    
    df_clean = pd.merge(df_sentiment, df_returns, on = ['Symbol', 'FilingDate'],  how = 'left')
    df_clean.dropna(axis = 0, inplace = True)
    
    def min_max_norm(df, column):
        df[f'{column}_norm'] = (df[column]-df[column].min())/(df[column].max()-df[column].min())

        return df[f'{column}_norm']

    sentiment_norm_list = []
    for i in sentiment_list:
        df_clean[f'{i}_norm'] = min_max_norm(df_clean, i)
        sentiment_norm_list.append(f'{i}_norm')
    
    df_train, df_test = train_test_split(df_clean, test_size=0.2, random_state=0)

    features = sentiment_norm_list

    X_train = df_train[features]
    y_train = df_train[predict_target]
    X_test = df_test[features]
    y_test = df_test[predict_target]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = f'{mean_squared_error(y_test, y_pred)}'
    rmse = f'{mean_squared_error(y_test, y_pred)**0.5:.4f}'
    mae = f'{mean_absolute_error(y_test,y_pred)}'
    r2 = f'{r2_score(y_test, y_pred)}'
    
    return (mse, rmse, mae, r2)