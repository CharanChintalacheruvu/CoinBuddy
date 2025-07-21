import praw
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get Reddit API credentials
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

# Setup Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Fetch top posts
def test_reddit_api():
    try:
        subreddit = reddit.subreddit("cryptocurrency")
        print("✅ Reddit API Connected. Fetching posts...\n")

        for post in subreddit.new(limit=5):
            print(f"Title: {post.title}\nScore: {post.score}\n---")

    except Exception as e:
        print("❌ Reddit API Error:", e)

# Run test
if __name__ == "__main__":
    test_reddit_api()
