import os
import google.generativeai as genai
import tweepy
import requests

# --- CONFIGURATION ---
# Replace these with your actual API keys or set them as environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
X_API_KEY = os.environ.get("X_API_KEY", "YOUR_X_API_KEY_HERE")
X_API_SECRET = os.environ.get("X_API_SECRET", "YOUR_X_API_SECRET_HERE")
X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN", "YOUR_X_ACCESS_TOKEN_HERE")
X_ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET", "YOUR_X_ACCESS_TOKEN_SECRET_HERE")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "YOUR_NEWS_API_KEY_HERE")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_latest_news():
    """Fetches the latest news using NewsAPI."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data.get("status") == "ok" and data.get("articles"):
        return data["articles"][0]["title"] + " - " + data["articles"][0]["description"]
    return "No news found today."

def summarize_with_gemini(text):
    """Summarizes news text into a tweet-sized format using Gemini."""
    prompt = f"Summarize the following news into a catchy tweet (under 280 characters) with relevant hashtags:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def post_to_x(tweet_text):
    """Posts the summary to X (formerly Twitter)."""
    client = tweepy.Client(
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    try:
        client.create_tweet(text=tweet_text)
        print("Successfully posted to X!")
    except Exception as e:
        print(f"Error posting to X: {e}")

if __name__ == "__main__":
    print("Fetching news...")
    news_content = get_latest_news()
    
    print("Summarizing with Gemini...")
    tweet = summarize_with_gemini(news_content)
    
    print(f"Generated Tweet: {tweet}")
    
    # Uncomment the line below to actually post
    # post_to_x(tweet)
