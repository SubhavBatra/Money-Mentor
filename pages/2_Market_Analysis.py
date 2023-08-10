import streamlit as st
from helper import get_info
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")
subheading = st.header("Learn and grow")

st.subheader("Let's see what's happening in the market today")

# dropdown
stock = st.selectbox("Select a stock", ["ACN", "AXP", "BLK", "BP", "CTSH", "CVX", "F", "GS", "INTC", "JPM", "KO", "MA", "MELI", "META", "MS", "MSFT", "ORCL", "TWTR", "V", "XOM"])

# Fetch stock data
if stock:
    stock_data = yf.download(stock, start="2018-01-01", end="2023-08-08")
    fig = px.line(stock_data, x=stock_data.index, y='Close', title=f'{stock} Stock Price')
    
    # Display the interactive graph
    st.plotly_chart(fig)


# get the latest news
latest_news = get_info(stock)

# display the news and if title or link is empty then delete that news
for news in latest_news:
    title = news.find("a").text
    link = news.find("a")["href"]
    if title=="" or link=="":
        continue
    st.markdown(f"### {title}")
    st.markdown(f"Link: {link}")
    st.markdown("---")
