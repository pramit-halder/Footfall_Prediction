import numpy as np
import statsmodels.api as sms
import sklearn.metrics as skl
# from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import time

def m_ar(f):
    s = time.time()
    df_tsa = pd.read_csv("TSA Passenger Volumes.csv", parse_dates=['Date'], index_col=['Date'])
    df_tsa.dropna(axis=0, inplace=True)
    df_tsa['footfall 1st Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(1)
    df_tsa['footfall 12 Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(12)
    df_tsa['footfall 2 Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(2)
    df_tsa.drop(df_tsa.iloc[:, 1:], inplace=True, axis=1)
    df_tsa['footfall First Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(1)
    df_tsa['footfall 30 Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(30)
    df_tsa['footfall 30 Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(30)
    df_tsa['footfall 365 Difference'] = df_tsa['footfall'] - df_tsa['footfall'].shift(365)
    stepwise_fit = auto_arima(df_tsa['footfall'], trace=True,suppress_warnings=True)
    train = df_tsa.iloc[:-75]
    test = df_tsa.iloc[-75:]
    model = ARIMA(train['footfall'], order=(3, 1, 1))
    model = model.fit()
    s1 = len(train)
    e1 = len(train) + len(test) - 1
    pred_ar = model.predict(start=s1, end=e1, typ='levels')
    p_ar = np.array(pred_ar)
    if f==1:
        start = len(train) + len(test) + 73
        end = len(train) + len(test) + 80
    if f==2:
        start = len(train) + len(test) + 80
        end = len(train) + len(test) + 87
    if f==3:
        start = len(train) + 46
        end = len(train) + 64
    pred = model.predict(start=start, end=end, typ='levels').rename('ARIMA Predictions')
    pred = np.array(pred)
    res1 = np.sum(pred)
    e = time.time()
    t = e - s
    test1 = np.array(test["footfall"])
    mae = round(skl.mean_absolute_error(test1, p_ar), 2)
    return f" ARIMA footfalls: {round(res1,2)} | Time: {round(t, 2)} secs | | Mean Absolute Error: {mae}"
print(m_ar(1))







