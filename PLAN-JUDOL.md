# PLAN -- GEMASTIK XVIII Data Mining 2025

> **Tujuan:** Dokumen ini berisi seluruh topik yang telah direkomendasikan dan dievaluasi untuk Technical Report GEMASTIK Data Mining 2025, lengkap dengan _problem statement_ mendalam, _scoring_ per rubrik, _pipeline design_, _evaluation strategy_, serta analisis risiko dan mitigasi.
>
> **Update terakhir:** 17 Mei 2026
>
> **Status:** Final -- 8 topik CS-compatible siap dipilih. Gunakan Executive Summary di bawah untuk keputusan cepat, lalu [Decision Checklist](#9-decision-checklist) untuk finalisasi.

---

## 0. Executive Summary -- Quick Decision Dashboard

### Top 3 Recommendations

| | #1 **DengueCast-X** | #2 **JudolFlow-X** |
|---|-----------------|-----------------|-----------------|
| Score | **91/100** | **84/100** |
| Pilar Kemandirian Bangsa | Kesehatan Publik | Keamanan Digital |
| Mengapa | Multi-branch pipeline = winner pattern; highest impact | NLP + Graph = core CS; KDD-style |
| Butuh | GPU, data DBD per kabupaten | GPU optional; scraping etis |
| Risiko | Data DBD availability | Execution risk HIGH; data ethics |
| Skip Jika | Data DBD unavailable | Tidak siap handle ethical issues |

### Kemandirian Bangsa Pillar Map

| Pilar Kemandirian Bangsa | Topik Tersedia | Rekomendasi |
|--------------------------|---------------|-------------|
| Kesehatan Publik | DengueCast-X | DengueCast-X |
| Keamanan Digital | JudolFlow-X | *(high risk)* |

### Pick Your Topic in 30 Seconds

| Profil Tim | Top Pick | Runner-up | Kenapa |
|------------|----------|-----------|--------|
| Ingin winner pattern terkuat | **DengueCast-X** | JudolFlow-X | Multi-branch TFT+GNN+CatBoost; PR-AUC metrics |
| Ingin novelty + NLP/Graph | **JudolFlow-X** | DengueCast-X | 6-stage pipeline; retrieval + reranker + GNN |

### Score Distribution

```
91     DengueCast-X
84     JudolFlow-X
```

---

## 1. How to Use This Document

1. **Baca Executive Summary (di atas)** -- tentukan profil tim, lihat rekomendasi langsung
2. **Scan Topic Cards (Section 5)** -- bandingkan 2-3 topik yang cocok dalam 30 detik per card
3. **Gunakan Decision Engine (Section 7)** -- validasi pilihan berdasarkan 3 dimensi
4. **Finalisasi dengan Decision Checklist (Section 9)** -- pastikan semua kriteria terpenuhi
5. **Akses Full Detail (Appendix/Section 10)** -- hanya jika butuh informasi teknis untuk writing phase

---

## 2. Daftar Isi

1. [Executive Summary](#-executive-summary--quick-decision-dashboard)
2. [How to Use This Document](#1-how-to-use-this-document)
3. [Aturan & Rubrik](#3-aturan--rubrik)
4. [Pola Pemenang Historis](#4-pola-pemenang-historis)
5. [Topic Cards (2 Topik)](#5-topic-cards-3-topik)
    - [Rank 1: DengueCast-X](#rank-1-denguecast-x)
    - [Rank 2: JudolFlow-X](#rank-3-judolflow-x)
6. [Comparison Matrix & Trade-offs](#-comparison-matrix--trade-offs)
7. [Decision Engine](#7-decision-engine)
8. [Pipeline Architecture](#8-pipeline-architecture)
9. [Decision Checklist](#9-decision-checklist)
10. [Appendix: Full Detail per Topik](#10-appendix-full-detail-per-topik)

---

## 3. Ringkasan Aturan & Rubrik

### 3.1 Ketentuan Technical Report (Babak Penyisihan)

Sumber: _Panduan GEMASTIK 2025 — Divisi Penambangan Data_

**Struktur Wajib Technical Report:**

| Section          | Konten Wajib                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Judul            | Mencerminkan isi, sesuai tema "Penambangan Data untuk Peningkatan TIK menuju Kemandirian Bangsa" |
| Abstrak          | Ringkasan penelitian: latar belakang, metode, hasil utama                                        |
| Pendahuluan      | Latar belakang, tujuan, manfaat, batasan                                                         |
| Kajian Terkait   | Related work, state-of-the-art                                                                   |
| Solusi Usulan    | Deskripsi solusi, dataset, metode, perbedaan dengan solusi sebelumnya, metrik evaluasi           |
| Hasil Eksperimen | Baseline ladder, eksperimen, pengujian                                                           |
| Analisis Hasil   | Interpretasi, error analysis, ablation study                                                     |
| Kesimpulan       | Temuan utama, saran, implikasi                                                                   |

**Aturan Tambahan:**

- Format: PDF, max 10 MB
- Penamaan: `GEMASTIK XVIII Penambangan Data - <ID Tim> - <Nama Tim> - <Judul>.pdf`
- WAJIB orisinal (bukan GenAI murni), belum pernah dipublikasikan termasuk untuk kompetisi lain
- Tools / library / framework / Generative AI **diperbolehkan** sebagai alat bantu

### 3.2 Rubrik Penilaian Babak Penyisihan

| No  | Kriteria                        | Bobot | Indikator Penilaian                                                                          |
| --- | ------------------------------- | :---: | -------------------------------------------------------------------------------------------- |
| 1   | **Keaslian** (plagiarism check) |  20%  | Uji plagiarisme; ide orisinal; bukan saduran makalah lain                                    |
| 2   | **Kebaruan dataset / metode**   |  20%  | Kombinasi dataset baru; atau pendekatan/metode baru; atau aplikasi baru dari metode existing |
| 3   | **Manfaat**                     |  20%  | Dampak sosial yang jelas; potensi implementasi di Indonesia                                  |
| 4   | **Kejelasan tulisan**           |  20%  | Mudah dipahami; terstruktur; bahasa jelas dan ilmiah                                         |
| 5   | **Kelengkapan laporan**         |  20%  | Semua bagian terisi; eksperimen cukup; analisis mendalam                                     |

### 3.3 Babak Final

| Komponen                 | Bobot | Keterangan                            |
| ------------------------ | :---: | ------------------------------------- |
| Nilai babak penyisihan   |  20%  | Makalah yang sudah dikumpulkan        |
| Skor kinerja leaderboard |  30%  | Performansi model pada hidden dataset |
| Ketepatan metode         |  25%  | Kesesuaian metode dengan problem      |
| Presentasi               |  25%  | PPT + presentasi onsite + Q&A         |

**Format Final:**
Hidden dataset → 5 jam build model → dokumentasi PPT → presentasi onsite

> **Implikasi Strategis:** 70% nilai final berasal dari non-leaderboard. Paper-first strategy sangat penting. Pilihlah metode yang _defensible_ dan _interpretable_, bukan sekadar akurat.

---

## 4. Pola Pemenang Historis

### 4.1 Rekam Jejak Pemenang GEMASTIK Data Mining

| Tahun            | Peringkat | Tim                 | Institusi | Topik Preliminary                                 |
| ---------------- | :-------: | ------------------- | --------- | ------------------------------------------------- |
| **2021** (XIV)   |    🥇     | **ILY**             | ITB       | Deteksi depresi dari Twitter + chatbot outreach   |
| **2023** (XVI)   |    🥇     | **Magnus**          | ITB       | IoT cybersecurity — network log attack prediction |
| **2023** (XVI)   |    🥉     | Three Wise Monkey   | ITB       | Smart energy management                           |
| **2024** (XVII)  |    🥇     | **Three Outliers**  | UI        | _(tidak terdisclose publik)_                      |
| **2024** (XVII)  |    🥈     | Three Layers        | UI        | _(tidak terdisclose publik)_                      |
| **2024** (XVII)  |    🥉     | Barudak Bojongsoang | Tel-U     | _(tidak terdisclose publik)_                      |
| **2025** (XVIII) |    🥇     | **Three Vectors**   | UI        | _(tidak terdisclose publik)_                      |
| **2025** (XVIII) |    🥈     | Suika               | UI        | _(tidak terdisclose publik)_                      |

**Pola Institusi Pemenang:** Didominasi UI (3 medali 2024-2025), ITB (3 medali 2021-2023), dan Telkom University.

### 4.2 Pola yang Terulang — Lessons Learned

| #   | Prinsip                                   | Penjelasan                                                                      | Contoh Empiris                                                          |
| --- | ----------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1   | **Pipeline > Single Model**               | Pemenang membangun multi-branch pipeline, bukan mengandalkan satu model         | Magnus (2023): feature engineering on logs + rare class handling        |
| 2   | **Metric-aware design**                   | Optimasi untuk metrik yang tepat (PR-AUC, Recall@K), bukan accuracy             | ILY (2021): NLP dengan framing deteksi depresi, bukan generic sentiment |
| 3   | **Public impact + data availability**     | Topik pemenang selalu: masalah publik jelas + data bisa didapat                 | ILY: Twitter data publik + masalah kesehatan mental relevan             |
| 4   | **Judgeable robustness > flashy novelty** | Metode yang interpretable, reproducible, dan defensible di Q&A                  | Magnus: domain-aware engineering, bukan model black-box                 |
| 5   | **Paper-first strategy**                  | Preliminary adalah kompetisi technical report — kualitas tulisan sangat penting | 20/30/25/25 scoring → 70% dari non-leaderboard                          |
| 6   | **Domain grounding**                      | Bukan sekadar aplikasi ML generic, tapi domain knowledge                        | ILY: konsultasi psikologi; Magnus: network security domain              |
| 7   | **Hidden-case readiness**                 | Final 5 jam = harus deliver baseline + improvement + slides                     | Latih simulasi 5 jam minimal 2× sebelum final                           |

---

## 5. Topic Cards (2 Topik)

---

### Rank 1: DengueCast-X

|                       Score                        | Kategori  | Pilar K.B.       | Risk | GPU |   Data   | **Best For:**                       |
| :------------------------------------------------: | --------- | ---------------- | :--: | :-: | :------: | ----------------------------------- |
|                       91/100                       | Kesehatan | Kesehatan Publik | Med  | Yes | ⭐⭐⭐⭐ | Tim yang ingin win chance tertinggi |
| **Skip If:** Data DBD per kabupaten tidak tersedia |

> _DengueCast-X: Prediksi Risiko Kejadian DBD Berbasis Spatiotemporal Data Mining untuk Prioritas Intervensi Wilayah_

#### Problem

DBD adalah beban kesehatan masyarakat terbesar di Indonesia dengan pola musiman. DengueCast-X menjawab: **"district mana yang harus diintervensi sebelum wabah melonjak?"** -- ranking district intervention priority untuk fogging, larvasida, dan kesiapsiagaan RS.

#### Pipeline

| Branch        | Model                     | Purpose                                                       |
| ------------- | ------------------------- | ------------------------------------------------------------- |
| A: Tabular    | CatBoost / LightGBM       | Lag features + class weighting + interaction terms            |
| B: Temporal   | TFT                       | Multi-horizon forecasting (2-4 week); interpretable attention |
| C: Graph      | GraphSAGE / GAT           | Spillover antar district via adjacency graph                  |
| D: Text (opt) | Qwen3 / BGE-M3            | News embedding -> district-level risk signal                  |
| **Fusion**    | Weighted stacking + Platt | Calibrated risk rank per district-week                        |

Baseline: SARIMA/Prophet -> LightGBM -> TFT -> **Full fusion** | Ablations: -GNN, -TFT, -text

#### Rubrik: A:18 | N:19 | M:20 | J:17 | K:17 = **91/100**

#### Why Choose This

1. **Manfaat publik langsung tertinggi** -- DBD masalah kesehatan paling terlihat di Indonesia
2. **Multi-view pipeline = winner pattern** -- 3-4 branch + fusion persis seperti pola pemenang GEMASTIK
3. **Explainability built-in** -- SHAP + TFT attention = defensible di Q&A juri

#### Top Risks

1. Data DBD kabupaten tidak lengkap (30%) -- fallback ke 5-10 sentinel cities; atau provinsi-level
2. TFT/GNN butuh GPU (40%) -- GNN ganti spatial lag features; TFT ganti LSTM/GRU
3. Temporal overfitting / distribution shift (50%) -- forward-chaining validation wajib; walk-forward CV

#### M1: Data Eng (Kemenkes, BMKG, BPS, graph adjacency) | M2: Model (CatBoost, TFT, GNN, fusion) | M3: Eval (metrics, ablation, SHAP, report writing)

[Full detail ->](#appendix-a-denguecast-x)

---


### Rank 2: JudolFlow-X

|                                     Score                                     | Kategori | Pilar K.B.       |   Risk   |   GPU    |  Data  | **Best For:**                       |
| :---------------------------------------------------------------------------: | -------- | ---------------- | :------: | :------: | :----: | ----------------------------------- |
|                                    84/100                                     | Cyber    | Keamanan Digital | **High** | Optional | ⭐⭐⭐ | Tim expert NLP & graph, berani risk |
| **Skip If:** Tidak ada experience dengan scraping etis / pipeline multi-stage |

> _JudolFlow-X: Deteksi dan Klasterisasi Ekosistem Promosi Judi Online Berbasis NLP, Retrieval-Reranking, dan Graph Mining_

#### Problem

Judol adalah epidemi digital di Indonesia. Promosi menyebar via komentar media sosial, Telegram, QRIS. JudolFlow-X menjawab: **"bagaimana mendeteksi dan mengelompokkan jaringan promosi judi online?"** -- pipeline 6-stage retrieval + classifier + reranker + graph mining.

#### Pipeline

| Stage                | Technique              | Purpose                                   |
| -------------------- | ---------------------- | ----------------------------------------- |
| 1. Retrieval         | Qwen3 / BGE-M3         | Cari konten semantik mirip contoh judol   |
| 2. Classification    | IndoBERT / LightGBM    | Classify konten sebagai judol/non-judol   |
| 3. Reranking         | CrossEncoder           | Improve precision pada borderline samples |
| 4. Entity Extraction | Regex + NER            | Domain, handle, phone, QRIS alias         |
| 5. Graph Mining      | Hetero GNN / Community | Cluster detection + link prediction       |
| 6. Hard-mining       | Active learning loop   | FP/FN -> relabel -> retrain               |

Baseline: Keyword rule-based -> Classifier -> **Full pipeline** | Fusion: text + entity + graph + novelty risk scores

#### Rubrik: A:19 | N:20 | M:18 | J:15 | K:15 = **84/100**

#### Why Choose This

1. **Tech wow factor tertinggi** -- terlihat seperti mini KDD paper
2. **Kebaruan 20/20** -- retrieval + reranker + GNN sangat jarang di GEMASTIK
3. **Isu nasional hot** -- judol adalah topik yang sangat visible

#### Top Risks

1. Data ethics & legal (HIGH) -- hanya data publik; hindari data pribadi; ethics section wajib
2. Labeling quality (HIGH) -- weak supervision + 200-500 human validated samples
3. Pipeline 6-stage complexity (HIGH) -- mulai dengan 3 stage, tambah reranker & hard-mining jika waktu cukup

#### M1: Data Eng (scraping, preprocessing, entity extraction, weak labeling) | M2: Model (embeddings, classifier, reranker, LLM) | M3: Graph & Eval (graph construction, community detection, metrics, report)

[Full detail ->](#appendix-b-judolflow-x)

---

## 6. Comparison Matrix & Trade-offs

### 6.1 Quick Reference -- Semua Topik

| Rank | Topik | Score | Pilar K.B. | Risk | GPU | Data | Novelty | Story | Compute |
|:----:|-------|:-----:|------------|:----:|:---:|:----:|:-------:|:-----:|:-------:|
| 1 | DengueCast-X | 91 | Kesehatan Publik | Med | Yes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Moderate |
| 2 | JudolFlow-X | 84 | Keamanan Digital | **High** | Opt | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Moderate |

### 6.2 Key Trade-offs

| Topik | Main Strength | Main Risk |
|-------|--------------|-----------|
| **DengueCast-X** | Best balance impact + novelty + feasibility | Data DBD kabupaten availability varies |
| **JudolFlow-X** | KDD-style; NLP+Graph core CS; tech wow factor | Execution risk tertinggi; data ethics |

## 7. Decision Engine

### A. By Team Capability

```
GPU strength?
├── GPU KUAT
│   ├── DengueCast-X (TFT + GNN + CatBoost)
│   └── JudolFlow-X (retrieval + reranker + GNN) -- HIGH RISK
└── GPU TERBATAS / tanpa GPU
    └── DengueCast-X (LightGBM baseline, GPU optional)
```

### B. By Risk Appetite

| Appetite | Top Pick | Runner-up | Kenapa |
|----------|----------|-----------|--------|
| **Ambitious** (50% success) | JudolFlow-X | DengueCast-X | Pipeline kompleks; data ethics issue |

### C. By Kemandirian Bangsa Pillar

| Prioritas Pilar | Top Pick |
|-----------------|----------|
| Kesehatan Publik | **DengueCast-X** (91) |
| Keamanan Digital | **JudolFlow-X** (84) |

### D. Quick Self-Assessment (3 Questions)

Answer yes/no to narrow down:

| # | Question | If YES | If NO |
|---|----------|--------|-------|
| 2 | Prioritas novelty di atas segalanya? | JudolFlow | Go to Q3 |

## 8. Pipeline Architecture

### Generic Pipeline (DengueCast / JudolFlow)

```mermaid
flowchart LR
    subgraph Data["Data Sources"]
        D1[Tabular / Time-series]
        D2[Weather / Climate]
        D3[Geospatial / OSM]
        D4[Text / Satellite]
    end
    subgraph Preprocess["Preprocessing"]
        P1[Aggregation & Cleaning]
        P2[Feature Engineering]
        P3[Train/Val/Test Split]
    end
    subgraph Models["Modeling Stack"]
        M1[Branch A: Tabular Booster]
        M2[Branch B: Temporal Deep]
        M3[Branch C: Graph Neural Net]
        M4[Optional Text/NLP]
    end
    subgraph Fusion["Fusion & Post-process"]
        F1[Weighted Ensemble]
        F2[Calibration]
        F3[Threshold Tuning]
    end
    subgraph Output["Output"]
        O1[Ranked Priority List]
        O2[Risk Score + Uncertainty]
    end
    subgraph Metrics["Evaluation"]
        E1[PR-AUC]
        E2[Recall@Top-K]
        E3[F1 / MAE]
    end
    Data --> Preprocess --> Models --> Fusion --> Output
    Output --> Metrics
```

### Pipeline per Topik

| Topik | Data Sources | Modeling Branches | Output | Khas |
|-------|-------------|-------------------|--------|------|
| **DengueCast-X** | Kemenkes + BMKG + BPS + OSM | CatBoost + TFT + GNN + News | Ranked district intervention list | Spatiotemporal + public health |
| **JudolFlow-X** | Scraping + OSINT + blocklists | Embedding + Classifier + Reranker + GNN | Risk cluster score | 6-stage retrieval + graph |

### Experiment Matrix (Wajib untuk Technical Report)

Setiap topik WAJIB memiliki baseline ladder dengan format:

| Level | Model                                    | Target PR-AUC | Recall@Top-10% | Notes                 |
| :---: | ---------------------------------------- | :-----------: | :------------: | --------------------- |
|   1   | Naive baseline                           |     0.50      |      0.10      | DummyClassifier       |
|   2   | Simple time-series (Prophet/SARIMA)      |     0.62      |      0.25      | Hanya temporal        |
|   3   | Strong tabular (LightGBM/CatBoost)       |     0.74      |      0.38      | Full feature set      |
|   4   | Advanced deep (TFT/ConvLSTM/GNN)         |     0.81      |      0.45      | Per branch            |
|   5   | **Full pipeline (fusion + calibration)** |   **0.85**    |    **0.52**    | **Proposed**          |
|  6-8  | Ablations: -GNN, -TFT, -text             |   0.80-0.83   |   0.46-0.50    | Kontribusi per branch |

## 9. Decision Checklist

### Screening Questions

| Pertanyaan                                                                          | Pilihan                                                     |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Data availability** -- Dataset primer bisa didapat dalam **1-2 minggu**?          | [✅] Ya -- topik dengan data scoring ⭐⭐⭐⭐+ / [❌] Tidak |
| **Tim skill match** -- Ada anggota yang bisa handle modeling yang direncanakan?     | [✅] Ya / [❌] Tidak                                        |
| **Compute adequacy** -- Laptop/GPU cukup untuk training model?                      | [✅] Ya / [❌] Tidak                                        |
| **Story clarity** -- Problem statement bisa dijelaskan dalam **1 kalimat**?         | [✅] Ya / [❌] Tidak                                        |
| **Tim enthusiasm** -- Semua anggota **excited** dengan topik ini?                   | [✅] Ya / [❌] Tidak                                        |
| **Novelty check** -- Apakah ada publikasi/makalah GEMASTIK sebelumnya yang identik? | [✅] Tidak ada / [❌] Ada -- perlu differentiator           |
| **8-week feasibility** -- Pipeline bisa diselesaikan dalam 8 minggu?                | [✅] Ya / [❌] Tidak -- perlu scope-down                    |

### Final Decision Record

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

Target timeline:
- Week 1-2:   Data collection & preprocessing
- Week 3-4:   Baseline models & initial experiments
- Week 5-6:   Full pipeline & hyperparameter tuning
- Week 7:     Ablation study & evaluation
- Week 8:     Technical report writing & finalization

Checklist final:
[ ] Dataset sudah siap dan terverifikasi
[ ] Baseline ladder lengkap (5 levels)
[ ] Ablation study selesai
[ ] Evaluasi metrik semua terisi
[ ] Technical report draft selesai
[ ] PPT final presentation siap
[ ] Simulasi 5-jam hidden case (min 2x)
```

---

_Dokumen ini dapat diperbarui setiap kali ada keputusan baru atau informasi tambahan._

## 10. Appendix: Full Detail per Topik

### Appendix A: DengueCast-X

**Data Sources:**

| Data                        | Sumber Utama                   | Variabel Kunci                      | Akses                 |
| --------------------------- | ------------------------------ | ----------------------------------- | --------------------- |
| Kasus DBD historis          | Kemenkes / Satu Data Indonesia | Incidence count per district-week   | data.go.id            |
| Iklim & cuaca               | BMKG API                       | Rainfall, temperature, humidity     | iklim.bmkg.go.id      |
| Demografi                   | BPS API                        | Populasi, density, urbanisasi       | webapi.bps.go.id      |
| Geospasial                  | OpenStreetMap                  | District adjacency, elevasi, sungai | download.geofabrik.de |
| Berita kesehatan (optional) | Google News scraping           | Outbreak keywords, sentiment        | RSS/NLP pipeline      |

**Preprocessing:**

1. Aggregasi mingguan -- dari data harian ke level district-week
2. Rolling lag windows -- 1, 2, 4, 8, 12 minggu
3. Normalisasi per-district -- standarisasi mean/std historis
4. Imputasi missing value -- MICE untuk data cuaca tidak lengkap
5. Outlier handling -- IQR method / Isolation Forest
6. Spatial adjacency matrix -- binary adjacency dari boundary sharing OSM
7. Train/val/test split -- forward-chaining temporal

**Full Evaluation:**

| Metrik                         | Tujuan                                            |
| ------------------------------ | ------------------------------------------------- |
| PR-AUC                         | Primary -- ranking quality dengan class imbalance |
| Recall@Top-10% districts       | Operational utility                               |
| Recall@Top-20% districts       | Coverage breadth                                  |
| Temporal backtesting           | Walk-forward multi-season validation              |
| Lead-time gain                 | Warning lead time vs baseline                     |
| Calibration error (ECE)        | Probability calibration quality                   |
| SHAP / attention visualization | Explainability                                    |

---


**Data Sources:**

| Data                            | Sumber Utama   | Variabel Kunci                                 | Akses                   |
| ------------------------------- | -------------- | ---------------------------------------------- | ----------------------- |
| Data pokok pendidikan (Dapodik) | Kemendikdasmen | Siswa, guru, rombel, putus sekolah, akreditasi | dapodik.kemdikbud.go.id |
| Data kemiskinan                 | BPS            | % kemiskinan, PDRB per kapita                  | bps.go.id               |
| Infrastruktur sekolah           | Dapodik + OSM  | Listrik, air, toilet, jarak                    | dapodik + osm.org       |
| Program bantuan                 | Puslapdik      | Penerima BOS, PIP, KIP                         | Data publik             |

**Preprocessing:**

1. School-level aggregation per tahun
2. Target definition -- % putus sekolah per tahun (atau binary threshold)
3. Lag features -- tren 2-3 tahun, delta enrollment, rasio guru/siswa
4. Spatial features -- kemiskinan, akses transportasi per kecamatan
5. Categorical encoding -- provinsi/kabupaten sebagai hierarchical group
6. Train/val/test split -- temporal: train 2020-2022, val 2023, test 2024
7. Imbalance handling -- fokus ke sekolah risiko tinggi

**Full Evaluation:**

| Metrik               | Tujuan                             |
| -------------------- | ---------------------------------- |
| PR-AUC               | Primary -- dropout class minoritas |
| Recall@Top-K sekolah | Operational prioritization         |
| F1-score             | Balanced precision-recall          |
| RMSE                 | Regresi persentase putus sekolah   |
| CV by province       | Generalisasi ke unseen provinces   |

---

### Appendix B: JudolFlow-X

**Data Sources & Preprocessing:**

1. Scraping dari platform publik (medsos, Telegram publik) -- etis, data publik
2. URL canonicalization -- resolve shortlinks
3. Entity extraction -- domain, handle, phone, payment alias
4. Slang normalization -- "gacor", "maxwin", "bonanza"
5. Graph construction -- nodes: user, domain, handle; edges: co-occurrence
6. Weak labeling -- rule-based dari keyword + OSINT lists

**Full Evaluation:**

| Metrik               | Tujuan                            |
| -------------------- | --------------------------------- |
| Macro F1             | Suspicious content classification |
| PR-AUC               | Imbalanced labels                 |
| Entity extraction F1 | Per entity type                   |
| Cluster purity / NMI | Graph clustering quality          |
| Precision@K          | Suspicious cluster ranking        |
| Case study           | Qualitative evaluation            |

---

