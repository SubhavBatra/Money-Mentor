import streamlit as st
from helper import get_info

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")
subheading = st.header("Learn and grow")

st.subheader("Let's see what's happening in the market today")

# dropdown
stock = st.selectbox("Select a stock", ["BLK", "MSFT", "TSLA","GS", "JPM", "META", "ORCL", "TWTR"])

#display the image of the stock from images folder
st.image(f"images/{stock}.jpeg")


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
