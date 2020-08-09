import requests
import time
from io import StringIO
import pandas as pd
import numpy as np
import pickle


def create_today_timestamp():
    today = time.strftime("%Y-%m-%d", time.gmtime())
    return int(time.mktime(time.strftime(today, "%Y-%m-%d")))


def create_timestamp_from_today(n):
    today = create_today_timestamp()
    return today + n*24*3600


# tomorrow_timestamp = create_timestamp_from_today(1)

def create_tw_stock_info_list():
    res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
    df = pd.read_html(res.text)[0]
    df.columns = df.iloc[0]
    f = df['有價證券代號及名稱'] != df['國際證券辨識號碼(ISIN Code)']
    df = df[f]
    df = df.iloc[2:]
    df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)
    df = df.reset_index(drop=True)
    new_df = df['有價證券代號及名稱'].str.replace(
        u'\u3000', ' ').str.split(u' ', 1)
    new_df.columns = ['Ticker', 'StockName']
    new_df['Sector'] = df['產業別']
    return new_df


tw_stack_list = create_tw_stock_info_list()
print(tw_stack_list)
