# X News Bot (Gemini Version)

A simple Python script that fetches the latest news, summarizes it using the Google Gemini API, and posts it to X (Twitter).

## Setup Guide

### 1. Get a Free Gemini API Key
Google offers a free tier for the Gemini API through **Google AI Studio**.
- Go to [Google AI Studio](https://aistudio.google.com/).
- Sign in with your Google account.
- Click on **"Get API key"** in the sidebar.
- Click **"Create API key in new project"**.
- Copy your key and keep it safe!

### 2. Get X (Twitter) API Keys
- Go to the [X Developer Portal](https://developer.twitter.com/).
- Create a new Project and App.
- Ensure you have **Read and Write** permissions enabled.
- Generate your API Key, API Secret, Access Token, and Access Token Secret.

### 3. Get a NewsAPI Key
- Go to [NewsAPI.org](https://newsapi.org/) and register for a free account to get an API key.

### 4. Installation
Clone this repository and install the required dependencies:
```bash
pip install google-generativeai tweepy requests
```

### 5. Configuration
You can either paste your keys directly into the `x_news_bot.py` file (not recommended for public repos) or set them as environment variables:
```bash
export GEMINI_API_KEY='your_key'
export X_API_KEY='your_key'
# ... and so on
```

### 6. Running the Script
Run the bot with:
```bash
python x_news_bot.py
```
*Note: The posting function is commented out by default in the script. Uncomment `post_to_x(tweet)` in the `main` block to enable live posting.*
