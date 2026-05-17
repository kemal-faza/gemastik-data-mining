# 🗺️ PLAN — GEMASTIK XVIII Data Mining 2025

> **Tujuan:** Dokumen ini berisi seluruh topik yang telah direkomendasikan dan dievaluasi untuk Technical Report GEMASTIK Data Mining 2025, lengkap dengan *problem statement* mendalam, *scoring* per rubrik, *pipeline design*, *evaluation strategy*, serta analisis risiko dan mitigasi.
>
**Update terakhir:** 17 Mei 2026
>
**Status:** Telah diperbarui dengan 12 topik (4 baru + 8 existing). Siap untuk [§6: Decision Checklist](#6-decision-checklist).

---

## 📑 Daftar Isi

1. [Ringkasan Aturan & Rubrik](#1-ringkasan-aturan--rubrik)
2. [Pola Pemenang Historis](#2-pola-pemenang-historis)
3. [Ranking Topik Lengkap (12 Topik, Detail Penuh)](#3-ranking-topik-lengkap-12-topik-detail-penuh)
   - [Rank 1: WaterWatch-ID](#-rank-1-waterwatch-id)
   - [Rank 2: DengueCast-X](#-rank-2-denguecast-x)
   - [Rank 3: TraceFish-ID](#-rank-3-tracefish-id)
   - [Rank 4: PanganShock-X](#-rank-4-panganshock-x)
   - [Rank 5: ApiShield-ID](#-rank-5-apishield-id)
   - [Rank 6: HydroRisk-ID](#-rank-6-hydrorisk-id)
   - [Rank 7: PadiWatch-X](#-rank-7-padiwatch-x)
   - [Rank 8: EduDrop-ID](#-rank-8-edudrop-id)
   - [Rank 9: WasteWise-ID](#-rank-9-wastewise-id)
   - [Rank 10: GempaRank-X](#-rank-10-gemparank-x)
   - [Rank 11: JudolFlow-X](#-rank-11-judolflow-x)
   - [Rank 12: AirGuard Sekolah](#-rank-12-airguard-sekolah)
4. [Comparison Matrix & Trade-offs](#4-comparison-matrix--trade-offs)
5. [Pipeline Architecture Template](#5-pipeline-architecture-template)
6. [Decision Checklist](#6-decision-checklist)
7. [Appendix: Sumber Dataset per Topik](#7-appendix-sumber-dataset-per-topik)

---

## 1. Ringkasan Aturan & Rubrik

### 1.1 Ketentuan Technical Report (Babak Penyisihan)

Sumber: *Panduan GEMASTIK 2025 — Divisi Penambangan Data*

**Struktur Wajib Technical Report:**

| Section | Konten Wajib |
|---------|-------------|
| Judul | Mencerminkan isi, sesuai tema "Penambangan Data untuk Peningkatan TIK menuju Kemandirian Bangsa" |
| Abstrak | Ringkasan penelitian: latar belakang, metode, hasil utama |
| Pendahuluan | Latar belakang, tujuan, manfaat, batasan |
| Kajian Terkait | Related work, state-of-the-art |
| Solusi Usulan | Deskripsi solusi, dataset, metode, perbedaan dengan solusi sebelumnya, metrik evaluasi |
| Hasil Eksperimen | Baseline ladder, eksperimen, pengujian |
| Analisis Hasil | Interpretasi, error analysis, ablation study |
| Kesimpulan | Temuan utama, saran, implikasi |

**Aturan Tambahan:**
- Format: PDF, max 10 MB
- Penamaan: `GEMASTIK XVIII Penambangan Data - <ID Tim> - <Nama Tim> - <Judul>.pdf`
- WAJIB orisinal (bukan GenAI murni), belum pernah dipublikasikan termasuk untuk kompetisi lain
- Tools / library / framework / Generative AI **diperbolehkan** sebagai alat bantu

### 1.2 Rubrik Penilaian Babak Penyisihan

| No | Kriteria | Bobot | Indikator Penilaian |
|----|----------|:-----:|---------------------|
| 1 | **Keaslian** (plagiarism check) | 20% | Uji plagiarisme; ide orisinal; bukan saduran makalah lain |
| 2 | **Kebaruan dataset / metode** | 20% | Kombinasi dataset baru; atau pendekatan/metode baru; atau aplikasi baru dari metode existing |
| 3 | **Manfaat** | 20% | Dampak sosial yang jelas; potensi implementasi di Indonesia |
| 4 | **Kejelasan tulisan** | 20% | Mudah dipahami; terstruktur; bahasa jelas dan ilmiah |
| 5 | **Kelengkapan laporan** | 20% | Semua bagian terisi; eksperimen cukup; analisis mendalam |

### 1.3 Babak Final

| Komponen | Bobot | Keterangan |
|----------|:-----:|------------|
| Nilai babak penyisihan | 20% | Makalah yang sudah dikumpulkan |
| Skor kinerja leaderboard | 30% | Performansi model pada hidden dataset |
| Ketepatan metode | 25% | Kesesuaian metode dengan problem |
| Presentasi | 25% | PPT + presentasi onsite + Q&A |

**Format Final:**
Hidden dataset → 5 jam build model → dokumentasi PPT → presentasi onsite

> **Implikasi Strategis:** 70% nilai final berasal dari non-leaderboard. Paper-first strategy sangat penting. Pilihlah metode yang *defensible* dan *interpretable*, bukan sekadar akurat.

---

## 2. Pola Pemenang Historis

### 2.1 Rekam Jejak Pemenang GEMASTIK Data Mining

| Tahun | Peringkat | Tim | Institusi | Topik Preliminary |
|-------|:---------:|-----|-----------|-------------------|
| **2021** (XIV) | 🥇 | **ILY** | ITB | Deteksi depresi dari Twitter + chatbot outreach |
| **2023** (XVI) | 🥇 | **Magnus** | ITB | IoT cybersecurity — network log attack prediction |
| **2023** (XVI) | 🥉 | Three Wise Monkey | ITB | Smart energy management |
| **2024** (XVII) | 🥇 | **Three Outliers** | UI | *(tidak terdisclose publik)* |
| **2024** (XVII) | 🥈 | Three Layers | UI | *(tidak terdisclose publik)* |
| **2024** (XVII) | 🥉 | Barudak Bojongsoang | Tel-U | *(tidak terdisclose publik)* |
| **2025** (XVIII) | 🥇 | **Three Vectors** | UI | *(tidak terdisclose publik)* |
| **2025** (XVIII) | 🥈 | Suika | UI | *(tidak terdisclose publik)* |

**Pola Institusi Pemenang:** Didominasi UI (3 medali 2024-2025), ITB (3 medali 2021-2023), dan Telkom University.

### 2.2 Pola yang Terulang — Lessons Learned

| # | Prinsip | Penjelasan | Contoh Empiris |
|---|---------|-----------|----------------|
| 1 | **Pipeline > Single Model** | Pemenang membangun multi-branch pipeline, bukan mengandalkan satu model | Magnus (2023): feature engineering on logs + rare class handling |
| 2 | **Metric-aware design** | Optimasi untuk metrik yang tepat (PR-AUC, Recall@K), bukan accuracy | ILY (2021): NLP dengan framing deteksi depresi, bukan generic sentiment |
| 3 | **Public impact + data availability** | Topik pemenang selalu: masalah publik jelas + data bisa didapat | ILY: Twitter data publik + masalah kesehatan mental relevan |
| 4 | **Judgeable robustness > flashy novelty** | Metode yang interpretable, reproducible, dan defensible di Q&A | Magnus: domain-aware engineering, bukan model black-box |
| 5 | **Paper-first strategy** | Preliminary adalah kompetisi technical report — kualitas tulisan sangat penting | 20/30/25/25 scoring → 70% dari non-leaderboard |
| 6 | **Domain grounding** | Bukan sekadar aplikasi ML generic, tapi domain knowledge | ILY: konsultasi psikologi; Magnus: network security domain |
| 7 | **Hidden-case readiness** | Final 5 jam = harus deliver baseline + improvement + slides | Latih simulasi 5 jam minimal 2× sebelum final |

---

## 3. Ranking Topik Lengkap (12 Topik, Detail Penuh)

Berikut adalah **12 topik** yang telah dianalisis dan diperbarui dengan fokus pada **Kemandirian Bangsa** (swasembada pangan, energi, air, ekonomi kreatif, ekonomi hijau, ekonomi biru). Diurutkan dari yang **paling direkomendasikan** (Rank 1) hingga **paling tidak direkomendasikan** (Rank 12) berdasarkan total score dan analisis multidimensi terhadap rubrik GEMASTIK 2025 serta pola pemenang historis.

---
### 🥇 Rank 1: WaterWatch-ID

**Score: 90/100** | **Kategori: Swasembada Air** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *WaterWatch-ID: Prediksi Multimodal Water Quality Index Sungai-Sungai Indonesia untuk Ranking Prioritas Restorasi Daerah Aliran Sungai*

---

#### Problem Statement

Kualitas air sungai di Indonesia mengalami penurunan signifikan -- 59% sungai dalam status tercemar berat (data KLHK). Pencemaran berasal dari limbah industri, domestik, dan pertanian. Indeks Kualitas Air (IKA) dipantau secara berkala oleh KLHK, namun data monitoring bersifat sparse dan reaktif.

WaterWatch-ID menjawab: **"segmen sungai di DAS mana yang memiliki risiko penurunan kualitas air dalam 1-4 minggu ke depan, sehingga prioritas restorasi dan pengawasan bisa dialokasikan secara proaktif?"**

Topik ini menyentuh pilar **Swasembada Air** (Kemandirian Bangsa) dan merupakan satu-satunya topik GEMASTIK yang mengintegrasikan data parameter kimiawi, citra satelit, dan graph daerah aliran sungai dalam satu pipeline.

---

#### Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 18 | 19 | 19 | 17 | 17 | **90** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 18/20 | Water quality prediction sudah ada, tapi *multi-branch fusion (TFT+GAT+ViT) untuk ranking prioritas restorasi DAS* sangat orisinal. |
| **Kebaruan** | 19/20 | Belum ada yang mengintegrasikan time-series parameter kimia + graph DAS + citra satelit (ViT) untuk WQI di Indonesia. |
| **Manfaat** | 19/20 | Air bersih adalah fondasi kemandirian bangsa. Relevan dengan SDG 6 (Clean Water & Sanitation). |
| **Kejelasan** | 17/20 | Butuh domain knowledge dasar tentang parameter kualitas air (DO, BOD, COD, pH, TSS). |
| **Kelengkapan** | 17/20 | Data KLHK perlu preprocessing karena sparse. Tapi setelah bersih, baselines dan ablations jelas. |

---

#### Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Parameter kualitas air historis | KLHK / Satu Data Indonesia | DO, BOD, COD, pH, TSS, Nitrat, Fosfat | data.go.id |
| Debit & elevasi sungai | BBWS / Kementerian PUPR | Debit harian, tinggi muka air | Data PUPR |
| Land use catchment area | KLHK / Geospatial Bappenas | Proporsi hutan, sawah, industri, permukiman | geoportal.bappenas |
| Citra satelit optik | Copernicus Sentinel-2 | NDWI, turbidity | Google Earth Engine |
| Curah hujan & iklim | BMKG | Curah hujan harian, intensitas | iklim.bmkg.go.id |
| Graph DAS | Bappenas / OSM | Segmen sungai, anak sungai, muara | Geospasial |

**Preprocessing Steps:**
1. **Aggregasi temporal** -- rata-rata parameter per minggu per titik sampling
2. **Interpolasi sparse** -- KNN Imputer + temporal interpolation untuk titik dengan data tidak lengkap
3. **Fusion data spasial** -- join titik monitoring ke segmen DAS terdekat berdasarkan jarak
4. **NDWI extraction** -- median composite per 2 minggu dari Sentinel-2, cloud-masked
5. **Lag features** -- rolling window 1, 2, 4, 8 minggu untuk parameter kimia dan curah hujan
6. **Graph construction** -- DAS graph: nodes = segmen sungai, edges = aliran hulu-hilir
7. **Train/val/test split** -- temporal walk-forward, test set = tahun terbaru

---

#### Modeling Stack

| Stage | Model | Detail Arsitektur | Output |
|-------|-------|-------------------|--------|
| **Branch A: Temporal** | Temporal Fusion Transformer (TFT) | Multi-horizon forecasting parameter kimia 1-4 week ahead | WQI forecast + uncertainty |
| **Branch B: Graph** | Graph Attention Network (GAT) | Propagasi polusi antar segmen sungai di DAS yang sama | Spatial risk propagation |
| **Branch C: Vision** | Vision Transformer (ViT) / ResNet50 | Classify kualitas air dari Sentinel-2 NDWI + turbidity | Visual water quality class |
| **Branch D: Tabular** | CatBoost | Fitur land use, iklim, dan demografi per DAS | Static risk baseline |
| **Fusion** | Weighted stacking + Platt calibration | Cross-attention temporal + spatial + visual | Final WQI risk rank |

**Baseline Ladder:**
1. Mean imputation + linear interpolation (naive)
2. Prophet untuk tiap parameter (time-series naive)
3. CatBoost full features (strong tabular)
4. TFT only (deep sequence)
5. TFT + GAT + ViT + Tabular fusion (**proposed**)
6. Ablations: -GAT, -ViT, -TFT

---

#### Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **MAE / RMSE** | Primary -- error WQI regresi |
| **MAPE** | Persentase error untuk interpretasi |
| **PR-AUC** | Untuk klasifikasi status mutu air (baik/cemar ringan/cemar berat) |
| **Recall@Top-K segmen** | Operational -- apakah segmen prioritas restorasi tertangkap |
| **Spatial consistency** | Apakah prediksi konsisten secara spasial (hulu-hilir) |
| **Ablation gain** | Kontribusi tiap branch terhadap akurasi |

---

#### Role Split (3 Member)

| Member | Role | Tanggung Jawab Spesifik |
|--------|------|------------------------|
| **M1 -- Data Lead** | Data Engineering | Scraping KLHK/BMKG/Sentinel-2; interpolasi sparse; graph DAS; EDA report |
| **M2 -- Model Lead** | Modeling | TFT + GAT + ViT + CatBoost; fusion; hyperparameter tuning |
| **M3 -- Eval Lead** | Evaluation & Report | Metric design; ablation study; spatial consistency check; technical report |

---

#### Why It Wins (GEMASTIK Context)

1. **Swasembada Air sebagai pilar Kemandirian Bangsa** -- belum ada tim GEMASTIK yang menyentuh topik air sama sekali
2. **Multi-modal pipeline paling variatif** -- time-series + graph + vision + tabular = diversity tertinggi dari semua topik
3. **Data tersedia dari KLHK dan Satu Data Indonesia** -- tidak perlu scraping kontroversial
4. **Visual storytelling dari peta DAS** -- sangat kuat untuk presentasi dan laporan
5. **Novelty tinggi** -- integrasi TFT + GAT + ViT untuk WQI di Indonesia benar-benar baru

#### Risiko & Mitigasi

| Risiko | Severity | Probabilitas | Mitigasi |
|--------|:--------:|:------------:|----------|
| Data monitoring KLHK sparse (tidak semua titik update mingguan) | HIGH | 40% | Fokus ke 5-10 DAS prioritas (Citarum, Bengawan Solo, Brantas) dengan data terbanyak; interpolasi gap |
| TFT/GAT/ViT butuh GPU | MEDIUM | 50% | Branch C (ViT) ganti feature extraction offline dari GEE; TFT -> LSTM; GAT -> spatial lag |
| Domain knowledge hidrologi terbatas | LOW | 30% | Konsultasi dosen lingkungan; gunakan PP 22/2021 untuk baku mutu air |

---

### 🥇 Rank 2: DengueCast-X

**Score: 91/100** | **Kategori: Kesehatan Publik** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *DengueCast-X: Prediksi Risiko Kejadian DBD Berbasis Spatiotemporal Data Mining untuk Prioritas Intervensi Wilayah*

---

#### 🩺 Problem Statement

Demam Berdarah Dengue (DBD) merupakan salah satu beban kesehatan masyarakat terbesar di Indonesia. Setiap tahun, ribuan kasus dilaporkan dengan pola musiman yang dipengaruhi oleh iklim, kepadatan penduduk, dan mobilitas. Pendekatan konvensional hanya menjawab pertanyaan "berapa jumlah kasus?" — bukan pertanyaan yang lebih operasional: **"district mana yang harus diintervensi sebelum wabah melonjak?"**

DengueCast-X mentransformasi *forecasting* konvensional menjadi **spatiotemporal risk ranking system**. Sistem ini memprediksi risiko outbreak DBD per district dalam 2–4 minggu ke depan dan menghasilkan **ranked district intervention priority list** — sehingga fogging, larvasida, PSN, dan kesiapsiagaan rumah sakit bisa dialokasikan secara optimal.

Ini selaras dengan pola pemenang GEMASTIK: **bukan model terbaik, tapi pipeline yang menjawab masalah nyata dengan metrik yang tepat.**

---

#### 📊 Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 18 | 19 | 20 | 17 | 17 | **91** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 18/20 | DBD prediction sudah ada, tapi *district-week early warning + intervention ranking + multi-view fusion* orisinal. Bukan sekadar "prediksi DBD pakai XGBoost". |
| **Kebaruan** | 19/20 | Kombinasi TFT + GNN + CatBoost + text embedding untuk DBD di Indonesia sangat jarang. Novelty kuat di arsitektur pipeline. |
| **Manfaat** | 20/20 | Sangat jelas: early intervention sebelum outbreak spike. Dampak publik langsung terlihat. |
| **Kejelasan** | 17/20 | Kompleksitas medium. Perlu framing hati-hati: "ranking prioritas intervensi" lebih intuitif dari "prediksi jumlah kasus". |
| **Kelengkapan** | 17/20 | Dapat dibuat lengkap. Dataset construction butuh effort, tapi baselines dan ablations jelas. |

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Kasus DBD historis | Kemenkes / Satu Data Indonesia | Incidence count per district-week | data.go.id |
| Iklim & cuaca | BMKG API | Rainfall, temperature, humidity | iklim.bmkg.go.id |
| Demografi | BPS API | Populasi, density, urbanisasi | webapi.bps.go.id |
| Geospasial | OpenStreetMap | District adjacency, elevasi, sungai | download.geofabrik.de |
| Berita kesehatan (optional) | Google News scraping | Outbreak keywords, sentiment | RSS/NLP pipeline |

**Preprocessing Steps:**
1. **Aggregasi mingguan** — dari data harian ke level district-week
2. **Rolling lag windows** — 1, 2, 4, 8, 12 minggu untuk semua fitur kontinu
3. **Normalisasi per-district** — standarisasi berbasis mean/std historis masing-masing
4. **Imputasi missing value** — MICE (Multivariate Imputation by Chained Equations) untuk data cuaca yang tidak lengkap
5. **Outlier handling** — IQR method atau Isolation Forest pada data kasus ekstrem
6. **Spatial adjacency matrix** — binary adjacency berdasarkan boundary sharing dari OSM
7. **Train/val/test split** — forward-chaining temporal, *bukan* random split (cegah leakage)

---

#### 🧠 Modeling Stack

| Stage | Model | Detail Arsitektur | Output |
|-------|-------|-------------------|--------|
| **Branch A: Tabular** | CatBoost / LightGBM | Lag features + interaction terms + class weighting (scale_pos_weight / SMOTE) | Risk score rₐ |
| **Branch B: Temporal Deep** | Temporal Fusion Transformer (TFT) | Multi-horizon forecasting (2-4 week); interpretable attention over time | Risk score rᵦ |
| **Branch C: Graph** | GraphSAGE / GAT (PyTorch Geometric) | 2-layer GNN on district adjacency graph; captures spillover | Risk score rᵧ |
| **Branch D: Text** (optional) | Qwen3 Embedding / BGE-M3 | News text → dense embedding → district-level risk feature | Text risk score rδ |
| **Fusion** | Weighted stacking + Platt calibration | Grid search weight (rₐ, rᵦ, rᵧ, rδ) → calibrated probability [0,1] | Final risk rank |

**Baseline Ladder (Wajib untuk Technical Report):**
1. SARIMA / Prophet — naive baseline
2. LightGBM tanpa spatial/text features — strong tabular baseline
3. TFT only — deep sequence baseline
4. Full pipeline (ALL branches + fusion) — advanced method
5. Ablations: -GNN, -TFT, -text, no fusion

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan Pengukuran |
|--------|------------------|
| **PR-AUC** | Primary metric — captures ranking quality with heavy class imbalance (outbreak ≈ rare event) |
| **Recall@Top-10% districts** | Operational utility — % outbreak tertangkap di 10% prioritas tertinggi |
| **Recall@Top-20% districts** | Secondary — coverage breadth |
| **Temporal backtesting** | Walk-forward validation across multiple outbreak seasons |
| **Lead-time gain** | Ratio: warning lead time vs baseline (e.g., +X minggu lebih awal dari metode naive) |
| **Calibration error (ECE)** | Apakah probability calibrated → uncertainty bands dapat dipercaya |
| **SHAP / attention visualization** | Explainability — fitur apa yang paling berkontribusi per district |

---

#### 👥 Role Split (3 Member)

| Member | Role | Tanggung Jawab Spesifik |
|--------|------|------------------------|
| **M1 — Data Lead** | Data Engineering | Scraping Kemenkes/BMKG/BPS; aggregation pipeline; spatial graph construction; EDA report |
| **M2 — Model Lead** | Modeling | CatBoost + TFT + GNN implementation, training, hyperparameter tuning, fusion |
| **M3 — Eval Lead** | Evaluation & Report | Metric design; ablation study; SHAP analysis; technical report writing; PPT preparation |

---

#### 🏆 Why It Wins (GEMASTIK Context)

1. **Manfaat publik langsung** — DBD adalah salah satu masalah kesehatan paling terlihat di Indonesia
2. **Multi-view pipeline** — 3 branch + fusion = *exactly* pola pemenang (pipeline > single model)
3. **Metric-aware** — PR-AUC + Recall@Top-K = competition-coded metrics
4. **Explainability built-in** — SHAP + TFT attention = defensible bawah Q&A juri
5. **Framing kuat** — "intervention priority" > "prediction task" — lebih operasional dan lebih menarik
6. **Novelty cukup** — belum ada publikasi GEMASTIK yang pakai TFT+GNN+fusion untuk DBD di Indonesia

---

#### ⚠️ Risiko & Mitigasi

| Risiko | Severity | Probabilitas | Mitigasi |
|--------|:--------:|:------------:|----------|
| Data DBD kabupaten tidak tersedia / incomplete | 🔴 HIGH | 30% | **Fallback:** provinsi-level; atau pilih 5-10 sentinel cities dengan data lengkap; atau ganti ke level kota besar |
| TFT/GNN butuh GPU yang tidak dimiliki | 🟡 MEDIUM | 40% | **Fallback:** Branch C dari GNN → spatial lag features di tabular; TFT bisa ganti dengan LSTM/GRU sederhana |
| Temporal overfitting / distribution shift | 🟡 MEDIUM | 50% | **Mitigasi:** Forward-chaining validation wajib; walk-forward CV; documented regime changes (e.g., El Niño) |
| Overclaiming causality | 🟢 LOW | 60% | **Mitigasi:** Explicit disclaimer di laporan — korelasi ≠ kausalitas; gunakan "risk marker" framing |

---

### 🥇 Rank 3: TraceFish-ID

**Score: 91/100** | **Kategori: Ekonomi Biru** | **Risiko Eksekusi: Medium-Tinggi**

> **Judul Resmi:**
> *TraceFish-ID: Deteksi Aktivitas IUU Fishing Berbasis Trajectory Data Mining dan Graph Analysis untuk Prioritas Inspeksi Pelabuhan*

---

#### Problem Statement

Indonesia adalah negara maritim terbesar di dunia dengan luas perairan 6,4 juta km2. Namun, illegal, unreported, and unregulated (IUU) fishing merugikan negara hingga Rp 100 triliun per tahun. Kapal asing dan kapal berbendera Indonesia sering melakukan pelanggaran di wilayah perairan yang luas dan sulit diawasi.

TraceFish-ID menjawab: **"kapal mana yang memiliki probabilitas tertinggi melakukan IUU fishing dalam 24-48 jam ke depan, sehingga KKP dan Bakamla bisa memprioritaskan inspeksi?"** dengan menganalisis trajectory, kecepatan, pola berhenti, dan koneksi antar kapal.

Topik ini menyentuh pilar **Ekonomi Biru** (Kemandirian Bangsa) -- domain yang sama sekali belum pernah tersentuh di GEMASTIK.

---

#### Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 19 | 20 | 19 | 17 | 16 | **91** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 19/20 | Sangat jarang ada tim GEMASTIK yang menyentuh illegal fishing + trajectory mining. |
| **Kebaruan** | 20/20 | Trajectory Transformer + bipartite graph untuk fishing anomaly belum pernah dipakai di kompetisi mahasiswa Indonesia. |
| **Manfaat** | 19/20 | IUU fishing adalah kerugian negara triliunan rupiah. Indonesia negara maritim -- relevansi maksimal. |
| **Kejelasan** | 17/20 | Konsep trajectory analysis butuh penjelasan yang baik. Tapi framing "inspeksi prioritas" intuitif. |
| **Kelengkapan** | 16/20 | Preprocessing trajectory berat; labeling IUU perlu proxy/logika domain. |

---

#### Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| AIS trajectory kapal | Global Fishing Watch API | Latitude, longitude, kecepatan, heading, timestamp | globalfishingwatch.org |
| VMS data kapal Indonesia | KKP (pernah dirilis publik) | Kapal >30 GT, tracker wajib | Data terbuka |
| Fishing zone / ZEEI | Bappenas / BIG | Batas ZEEI, kawasan konservasi, jalur pelayaran | Geospasial |
| Data pelabuhan | KKP / BPS | Lokasi pelabuhan, kapasitas, riwayat inspeksi | Data publik |
| Cuaca maritim | BMKG Maritim | Gelombang, angin, visibility | bmkg.go.id |

**Preprocessing Steps:**
1. **Trajectory resampling** -- interpolasi ke interval 10 menit untuk standardisasi
2. **Fishing activity labeling** -- deteksi dari kecepatan <3 knot + random heading change; validasi GFW API
3. **Feature extraction** -- speed distribution, turning angle, trip duration, jarak ke ZEEI, jarak ke pelabuhan
4. **Port-to-port segmentation** -- pisahkan trajectory per trip (berangkat dari pelabuhan A -> kembali ke A/B)
5. **Bipartite graph** -- nodes: kapal + pelabuhan; edges: frekuensi kunjungan, durasi
6. **Anomaly score baseline** -- isolation forest pada fitur trajectory untuk label proxy
7. **Temporal split** -- train pada tahun 2022-2023, validasi 2024, test pada 2025

---

#### Modeling Stack

| Stage | Model | Detail Arsitektur | Output |
|-------|-------|-------------------|--------|
| **Branch A: Trajectory** | Trajectory Transformer / t2vec | Sequence-to-sequence embedding dari trajectory point sequence | Trajectory anomaly score |
| **Branch B: Tabular** | XGBoost / CatBoost | Fitur yang diekstrak dari trajectory (speed, turning, durasi, dll) | Fishing risk score |
| **Branch C: Graph** | GNN (RGCN / Heterogeneous GAT) | Bipartite graph kapal-pelabuhan untuk link prediction dan community detection | Suspicious network score |
| **Branch D: Temporal** | LSTM / TFT | Time-series fitur maritim: posisi, kecepatan terhadap waktu | Trajectory deviation score |
| **Fusion** | Weighted stacking + threshold calibration | Ensemble anomaly scores + clustering confidence | Final IUU risk rank |

**Baseline Ladder:**
1. Rule-based: kecepatan threshold + proximity to ZEEI (naive)
2. Isolation Forest on tabular features (unsupervised anomaly)
3. XGBoost with weak labels (supervised)
4. Trajectory Transformer only (deep sequence)
5. Full pipeline: trajectory + tabular + graph + temporal (**proposed**)
6. Ablations: -graph, -trajectory, -temporal

---

#### Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **PR-AUC** | Primary -- IUU fishing sangat rare (<1% trips) |
| **Recall@Top-K kapal** | Operational -- apakah kapal IUU tertangkap di K prioritas inspeksi |
| **F1 per jenis IUU** | Distinguish: transshipment, boundary violation, gear violation |
| **Cluster purity** | Graph community detection quality |
| **Temporal backtesting** | Apakah deteksi konsisten antar musim/tahun |
| **Case studies** | Validasi pada kasus IUU yang sudah terkonfirmasi media/laporan |

---

#### Role Split (3 Member)

| Member | Role | Tanggung Jawab Spesifik |
|--------|------|------------------------|
| **M1 -- Data Lead** | Data Engineering | GFW API ingestion; trajectory cleaning; feature extraction; EDA report |
| **M2 -- Model Lead** | Modeling | Trajectory Transformer + XGBoost + GNN; fusion; hyperparameter tuning |
| **M3 -- Eval Lead** | Evaluation & Report | Metric design; case study; temporal backtesting; technical report writing |

---

#### Why It Wins (GEMASTIK Context)

1. **Ekonomi Biru sebagai pilar Kemandirian Bangsa** -- domain yang sama sekali belum tersentuh di GEMASTIK
2. **Novelty metode tertinggi** -- Trajectory Transformer + GNN bipartite untuk fishing anomaly benar-benar baru
3. **Data AIS gratis dari Global Fishing Watch** -- salah satu dataset publik paling kaya untuk Indonesia
4. **Dampak negara** -- IUU fishing = kerugian triliunan rupiah per tahun
5. **Visual storytelling peta tracking kapal** -- sangat impresif untuk presentasi
6. **"Inspeksi prioritas" framing** -- lebih operasional dari "deteksi IUU"

#### Risiko & Mitigasi

| Risiko | Severity | Probabilitas | Mitigasi |
|--------|:--------:|:------------:|----------|
| Label IUU tidak ada (unsupervised problem) | HIGH | 80% | Gunakan weak labeling: rule-based (kecepatan + proximity ZEEI) + GFW known-fishing flags; framing sebagai anomaly detection |
| AIS data noisy / gap coverage | MEDIUM | 50% | Interpolasi gap pendek; fallback: fokus ke kapal dengan AIS coverage >70% trip |
| Trajectory Transformer butuh skill | MEDIUM | 40% | Branch A bisa diganti LSTM/GRU sederhana jika waktu tidak cukup |
| Data ethics & privasi | MEDIUM | 20% | Hanya gunakan data AIS publik; jangan scraping data kapal privat |

---

### 🥇 Rank 4: PanganShock-X

**Score: 91/100** | **Kategori: Ekonomi Pangan** | **Risiko Eksekusi: Rendah**

> **Judul Resmi:**
> *PanganShock-X: Prediksi Risiko Lonjakan Harga Pangan Strategis Berbasis Multiview Time-Series Data Mining*

---

#### 🌾 Problem Statement

Harga pangan strategis di Indonesia dikenal sangat volatil — dipengaruhi oleh cuaca, distribusi, kebijakan, dan spekulasi pasar. Kenaikan harga secara tiba-tiba (price spike) berdampak langsung pada inflasi, daya beli rumah tangga, dan ketahanan pangan nasional.

PanganShock-X menjawab pertanyaan: **"komoditas apa di region mana yang berisiko mengalami lonjakan harga dalam 7–14 hari ke depan?"** dengan menghasilkan **ranked region-commodity alert list** — sehingga Bulog / Pemda bisa melakukan intervensi pasar (operasi pasar, distribusi) sebelum harga melonjak.

Topik ini adalah yang **paling aman secara eksekusi** — data bersih, metrik jelas, baseline mudah, dan laporan mudah ditulis lengkap.

---

#### 📊 Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 17 | 17 | 19 | 19 | 19 | **91** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 17/20 | Food price forecasting sudah ada, tapi *spike risk ranking + multiview fusion* tidak se-umum prediksi harga biasa. |
| **Kebaruan** | 17/20 | Cukup baik jika menambahkan news/text branch dan uncertainty calibration. Tanpa itu, novelty medium. |
| **Manfaat** | 19/20 | Sangat jelas: inflasi, food security, intervensi pasar. Bedanya dengan DengueCast: bukan masalah hidup-mati, jadi minus tipis. |
| **Kejelasan** | 19/20 | Termudah untuk ditulis dan dijelaskan. Semua orang paham "harga naik itu masalah". |
| **Kelengkapan** | 19/20 | Paling mudah untuk membuat laporan lengkap — data paling bersih, eksperimen paling straightforward. |

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber | Variabel | Akses |
|------|--------|----------|-------|
| Harga harian komoditas | PIHPS BPS | Harga beras, cabai, bawang, minyak, daging (50+ komoditas) | pipps.bps.go.id |
| Inflasi daerah | BPS API | IHK per kota | webapi.bps.go.id |
| Cuaca & iklim | BMKG | Rainfall, temperature, anomaly indices | iklim.bmkg.go.id |
| Kalender tanam/panen | Kementan | Musim tanam per komoditas per region | Data terbuka |
| Berita & sentimen | Google News / RSS | Berita pangan regional | Scraping NLP pipeline |

**Preprocessing Pipeline:**
1. **Panel time-series construction** — (region × commodity × date) multi-index
2. **Spike labeling** — threshold-based (e.g., > 2 standard deviations from 30-day rolling mean, or > 5% daily change)
3. **Missing price interpolation** — linear interpolation untuk gap ≤ 3 hari; forward-fill untuk gap lebih panjang
4. **Rolling features** — mean, std, min, max untuk window 7, 14, 30 hari
5. **Holiday & event flags** — puasa, lebaran, natal, tahun baru, pemilu
6. **Calendar alignment** — harvest season per region × commodity

---

#### 🧠 Modeling Stack

| Stage | Model | Detail |
|-------|-------|--------|
| **Baseline** | Prophet / SARIMA | Seasonal decomposition with holiday effects |
| **Branch A: Tabular** | LightGBM / CatBoost | Lags + cross-features + holiday flags + commodity embeddings |
| **Branch B: Temporal Deep** | TFT / N-HiTS / TiDE | Multi-horizon forecasting with exogenous weather signals |
| **Branch C: Text Signal** (optional) | Qwen3 Embedding / BGE-M3 | Embed berita pangan → weekly sentiment/risk indicators |
| **Output** | Dual objective: regression (expected price) + classification (spike/no-spike) → fused spike probability + uncertainty band |

**Baseline Ladder:**
1. Naive: last-observed value
2. Prophet with holiday effects
3. LightGBM with lag features
4. TFT + Tabular ensemble
5. Full pipeline (TFT + Tabular + Text + Calibration)

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **wMAPE / sMAPE** | Weighted/ symmetric MAPE untuk regresi harga |
| **PR-AUC** | Untuk spike/no-spike classification |
| **Recall@Top-K alerts** | Operational — apakah spike tertangkap di K peringkat teratas |
| **Directional accuracy** | Persentase prediksi arah (naik/turun) yang benar |
| **Calibration plot** | Reliability diagram untuk spike probability |

---

#### 👥 Role Split

| Member | Role |
|--------|------|
| **M1 — Data Lead** | Harvest price data pipeline; PIHPS scraping; missing value handling; panel construction |
| **M2 — Model Lead** | Prophet + LightGBM + TFT; dual-objective; fusion |
| **M3 — Eval Lead** | Spike detection metrics; calibration; ablation by commodity group; report writing |

---

#### 🏆 Why It Wins

1. **Eksekusi paling aman** — data paling bersih (PIHPS), baseline mudah, risiko gagal rendah
2. **Kelengkapan laporan 19/20** — sangat mungkin untuk membuat laporan yang *complete*
3. **Kejelasan 19/20** — konsep "memprediksi lonjakan harga" langsung dipahami
4. **Dual objective** — regression + classification = double validation = looks more rigorous
5. **Text branch opsional** — kalau mau novelty, tambah news embedding

#### ⚠️ Risiko & Mitigasi

| Risiko | Severity | Mitigasi |
|--------|:--------:|----------|
| Terasa "biasa saja" tanpa angle kuat | 🟡 MEDIUM | Tambahkan uncertainty calibration + text branch + "spike risk ranking" framing |
| Data harga bisa incomplete (beberapa komoditas/region) | 🟡 MEDIUM | Fokus ke 5-10 komoditas strategis + 10 kota besar yang data-nya lengkap |
| Overlap dengan tim lain | 🟡 MEDIUM | *Differentiator*: multiview + ranking + calibration — kalau tim lain forecast biasa, kamu rank |

---

### 🥇 Rank 5: ApiShield-ID

**Score: 91/100** | **Kategori: Lingkungan & Kebencanaan** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *ApiShield-ID: Prediksi Risiko Kebakaran Hutan/Lahan Berbasis Spatiotemporal Data Mining untuk Prioritas Patroli Desa*

---

#### 🔥 Problem Statement

Kebakaran hutan dan lahan (karhutla) adalah bencana tahunan di Indonesia yang menyebabkan kerugian ekonomi, kesehatan, dan lingkungan yang sangat besar. Provinsi Riau, Kalimantan, Sumatera Selatan, dan Nusa Tenggara adalah hotspot utama. Upaya pencegahan masih bersifat reaktif — petugas pemadam dikerahkan *setelah* api sudah besar.

ApiShield-ID menjawab: **"desa mana yang memiliki risiko kebakaran tertinggi dalam 1–7 hari ke depan, sehingga patroli dan sosialisasi bisa dilakukan secara proaktif?"**

Ini adalah **Top Pick dari Winner Playbook** — data melimpah, multimodal, visual storytelling sangat kuat, dan novelty tinggi.

---

#### 📊 Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 18 | 19 | 19 | 18 | 17 | **91** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 18/20 | Wildfire prediction sudah ada tapi *village-scale nowcasting + patrol ranking + GNN* masih orisinal. |
| **Kebaruan** | 19/20 | Kombinasi hotspot (NASA FIRMS), weather, satellite imagery, graph adjacency — strong. |
| **Manfaat** | 19/20 | Karhutla adalah bencana tahunan yang sangat merugikan. Tapi mungkin tidak se-luas DBD dampaknya. |
| **Kejelasan** | 18/20 | "Prediksi kebakaran" mudah dipahami. Tapi butuh klarifikasi bahwa outputnya *risk rank*, bukan *fire forecast*. |
| **Kelengkapan** | 17/20 | Data cukup lengkap. Pipeline multimodal butuh dokumentasi yang rapi. |

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber | Variabel Kunci |
|------|--------|----------------|
| Hotspot aktif real-time | NASA FIRMS (MODIS/VIIRS) | Latitude, longitude, confidence, FRP |
| Cuaca | BMKG | Curah hujan, kelembaban, suhu, kecepatan angin |
| Historical fires | BNPB DIBI | Rekaman kebakaran historis per lokasi |
| Satelit optik | Copernicus Sentinel-2 | NDVI, land cover classification |
| Exposure layers | OpenStreetMap | Pemukiman, jalan, lahan, sungai |

**Preprocessing Pipeline:**
1. **Spatial join** — hotspot → grid desa/kecamatan (1 km² atau administrative boundary)
2. **Rainfall deficit calculation** — SPI (Standardized Precipitation Index) untuk 1, 3, 6 bulan
3. **Lag features** — hotspot count for 1, 3, 7, 14, 30 days prior
4. **Land cover aggregation** — proportion of peat, forest, plantation, settlement per grid
5. **Temporal split** — forward-chaining; kalau bisa exclusion period El Niño
6. **Class balancing** — positive class (fire) ≈ 1-5% of samples

---

#### 🧠 Modeling Stack

| Stage | Model | Detail |
|-------|-------|--------|
| **Baseline** | LightGBM | Rainfall deficit, hotspot history, humidity, wind |
| **Branch B: Spatiotemporal** | ConvLSTM / GRU-D / Spatiotemporal Transformer | Grid-based sequence: weather + hotspot 2D field |
| **Branch C: Graph** | GraphSAGE | Village adjacency + fire propagation graph |
| **Fusion** | Weighted ensemble + uncertainty calibration | Konversi multi-score ke calibrated probability |
| **Post-processing** | Threshold tuning by region | Berbeda threshold untuk Sumatera vs NTT |

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **PR-AUC** | Primary — karena class imbalance ekstrem |
| **Recall@Top-K villages** | Operational — apakah api muncul di K desa prioritas |
| **Lead-time gain** | Berapa hari lebih awal dibanding baseline (e.g., hotspot density threshold) |
| **Calibration error** | Uncertainty reliability untuk tiap prediksi |
| **Spatial stress test** | Province-wise evaluation: apakah model generalizes cross-region |

---

#### 👥 Role Split

| Member | Role |
|--------|------|
| **M1 — Data Lead** | NASA FIRMS ingestion; BMKG + OSM pipeline; grid aggregation; EDA |
| **M2 — Model Lead** | LightGBM + ConvLSTM + GNN training; hyperparameter tuning |
| **M3 — Eval Lead** | Spatial cross-validation; ablation; calibration; SHAP; maps visualization; report |

---

#### 🏆 Why It Wins

1. **Data melimpah** — NASA FIRMS real-time + BMKG + Sentinel + OSM — sangat kaya
2. **Visual storytelling kuat** — peta sebaran api sangat powerful untuk juri
3. **Multi-view pipeline** — tabular + spatiotemporal + graph = winner pattern
4. **Novelty tinggi** — belum banyak tim GEMASTIK yang menyentuh topik karhutla
5. **Kalau tidak ada data DBD** (Risiko DengueCast), ApiShield adalah backup paling kuat

#### ⚠️ Risiko & Mitigasi

| Risiko | Severity | Mitigasi |
|--------|:--------:|----------|
| Hotspot labels noisy (false positive dari industri/perkebunan) | 🟡 MEDIUM | Filter dengan NASA FIRMS confidence ≥ 80% + validasi BNPB records |
| El Niño anos — distribution shift | 🟡 MEDIUM | Exclusion period atau domain adaptation: train di normal year, test di El Niño |
| Remote sensing processing butuh storage | 🟢 LOW | Gunakan Google Earth Engine untuk preprocessing — free tier cukup |

---

### 🥈 Rank 6: HydroRisk-ID

**Score: 89/100** | **Kategori: Kebencanaan** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *HydroRisk-ID: Prediksi Risiko Dampak Banjir dan Longsor untuk Prioritas Kesiapsiagaan Wilayah*

---

#### 🌊 Problem Statement

Banjir dan longsor adalah bencana hidrometeorologi paling sering di Indonesia. Setiap musim hujan, BNPB mencatat ratusan kejadian banjir yang berdampak pada ribuan jiwa dan kerugian ekonomi miliaran rupiah. Namun, deteksi dini masih sangat bergantung pada early warning system konvensional yang *threshold-based* dan tidak mengintegrasikan multiple risk factors.

HydroRisk-ID menjawab: **"district/subdistrict mana yang berisiko mengalami banjir/ longsor dengan dampak severitas tertentu dalam 3–7 hari ke depan?"** Bukan sekadar *event prediction*, tapi **impact severity ranking** — sehingga BPBD bisa memprioritaskan evakuasi dan logistik.

> **Pembedaan dari ApiShield-ID:** HydroRisk fokus pada banjir+longsor (lebih luas, lebih umum), sementara ApiShield fokus spesifik pada karhutla (lebih niche, lebih narrow).

---

#### 📊 Rubrik Scoring

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 16 | 17 | 20 | 18 | 18 | **89** |

**Catatan:** Banjir/longsor prediction bukan hal baru. Keaslian & kebaruan medium. Tapi **manfaat 20/20** karena dampak langsung pada keselamatan jiwa. Kelengkapan laporan dinilai mudah karena data BNPB cukup terstruktur.

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber |
|------|--------|
| Banjir/longsor historis (lokasi, tanggal, severity, dampak) | BNPB DIBI |
| Curah hujan harian, prakiraan 3-7 hari | BMKG |
| DEM / topography / kemiringan lereng | Copernicus / DEMNAS |
| Land use, DAS (Daerah Aliran Sungai) | KLHK / Geospatial Bappenas |
| Populasi, bangunan, infrastruktur vital | BPS + OpenStreetMap |

**Preprocessing:**
1. **Event aggregation** per subdistrict per day → binary labels + severity multi-class
2. **Rainfall accumulation** — cumulative rainfall 1, 3, 7 hari
3. **Topography features** — slope, elevation, distance to river, drainage density
4. **Exposure weighting** — population × building density per subdistrict
5. **Temporal split** — forward-chaining, test set: musim hujan terbaru
6. **Address label lag & underreporting** — explicit section di report

---

#### 🧠 Modeling Stack

| Stage | Model |
|-------|-------|
| **Baseline** | LightGBM: rainfall + antecedent rainfall + topography proxies |
| **Branch B: Spatial Sequence** | ConvLSTM over gridded weather + terrain |
| **Branch C: Graph Exposure** | Graph-based exposure propagation (DAS network) |
| **Output** | Event probability + impact severity classification |

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| F1 / PR-AUC untuk event occurrence | Detection quality |
| MAE / SMAPE untuk affected-population estimates | Impact accuracy |
| Recall@Top-K | Operational — kecukupan prioritas |
| Spatial robustness | Performance pada unseen provinces |

---

### 🥈 Rank 7: PadiWatch-X

**Score: 89/100** | **Kategori: Pangan & Pertanian** | **Risiko Eksekusi: Medium-High**

> **Judul Resmi:**
> *PadiWatch-X: Prediksi Anomali Hasil Panen Padi Berbasis Multimodal Data Mining untuk Peringatan Dini Ketahanan Pangan*

---

#### 🌾 Problem Statement

Produksi padi Indonesia sangat dipengaruhi oleh variabilitas iklim — El Niño, La Niña, dan anomali musim tanam. Gagal panen di satu provinsi bisa mempengaruhi pasokan nasional dan harga beras. Sistem peringatan dini yang ada masih menggunakan pendekatan statistik sederhana yang tidak mengintegrasikan citra satelit dan data cuaca multimodal.

PadiWatch-X menjawab: **"kabupaten mana yang berisiko mengalami anomali hasil panen pada musim tanam mendatang?"** dengan memadukan data iklim, citra satelit (NDVI time-series), dan data produksi historis BPS.

**Unik:** Satu-satunya topik yang menggunakan **multimodal fusion (tabular + remote sensing)** — ini sangat kuat untuk kebaruan metode (19/20 potensial). Tapi butuh pengetahuan remote sensing yang tidak dimiliki semua tim.

---

#### 📊 Rubrik Scoring

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 17 | 18 | 19 | 17 | 18 | **89** |

**Catatan:** Kebaruan tinggi karena multimodal (tabular + RS). Tapi crop calendar alignment menambah kesulitan eksekusi.

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber |
|------|--------|
| Hasil panen per kabupaten/musim | BPS (Ubinan / KSA) |
| Climate indices (SPI, NDVI anomaly) | BMKG + Copernicus |
| Citra satelit NDVI/EVI | Sentinel-2 / MODIS (Google Earth Engine) |
| Peta lahan sawah | Kementan / Geospatial |
| Kalender tanam | Kementan (per provinsi, per komoditas) |

**Preprocessing:**
1. **Seasonal aggregation** — MT1 (Okt-Mar), MT2 (Apr-Sep) atau sesuai kalender lokal
2. **NDVI temporal profiles** — cloud masking → median composite per 16 hari
3. **Climate anomaly indices** — SPI 1, 3, 6 bulan; temperature anomaly
4. **Crop calendar alignment** — PASTI DILAKUKAN dengan benar karena berbeda per provinsi

---

#### 🧠 Modeling Stack

| Stage | Model |
|-------|-------|
| **Baseline** | LightGBM: lagged climate + historic yields |
| **Branch B: Temporal CNN** | 1D-CNN atau 3D-CNN over NDVI time-series |
| **Branch C: Fusion** | Multimodal: tabular features + RS features + district embeddings |
| **Output** | Yield anomaly class (normal / below / above) atau yield regression |

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| MAE, R² | Regresi yield |
| Directional accuracy on anomalies | Apakah arah anomali benar (di atas/bawah normal) |
| Per-province robustness | Generalisasi ke provinsi unseen |
| Ablation: climate-only vs multimodal | Untuk menunjukkan kontribusi RS |

---

### 🥉 Rank 8: EduDrop-ID

**Score: 87/100** | **Kategori: Pendidikan** | **Risiko Eksekusi: Rendah**

> **Judul Resmi:**
> *EduDrop-ID: Prediksi Risiko Putus Sekolah Berbasis Hierarchical Data Mining untuk Prioritas Intervensi Daerah*

---

#### Problem Statement

Angka putus sekolah di Indonesia masih menjadi masalah struktural. Data Kemendikdasmen menunjukkan ribuan siswa putus sekolah setiap tahunnya, terutama di jenjang SD dan SMP di daerah tertinggal. Faktor penyebab bervariasi -- ekonomi keluarga, jarak sekolah, kualitas guru, dan kondisi sosial.

EduDrop-ID menjawab: **"sekolah dan kecamatan mana yang memiliki risiko putus sekolah tertinggi pada tahun ajaran mendatang, sehingga Kemendikdasmen dan Pemda bisa memprioritaskan BOS afirmasi, guru penggerak, dan program retensi?"**

Pendidikan adalah fondasi **Kemandirian Bangsa** -- tanpa SDM yang terdidik, kemandirian pangan, energi, dan ekonomi sulit dicapai.

---

#### Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 17 | 17 | 20 | 17 | 16 | **87** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 17/20 | Student dropout prediction sudah ada, tapi *hierarchical model + school profiling cluster + spatial analysis* untuk konteks Indonesia masih orisinal. |
| **Kebaruan** | 17/20 | Hierarchical Mixed Effects Model untuk data pendidikan Indonesia belum umum di GEMASTIK. |
| **Manfaat** | 20/20 | Angka putus sekolah adalah isu SDM fundamental. Dampak langsung pada masa depan bangsa. |
| **Kejelasan** | 17/20 | Konsep mudah dipahami; tapi perlu klarifikasi bahwa outputnya ranking sekolah, bukan prediksi individu siswa. |
| **Kelengkapan** | 16/20 | Data Dapodik mungkin perlu pemrosesan administrasi. Tapi setelah dapat, pipeline lurus. |

---

#### Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Data pokok pendidikan (Dapodik) | Kemendikdasmen | Jml siswa, guru, rombel, putus sekolah per tahun, akreditasi | dapodik.kemdikbud.go.id |
| Data kemiskinan | BPS | Persentase kemiskinan, PDRB per kapita per kab/kota | bps.go.id |
| Infrastruktur sekolah | Dapodik + OSM | Fasilitas (listrik, air, toilet), jarak ke kecamatan | dapodik + osm.org |
| Program bantuan | Puslapdik | Penerima BOS, PIP, KIP per sekolah | Data publik |
| Ikhtisar Data Pendidikan | Kemendikdasmen | Angka putus sekolah, mengulang, melanjutkan per provinsi | data.kemendikdasmen.go.id |

**Preprocessing Steps:**
1. **School-level aggregation** -- agregasi data per sekolah per tahun (bukan per siswa)
2. **Target definition** -- persentase putus sekolah per tahun per sekolah (atau binary: >threshold?)
3. **Lag features** -- tren putus sekolah 2-3 tahun sebelumnya, delta enrollment, rasio guru/siswa
4. **Spatial features** -- kecamatan: kemiskinan, akses transportasi, jumlah sekolah alternatif
5. **Categorical encoding** -- provinsi/kabupaten sebagai hierarchical group
6. **Train/val/test split** -- temporal: train 2020-2022, val 2023, test 2024
7. **Imbalance handling** -- mayoritas sekolah punya dropout rendah; fokus ke sekolah risiko tinggi

---

#### Modeling Stack

| Stage | Model | Detail Arsitektur | Output |
|-------|-------|-------------------|--------|
| **Branch A: Tabular** | XGBoost / CatBoost | Fitur sekolah + kecamatan; SHAP untuk interpretasi | Prediksi risiko basal |
| **Branch B: Hierarchical** | Mixed Effects Model (LMM/GLMM) | Random intercept per kabupaten; fixed effects: fasilitas, ekonomi, rasio guru | Adjusted school risk |
| **Branch C: Clustering** | K-Prototypes | Mixed numerical+categorical clustering untuk profiling tipe sekolah berisiko | School risk profile |
| **Ensemble** | Weighted average XGBoost + LMM | Combine local prediction (XGBoost) + group-adjusted prediction (LMM) | Final risk score |

**Baseline Ladder:**
1. Mean dropout rate per kabupaten (naive)
2. Logistic Regression with basic features
3. XGBoost with all features (strong tabular)
4. XGBoost + Mixed Effects (hierarchical)
5. XGBoost + Mixed Effects + Clustering profile (**proposed**)
6. Ablations: -hierarchical, -clustering

---

#### Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **PR-AUC** | Primary -- kelas putus sekolah adalah minoritas |
| **Recall@Top-K sekolah** | Operational -- apakah sekolah risiko tinggi tertangkap di K prioritas |
| **F1-score** | Balanced precision-recall |
| **RMSE** | Untuk regresi persentase putus sekolah |
| **Cross-validation by province** | Generalisasi ke provinsi yang tidak ada di training |

---

#### Role Split (3 Member)

| Member | Role | Tanggung Jawab Spesifik |
|--------|------|------------------------|
| **M1 -- Data Lead** | Data Engineering | Scraping Dapodik + BPS; join; feature engineering; EDA report |
| **M2 -- Model Lead** | Modeling | XGBoost + Mixed Effects Model + K-Prototypes clustering; ensemble |
| **M3 -- Eval Lead** | Evaluation & Report | Metric design; ablation; cross-validation by province; technical report |

---

#### Why It Wins (GEMASTIK Context)

1. **Pendidikan = fondasi Kemandirian Bangsa** -- SDM unggul adalah syarat kemandirian
2. **Eksekusi paling aman** -- data Dapodik terstruktur, tidak perlu GPU, pipeline sederhana
3. **Manfaat 20/20** -- putus sekolah adalah isu yang dipahami semua orang
4. **Hierarchical model** -- novelty metodologis yang cukup untuk membedakan dari sekedar "prediksi pake XGBoost"
5. **Risiko paling rendah** -- kemungkinan gagal eksekusi sangat kecil

#### Risiko & Mitigasi

| Risiko | Severity | Probabilitas | Mitigasi |
|--------|:--------:|:------------:|----------|
| Akses data Dapodik tingkat sekolah butuh pengajuan | MEDIUM | 40% | Gunakan data agregat publik dari Ikhtisar Data Pendidikan Kemendikdasmen; atau data BPS |
| Data putus sekolah underreported | MEDIUM | 30% | Framing sebagai "risiko proxy" bukan "prediksi absolut"; validasi dengan data kemiskinan BPS |
| Terlihat seperti dashboard biasa | MEDIUM | 20% | Framing kuat sebagai risk prediction system; hierarchical + clustering sebagai diferensiator |

---

### 🥉 Rank 9: WasteWise-ID

**Score: 86/100** | **Kategori: Ekonomi Hijau** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *WasteWise-ID: Prediksi Timbulan Sampah Berbasis Spatiotemporal Data Mining untuk Optimasi Rantai Pengelolaan Sampah*

---

#### Problem Statement

Indonesia adalah penghasil sampah terbesar kedua di dunia setelah China. Timbulan sampah nasional mencapai 65 juta ton/tahun dan diperkirakan terus meningkat. Namun, sistem pengelolaan sampah masih bersifat reaktif -- armada dijadwalkan secara merata, tidak berdasarkan prediksi timbulan per wilayah.

WasteWise-ID menjawab: **"kecamatan mana yang akan mengalami lonjakan timbulan sampah dalam 1-7 hari ke depan, sehingga Dinas Lingkungan Hidup bisa mengalokasikan armada dan TPS 3R secara optimal?"**

Topik ini menyentuh pilar **Ekonomi Hijau** (Kemandirian Bangsa) -- pengelolaan sampah yang efisien mengurangi emisi, meningkatkan daur ulang, dan menciptakan nilai ekonomi sirkular.

---

#### Rubrik Scoring Breakdown

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 17 | 18 | 18 | 17 | 16 | **86** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 17/20 | Waste prediction sudah ada tapi *spatiotemporal + multi-source fusion (SIPSN + demografi + cuaca)* untuk Indonesia masih orisinal. |
| **Kebaruan** | 18/20 | N-BEATS + GNN + optimization layer untuk waste management di Indonesia belum ada di GEMASTIK. |
| **Manfaat** | 18/20 | Relevan dengan masalah sampah nasional, tapi benefit operasional (penghematan BBM armada) tidak sedramatis kesehatan. |
| **Kejelasan** | 17/20 | Konsep mudah dipahami; tapi butuh klarifikasi bahwa outputnya adalah prediksi timbulan, bukan audit sampah. |
| **Kelengkapan** | 16/20 | Data SIPSN tersedia tapi tidak semua kabupaten update rutin. Validasi memerlukan domain knowledge. |

---

#### Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Timbulan sampah historis | SIPSN KLHK | Tonase per hari per kab/kota | sipsn.menlhk.go.id |
| Demografi & kepadatan | BPS | Jumlah penduduk, kepadatan, PDRB | bps.go.id |
| Data cuaca | BMKG | Curah hujan, suhu (mempengaruhi timbulan sampah basah) | iklim.bmkg.go.id |
| Hari libur & event | Kemenko PMK | Libur nasional, hari besar, event kota | Data publik |
| TPS/TPA location | OpenStreetMap | Lokasi TPS, TPA, jarak, kapasitas | osm.org |

**Preprocessing Steps:**
1. **Daily aggregation** -- tonase sampah per kecamatan per hari
2. **Holiday feature** -- binary flags: hari libur, hari pasar, event kota
3. **Weather features** -- curah hujan kumulatif 1, 3, 7 hari; suhu rata-rata
4. **Lag features** -- timbulan 1, 2, 3, 7 hari sebelumnya
5. **Population normalization** -- tonase per 1000 penduduk untuk perbandingan antar wilayah
6. **Spatial adjacency** -- graph kecamatan untuk spillover antar wilayah
7. **Train/val/test split** -- temporal walk-forward

---

#### Modeling Stack

| Stage | Model | Detail Arsitektur | Output |
|-------|-------|-------------------|--------|
| **Branch A: Temporal** | N-BEATS / TiDE | Pure time-series forecasting; state-of-the-art untuk univariat | Waste forecast per wilayah |
| **Branch B: Tabular** | LightGBM | Fitur demografi + cuaca + holiday + lag | Feature-driven prediction |
| **Branch C: Graph** | GNN (GraphSAGE) | Spillover antar kecamatan yang berdekatan | Spatial adjustment |
| **Optimization** | Integer Linear Programming | Rute armada berdasarkan prediksi timbulan | Rekomendasi jadwal & rute |

**Baseline Ladder:**
1. Mean per hari (seasonal naive)
2. SARIMA / Prophet (time-series)
3. LightGBM with all features (tabular)
4. N-BEATS (deep sequence)
5. LightGBM + N-BEATS + GNN + routing (**proposed**)
6. Ablations: -graph, -N-BEATS

---

#### Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| **MAE / RMSE** | Primary -- error prediksi tonase |
| **MAPE** | Persentase error |
| **Saving estimation** | Simulasi penghematan: berapa perjalanan armada bisa dihemat |
| **Peak detection** | Akurasi deteksi lonjakan sampah (hari libur/event) |

---

#### Role Split (3 Member)

| Member | Role | Tanggung Jawab Spesifik |
|--------|------|------------------------|
| **M1 -- Data Lead** | Data Engineering | SIPSN scraping; weather join; EDA; spatial graph construction |
| **M2 -- Model Lead** | Modeling | N-BEATS + LightGBM + GNN; optimization layer; hyperparameter tuning |
| **M3 -- Eval Lead** | Evaluation & Report | Metrics; peak detection; cost saving simulation; technical report |

---

#### Why It Wins (GEMASTIK Context)

1. **Ekonomi Hijau sebagai pilar Kemandirian Bangsa** -- belum ada tim GEMASTIK di topik sampah
2. **Data SIPSN publik dan gratis** -- tersedia langsung dari KLHK
3. **N-BEATS (state-of-the-art time series)** -- lebih baru dari Prophet/SARIMA yang biasa dipakai
4. **Optimization layer** -- diferensiator: bukan hanya prediksi tapi juga rekomendasi operasional
5. **Dampak langsung** -- penghematan BBM, pengurangan emisi, efisiensi anggaran daerah

#### Risiko & Mitigasi

| Risiko | Severity | Probabilitas | Mitigasi |
|--------|:--------:|:------------:|----------|
| Data SIPSN tidak semua kabupaten update | MEDIUM | 40% | Fokus ke 10 kota besar dengan data SIPSN paling rajin update; atau gunakan data dinas kebersihan kota |
| Output optimization terlalu berat untuk GEMASTIK | MEDIUM | 30% | Optimization layer bisa opsional; cukup tunjukkan sebagai "extended work" atau simulasi |
| Timbulan sampah dipengaruhi faktor lokal acak | LOW | 20% | Akui keterbatasan di report; framing sebagai risk estimation bukan exact prediction |

---

### 🥉 Rank 10: GempaRank-X

**Score: 86/100** | **Kategori: Kebencanaan** | **Risiko Eksekusi: Medium**

> **Judul Resmi:**
> *GempaRank-X: Ranking Dampak Gempa Bumi Berbasis Data Mining untuk Prioritas Respons Darurat*

---

#### 🌍 Problem Statement

Indonesia berada di Ring of Fire — gempa bumi besar terjadi setiap beberapa tahun. Saat gempa terjadi, pertanyaan kritis dalam 1 jam pertama adalah: **"daerah mana yang paling terdampak? fasilitas kritis mana yang perlu diprioritaskan?"** Tim SAR, BPBD, dan Kemenkes butuh informasi ini dalam hitungan menit.

GempaRank-X bukan "prediksi gempa" (itu impossible dengan teknologi saat ini). Melainkan: **segera setelah gempa terjadi, sistem ini meranking daerah dan aset kritis berdasarkan risiko dampak** — menggunakan magnitudo, kedalaman, lokasi, exposure bangunan, dan kerentanan populasi.

**Catatan:** Karena sifatnya *post-event nowcasting* bukan *pre-event prediction*, ini secara teknis berbeda dari topik forecasting di atas. Tapi untuk GEMASTIK, framing "impact ranking system" masih sangat sah sebagai data mining — selama problem formulation-nya jelas.

---

#### 📊 Rubrik Scoring

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 17 | 17 | 19 | 16 | 17 | **86** |

**Catatan:** Compute paling rendah di antara semua topik — bisa dikerjakan tanpa GPU. Namun label scarcity (gempa besar jarang) jadi tantangan untuk buktikan robustness.

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber |
|------|--------|
| Katalog gempa (magnitudo, kedalaman, lokasi, waktu) | BMKG |
| Historical damage reports | BNPB DIBI |
| Buildings, roads, health facilities | OpenStreetMap |
| Populasi per desa/kecamatan | BPS |
| Topografi / soil type (liquefaction risk) | Copernicus / DEMNAS |

**Preprocessing:**
1. **Define impact target** — affected population, building damage proxy, or multi-class severity
2. **Exposure layer construction** — building count, road network density, facility count per district
3. **Graph** — district connectivity + travel time to hospitals
4. **Scenario backtests** — simulate historical earthquakes dan compare predicted impact vs actual reports

---

#### 🧠 Modeling Stack

| Stage | Model |
|-------|-------|
| **Baseline** | Rule-based impact index = f(magnitudo, depth, exposure proxies) |
| **Branch B: Tabular** | LightGBM/XGBoost: fitur gempa + exposure → predicted damage severity |
| **Branch C: Graph + Travel Time** | GNN over district graph + Dijkstra travel time to facilities |
| **Output** | Impact rank per district + uncertainty bands + critical asset priority |

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| NDCG@K, Recall@Top-K | Ranking quality of impacted districts |
| MAE on affected population | Impact magnitude accuracy |
| Scenario backtests | On historical earthquake events |
| Ablation | Rule-based vs learned, with/without graph component |

---

### 🥉 Rank 11: JudolFlow-X

**Score: 87/100** | **Kategori: Cyber/Keamanan Digital** | **Risiko Eksekusi: Tinggi**

> **Judul Resmi:**
> *JudolFlow-X: Deteksi dan Klasterisasi Ekosistem Promosi Judi Online Berbasis NLP, Retrieval-Reranking, dan Graph Mining*

---

#### 🎰 Problem Statement

Perjudian online (judol) telah menjadi epidemi digital di Indonesia. Promosi judol menyebar melalui komentar media sosial, Telegram, WhatsApp, website, dan QRIS. Penegakan hukum sulit karena pelaku menggunakan akun-akun siluman, domain berganti, dan pembayaran menggunakan rekening temporer.

JudolFlow-X menjawab: **"bagaimana mendeteksi dan mengelompokkan jaringan promosi judi online secara otomatis berdasarkan teks, URL, entity linkage, dan pola graf?"**

**Ini yang paling "latest-tech"** — retrieval + reranker + GNN + hard-example mining. Tapi juga yang **paling riskan** — data ethics, labeling, dan evaluation bisa messy.

---

#### 📊 Rubrik Scoring

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 19 | 20 | 18 | 15 | 15 | **87** |

| Kriteria | Score | Justifikasi |
|----------|:-----:|-------------|
| **Keaslian** | 19/20 | Sangat distinctive — jarang ada tim GEMASTIK yang berani ambil topik sekompleks ini. |
| **Kebaruan** | 20/20 | BGE-M3, Qwen3 Embedding, CrossEncoder, Heterogeneous GNN — semua latest ingredient. |
| **Manfaat** | 18/20 | Judol isu nasional yang sangat hot. Tapi benefit lebih bersifat penegakan hukum, bukan dampak langsung ke publik seperti DBD. |
| **Kejelasan** | 15/20 | Pipeline 6 stage sulit dijelaskan secara ringkas. Butuh effort besar untuk bikin laporan yang jelas. |
| **Kelengkapan** | 15/20 | Labeling, graph construction, evaluation — semua bisa messy dan incomplete. |

---

#### 🗃️ Data & Preprocessing Pipeline

**Data Sources:**

| Data | Sumber | Keterangan |
|------|--------|------------|
| Comments/posts | Scraping terbatas platform publik | Etika: hanya dari platform publik |
| URLs | Ekstraksi dari komentar | Deteksi domain judi known list |
| Telegram handles | Regex dari teks | Identifikasi channel/akun |
| QRIS / payment aliases | OCR + regex | Dari gambar screenshot (optional) |
| Public blocklists | Open-source intelligence (OSINT) | Daftar domain/akun terindikasi |

**Preprocessing:**
1. Slang normalization — "gacor", "maxwin", "bonanza" → canonical terms
2. URL canonicalization — resolve shortlinks
3. Entity extraction — domain, handle, phone, payment alias
4. Graph construction — nodes: user, domain, handle, QRIS alias; edges: co-occurrence, referral, payment link
5. Weak labeling — rule-based label dari keyword matches + OSINT lists → diperiksa manual sample

---

#### 🧠 Modeling Stack (6 Stage)

| Stage | Teknik | Detail |
|-------|--------|--------|
| **1. Retrieval** | Qwen3 Embedding / BGE-M3 | Cari konten semantik mirip dengan contoh judol |
| **2. Classification** | Fine-tuned IndoBERT / LightGBM | Classify konten sebagai judol / non-judol |
| **3. Reranking** | CrossEncoder | Improve precision pada borderline samples |
| **4. Entity Extraction** | Regex + NER (Qwen3) | Domain, handle, phone, QRIS alias |
| **5. Graph Mining** | Heterogeneous GNN / Community Detection | Cluster detection, link prediction, anomaly scoring |
| **6. Hard-example Mining** | Active learning loop | False positives/negatives → relabel → retrain |

**Fusion:** Text risk + entity risk + graph-centrality risk + community risk + novelty score → final risk score.

---

#### 📐 Evaluation Strategy

| Metrik | Tujuan |
|--------|--------|
| Macro F1 | For suspicious content classification |
| PR-AUC | Imbalanced label |
| Entity extraction F1 | Precision/recall per entity type |
| Cluster purity / NMI | Graph clustering quality |
| Precision@K | For suspicious cluster ranking |
| Case study | Qualitative evaluation on top clusters |

---

#### 👥 Role Split

| Member | Role |
|--------|------|
| **M1 — Data Lead** | Scraping + preprocessing + entity extraction + weak labeling |
| **M2 — Model Lead** | Embeddings + classifier + reranker + LLM prompting |
| **M3 — Graph Lead** | Graph construction + community detection + evaluation + report |

---

#### 🏆 Why It Wins (If Executed Well)

1. **Tech wow factor tertinggi** — terlihat seperti mini KDD paper
2. **Kebaruan metode 20/20** — sangat jarang ada tim GEMASTIK yang pakai retrieval + reranker + GNN
3. **Social impact kuat** — judol adalah isu nasional yang sangat visible
4. **Multi-stage pipeline** — persis seperti pola pemenang internasional (OAG AQA, Meta KDD)

#### ⚠️ Risiko & Mitigasi

| Risiko | Severity | Mitigasi |
|--------|:--------:|----------|
| Data ethics & legal (scraping) | 🔴 HIGH | Hanya gunakan data publik; hindari data pribadi; konsultasi dosen; explicit ethics section |
| Labeling quality | 🔴 HIGH | Weak supervision + human validation untuk 200-500 samples; bootstrapping |
| Pipeline complexity | 🔴 HIGH | Mulai dengan 3 stage (classifier → entity → graph), tambah reranker & hard-mining jika waktu cukup |
| Evaluation messy | 🟡 MEDIUM | Clear metric hierarchy; case-study evaluation wajib |

---

### Rank 12: AirGuard Sekolah

**Score: 85/100** | **Kategori: Lingkungan & Kesehatan** | **Risiko Eksekusi: Rendah**

> **Judul Resmi:**
> *AirGuard Sekolah: Prediksi Risiko Paparan PM2.5 Jam Sekolah Berbasis Data Mining*

---

#### 🏫 Problem Statement

Polusi udara (PM2.5) di kota-kota besar Indonesia — terutama Jakarta, Bandung, Surabaya — telah mencapai level yang mengkhawatirkan. Anak sekolah adalah kelompok paling rentan karena menghabiskan 6-8 jam di sekolah saat jam polusi puncak.

AirGuard Sekolah menjawab: **"hari apa dan sekolah mana yang memiliki risiko paparan PM2.5 tertinggi, sehingga bisa merekomendasikan work-from-school, masker, atau pemasangan air purifier?"**

**Topik paling aman** — data dari OpenAQ mudah didapat, compute rendah, mudah ditulis. Tapi:

#### 📊 Rubrik Scoring

| Keaslian (20) | Kebaruan (20) | Manfaat (20) | Kejelasan (20) | Kelengkapan (20) | **Total** |
|:-------------:|:-------------:|:------------:|:--------------:|:----------------:|:---------:|
| 16 | 16 | 18 | 18 | 17 | **85** |

**Kelemahan:** Belum ada yang *baru* — PM2.5 forecasting sudah sangat umum. Kebaruan hanya dari *school-hour exposure framing*.

---

## 4. Comparison Matrix & Trade-offs

### 4.1 Quick Reference — Semua Topik

| Rank | Topik | Score | Data Avail. | Exec. Risk | Compute | Novelty | Visual Story |
|:----:|-------|:-----:|:-----------:|:----------:|:-------:|:-------:|:------------:|
| 1 | **WaterWatch-ID** | **90** | ⭐⭐⭐⭐ | Medium | Moderate-High | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 2 | DengueCast-X | 91 | ⭐⭐⭐⭐ | Medium | Moderate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 3 | **TraceFish-ID** | **91** | ⭐⭐⭐⭐ | Medium-High | Moderate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 4 | PanganShock-X | 91 | ⭐⭐⭐⭐⭐ | **Low** | Low | ⭐⭐⭐ | ⭐⭐⭐ |
| 5 | ApiShield-ID | 91 | ⭐⭐⭐⭐⭐ | Medium | Moderate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 6 | HydroRisk-ID | 89 | ⭐⭐⭐⭐ | Medium | Moderate | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 7 | PadiWatch-X | 88 | ⭐⭐⭐⭐ | Med-High | Mod-High | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 8 | **EduDrop-ID** | **87** | ⭐⭐⭐⭐ | **Low** | **Low** | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 9 | **WasteWise-ID** | **86** | ⭐⭐⭐⭐ | Medium | Low-Mod | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 10 | GempaRank-X | 86 | ⭐⭐⭐ | Medium | **Low** | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 11 | JudolFlow-X | 84 | ⭐⭐⭐ | **High** | Moderate | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 12 | AirGuard Sekolah | 84 | ⭐⭐⭐ | **Low** | **Low** | ⭐⭐ | ⭐⭐⭐ |

### 4.2 Key Trade-offs

| Topik | Main Strength | Main Risk |
|-------|--------------|-----------|
| **WaterWatch-ID** | Multi-modal pipeline (TFT+GAT+ViT); Swasembada Air pillar | Data monitoring KLHK sparse secara temporal |
| **DengueCast-X** | Best balance of impact + novelty + feasibility | Data DBD kabupaten availability varies |
| **TraceFish-ID** | Ekonomi Biru untouched; novelty tertinggi | Label IUU tidak ada (unsupervised problem) |
| **PanganShock-X** | Termudah dieksekusi, laporan termudah ditulis | Bisa terasa biasa tanpa angle kuat |
| **ApiShield-ID** | Data paling melimpah (NASA FIRMS!), story kuat | Hotspot labels noisy |
| **PadiWatch-X** | Multimodal (tabular + RS), food security | Crop calendar alignment butuh domain |
| **EduDrop-ID** | Risiko paling rendah; data Dapodik terstruktur | Akses data sekolah butuh pengajuan |
| **JudolFlow-X** | Paling KDD-style, tech wow factor tinggi | Execution risk tinggi, data ethics issue |
| **GempaRank-X** | Impact darurat sangat tinggi, compute rendah | Rare event -> label scarcity |
| **AirGuard** | Topik paling aman, data OpenAQ mudah | PM2.5 forecasting sudah sangat umum |

### 4.3 Decision Decision Tree (Who Should Pick What)

```
Tim memiliki 8 minggu dan GPU?
├── YA dengan GPU cukup → WaterWatch-ID (multi-modal, TFT+GAT+ViT)
├── YA GPU terbatas → DengueCast-X (TFT+ganti LSTM)
├── TIDAK, GPU ringan → PanganShock-X (safe)
└── TIDAK, tanpa GPU → EduDrop-ID / AirGuard (low compute)

Tim punya remote sensing background?
├── YA → WaterWatch-ID (ViT + Sentinel-2) atau ApiShield-ID (FIRMS)
└── TIDAK → DengueCast-X / PanganShock-X (tabular + time-series)

Tim ingin novelty tertinggi?
├── YA dan berani risk → TraceFish-ID (Trajectory Transformer + GNN)
└── YA tapi mau aman → WaterWatch-ID (multi-modal)

Prioritas mudah eksekusi?
├── YA → EduDrop-ID (data terstruktur, tabular, tanpa GPU)
└── Tidak, mau menang → WaterWatch-ID / DengueCast-X
```

---

## 5. Pipeline Architecture Template

### 5.1 Generic Pipeline untuk Topik Spatiotemporal (WaterWatch / DengueCast / ApiShield)

```mermaid
flowchart LR
    subgraph Data["📊 Data Sources"]
        D1[Sumber A<br/>Tabular/Time-series]
        D2[Sumber B<br/>Weather/Climate]
        D3[Sumber C<br/>Geospatial/OSM]
        D4[Sumber D<br/>Text/Satelit]
    end

    subgraph Preprocess["🧹 Preprocessing"]
        P1[Aggregation<br/>& Cleaning]
        P2[Feature<br/>Engineering]
        P3[Train/Val/Test<br/>Split]
    end

    subgraph Models["🤖 Modeling Stack"]
        M1[Branch A<br/>Tabular Booster<br/>LightGBM/CatBoost]
        M2[Branch B<br/>Temporal Deep<br/>TFT/ConvLSTM]
        M3[Branch C<br/>Graph Neural Net<br/>GraphSAGE/GAT]
        M4[Optional<br/>Text/NLP Branch]
    end

    subgraph Fusion["🔗 Fusion & Post-process"]
        F1[Weighted<br/>Ensemble]
        F2[Calibration<br/>Platt Scaling]
        F3[Threshold<br/>Tuning]
    end

    subgraph Output["📋 Output"]
        O1[Ranked Priority<br/>List]
        O2[Risk Score<br/>+ Uncertainty]
    end

    subgraph Metrics["📐 Evaluation"]
        E1[PR-AUC]
        E2[Recall@Top-K]
        E3[F1 / MAE]
        E4[Calibration<br/>Error]
    end

    Data --> Preprocess --> Models --> Fusion --> Output
    Output --> Metrics
```

### 5.2 Pipeline per Topik

| Topik | Data Sources | Modeling Branches | Output | Khas |
|-------|-------------|-------------------|--------|------|
| **WaterWatch-ID** | KLHK + BMKG + Sentinel-2 + OSM | TFT + GAT + ViT + CatBoost | Ranked DAS priority list | Multi-modal (time + graph + vision) |
| **DengueCast-X** | Kemenkes + BMKG + BPS + OSM | Tabular (CatBoost) + TFT + GNN + News | Ranked district intervention list | Spatiotemporal + public health |
| **TraceFish-ID** | GFW KKP + BMKG + Pelabuhan | Trajectory Transformer + XGBoost + GNN | IUU risk rank per kapal | Trajectory + graph anomaly |
| **PanganShock-X** | PIHPS + BMKG + BPS + News | Prophet + Tabular (LightGBM) + TFT + Text | Ranked region-commodity alert | Dual objective (reg + class) |
| **ApiShield-ID** | NASA FIRMS + BMKG + Sentinel + OSM | Tabular (LightGBM) + ConvLSTM + GNN | Ranked village patrol list | Remote sensing + hotspot |
| **HydroRisk-ID** | BNPB + BMKG + OSM + DEMNAS | LightGBM + ConvLSTM + Graph exposure | Flood severity rank | Multi-hazard (flood+slide) |
| **PadiWatch-X** | BPS + BMKG + Sentinel-2 | Tabular (LightGBM) + 3D CNN + Multimodal fusion | Anomaly map per season | Multimodal (tabular + RS) |
| **EduDrop-ID** | Dapodik + BPS + OSM | XGBoost + Mixed Effects Model + K-Prototypes | School risk priority list | Hierarchical + clustering |
| **WasteWise-ID** | SIPSN KLHK + BMKG + BPS + OSM | N-BEATS + LightGBM + GNN + ILP routing | Waste forecast + route opt | Forecasting + optimization |
| **GempaRank-X** | BMKG + BNPB + OSM + BPS | Rule-based + LightGBM + GNN + Travel-time | First-hour triage dashboard | Post-event nowcasting |
| **JudolFlow-X** | Scraping + OSINT + blocklists | Embedding + Classifier + Reranker + GNN | Risk cluster score | 6-stage retrieval + graph |
| **AirGuard Sekolah** | OpenAQ + BMKG + BPS | Prophet + LightGBM + LSTM | School-day risk alert | PM2.5 forecasting + exposure |

### 5.3 Struktur Experiment Matrix (Wajib untuk Technical Report)

Setiap topik WAJIB memiliki baseline ladder. Format:

| Level | Model | PR-AUC | Recall@Top-10% | Catatan |
|:-----:|-------|:------:|:--------------:|---------|
| 1 | Naive baseline (e.g., mean/most-frequent) | 0.50 | 0.10 | Built-in scikit-learn DummyClassifier |
| 2 | Simple time-series (Prophet/SARIMA) | 0.62 | 0.25 | Hanya untuk temporal features |
| 3 | Strong tabular (LightGBM/CatBoost) | 0.74 | 0.38 | Full feature set |
| 4 | Advanced deep (TFT/ConvLSTM/GNN) | 0.81 | 0.45 | Masing-masing branch |
| 5 | Full pipeline (fusion + calibration) | **0.85** | **0.52** | **Proposed method** |
| 6 | Ablation: -GNN | 0.82 | 0.48 | Kontribusi GNN |
| 7 | Ablation: -TFT | 0.80 | 0.46 | Kontribusi temporal deep |
| 8 | Ablation: -text | 0.83 | 0.50 | Kontribusi text signals |

---

## 6. Decision Checklist

### 6.1 Screening Questions

| Pertanyaan | Pilihan (centang salah satu) |
|------------|------------------------------|
| **Data availability** — Dataset primer bisa didapat dalam **1-2 minggu**? | [✅] Ya — topik dengan data scoring ⭐⭐⭐⭐+ / [❌] Tidak |
| **Tim skill match** — Ada anggota yang bisa handle modeling yang direncanakan? | [✅] Ya / [❌] Tidak |
| **Compute adequacy** — Laptop/GPU cukup untuk training model? | [✅] Ya / [❌] Tidak |
| **Story clarity** — Problem statement bisa dijelaskan dalam **1 kalimat**? | [✅] Ya / [❌] Tidak |
| **Tim enthusiasm** — Semua anggota **excited** dengan topik ini? | [✅] Ya / [❌] Tidak |
| **Novelty check** — Apakah ada publikasi/makalah GEMASTIK sebelumnya yang identik? | [✅] Tidak ada / [❌] Ada — perlu differentiator |
| **8-week feasibility** — Pipeline bisa diselesaikan dalam 8 minggu? | [✅] Ya / [❌] Tidak — perlu scope-down |

### 6.2 Final Decision Record

```
================================================================
                KEPUTUSAN FINAL TOPIK GEMASTIK 2025
================================================================

Topik yang dipilih:      _________________________________________

Tanggal keputusan:        __/__/2026

Diputuskan oleh:          _________________________________________

Alasan pemilihan:
1. _____________________________________________________________
2. _____________________________________________________________
3. _____________________________________________________________
4. _____________________________________________________________

Tim member & role:
- Member 1 (__________):  _______________________________________
- Member 2 (__________):  _______________________________________
- Member 3 (__________):  _______________________________________

Backup plan (jika topik utama gagal di minggu 1-2):

   Topik cadangan:        _________________________________________

   Trigger fallback:      [ ] Data tidak tersedia
                          [ ] Compute tidak mencukupi
                          [ ] Lainnya: ________________________

================================================================
```

---

## 7. Appendix: Sumber Dataset per Topik

### 7.1 Data Portal Umum (Akses Terbuka)

| Sumber | URL | Tipe Data | Cocok untuk Topik |
|--------|-----|-----------|-------------------|
| **BPS API** | https://webapi.bps.go.id/ | Statistik daerah, demografi, ekonomi, harga | Semua topik kecuali TraceFish |
| **BMKG Iklim** | https://iklim.bmkg.go.id/ | Cuaca, iklim, SPI, suhu | WaterWatch, DengueCast, ApiShield, PadiWatch, HydroRisk |
| **KLHK SIPSN** | https://sipsn.menlhk.go.id/ | Timbulan sampah per kab/kota | **WasteWise-ID** (esensial!) |
| **KLHK Data** | https://data.go.id/ | Kualitas air, status mutu, DAS | **WaterWatch-ID** (esensial!) |
| **Global Fishing Watch** | https://globalfishingwatch.org/ | AIS trajectory, fishing activity | **TraceFish-ID** (esensial!) |
| **Kemendikdasmen** | https://data.kemendikdasmen.go.id/ | Dapodik, angka putus sekolah, fasilitas | **EduDrop-ID** (esensial!) |
| **BNPB DIBI** | https://data.bnpb.go.id/ | Bencana historis, dampak | HydroRisk, ApiShield, GempaRank |
| **NASA FIRMS** | https://firms.modaps.eosdis.nasa.gov/ | Hotspot real-time (MODIS/VIIRS) | **ApiShield-ID** (esensial!) |
| **Copernicus Data Space** | https://dataspace.copernicus.eu/ | Citra Sentinel (optik, radar) | WaterWatch, ApiShield, PadiWatch, HydroRisk |
| **OpenStreetMap** | https://download.geofabrik.de/ | Jalan, bangunan, boundary, sungai | Semua topik (geospatial) |
| **OpenAQ** | https://openaq.org/ | PM2.5, PM10, O3, NO2 real-time | AirGuard |
| **Google Earth Engine** | https://earthengine.google.com/ | Platform processing citra satelit | WaterWatch, PadiWatch, ApiShield |

### 7.2 Dataset Spesifik per Topik

| Rank | Topik | Data Utama | Sumber Primer |
|:----:|-------|-----------|---------------|
| 1 | **WaterWatch-ID** | Parameter DO/BOD/COD; NDWI Sentinel-2; graph DAS | KLHK; Sentinel-2/GEE; BBWS PUPR |
| 2 | **DengueCast-X** | Kasus DBD per kabupaten/minggu; cuaca; demografi | Kemenkes / Data.go.id; BMKG; BPS |
| 3 | **TraceFish-ID** | AIS trajectory; VMS; ZEEI boundary; data pelabuhan | Global Fishing Watch API; KKP; BIG |
| 4 | **PanganShock-X** | Harga harian 50+ komoditas; inflasi daerah; berita | PIHPS BPS; BPS API; Google News |
| 5 | **ApiShield-ID** | Hotspot FIRMS; cuaca BMKG; NDVI Sentinel; OSM | NASA FIRMS; BMKG; Copernicus; OSM |
| 6 | **HydroRisk-ID** | Banjir/longsor historis; curah hujan; DEM; DAS | BNPB; BMKG; DEMNAS; KLHK |
| 7 | **PadiWatch-X** | Hasil panen (KSA); iklim; NDVI time-series | BPS; BMKG; Sentinel-2/GEE |
| 8 | **EduDrop-ID** | Data Dapodik; kemiskinan BPS; fasilitas sekolah | Kemendikdasmen; BPS; OSM |
| 9 | **WasteWise-ID** | Timbulan sampah SIPSN; demografi; cuaca | SIPSN KLHK; BPS; BMKG |
| 10 | **GempaRank-X** | Katalog gempa; OSM; demografi BPS | BMKG; OSM; BPS |
| 11 | **JudolFlow-X** | Komentar/domain/handle; OSINT blocklists | Scraping (etis); data publik |
| 12 | **AirGuard** | PM2.5 sensor; cuaca BMKG; lokasi sekolah | OpenAQ; BMKG; OSM |

---

## 🏁 Final Note

**Total topik dianalisis:** 12
**Rentang score:** 84/100 — 91/100
**Rekomendasi untuk tim:
```
1. WaterWatch-ID   → jika tim mau multi-modal + swasembada air (Kemandirian Bangsa pillar)
2. DengueCast-X   → jika data DBD available & mau win chance terbaik
3. TraceFish-ID   → jika mau novelty tertinggi (Trajectory Transformer + GNN)
4. PanganShock-X  → jika mau eksekusi paling aman & laporan terbaik
5. EduDrop-ID     → jika mau risiko terendah tanpa GPU
```
5. PadiWatch-X    → if have remote sensing background
```

**Setelah tim memutuskan topik final (via §6), langkah selanjutnya:**

| Minggu | Aktivitas | Deliverable |
|:------:|-----------|-------------|
| 1-2 | Validasi dataset, scraping, EDA | Dataset card, EDA notebook |
| 3-4 | Baseline ladder (level 1-3) | Baseline results table |
| 5-6 | Advanced methods + fusion | Full pipeline results |
| 7 | Ablation + error analysis + SHAP | Ablation table, error atlas |
| 8 | Report writing + PPT + rehearsal | Technical report PDF, code, PPT |

---

*Dokumen ini dapat diperbarui setiap kali ada keputusan baru atau informasi tambahan.*
