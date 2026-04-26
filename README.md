🎮 Steam İndirim Botu (Discord)

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-orange?style=for-the-badge&logo=github-actions&logoColor=white)
![Steam](https://img.shields.io/badge/Steam-Sales_Tracker-black?style=for-the-badge&logo=steam&logoColor=white)

Bu bot, **CheapShark API**'sini kullanarak Steam üzerindeki **%75 ve üzeri** indirimleri otomatik olarak yakalar ve belirlediğiniz bir Discord kanalına günde iki kez şık bir mesaj olarak gönderir.

## ✨ Özellikler
* 🚀 **Otomatik Bildirim:** Her gün sabah **10:00** ve akşam **19:00**'da (Azerbaycan saati) çalışır.
* 🏷️ **Akıllı Filtre:** Sadece %75 ve daha yüksek indirimleri listeler.
* 🔗 **Doğrudan Link:** Oyun isimlerine tıklandığında direkt Steam mağaza sayfasına yönlendirir.
* ☁️ **Sıfır Maliyet:** Tamamen GitHub Actions üzerinde çalışır, sunucu gerektirmez.

---

## 🛠️ Kurulum ve Ayarlar

### 1. GitHub Secrets Ayarları
Botun Discord kanalınıza mesaj gönderebilmesi için Webhook URL'nizi güvenli bir şekilde tanımlamanız gerekir:
1. GitHub deponuzda **Settings > Secrets and variables > Actions** yoluna gidin.
2. **New repository secret** butonuna tıklayın.
3. İsim (Name) kısmına: `DISCORD_WEBHOOK` yazın.
4. Değer (Value) kısmına: Discord kanalınızdan aldığınız **Webhook URL**'sini yapıştırın.

### 2. Workflow Dosyası (.yml)
İş akışının doğru çalışması için `.github/workflows/main.yml` dosyanızın aşağıdaki yapıda olduğundan emin olun:

```yaml
on:
  schedule:
    - cron: '0 6,15 * * *' # Sabah 10:00 ve Akşam 19:00 (GMT+4)
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
        run: python bot.py
