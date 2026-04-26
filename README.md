markdown_v2_content = """# 🎮 Steam İndirim Botu (Discord) - v0.2

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-orange?style=for-the-badge&logo=github-actions&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.2-green?style=for-the-badge)

Bu bot, Steam üzerindeki dev indirimleri takip eder ve yerel para birimi (AZN), kalite puanı ve fiyat rekoru gibi detaylarla Discord kanalınıza raporlar.

## 🚀 v0.2 Yenilikleri
* 🇦🇿 **AZN Kur Desteği:** Fiyatlar artık otomatik olarak Azerbaycan Manatı'na (AZN) çevriliyor.
* 🔥 **Rekor Fiyat Takibi:** Eğer bir oyun tarihindeki en düşük fiyata indiyse özel bir işaretle gösteriliyor.
* ⭐ **Metacritic Puanları:** Oyunun kalitesini anlamanız için eleştirmen puanları listeye eklendi.
* 🧹 **Temiz Görünüm:** Gereksiz link önizlemeleri kaldırıldı, mesaj yapısı daha derli toplu hale getirildi.

---

## 🔍 Dosya İçeriği ve Terimler
Kodun içindeki önemli kısımların ne anlama geldiği aşağıdadır:

* **`USD_AZN_RATE = 1.70`**: Dolar kurunu belirler. Manat karşılığını görmek için bu değer kullanılır.
* **`is_cheapest (🔥)`**: CheapShark API'sinden gelen veriye göre oyunun daha önce hiç bu kadar ucuza satılmadığını ifade eder.
* **`metascore (⭐)`**: Oyunun Metacritic üzerindeki 100 üzerinden başarı puanıdır.
* **`OYUN_LIMITI = 20`**: Kanalı çok fazla mesajla doldurmamak için tek seferde gönderilecek maksimum oyun sayısıdır.

---

## 🛠️ Kurulum ve Ayarlar

### 1. GitHub Secrets
Botun çalışması için GitHub deponuzda şu gizli anahtarı tanımlamanız gerekir:
* **`DISCORD_WEBHOOK`**: Discord kanalınızın Webhook URL'si.

### 2. Workflow Yapılandırması
`.github/workflows/main.yml` dosyanızda botun adını güncellediğinizden emin olun:

```yaml
      - name: Botu Calistir
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
        run: python Bot_0.2.py  # Dosya adınızın doğru olduğundan emin olun
