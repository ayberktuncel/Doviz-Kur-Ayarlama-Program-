# 💰 Döviz Kur Hesaplama Programı

Bu proje, Python ve Streamlit kullanılarak geliştirilmiş, anlık piyasa verilerini kullanarak döviz çevirisi yapan bir web uygulamasıdır.

**Frankfurter API** kullanılarak **USD** ve **EUR** kurlarını anlık olarak **TRY** (Türk Lirası) karşılığına çevirir.

## 🚀 Özellikler
* **Canlı Veri:** Kurlar statik değildir, API üzerinden saniyelik çekilir.
* **Esnek Giriş:** Kuruşlu hesaplamalar için *float* desteği.
* **Kolay Arayüz:** Kullanıcı dostu seçim menüleri.
* **JSON Analizi:** Arka planda gelen karmaşık veri ayıklanarak işlenir.

## 🛠️ Kullanılan Teknolojiler
* **Python 3.x**
* **Streamlit** (Arayüz için)
* **Requests** (API bağlantısı için)

## 💻 Nasıl Çalıştırılır?

1.  Projeyi indirin:
    ```bash
    git clone [https://github.com/ayberktuncel/doviz-cevirici.git](https://github.com/ayberktuncel/doviz-cevirici.git)
    cd doviz-cevirici
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install streamlit requests
    ```

3.  Uygulamayı başlatın:
    ```bash
    streamlit run doviz.py
    ```
---
**Geliştirici:** **Ayberk Tuncel**
* 💼 **[LinkedIn Profilim](https://www.linkedin.com/in/ayberk-tuncel/)**
* 🐙 **[GitHub Profilim](https://github.com/ayberktuncel)**
