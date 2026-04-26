import requests
import os

# Ayarlar
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
USD_AZN_RATE = 1.70  # Sabit kur
OYUN_LIMITI = 20

def get_filtered_deals():
    # CheapShark API - Steam indirimleri
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&onSale=1&pageSize=50"
    try:
        response = requests.get(url)
        data = response.json()
        processed_deals = []

        for item in data:
            savings = float(item.get('savings', 0))
            if savings >= 75:
                # Rekor fiyat kontrolü (Tarihin en düşüğü mü?)
                is_cheapest = "🔥" if item.get('isLowestPrice') == "1" else ""
                metascore = f"⭐{item.get('metacriticScore')}" if item.get('metacriticScore') != "0" else ""
                
                new_price = float(item.get('salePrice'))
                azn_price = round(new_price * USD_AZN_RATE, 2)

                processed_deals.append({
                    'name': item.get('title'),
                    'new_price': new_price,
                    'azn_price': azn_price,
                    'old_price': float(item.get('normalPrice')),
                    'discount': int(savings),
                    'score': metascore,
                    'rekor': is_cheapest,
                    'link': f"https://store.steampowered.com/app/{item.get('steamAppID')}"
                })

        processed_deals.sort(key=lambda x: x['discount'], reverse=True)
        return processed_deals[:OYUN_LIMITI]
    except Exception as e:
        print(f"Hata: {e}")
        return []

def send_to_discord():
    deals = get_filtered_deals()
    if not deals:
        return

    # Başlık Mesajı
    requests.post(DISCORD_WEBHOOK_URL, json={
        "content": "🚀 **STEAM GÜNÜN BOMBA FIRSATLARI**",
        "embeds": [{
            "description": f"📅 *Kur: 1 USD = {USD_AZN_RATE} AZN*",
            "color": 5814783
        }]
    })

    # Oyunları Gruplandırarak Gönder
    msg_lines = []
    for d in deals:
        line = (f"{d['rekor']} **%{d['discount']}** | [{d['name']}](<{d['link']}>) | "
                f"`{d['new_price']}$` (~**{d['azn_price']} AZN**) "
                f"{d['score']}")
        msg_lines.append(line)

    # Discord 2000 karakter sınırı için parçalara böl
    for i in range(0, len(msg_lines), 10):
        chunk = "\n".join(msg_lines[i:i+10])
        requests.post(DISCORD_WEBHOOK_URL, json={"content": chunk})

if __name__ == "__main__":
    send_to_discord()
