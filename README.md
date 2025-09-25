# MLOps_2 --- Iris Dataset ile Uçtan Uca MLOps Pipeline

Bu proje, Iris veri seti üzerinden bir MLOps (Machine Learning
Operations) pipeline'ı kurmayı hedefler. Veri işleme, özellik
mühendisliği, model eğitimi, optimizasyon ve değerlendirme aşamalarını
DVC ile otomatikleştirir.

------------------------------------------------------------------------

## 🗂 Proje Yapısı

    ├── .dvc/                  # DVC metadata klasörü  
    ├── data/                  
    │   ├── raw/               # Ham verinin bulunduğu klasör (örneğin iris.csv)  
    │   └── processed/         # Temizlenmiş ve özellik mühendisliği sonrası veri  
    ├── metrics/               # Model değerlendirme çıktıları (ör. metrics.json)  
    ├── models/                # Eğitilmiş modellerin saklandığı yer  
    ├── src/                   # Python kaynak kodun  
    |   |── best_model_optimize.py # En iyi sonucu veren model parametlerinin optimize edilme işlemi
    |   |── veri_indirme    # Iris datasetin projeye dahil edilmesi
    │   ├── veri_temizleme/              # Veriyi okuma, temizleme, işleme ile ilgili scriptler  
    │   ├── model_gelistirme/            # Model eğitimi, değerlendirme, optimizasyon scriptleri  
    │   └── feature_engineering.py  
    ├── venv/                  # Sanal ortam (repo dışı bırakılmalı)  
    ├── .dvcignore             # DVC’nin yok sayacağı dosya/klasörleri belirtir  
    ├── dvc.yaml                # DVC pipeline tanımı (stages, deps, outs)  
    ├── dvc.lock                # Kilitlenmiş pipeline sürümü, hash bilgileri  
    ├── requirements.txt        # Gerekli Python paketleri  
    └── run_pipeline.py         # Pipeline’ı kolayca çalıştırmak için yardımcı script  

------------------------------------------------------------------------

## 🚀 Kurulum & Çalıştırma

Aşağıdaki adımlar ile projeyi yerel ortamında çalıştırabilirsin:

1.  Repo'yu klonla

    ``` bash
    git clone https://github.com/Altayai/MLOps_2.git
    cd MLOps_2
    ```

2.  Sanal ortam oluştur & aktif et

    ``` bash
    python -m venv venv
    # PowerShell için:
    .\venv\Scripts\Activate.ps1  
    # CMD için:
    .\venv\Scripts\activate.bat  
    ```

3.  Gerekli paketleri yükle

    ``` bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

------------------------------------------------------------------------

## 📊 Pipeline Açıklaması (DVC ile)

Bu proje, DVC tabanlı bir pipeline mimarisi kullanır. Aşamalar ve
görevleri şunlardır:

  --------------------------------------------------------------------------------------
  Stage Adı                                        Açıklama
  ------------------------------------------------ -------------------------------------
  **ingest**                                       `src/data/ingest.py` ile Iris verisi
                                                   oluşturulur ve `data/raw/iris.csv`
                                                   dosyasına kaydedilir.

  **clean**                                        `src/data/clean.py` ile veri
                                                   temizleme yapılır ve
                                                   `data/processed/clean_data.csv`
                                                   üretilir.

  **feature_engineering**                          `src/feature_engineering.py` ile yeni
                                                   özellikler çıkarılır,
                                                   `data/processed/feature_data.csv`
                                                   oluşturulur.

  **train**                                        `src/models/train.py` ile modeller
                                                   (örneğin RandomForest,
                                                   LogisticRegression) eğitilir ve
                                                   `models/` klasörüne kaydedilir.

  **optimize**                                     `src/models/best_model_optimize.py`
                                                   ile modellerin hiperparametre
                                                   optimizasyonu yapılır, en iyi model
                                                   `models/best_model.joblib` olarak
                                                   saklanır.

  **evaluate**                                     `src/models/evaluate.py` ile test
                                                   verisi üzerinden model performansları
                                                   ölçülür, `metrics/metrics.json`
                                                   dosyasına kaydedilir.
  --------------------------------------------------------------------------------------

Pipeline'ı çalıştırmak için:

``` bash
python run_pipeline.py
```

veya doğrudan:

``` bash
dvc repro
```

------------------------------------------------------------------------

## 📈 Model Değerlendirme & Sonuçlar

-   `metrics/metrics.json` dosyasında her model için **accuracy**,
    **precision**, **recall**, **f1-score** gibi metrikler bulunur.
-   Terminal çıktısında da modellerin karşılaştırmalı performansları
    basılır.

*Örnek çıktı:*

    Model Karşılaştırma Sonuçları
    🔹 random_forest
    Accuracy: 0.97
    Classification Report:
      0           P: 1.00 R: 1.00 F1: 1.00 (n=10)
      1           P: 0.89 R: 1.00 F1: 0.94 (n=10)
      2           P: 1.00 R: 0.80 F1: 0.89 (n=10)
    🔹 logistic_regression
    ...

------------------------------------------------------------------------

## 📦 Neden Bu Yapı?

-   **Reproducibility (Tekrarlanabilirlik):** DVC ile veri, model ve
    aşamalar sabitlenir; herkes aynı pipeline'ı çalıştırdığında aynı
    çıktıyı alır.\
-   **Modüler Kod:** `src/` klasöründe her aşama ayrı script'lerde
    tutulur --- okunabilirlik ve bakım kolaylığı sağlar.\
-   **Model Yönetimi:** Yüksek seviyede model versiyonlaması mümkündür;
    optimize edilmiş modeller `models/` klasöründe tutulur.\
-   **Kolay Çalıştırma:** `run_pipeline.py` ile pipeline'ı tek komutla
    çalıştırabilirsin.

------------------------------------------------------------------------

## ⚠️ Dikkat Edilmesi Gerekenler

-   `venv/` klasörü Git'e dahil edilmemiştir.\
-   DVC'nin takip ettiği dosyalar (veri, modeller) Git'e doğrudan
    konmaz, `dvc push` ile remote'a gönderilir.\
-   Projeye katkı yapmak istersen katkı rehberine (`CONTRIBUTING.md`)
    bakmayı unutma (isteğe bağlı).

------------------------------------------------------------------------

## 🙏 Katkılar & Lisans

-   Katkılar memnuniyetle kabul edilir --- yeni modeller, hata
    düzeltmeleri, iyileştirmeler ekleyebilirsin.\
-   Proje lisansını eklemek istersen (MIT, Apache 2.0 gibi) README'nin
    sonuna lisans bölümünü yerleştirebilirsin.
