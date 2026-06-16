import os
import requests
import tweepy
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- CONFIGURATION ---
# Replace these with your actual X (Twitter) API keys
# Make sure your X App has 'Read and Write' permissions and 'Web App, Android, iOS' user authentication settings enabled.
X_API_KEY = "YOUR_X_API_KEY_HERE"
X_API_SECRET = "YOUR_X_API_SECRET_HERE"
X_ACCESS_TOKEN = "YOUR_X_ACCESS_TOKEN_HERE"
X_ACCESS_TOKEN_SECRET = "YOUR_X_ACCESS_TOKEN_SECRET_HERE"
X_BEARER_TOKEN = "YOUR_X_BEARER_TOKEN_HERE"

def get_x_clients():
    # V1.1 Client for media upload
    auth = tweepy.OAuth1UserHandler(X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
    api_v1 = tweepy.API(auth)
    
    # V2 Client for posting tweets
    client_v2 = tweepy.Client(
        bearer_token=X_BEARER_TOKEN,
        consumer_key=X_API_KEY,
        consumer_secret=X_API_SECRET,
        access_token=X_ACCESS_TOKEN,
        access_token_secret=X_ACCESS_TOKEN_SECRET
    )
    return api_v1, client_v2

@app.route('/post-tweet', methods=['POST'])
def post_tweet():
    data = request.json
    tweet_text = data.get('text')
    image_url = data.get('image_url')

    if not tweet_text:
        return jsonify({"error": "No text provided"}), 400

    try:
        api_v1, client_v2 = get_x_clients()
        media_ids = []

        if image_url:
            print(f"Downloading image: {image_url}")
            img_data = requests.get(image_url).content
            filename = 'temp_image.jpg'
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            
            # Upload media using v1.1 API
            media = api_v1.media_upload(filename=filename)
            media_ids.append(media.media_id)
            os.remove(filename)

        # Post tweet using v2 API
        response = client_v2.create_tweet(text=tweet_text, media_ids=media_ids if media_ids else None)
        print(f"Successfully posted tweet: {response.data['id']}")
        return jsonify({"status": "success", "tweet_id": response.data['id']}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Runs on port 5000 by default
    app.run(host='0.0.0.0', port=5000)
