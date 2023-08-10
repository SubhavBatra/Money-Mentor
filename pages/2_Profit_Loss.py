import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.sidebar.title("Ms. RYE")
# st.markdown("Learn and grow")
# subheading = st.header("Learn and grow")

money = 10000

# display the current money on top of the page
st.sidebar.markdown("## Current Money in $")
st.sidebar.markdown(money)

# write lets play button on centre
st.markdown("## Let's Play")

#dropdown for stocks
st.markdown("### Which Stock you want to buy today?")
stock = st.selectbox("Select a stock", ["BLK", "MSFT", "TSLA","GS", "JPM", "META", "ORCL", "TWTR"])

# text for how much money to invest in stock
st.markdown("### How much money do you want to invest in this stock?")
# slider for money
money_invest = st.number_input("Money")
if money_invest>money:
    st.markdown("### You don't have enough money to invest in this stock")
    st.stop()

# duration of investment
st.markdown("### For how many days do you want to invest in this stock?")
# slider for duration
duration = st.slider("", 1, 29, 1)

# button to buy
buy = st.button("Buy")

stock_data = pd.read_csv(f"data/{stock}.csv")

if buy == True:
    # calculate the number of stocks
    number_of_stocks = money_invest/stock_data["Close"][0]
    # calculate the money left
    money_left = money - (number_of_stocks*stock_data["Close"][0])
    # calculate the money after duration
    money_after_invest = money_left + (number_of_stocks*stock_data["Close"][duration])
    # display the money left
    st.markdown("## Money Left in $")
    st.markdown(money_left)
    # display the number of stocks
    st.markdown("## Number of Stocks")
    st.markdown(number_of_stocks)
    # display the profit or loss
    st.markdown("## Profit/Loss")
    st.markdown(f"{round((money_after_invest-money),2)}")

    st.markdown("## Money after investment in $")
    st.markdown(money+round((money_after_invest-money),2))

# change the money to money after investment and update in sidebar and delete the previous money
    money = money+round((money_after_invest-money),2)
    st.sidebar.markdown("## Current Money in $")
    st.sidebar.markdown(money)



