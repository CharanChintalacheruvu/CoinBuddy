import praw
from dotenv import load_dotenv
from textblob import TextBlob
import os

# Load Reddit API keys
load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_reddit_sentiment(subreddit="cryptocurrency", limit=10):
    posts = reddit.subreddit(subreddit).new(limit=limit)
    sentiment_scores = []

    for post in posts:
        analysis = TextBlob(post.title)
        sentiment_scores.append(analysis.sentiment.polarity)  # range: -1 to +1

    if sentiment_scores:
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        return avg_sentiment
    else:
        return 0
