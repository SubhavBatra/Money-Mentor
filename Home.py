import streamlit as st
import pandas as pd
import numpy as np
import pickle
def get_status():
   return 1  
st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")
subheading = st.header("Learn and grow")
st.subheader("Baisc Questionnaire for us to serve you better")
score = 0
# set default radio button to null
status=2

q1 = st.slider("Are you aware of Stock Market?", 0, 5, 2)
score += q1
q2 = st.slider("Have you ever invested in Stock Market?", 0,5,2)
score += q2
q3 = st.slider("Do you Trade frequently?", 0,5,2)
score += q3
q4 = st.slider("Have you ever made a Portfolio?", 0,5,2)
score += q4
q5 = st.slider("Do you have a Demat Account?", 0,5,2)
score += q5

butt = st.button("Submit")

if butt == True:

    if score>=15:
        st.subheader("You are an **_Intermediate_ Trader**")
    else:
        st.subheader("You are a **Beginner**")

    if score>=15:
        status = 1
    else:
        status = 0

    if status == 0:
        st.title("Learn About Stocks")

        st.markdown("""
        ## How to invest in stocks?
        There are many different ways to invest in stocks. You can buy stocks directly through a stockbroker, or you can invest in mutual funds or ETFs. Mutual funds and ETFs are baskets of stocks that are managed by professional investors. This can be a good way to invest in stocks if you don't want to pick stocks yourself.

        ## Risks of investing in stocks.
        Investing in stocks is not without risk. The price of stocks can go down as well as up, and you could lose money if you sell your stocks when the price is low. It is important to understand the risks involved before you invest in stocks.

        ## How to read a stock chart
                    
        A stock chart is a visual representation of the price history of a stock. It can be used to track the stock's performance over time and to identify trends.
        The most common type of stock chart is the line chart. A line chart shows the stock's price over time as a single line. Other types of stock charts include bar charts, candlestick charts, and point-and-figure charts.
        To read a stock chart, you need to understand the different elements that make it up. The most important elements are the price, the volume, and the moving averages.
        The price is the most obvious element of a stock chart. It is the current price of the stock.
        The volume is the number of shares that have been traded in a given period of time. The volume can be used to gauge the interest in a stock.
        Moving averages are lines that are plotted on a stock chart to smooth out the price data. Moving averages can be used to identify trends and to make predictions about the future price of a stock.
        Once you understand the different elements of a stock chart, you can start to use it to track the stock's performance and to identify trends. You can also use moving averages to make predictions about the future price of a stock.

        ## How to calculate the intrinsic value of a stock
                    
        The intrinsic value of a stock is the value that the stock is actually worth. It is calculated by discounting the future cash flows of the company to the present value.
        The intrinsic value of a stock can be used to determine whether a stock is undervalued or overvalued. If the stock's price is below its intrinsic value, then it is considered to be undervalued. If the stock's price is above its intrinsic value, then it is considered to be overvalued.
        There are many different methods for calculating the intrinsic value of a stock. One common method is the discounted cash flow (DCF) method. The DCF method discounts the future cash flows of the company to the present value. The future cash flows are discounted using a discount rate, which is the rate of return that an investor expects to earn on their investment.
        The DCF method is a complex method, but it is the most accurate method for calculating the intrinsic value of a stock.
                    
        ## How to research a company before investing in it. 
        Before you invest in a company, it is important to research the company thoroughly. This includes researching the company's financial statements, its products and services.""")

