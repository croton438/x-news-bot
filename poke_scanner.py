# Bu dosya referans amaçlıdır - Poke tarafında çalışır, bilgisayarınıza kurmayın.
# This file is for reference only - it runs on the Poke side, do not install on your computer.

"""
Poke Otomasyon Mantığı (Özet):
1. RSS beslemelerini tarar.
2. Yeni haberleri Google Gemini ile Türkçe'ye çevirir ve özetler.
3. Haber içeriğine uygun bir görsel üretir.
4. Sonucu yerel bilgisayarınızda çalışan Flask webhook'una (ngrok üzerinden) gönderir.
"""

import requests

def poke_automation_logic(webhook_url, tweet_text, image_url):
    payload = {
        "text": tweet_text,
        "image_url": image_url
    }
    response = requests.post(webhook_url, json=payload)
    return response.json()

# Örnek kullanım:
# poke_automation_logic("https://your-ngrok-url.ngrok-free.app/post-tweet", "Haber özeti burada", "https://image-url.com/pic.jpg")
