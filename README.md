# X News Bot - İki Parçalı Mimari

Bu proje, haberleri otomatik olarak tarayan, özetleyen ve X (Twitter) üzerinde paylaşan bir sistemdir. Sistem iki ana parçadan oluşur:

1.  **Poke (Bulut):** RSS tarama, Gemini ile özetleme ve görsel üretme işlemlerini yapar.
2.  **Local Webhook (Sizin Bilgisayarınız):** Poke'den gelen veriyi alır ve sizin X hesabınızda paylaşır.

## Kurulum Adımları (Windows)

### 1. Python ve Kütüphaneler
Bilgisayarınızda Python yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için terminale (CMD veya PowerShell) şunu yazın:
```bash
pip install flask tweepy requests
```

### 2. X (Twitter) API Anahtarlarını Alın
- [X Developer Portal](https://developer.x.com/) adresine gidin.
- Bir uygulama oluşturun.
- **User Authentication Settings** kısmından "OAuth 1.0a"yı açın ve "Read and Write" izni verin.
- `API Key`, `API Secret`, `Access Token`, `Access Token Secret` ve `Bearer Token` değerlerini kopyalayıp `x_news_bot.py` dosyasındaki ilgili yerlere yapıştırın.

### 3. ngrok Kurulumu (Dış Dünyaya Açılma)
Poke'nin sizin bilgisayarınıza veri gönderebilmesi için yerel portunuzu internete açmanız gerekir:
- [ngrok.com](https://ngrok.com/) adresinden ngrok'u indirin ve kurun.
- Terminale şu komutu yazarak 5000 portunu dışarı açın:
  ```bash
  ngrok http 5000
  ```
- Ekranda çıkan `Forwarding` kısmındaki `https://...` ile başlayan URL'yi kopyalayın. Bu sizin Webhook URL'nizdir.

### 4. Botu Çalıştırma
`x_news_bot.py` dosyasını çalıştırın:
```bash
python x_news_bot.py
```
Artık bilgisayarınız Poke'den gelecek paylaşım isteklerini dinlemeye hazır!

---

## Dosyalar Hakkında
- `x_news_bot.py`: Bilgisayarınızda çalışması gereken ana Flask sunucusu.
- `poke_scanner.py`: Poke tarafında çalışan mantığı gösteren referans dosyasıdır (Bilgisayarınıza kurmanıza gerek yoktur).
