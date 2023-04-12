import numpy as np
import pandas as pd
import time
from statsmodels.tsa.api import SimpleExpSmoothing
import sklearn.metrics as skl

def m_ew(f):
    s = time.time()
    df_tsa = pd.read_csv("TSA Passenger Volumes.csv", parse_dates=['Date'], index_col=['Date'])
    df_tsa.dropna(axis=0, inplace=True)
    df_tsa['footfall:10 days rolling'] = df_tsa['footfall'].rolling(window=10, min_periods=1).mean()
    df_tsa['footfall:20 days rolling'] = df_tsa['footfall'].rolling(window=20, min_periods=1).mean()
    df_tsa['footfall:30 days rolling'] = df_tsa['footfall'].rolling(window=30, min_periods=1).mean()
    df_tsa['footfall:40 days rolling'] = df_tsa['footfall'].rolling(window=50, min_periods=1).mean()
    df_tsa['EMA_0.1'] = df_tsa['footfall'].ewm(alpha=0.1, adjust=False).mean()
    df_tsa['EMA_0.3'] = df_tsa['footfall'].ewm(alpha=0.3, adjust=False).mean()
    df_tsa['EMA_5days'] = df_tsa['footfall'].ewm(span=5).mean()

    train = df_tsa.iloc[:-75]
    test = df_tsa.iloc[-75:]
    model = SimpleExpSmoothing(df_tsa['footfall'])
    model_fit = model.fit(smoothing_level=0.2, optimized=False)
    s1 = len(train)
    e1 = len(train) + len(test) - 1
    pred_ew = model_fit.predict(start=s1, end=e1)
    p_ew = np.array(pred_ew)
    if f==1:
        start = len(train) + len(test) + 73
        end = len(train) + len(test) + 80
    if f==2:
        start = len(train) + len(test) + 80
        end = len(train) + len(test) + 87
    if f==3:
        start = len(train) + 46
        end = len(train) + 64
    pred = model_fit.predict(start=start, end=end).rename('ewma Predictions')
    pred = np.array(pred)
    res3 = np.sum(pred)
    e = time.time()
    t = e - s
    t1 = np.array(test["footfall"])
    mae = round(skl.mean_absolute_error(t1, p_ew), 2)
    return f"EWMA footfalls: {round(res3,2)} | Time: {round(t, 2)} secs | Mean Absolute Error: {mae}"
print(m_ew(1))


