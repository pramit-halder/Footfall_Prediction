import pandas as pd
import numpy as np
import time
import sklearn.metrics as skl
from statsmodels.tsa.statespace.sarimax import SARIMAX
def m_sar(f):
    s = time.time()
    df_tsa = pd.read_csv("TSA Passenger Volumes.csv", parse_dates=['Date'], index_col=['Date'])
    df_tsa.dropna(axis=0, inplace=True)
    train = df_tsa.iloc[:-75]
    test = df_tsa.iloc[-75:]
    model_SARIMA=SARIMAX(train['footfall'],order=(3,1,1),seasonal_order=(0,1,0,30))
    s1 = len(train)
    e1 = len(train) + len(test) - 1
    model_SARIMA_fit = model_SARIMA.fit()
    pred1 = model_SARIMA_fit.predict(start=s1, end=e1, typ='levels')
    pred1 = np.array(pred1)
    if f==1:
        start = len(train) + len(test) + 73
        end = len(train) + len(test) + 80
    if f==2:
        start = len(train) + len(test) + 80
        end = len(train) + len(test) + 87
    if f==3:
        start = len(train) + 46
        end = len(train) + 64
    predicted_footfall = model_SARIMA_fit.predict(start=start,end=end,dynamic=True)
    predicted_footfall = np.array(predicted_footfall)
    test1 = np.array(test["footfall"])
    res2 = np.sum(predicted_footfall)
    e = time.time()
    t = e - s
    mae = round(skl.mean_absolute_error(test1, pred1), 2)
    return f"  SARIMA footfalls: {round(res2,2)} | Time: {round(t, 3)} secs | Mean Absolute Error: {mae}"
