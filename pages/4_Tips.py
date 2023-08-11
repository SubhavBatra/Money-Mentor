import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")

subheading = st.header("Learn and grow")
status = st.selectbox("Select your status", ["NA", "Beginner", "Intermediate"])
# status = 1
if status == "Beginner":
    st.subheader("As you are a Beginner, we recommend you to start with the basics")

elif status == "Intermediate":
    st.subheader("As you are an Intermediate, we recommend you to study the following")

lang = st.selectbox("Select a language", ["English", "Hindi"])

english_articles_beg = ["https://www.motilaloswal.com/blog-details/8-must-read-stock-trading-books-for-beginners/20200", "https://www.ig.com/en/trading-need-to-knows/trading-for-beginners", "https://www.nerdwallet.com/article/investing/how-to-day-trade-safely", "https://www.bankrate.com/investing/stock-market-basics-for-beginners/", "https://www.wallstreetmojo.com/best-stock-market-books-for-beginners/"]

english_articles_inter = ["https://www.investopedia.com/advanced-trading-strategies-and-instruments-4689645", "https://www.ig.com/en/trading-strategies/6-advanced-forex-trading-techniques-230420", "https://www.thebalancemoney.com/advanced-forex-trading-techniques-1344817", "https://the5ers.com/top-8-most-useful-day-trading-tips/"]

short_videos_hindi = ["https://youtube.com/shorts/80QeEdnpsco?feature=share", "https://www.youtube.com/shorts/6ECaD7mj8ZI", "https://www.youtube.com/shorts/1bM7fRwLAlU", "https://youtube.com/shorts/ShkkuxvAU0A?feature=share", "https://www.youtube.com/shorts/--BL4qjDW8c"]

long_videos_hindi = ["https://www.youtube.com/shorts/--BL4qjDW8c", "https://youtu.be/W3HQanGbPfE", "https://youtu.be/UwGSzhjsceI", "https://youtu.be/HNPbY6fSeo8", "https://youtu.be/_ucD8sc30xY"]

short_videos_eng = ["https://www.youtube.com/shorts/gzsbOglVR30", "https://youtube.com/shorts/Dbq8TXwciNk?feature=share", "https://youtube.com/shorts/ZF8Vvu7cnxw?feature=share", "https://youtube.com/shorts/MhZtYKDBdtE?feature=share", "https://youtube.com/shorts/YRk8NypX904?feature=share"]

long_videos_eng = ["https://youtube.com/shorts/YRk8NypX904?feature=share", "https://youtu.be/_YVQN6_nkfs", "https://youtu.be/p7HKvqRI_Bo", "https://www.youtube.com/watch?v=i5OZQQWj5-I", "https://youtu.be/ea6qNsLbxNA"]

translate = "http://translate.google.com/translate?js=n&sl=auto&tl=hi&u="

# generate set of random private keys of length 8 including numbers, alphabets, and special characters

keys = ["iVEsY9hnGg","8s66dzfO2W","OS1p5rJPhI","PIlZRp75qW","bIH8k02KYi","2lLegMN8Uy"]

# recommend 2 random articles, 2 random short videos, 1 random long video accroding to language and status
but = st.button("Recommend")

if but:

    if lang == "English":
        if status == "Beginner":
            st.markdown("### Articles")
            # random 2 articles
            st.markdown(f"1. [{english_articles_beg[0]}]({english_articles_beg[0]})")
            
            st.markdown(f"2. [{english_articles_beg[1]}]({english_articles_beg[1]})")


            st.markdown("### Short Videos")
            st.markdown(f"1. [{short_videos_eng[0]}]({short_videos_eng[0]})")
            st.markdown(f"2. [{short_videos_eng[1]}]({short_videos_eng[1]})")
            st.markdown(f"3. [{short_videos_eng[2]}]({short_videos_eng[2]})")

            st.markdown("### Long Videos")
            st.markdown(f"1. [{long_videos_eng[0]}]({long_videos_eng[0]})")
            st.markdown(f"2. [{long_videos_eng[1]}]({long_videos_eng[1]})")

        elif status == "Intermediate":
            st.markdown("### Articles")
            st.markdown(f"1. [{english_articles_inter[0]}]({english_articles_inter[0]})")
            st.markdown(f"2. [{english_articles_inter[1]}]({english_articles_inter[1]})")

            st.markdown("### Short Videos")
            st.markdown(f"1. [{short_videos_eng[3]}]({short_videos_eng[3]})")
            st.markdown(f"2. [{short_videos_eng[4]}]({short_videos_eng[4]})")

            st.markdown("### Long Videos")
            st.markdown(f"3. [{long_videos_eng[2]}]({long_videos_eng[2]})")
            st.markdown(f"4. [{long_videos_eng[3]}]({long_videos_eng[3]})")
    
    else:
        if status == "Beginner":
            st.markdown("### Articles")
            st.markdown(f"1. [{translate}{english_articles_beg[2]}]({translate}{english_articles_beg[2]})")
            st.markdown(f"2. [{translate}{english_articles_beg[3]}]({translate}{english_articles_beg[3]})")

            st.markdown("### Short Videos")
            st.markdown(f"1. [{short_videos_hindi[0]}]({short_videos_hindi[0]})")
            st.markdown(f"2. [{short_videos_hindi[1]}]({short_videos_hindi[1]})")
            st.markdown(f"3. [{short_videos_hindi[2]}]({short_videos_hindi[2]})")

            st.markdown("### Long Videos")
            st.markdown(f"1. [{long_videos_hindi[0]}]({long_videos_hindi[0]})")
            st.markdown(f"2. [{long_videos_hindi[1]}]({long_videos_hindi[1]})")

        elif status == "Intermediate":
            st.markdown("### Articles")
            st.markdown(f"1. [{translate}{english_articles_inter[2]}]({translate}{english_articles_inter[2]})")
            st.markdown(f"2. [{translate}{english_articles_inter[3]}]({translate}{english_articles_inter[3]})")

            st.markdown("### Short Videos")
            st.markdown(f"1. [{short_videos_hindi[3]}]({short_videos_hindi[3]})")
            st.markdown(f"2. [{short_videos_hindi[4]}]({short_videos_hindi[4]})")

            st.markdown("### Long Videos")
            st.markdown(f"1. [{long_videos_hindi[2]}]({long_videos_hindi[2]})")
            st.markdown(f"2. [{long_videos_hindi[3]}]({long_videos_hindi[3]})")
            # butt_key = st.button(" Generate Key")
            # if butt_key:
    
            #     key = np.random.choice(keys)
            #     st.sidebar.markdown(f"Your key is {key}")

    # butt_key = st.button(" Generate Key")
    # if butt_key:
    
    #     key = np.random.choice(keys)
    #     st.sidebar.markdown(f"Your key is {key}")

#make a session state to store the key
if "key" not in st.session_state:
    st.session_state["key"] = None
butt_key = st.button(" Generate Key")
if butt_key: 
    key = np.random.choice(keys)
    st.session_state["key"] = key
if "key" in st.session_state:
    st.sidebar.markdown(f"Your key is {st.session_state['key']}")
    del st.session_state["key"]
