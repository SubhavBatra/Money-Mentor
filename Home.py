import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Ms. RYE", layout="wide", initial_sidebar_state="expanded")  
st.title("Ms. RYE")
# st.markdown("Learn and grow")
subheading = st.header("Learn and grow")
st.subheader("Baisc Questionnaire for us to serve you better")
score = 0
# set default radio button to null

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

if score>=15:
    st.subheader("You are an **_Intermediate_ Trader**")
else:
    st.subheader("You are a **Beginner**")

if score>=3:
    status = 1
else:
    status = 0