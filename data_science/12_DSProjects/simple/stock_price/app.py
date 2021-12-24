import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # A Simple Stock Price App
    Shown are the stock closong price for Google!
    """
)

# define ticker symbol
ticker_symbol = 'GOOGL'

# get data on the ticker symbol
ticker_data = yf.Ticker(ticker_symbol)

# get historical prices for this ticker
ticker_df = ticker_data.history(period='id', start='2010-5-31', end='2020-5-31')

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)