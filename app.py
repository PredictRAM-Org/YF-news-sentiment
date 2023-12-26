import requests
import streamlit as st
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to fetch stock data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="1d")

# Function to perform sentiment analysis
def analyze_sentiment(headline):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(headline)['compound']
    return sentiment_score

# Streamlit app
st.title("Stock News Sentiment Analysis")

# User input for stock symbol
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL for Apple):")

# Fetch stock data
if symbol:
    stock_data = get_stock_data(symbol)
    st.subheader(f"Stock Data for {symbol}")
    st.write(stock_data)

    # Fetch news headlines
    url = "https://news-api14.p.rapidapi.com/top-headlines"
    querystring = {"country": "us", "language": "en", "pageSize": "5", "category": "business"}
    response = requests.get(url, headers=headers, params=querystring)
    news_data = response.json()

    # Display news headlines and sentiment scores
    st.subheader("Latest News Headlines:")
    for article in news_data.get('articles', []):
        headline = article.get('title', '')
        sentiment_score = analyze_sentiment(headline)
        st.write(f"- {headline} (Sentiment Score: {sentiment_score:.2f})")
