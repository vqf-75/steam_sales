# 🎮 Steam İndirim Botu (Discord) - v0.2

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-orange?style=for-the-badge&logo=github-actions&logoColor=white)
![Version](https://img.shields.io/badge/Version-0.2-green?style=for-the-badge)

Bu bot, Steam üzerindeki dev indirimleri takip eder ve yerel para birimi (AZN), kalite puanı ve fiyat rekoru gibi detaylarla Discord kanalınıza raporlar. Sunucu gerektirmez, tamamen GitHub Actions üzerinde ücretsiz çalışır.

---

## 🚀 v0.2 Yenilikleri (Mevcut Versiyon)
Bu sürümde bot daha akıllı ve kullanıcı dostu hale getirildi:

* 🇦🇿 **AZN Kur Desteği:** USD fiyatları otomatik olarak Azerbaycan Manatı'na (AZN) çevrilir.
* 🔥 **Rekor Fiyat Takibi:** Eğer bir oyun tarihindeki en düşük fiyata indiyse özel bir alev ikonuyla gösterilir.
* ⭐ **Metacritic Puanları:** Oyunun kalitesini anlamanız için 100 üzerinden eleştirmen puanları eklendi.
* 🧹 **Temiz Görünüm:** Gereksiz link önizlemeleri (embed kirliliği) kaldırıldı, mesaj yapısı sadeleştirildi.
* 📈 **Gelişmiş Filtreleme:** Sadece en yüksek indirim oranına sahip en iyi 20 oyun listelenir.

---

## 📜 Sürüm Geçmişi (v0.1 Özellikleri)
Projenin ilk sürümünde sunulan temel özellikler:
* **Otomatik Çalışma:** Günde 2 kez (10:00 ve 19:00) otomatik tetiklenme.
* **CheapShark API:** Steam verilerini çekmek için güvenilir API entegrasyonu.
* **Webhook Desteği:** Discord kanallarına anlık mesaj gönderimi.
* **Temel Filtre:** Sadece %75 ve üzeri indirimleri yakalama yeteneği.

---

## 🔍 Terimler Sözlüğü
Mesajlarda göreceğiniz simgelerin anlamları:
* **🔥 (Rekor):** Bu oyun daha önce hiç bu kadar ucuza satılmadı!
* **⭐ (Score):** Oyunun Metacritic puanı.
* **~X AZN:** Ürünün güncel kur (1.70) üzerinden tahmini manat fiyatı.
* **[Oyun Adı](link):** Direkt Steam mağaza sayfasına yönlendiren tıklanabilir bağlantı.

---

## 🛠️ Kurulum ve Ayarlar

### 1. GitHub Secrets
Botun çalışması için GitHub deponuzda şu gizli anahtarı tanımlamanız şarttır:
* **`DISCORD_WEBHOOK`**: Discord kanalınızın Ayarlar > Entegrasyonlar kısmından aldığınız Webhook URL'si.

### 2. Workflow Yapılandırması
`.github/workflows/main.yml` dosyanızda çalışma saatlerini ve dosya adını şu şekilde ayarlayın:

```yaml
on:
  schedule:
    - cron: '0 6,15 * * *' # 10:00 ve 19:00 (GMT+4)
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - run: pip install requests
      - name: Botu Calistir
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
        run: python Bot_0.2.py
