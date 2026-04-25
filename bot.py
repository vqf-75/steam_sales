import requests

# Discord Webhook URL'nizi buraya tırnaklar içine yapıştırın
DISCORD_WEBHOOK_URL = "WEBHOOK_URL_BURAYA"
OYUN_LIMITI = 20

def get_filtered_deals():
    # CheapShark API üzerinden Steam indirimlerini çeker
    url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&onSale=1&pageSize=60"
    try:
        response = requests.get(url)
        data = response.json()
        processed_deals = []
        for item in data:
            savings = float(item.get('savings', 0))
            if savings >= 75:
                processed_deals.append({
                    'name': item.get('title'),
                    'new_price': float(item.get('salePrice')),
                    'old_price': float(item.get('normalPrice')),
                    'discount': int(savings),
                    'link': f"https://store.steampowered.com/app/{item.get('steamAppID')}"
                })
        # En yüksek indirime göre sırala ve limit uygula
        processed_deals.sort(key=lambda x: x['discount'], reverse=True)
        return processed_deals[:OYUN_LIMITI]
    except Exception as e:
        print(f"Hata: {e}")
        return []

def send_to_discord():
    deals = get_filtered_deals()
    if not deals:
        print("Kriterlere uygun oyun bulunamadı.")
        return
    
    # Başlık Mesajı
    requests.post(DISCORD_WEBHOOK_URL, json={"content": f"🚀 **STEAM %75+ GÜNÜN FIRSATLARI**\n" + "-"*35})
    
    # Oyunları Discord'a gönder (Link önizlemeleri < > ile kapatıldı)
    for i in range(0, len(deals), 10):
        chunk = deals[i:i+10]
        msg_lines = []
        for d in chunk:
            msg_lines.append(f"🏷️ **%{d['discount']}** | [{d['name']}](<{d['link']}>) | `{d['new_price']}$` (~~{d['old_price']}$~~)")
        
        requests.post(DISCORD_WEBHOOK_URL, json={"content": "\n".join(msg_lines)})

if __name__ == "__main__":
    send_to_discord()
