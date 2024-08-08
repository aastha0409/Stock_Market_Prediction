import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from keras.models import load_model
import streamlit as st


start = '2010-01-01'
end = '2019-12-31'


st.title('Stock Market Prediction')


user_input = st.text_input("Enter Stock Ticker", 'AAPL')
df = yf.download(user_input, start, end)



st.subheader('Data from 2010 - 2019')
st.write(df.describe())