import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.sidebar.title("Ms. RYE")
# st.markdown("Learn and grow")
# subheading = st.header("Learn and grow")

if 'money' not in st.session_state:
    st.session_state['money'] = 10000

if 'Profit/Loss' not in st.session_state:
    st.session_state['Profit/Loss'] = 0

if 'Final' not in st.session_state:
    st.session_state['Final'] = 0

keys = ["iVEsY9hnGg","8s66dzfO2W","OS1p5rJPhI","PIlZRp75qW","bIH8k02KYi","2lLegMN8Uy"]

# display the current money on top of the page
st.sidebar.markdown("## Money before Investment in $")
st.sidebar.markdown(st.session_state['money'])

# write lets play button on centre
st.markdown("## Let's Play")

#dropdown for stocks
st.markdown("### Which Stock you want to buy today?")
stock_name = st.selectbox("Select a stock", ["ACN", "AXP", "BLK", "BP", "CTSH", "CVX", "F", "GS", "INTC", "JPM", "KO", "MA", "MELI", "META", "MS", "MSFT", "ORCL", "TWTR", "V", "XOM"])

# text for how much money to invest in stock
st.markdown("### How much money do you want to invest in this stock?")
# slider for money
money_invest = st.number_input("Money")
if money_invest>st.session_state['money']:
    st.markdown("### You don't have enough money to invest in this stock")
    st.stop()

# duration of investment
st.markdown("### For how many days do you want to invest in this stock?")
# slider for duration
duration = st.slider("", 1, 29, 1)

# button to buy
buy = st.button("Buy")

stock_data = pd.read_csv(f"data/{stock_name}_ans.csv")

if buy == True:
    # calculate the number of stocks
    number_of_stocks = money_invest/stock_data["Close"][0]
    # calculate the money left
    money_left = st.session_state['money'] - money_invest
    # calculate the money after duration
    money_after_invest = money_left + (number_of_stocks*stock_data["Close"][duration])
    # display the money left
    st.markdown("## Money Left in $")
    if money_left<0:
        st.markdown("0")
    st.markdown(money_left)
    # display the number of stocks
    st.markdown("## Number of Stocks")
    st.markdown(number_of_stocks)
    # display the profit or loss
    st.markdown("## Profit/Loss")
    st.session_state['Profit/Loss'] = round((money_after_invest-st.session_state['money']),2)
    st.markdown(f"{st.session_state['Profit/Loss']}")

    # st.markdown("## Money after investment in $")
    # st.markdown(money+round((money_after_invest-money),2))

# change the money to money after investment and update in sidebar and delete the previous money
    st.session_state['money'] = money_left
    st.sidebar.markdown("## Current Money/After Investment in $")
    st.sidebar.markdown(st.session_state['money'])

    # st.session_state['Profit/Loss'] = 0

    st.sidebar.markdown("## Final Profit/Loss in $")
    st.session_state['Final'] = st.session_state['Final'] + st.session_state['Profit/Loss']
    st.sidebar.markdown(st.session_state['Final'])

st.markdown("Want to add money")
key_input = st.text_input("Enter the key")
if key_input in keys:
    st.session_state['money'] = st.session_state['money'] + 10000
    st.sidebar.markdown("## Current Money/After Investment in $")
    st.sidebar.markdown(st.session_state['money'])
# increase_money = st.button("Add Money")
# if increase_money == True:
#     key_input = st.text_input("Enter the key")
#     if key_input in keys:
#         st.session_state['money'] = st.session_state['money'] + 10000
#         st.sidebar.markdown("## Current Money/After Investment in $")
#         st.sidebar.markdown(st.session_state['money'])