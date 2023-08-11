import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# from Home import get_status



def get_info(stock):
    url = "https://www.cnbc.com/quotes/"+stock
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    latest_news = soup.find_all('li', class_='LatestNews-item')
    return latest_news


if __name__ == "__main__":
    latest_news = get_info("GS")

    for news in latest_news:
        title = news.find("a").text
        link = news.find("a")["href"]
        print(f"Title: {title}")
        print(f"Link: {link}")