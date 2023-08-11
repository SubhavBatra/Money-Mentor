from Home import status
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")
subheading = st.header("Learn and grow")
status = 1
if status == 0:
    st.subheader("As you are a Beginner, we recommend you to start with the basics")

else:
    st.subheader("As you are an Intermediate, we recommend you to study the following")

lang = st.selectbox("Select a language", ["English", "Hindi"])

english_articles_beg = ["https://www.motilaloswal.com/blog-details/8-must-read-stock-trading-books-for-beginners/20200", "https://www.ig.com/en/trading-need-to-knows/trading-for-beginners", "https://www.nerdwallet.com/article/investing/how-to-day-trade-safely", "https://www.bankrate.com/investing/stock-market-basics-for-beginners/", "https://www.wallstreetmojo.com/best-stock-market-books-for-beginners/"]

english_articles_inter = ["https://www.investopedia.com/advanced-trading-strategies-and-instruments-4689645", "https://www.ig.com/en/trading-strategies/6-advanced-forex-trading-techniques-230420", "https://www.thebalancemoney.com/advanced-forex-trading-techniques-1344817", "https://the5ers.com/top-8-most-useful-day-trading-tips/"]

short_videos_hindi = ["https://youtube.com/shorts/80QeEdnpsco?feature=share", "https://www.youtube.com/shorts/6ECaD7mj8ZI", "https://www.youtube.com/shorts/1bM7fRwLAlU", "https://youtube.com/shorts/ShkkuxvAU0A?feature=share", "https://www.youtube.com/shorts/--BL4qjDW8c"]

long_videos_hindi = ["https://www.youtube.com/shorts/--BL4qjDW8c", "https://youtu.be/W3HQanGbPfE", "https://youtu.be/UwGSzhjsceI", "https://youtu.be/HNPbY6fSeo8", "https://youtu.be/_ucD8sc30xY"]

short_videos_eng = ["https://www.youtube.com/shorts/gzsbOglVR30", "https://youtube.com/shorts/Dbq8TXwciNk?feature=share", "https://youtube.com/shorts/ZF8Vvu7cnxw?feature=share", "https://youtube.com/shorts/MhZtYKDBdtE?feature=share", "https://youtube.com/shorts/YRk8NypX904?feature=share"]

long_videos_eng = ["https://youtube.com/shorts/YRk8NypX904?feature=share", "https://youtu.be/_YVQN6_nkfs", "https://youtu.be/p7HKvqRI_Bo", "https://www.youtube.com/watch?v=i5OZQQWj5-I", "https://youtu.be/ea6qNsLbxNA"]

translate = "http://translate.google.com/translate?js=n&sl=auto&tl=hi&u="

