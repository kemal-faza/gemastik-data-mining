# PLAN -- GEMASTIK XVIII Data Mining 2025

> **Tujuan:** Dokumen ini berisi seluruh topik yang telah direkomendasikan dan dievaluasi untuk Technical Report GEMASTIK Data Mining 2025, lengkap dengan *problem statement* mendalam, *scoring* per rubrik, *pipeline design*, *evaluation strategy*, serta analisis risiko dan mitigasi.
>
> **Update terakhir:** 17 Mei 2026
>
> **Status:** Final -- 12 topik siap dipilih. Gunakan Executive Summary di bawah untuk keputusan cepat, lalu [Decision Checklist](#6-decision-checklist) untuk finalisasi.

---

## 0. Executive Summary -- Quick Decision Dashboard

### Top 3 Recommendations

| | #1 **WaterWatch-ID** | #2 **DengueCast-X** | #3 **TraceFish-ID** |
|---|-------------------|-----------------|-----------------|
| Score | **90/100** | **91/100** | **91/100** |
| Pilar Kemandirian Bangsa | Swasembada Air | Kesehatan Publik | Ekonomi Biru |
| Mengapa | Best balance novelty + impact; multi-modal pipeline | Proven winner pattern; highest public impact | Highest novelty; untouched domain |
| Butuh | GPU, skill hidrologi/RS | GPU, data DBD per kabupaten | GPU, trajectory ML skill |
| Risiko | Data KLHK sparse | Data DBD availability | Label IUU unsupervised |
| Skip Jika | Tidak punya GPU | Data DBD unavailable | Tidak ada maritime domain |

### Kemandirian Bangsa Pillar Map

| Pilar Kemandirian Bangsa | Topik Tersedia | Rekomendasi |
|--------------------------|---------------|-------------|
| Swasembada Air | **WaterWatch-ID** | WaterWatch-ID |
| Swasembada Pangan | PanganShock-X, PadiWatch-X | PanganShock-X |
| Ekonomi Biru | **TraceFish-ID** | TraceFish-ID |
| Ekonomi Hijau | **WasteWise-ID** | WasteWise-ID |
| Kesehatan Publik | DengueCast-X, AirGuard | DengueCast-X |
| Pendidikan | **EduDrop-ID** | EduDrop-ID |
| Kebencanaan | ApiShield-ID, HydroRisk-ID, GempaRank-X | ApiShield-ID |
| Keamanan Digital | JudolFlow-X | *(advanced only)* |

### Pick Your Topic in 30 Seconds

| Profil Tim | Top Pick | Runner-up | Kenapa |
|------------|----------|-----------|--------|
| GPU kuat, RS skill, mau kompleks | **WaterWatch-ID** | TraceFish-ID | TFT + GAT + ViT multi-branch pipeline |
| GPU terbatas, tabular expert | **EduDrop-ID** | PanganShock-X | XGBoost + Mixed Effects; tanpa GPU |
| Remote sensing expert | **ApiShield-ID** | WaterWatch-ID | FIRMS + Sentinel, visual storytelling |
| Ingin public impact tertinggi | **DengueCast-X** | EduDrop-ID | DBD isu nasional #1, dampak langsung |
| Paling aman, no surprises | **PanganShock-X** | AirGuard | Data PIHPS bersih, pipeline lurus |
| Ingin novelty maksimal | **TraceFish-ID** | JudolFlow-X | Trajectory Transformer belum pernah ada |

### Score Distribution

```
90     WaterWatch-ID
91     DengueCast-X  TraceFish-ID
91     PanganShock-X  ApiShield-ID
89     HydroRisk-ID
88     PadiWatch-X
87     EduDrop-ID
86     WasteWise-ID  GempaRank-X
84     JudolFlow-X  AirGuard
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
5. [Topic Cards (12 Topik)](#-topic-cards-12-topik)
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
6. [Comparison Matrix & Trade-offs](#-comparison-matrix--trade-offs)
7. [Decision Engine](#-decision-engine)
8. [Pipeline Architecture](#-pipeline-architecture)
9. [Decision Checklist](#-decision-checklist)
10. [Appendix: Full Detail per Topik](#appendix-full-detail-per-topik)

---
## 3. Ringkasan Aturan & Rubrik

### 3.1 Ketentuan Technical Report (Babak Penyisihan)

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

### 3.2 Rubrik Penilaian Babak Penyisihan

| No | Kriteria | Bobot | Indikator Penilaian |
|----|----------|:-----:|---------------------|
| 1 | **Keaslian** (plagiarism check) | 20% | Uji plagiarisme; ide orisinal; bukan saduran makalah lain |
| 2 | **Kebaruan dataset / metode** | 20% | Kombinasi dataset baru; atau pendekatan/metode baru; atau aplikasi baru dari metode existing |
| 3 | **Manfaat** | 20% | Dampak sosial yang jelas; potensi implementasi di Indonesia |
| 4 | **Kejelasan tulisan** | 20% | Mudah dipahami; terstruktur; bahasa jelas dan ilmiah |
| 5 | **Kelengkapan laporan** | 20% | Semua bagian terisi; eksperimen cukup; analisis mendalam |

### 3.3 Babak Final

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

## 4. Pola Pemenang Historis

### 4.1 Rekam Jejak Pemenang GEMASTIK Data Mining

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

### 4.2 Pola yang Terulang — Lessons Learned

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

## 5. Topic Cards (12 Topik)

---

### Rank 1: WaterWatch-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 90/100 | Air | Swasembada Air | Med | Yes | ⭐⭐⭐⭐ | Tim multimodal, lingkungan |
| **Skip If:** No GPU, no remote sensing / hidrologi background |

> *WaterWatch-ID: Prediksi Multimodal Water Quality Index Sungai-Sungai Indonesia untuk Ranking Prioritas Restorasi Daerah Aliran Sungai*

#### Problem

59% sungai Indonesia tercemar berat (data KLHK). Monitoring kualitas air bersifat sparse dan reaktif. WaterWatch-ID menjawab: **"segmen DAS mana yang berisiko penurunan kualitas air dalam 1-4 minggu ke depan?"** -- ranking prioritas restorasi untuk KLHK/BBWS.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| A: Temporal | TFT | Multi-horizon forecasting parameter kimia (DO/BOD/COD) |
| B: Graph | GAT | Propagasi polusi hulu-hilir antar segmen DAS |
| C: Vision | ViT / ResNet50 | Klasifikasi kualitas air dari Sentinel-2 NDWI |
| D: Tabular | CatBoost | Baseline dari land use + iklim + demografi |
| **Fusion** | Weighted stacking + Platt scaling | Calibrated WQI risk rank |

Baseline: Mean imputation → Prophet → CatBoost → TFT → **TFT+GAT+ViT full fusion** | Ablations: -GAT, -ViT, -TFT

#### Rubrik: A:18 | N:19 | M:19 | J:17 | K:17 = **90/100**

#### Why Choose This

1. **Swasembada Air = pilar Kemandirian Bangsa untouched** -- belum ada tim GEMASTIK di topik air
2. **Multi-modal pipeline paling variatif** -- time-series + graph + vision + tabular dalam 1 sistem
3. **Data dari KLHK + Sentinel-2 gratis** -- tidak perlu scraping kontroversial

#### Top Risks

1. Data KLHK sparse per titik monitoring (40%) -- fokus ke 5 DAS prioritas (Citarum, Brantas, Bengawan Solo)
2. TFT/GAT/ViT butuh GPU (50%) -- ViT ganti feature extraction GEE offline; TFT -> LSTM
3. Domain hidrologi terbatas (30%) -- konsultasi dosen lingkungan; referensi PP 22/2021

#### M1: Data Eng (KLHK, BMKG, Sentinel-2, graph DAS) | M2: Model (TFT, GAT, ViT, fusion) | M3: Eval (metrics, ablation, spatial consistency)

[Full detail ->](#appendix-waterwatch-id)

---

### Rank 2: DengueCast-X

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 91/100 | Kesehatan | Kesehatan Publik | Med | Yes | ⭐⭐⭐⭐ | Tim yang ingin win chance tertinggi |
| **Skip If:** Data DBD per kabupaten tidak tersedia |

> *DengueCast-X: Prediksi Risiko Kejadian DBD Berbasis Spatiotemporal Data Mining untuk Prioritas Intervensi Wilayah*

#### Problem

DBD adalah beban kesehatan masyarakat terbesar di Indonesia dengan pola musiman. DengueCast-X menjawab: **"district mana yang harus diintervensi sebelum wabah melonjak?"** -- ranking district intervention priority untuk fogging, larvasida, dan kesiapsiagaan RS.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| A: Tabular | CatBoost / LightGBM | Lag features + class weighting + interaction terms |
| B: Temporal | TFT | Multi-horizon forecasting (2-4 week); interpretable attention |
| C: Graph | GraphSAGE / GAT | Spillover antar district via adjacency graph |
| D: Text (opt) | Qwen3 / BGE-M3 | News embedding -> district-level risk signal |
| **Fusion** | Weighted stacking + Platt | Calibrated risk rank per district-week |

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

[Full detail ->](#appendix-denguecast-x)

---

### Rank 3: TraceFish-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 91/100 | Maritim | Ekonomi Biru | Med-High | Yes | ⭐⭐⭐⭐ | Tim ingin novelty tertinggi |
| **Skip If:** Tidak ada maritime domain knowledge / skill trajectory ML |

> *TraceFish-ID: Deteksi Aktivitas IUU Fishing Berbasis Trajectory Data Mining dan Graph Analysis untuk Prioritas Inspeksi Pelabuhan*

#### Problem

IUU fishing merugikan Indonesia Rp 100 triliun/tahun. Kapal asing dan lokal sulit diawasi di perairan 6,4 juta km2. TraceFish-ID menjawab: **"kapal mana yang berisiko IUU fishing dalam 24-48 jam?"** -- ranking prioritas inspeksi untuk KKP/Bakamla.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| A: Trajectory | Trajectory Transformer / t2vec | Sequence embedding dari trajectory AIS -> anomaly score |
| B: Tabular | XGBoost / CatBoost | Speed, turning angle, trip duration, ZEEI proximity |
| C: Graph | RGCN / Hetero GAT | Bipartite graph kapal-pelabuhan untuk network anomaly |
| D: Temporal | LSTM / TFT | Time-series posisi dan kecepatan terhadap waktu |
| **Fusion** | Weighted stacking + threshold | Ensemble anomaly scores -> IUU risk rank |

Baseline: Rule-based (speed + ZEEI) -> Isolation Forest -> XGBoost -> Trajectory TF -> **Full pipeline** | Ablations: -graph, -trajectory, -temporal

#### Rubrik: A:19 | N:20 | M:19 | J:17 | K:16 = **91/100**

#### Why Choose This

1. **Ekonomi Biru = domain GEMASTIK yang belum tersentuh sama sekali**
2. **Novelty metode tertinggi** -- Trajectory Transformer + GNN bipartite untuk fishing anomaly
3. **Data AIS gratis dari Global Fishing Watch** -- dataset publik paling kaya untuk Indonesia

#### Top Risks

1. Label IUU tidak ada, problem unsupervised (80%) -- weak labeling rule-based + GFW fishing flags; framing sebagai anomaly detection
2. AIS data noisy / gap coverage (50%) -- fallback: fokus ke kapal dengan coverage >70% trip
3. Trajectory Transformer butuh skill spesifik (40%) -- branch A bisa diganti LSTM/GRU sederhana

#### M1: Data Eng (GFW API, trajectory cleaning, feature extraction) | M2: Model (Trajectory TF, XGBoost, GNN) | M3: Eval (case study, temporal backtesting, report)

[Full detail ->](#appendix-tracefish-id)

---

### Rank 4: PanganShock-X

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 91/100 | Pangan | Swasembada Pangan | Low | Optional | ⭐⭐⭐⭐⭐ | Tim yang ingin eksekusi paling aman |
| **Skip If:** Ingin novelty tinggi tanpa added text/news branch |

> *PanganShock-X: Prediksi Risiko Lonjakan Harga Pangan Strategis Berbasis Multiview Time-Series Data Mining*

#### Problem

Harga pangan strategis Indonesia sangat volatil, berdampak pada inflasi dan ketahanan pangan. PanganShock-X menjawab: **"komoditas apa di region mana yang berisiko lonjakan harga dalam 7-14 hari?"** -- ranked region-commodity alert untuk Bulog/Pemda.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | Prophet / SARIMA | Seasonal decomposition with holiday effects |
| A: Tabular | LightGBM / CatBoost | Lags + cross-features + holiday flags + commodity embeddings |
| B: Temporal | TFT / N-HiTS / TiDE | Multi-horizon forecasting with exogenous weather |
| C: Text (opt) | Qwen3 / BGE-M3 | Berita pangan -> sentiment/risk indicators |
| **Output** | Dual obj: regression (price) + classification (spike) | Fused spike probability + uncertainty band |

Baseline: Naive -> Prophet -> LightGBM -> TFT+Tabular -> **Full pipeline + calibration**

#### Rubrik: A:17 | N:17 | M:19 | J:19 | K:19 = **91/100**

#### Why Choose This

1. **Eksekusi paling aman** -- data PIHPS paling bersih, baseline mudah, risiko gagal rendah
2. **Kejelasan & kelengkapan laporan tertinggi** -- konsep "lonjakan harga" dipahami semua orang
3. **Dual objective** -- regression + classification = double validation = terlihat rigorous

#### Top Risks

1. Bisa terasa "biasa saja" tanpa angle kuat -- tambahkan uncertainty calibration + spike risk ranking framing
2. Data harga incomplete di beberapa region -- fokus ke 5-10 komoditas strategis + 10 kota besar
3. Overlap dengan tim lain -- diferensiator: multiview + ranking + calibration

#### M1: Data Eng (PIHPS scraping, panel construction, missing value) | M2: Model (Prophet, LightGBM, TFT, dual-objective) | M3: Eval (spike metrics, calibration, ablation per commodity)

[Full detail ->](#appendix-panganshock-x)

---

### Rank 5: ApiShield-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 91/100 | Lingkungan | Kebencanaan | Med | Yes | ⭐⭐⭐⭐⭐ | Tim dengan remote sensing background |
| **Skip If:** Tidak bisa olah data NASA FIRMS / citra satelit |

> *ApiShield-ID: Prediksi Risiko Kebakaran Hutan/Lahan Berbasis Spatiotemporal Data Mining untuk Prioritas Patroli Desa*

#### Problem

Karhutla adalah bencana tahunan di Indonesia dengan kerugian ekonomi dan lingkungan besar. ApiShield-ID menjawab: **"desa mana yang berisiko kebakaran tertinggi dalam 1-7 hari?"** -- ranking prioritas patroli untuk Manggala Agni/BPBD.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | LightGBM | Rainfall deficit + hotspot history + humidity + wind |
| B: Spatiotemporal | ConvLSTM / GRU-D | Grid-based sequence: weather + hotspot 2D field |
| C: Graph | GraphSAGE | Village adjacency + fire propagation graph |
| **Fusion** | Weighted ensemble + calibration | Convert multi-score ke calibrated probability |
| Post-proc | Threshold tuning by region | Threshold berbeda untuk Sumatera vs NTT |

Baseline: LightGBM -> ConvLSTM -> GraphSAGE -> **Fusion** | Spatially-validated cross-region

#### Rubrik: A:18 | N:19 | M:19 | J:18 | K:17 = **91/100**

#### Why Choose This

1. **Data paling melimpah** -- NASA FIRMS real-time + BMKG + Sentinel + OSM
2. **Visual storytelling paling kuat** -- peta sebaran api sangat powerful untuk presentasi
3. **Multi-view pipeline** -- tabular + spatiotemporal + graph = winner pattern

#### Top Risks

1. Hotspot labels noisy (false positive industri) -- filter FIRMS confidence >= 80% + validasi BNPB
2. El Nino anos -> distribution shift -- exclusion period atau domain adaptation
3. Remote sensing storage besar -- Google Earth Engine preprocessing (free tier cukup)

#### M1: Data Eng (FIRMS ingestion, BMKG+OSM, grid aggregation) | M2: Model (LightGBM, ConvLSTM, GNN) | M3: Eval (spatial CV, calibration, maps visualization, report)

[Full detail ->](#appendix-apishield-id)

---

### Rank 6: HydroRisk-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 89/100 | Bencana | Kebencanaan | Med | Optional | ⭐⭐⭐⭐ | Tim dengan background kebencanaan |
| **Skip If:** Ingin topik yang lebih niche / narrower |

> *HydroRisk-ID: Prediksi Risiko Dampak Banjir dan Longsor untuk Prioritas Kesiapsiagaan Wilayah*

#### Problem

Banjir dan longsor adalah bencana paling sering di Indonesia. HydroRisk-ID menjawab: **"district mana yang berisiko banjir/longsor dengan severitas tertentu dalam 3-7 hari?"** -- impact severity ranking untuk evakuasi dan logistik BPBD.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | LightGBM | Rainfall + antecedent rainfall + topography proxies |
| B: Spatial Sequence | ConvLSTM | Gridded weather + terrain sequence |
| C: Graph | Graph-based exposure | DAS network exposure propagation |
| **Output** | Event probability + severity class | Flood risk rank |

Baseline: LightGBM -> ConvLSTM -> Graph exposure -> **Impact severity ranking**

#### Rubrik: A:16 | N:17 | M:20 | J:18 | K:18 = **89/100**

#### Why Choose This

1. **Manfaat tertinggi (20/20)** -- banjir/longsor dampak langsung pada keselamatan jiwa
2. **Data BNPB terstruktur** -- kemudahan preprocessing dibanding topik lain
3. **Framing impact severity > event prediction** -- lebih operasional untuk BPBD

#### Top Risks

1. Banjir/longsor prediction bukan hal baru -> novelty medium
2. Label lag dan underreporting -- explicit section di report
3. Overlap dengan ApiShield (bencana juga) -- beda jenis bencana: hidrometeorologi basah vs kering

#### M1: Data Eng (BNPB, BMKG, DEMNAS, OSM, DAS) | M2: Model (LightGBM, ConvLSTM, Graph) | M3: Eval (PR-AUC, Recall@Top-K, spatial robustness)

[Full detail ->](#appendix-hydrorisk-id)

---

### Rank 7: PadiWatch-X

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 88/100 | Pertanian | Swasembada Pangan | Med-High | Yes | ⭐⭐⭐⭐ | Tim dengan remote sensing & agrikultur skill |
| **Skip If:** Tidak familiar crop calendar alignment / NDVI processing |

> *PadiWatch-X: Prediksi Anomali Hasil Panen Padi Berbasis Multimodal Data Mining untuk Peringatan Dini Ketahanan Pangan*

#### Problem

Produksi padi dipengaruhi El Nino/La Nina. Gagal panen di satu provinsi mempengaruhi pasokan nasional dan harga. PadiWatch-X menjawab: **"kabupaten mana yang berisiko anomali hasil panen musim depan?"** -- multimodal fusion iklim + NDVI + produksi historis.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | LightGBM | Lagged climate + historic yields |
| B: Temporal CNN | 1D/3D CNN | NDVI time-series dari Sentinel-2/MODIS |
| C: Fusion | Multimodal | Tabular features + RS features + district embeddings |
| **Output** | Yield anomaly class (above/normal/below) | Yield early warning |

Baseline: LightGBM climate-only -> 3D CNN NDVI -> **Multimodal fusion** | Ablation: climate-only vs multimodal

#### Rubrik: A:17 | N:18 | M:19 | J:17 | K:18 = **88/100**

#### Why Choose This

1. **Satu-satunya topik multimodal (tabular + RS)** -- novelty kuat di arsitektur pipeline
2. **Food security = isu strategis nasional** -- relevan dengan swasembada pangan
3. **Visualisasi NDVI time-series powerful** -- kuat untuk presentasi

#### Top Risks

1. Crop calendar alignment rumit (berbeda per provinsi) -- harus benar-benar akurat
2. Butuh remote sensing knowledge yang tidak semua tim punya
3. Seasonal aggregation membuat jumlah sampel terbatas

#### M1: Data Eng (BPS KSA, BMKG, Sentinel-2/GEE, kalender tanam) | M2: Model (LightGBM, 3D CNN, multimodal fusion) | M3: Eval (yield MAE, directional accuracy, ablation RS)

[Full detail ->](#appendix-padiwatch-x)

---

### Rank 8: EduDrop-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 87/100 | Pendidikan | Pendidikan | **Low** | **No** | ⭐⭐⭐⭐ | Tim tanpa GPU, beginner-friendly |
| **Skip If:** Ingin pipeline deep learning / high novelty |

> *EduDrop-ID: Prediksi Risiko Putus Sekolah Berbasis Hierarchical Data Mining untuk Prioritas Intervensi Daerah*

#### Problem

Ribuan siswa putus sekolah setiap tahun di Indonesia, terutama SD/SMP di daerah tertinggal. EduDrop-ID menjawab: **"sekolah dan kecamatan mana yang berisiko putus sekolah tertinggi tahun depan?"** -- ranking prioritas BOS afirmasi dan intervensi Kemendikdasmen.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| A: Tabular | XGBoost / CatBoost | Fitur sekolah + kecamatan; SHAP interpretasi |
| B: Hierarchical | Mixed Effects Model (LMM) | Random intercept per kabupaten; fixed effects fasilitas |
| C: Clustering | K-Prototypes | Mixed numerical+categorical profiling tipe sekolah berisiko |
| **Ensemble** | Weighted avg XGBoost + LMM | Local prediction + group-adjusted prediction |

Baseline: Mean dropout per kabupaten -> Logistic Regression -> XGBoost -> XGBoost+LMM -> **Full + Clustering** | Ablations: -hierarchical, -clustering

#### Rubrik: A:17 | N:17 | M:20 | J:17 | K:16 = **87/100**

#### Why Choose This

1. **Risiko eksekusi paling rendah** -- tabular, tanpa GPU, data Dapodik terstruktur
2. **Manfaat 20/20** -- putus sekolah isu SDM fundamental, dipahami semua orang
3. **Hierarchical model sebagai diferensiator** -- novelty metodologis vs "prediksi pake XGBoost" biasa

#### Top Risks

1. Akses data Dapodik butuh pengajuan (40%) -- fallback: data agregat publik Ikhtisar Pendidikan Kemendikdasmen
2. Data putus sekolah underreported (30%) -- framing sebagai "risk proxy" bukan prediksi absolut
3. Terlihat seperti dashboard biasa (20%) -- hierarchical + clustering sebagai diferensiator

#### M1: Data Eng (Dapodik, BPS, OSM, feature engineering) | M2: Model (XGBoost, Mixed Effects, K-Prototypes) | M3: Eval (PR-AUC, Recall@Top-K, CV by province, report)

[Full detail ->](#appendix-edudrop-id)

---

### Rank 9: WasteWise-ID

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 86/100 | Lingkungan | Ekonomi Hijau | Med | Optional | ⭐⭐⭐⭐ | Tim dengan interest lingkungan/ekonomi sirkular |
| **Skip If:** Tidak tertarik waktu optimization routing |

> *WasteWise-ID: Prediksi Timbulan Sampah Berbasis Spatiotemporal Data Mining untuk Optimasi Rantai Pengelolaan Sampah*

#### Problem

Indonesia penghasil sampah terbesar ke-2 dunia (65 ton/tahun). Pengelolaan masih reaktif. WasteWise-ID menjawab: **"kecamatan mana yang akan alami lonjakan timbulan sampah dalam 1-7 hari?"** -- rekomendasi alokasi armada dan TPS 3R untuk DLH.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| A: Temporal | N-BEATS / TiDE | SOTA time-series forecasting untuk waste per wilayah |
| B: Tabular | LightGBM | Demografi + cuaca + holiday + lag features |
| C: Graph | GraphSAGE | Spillover kecamatan berdekatan |
| **Optimization** | Integer Linear Programming | Route recommendation based on waste forecast |

Baseline: Mean seasonal -> SARIMA/Prophet -> LightGBM -> N-BEATS -> **Full + routing** | Ablations: -graph, -N-BEATS

#### Rubrik: A:17 | N:18 | M:18 | J:17 | K:16 = **86/100**

#### Why Choose This

1. **Ekonomi Hijau = pilar Kemandirian Bangsa untouched** -- belum ada tim GEMASTIK di topik sampah
2. **Data SIPSN publik gratis** -- langsung dari KLHK tanpa scraping
3. **N-BEATS + optimization layer** -- diferensiator: prediksi + rekomendasi operasional

#### Top Risks

1. Data SIPSN tidak semua kabupaten update (40%) -- fokus ke 10 kota besar dengan data paling rajin
2. Optimization layer terlalu berat untuk scope GEMASTIK -- bisa opsional, cukup simulasi
3. Timbulan sampah dipengaruhi faktor lokal acak -- framing sebagai risk estimation, bukan exact prediction

#### M1: Data Eng (SIPSN, BMKG, BPS, OSM TPS/TPA) | M2: Model (N-BEATS, LightGBM, GNN, ILP routing) | M3: Eval (MAE, peak detection, cost saving simulation, report)

[Full detail ->](#appendix-wastewise-id)

---

### Rank 10: GempaRank-X

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 86/100 | Bencana | Kebencanaan | Med | **No** | ⭐⭐⭐ | Tim tanpa GPU, interest kebencanaan |
| **Skip If:** Ingin pre-event prediction (ini post-event nowcasting) |

> *GempaRank-X: Ranking Dampak Gempa Bumi Berbasis Data Mining untuk Prioritas Respons Darurat*

#### Problem

Indonesia di Ring of Fire. Saat gempa terjadi, 1 jam pertama kritis. GempaRank-X menjawab: **"daerah mana yang paling terdampak? fasilitas kritis mana diprioritaskan?"** -- impact ranking system untuk SAR/BPBD/Kemenkes.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | Rule-based impact index | f(magnitudo, depth, exposure proxies) |
| B: Tabular | LightGBM / XGBoost | Gempa features + exposure -> damage prediction |
| C: Graph + Travel | GNN + Dijkstra | District connectivity + travel time to hospitals |
| **Output** | Impact rank + uncertainty | Critical asset priority list |

Baseline: Rule-based -> LightGBM -> **GNN + Travel-time** | Scenario backtests on historical earthquakes

#### Rubrik: A:17 | N:17 | M:19 | J:16 | K:17 = **86/100**

#### Why Choose This

1. **Compute paling rendah** -- bisa dikerjakan tanpa GPU sama sekali
2. **Post-event nowcasting** -- berbeda dari topik forecasting lain (diversifikasi portfolio tim)
3. **Manfaat darurat tinggi** -- ranking dampak dalam 1 jam pertama sangat operasional

#### Top Risks

1. Label scarcity (gempa besar jarang) -- scenario backtests pada historical earthquakes
2. Bukan pre-event prediction, framing harus hati-hati -- "impact ranking" bukan "prediksi gempa"
3. Data damage reports sering underreported -- acknowledge limitations di report

#### M1: Data Eng (BMKG catalog, BNPB DIBI, OSM, BPS) | M2: Model (LightGBM, GNN, travel-time algorithm) | M3: Eval (NDCG@K, scenario backtests, ablation)

[Full detail ->](#appendix-gemparank-x)

---

### Rank 11: JudolFlow-X

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 84/100 | Cyber | Keamanan Digital | **High** | Optional | ⭐⭐⭐ | Tim expert NLP & graph, berani risk |
| **Skip If:** Tidak ada experience dengan scraping etis / pipeline multi-stage |

> *JudolFlow-X: Deteksi dan Klasterisasi Ekosistem Promosi Judi Online Berbasis NLP, Retrieval-Reranking, dan Graph Mining*

#### Problem

Judol adalah epidemi digital di Indonesia. Promosi menyebar via komentar media sosial, Telegram, QRIS. JudolFlow-X menjawab: **"bagaimana mendeteksi dan mengelompokkan jaringan promosi judi online?"** -- pipeline 6-stage retrieval + classifier + reranker + graph mining.

#### Pipeline

| Stage | Technique | Purpose |
|-------|-----------|---------|
| 1. Retrieval | Qwen3 / BGE-M3 | Cari konten semantik mirip contoh judol |
| 2. Classification | IndoBERT / LightGBM | Classify konten sebagai judol/non-judol |
| 3. Reranking | CrossEncoder | Improve precision pada borderline samples |
| 4. Entity Extraction | Regex + NER | Domain, handle, phone, QRIS alias |
| 5. Graph Mining | Hetero GNN / Community | Cluster detection + link prediction |
| 6. Hard-mining | Active learning loop | FP/FN -> relabel -> retrain |

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

[Full detail ->](#appendix-judolflow-x)

---

### Rank 12: AirGuard Sekolah

| Score | Kategori | Pilar K.B. | Risk | GPU | Data | **Best For:** |
|:-----:|----------|------------|:----:|:---:|:----:|---------------|
| 84/100 | Lingkungan | Kesehatan Publik | **Low** | **No** | ⭐⭐⭐ | Tim pemula, butuh topik paling aman |
| **Skip If:** Ingin novelty tinggi / impact besar |

> *AirGuard Sekolah: Prediksi Risiko Paparan PM2.5 Jam Sekolah Berbasis Data Mining*

#### Problem

Polusi PM2.5 di kota besar Indonesia mengkhawatirkan. Anak sekolah paling rentan (6-8 jam di sekolah). AirGuard menjawab: **"hari & sekolah mana yang berisiko paparan PM2.5 tertinggi?"** -- rekomendasi work-from-school/masker/air purifier untuk sekolah.

#### Pipeline

| Branch | Model | Purpose |
|--------|-------|---------|
| Baseline | Prophet | PM2.5 time-series + holiday effects |
| A: Tabular | LightGBM | Meteorological features + lag + location |
| B: Temporal | LSTM | Sequence forecasting PM2.5 |
| **Output** | School-day risk alert | PM2.5 exposure level + recommendation |

Baseline: Mean -> Prophet -> LightGBM -> LSTM -> **Alert system**

#### Rubrik: A:16 | N:16 | M:18 | J:18 | K:17 = **84/100**

#### Why Choose This

1. **Eksekusi paling aman dari semua topik** -- data OpenAQ gratis, compute rendah, mudah ditulis
2. **Cocok untuk tim pemula** -- tanpa GPU, tanpa remote sensing, tanpa scraping
3. **Framing school-hour exposure** -- diferensiator dari prediksi PM2.5 biasa

#### Top Risks

1. PM2.5 forecasting sudah sangat umum -- novelty hanya dari school-hour framing
2. Data sensor terbatas di kota besar saja -- coverage hanya Jakarta, Bandung, Surabaya
3. Bisa terlihat seperti dashboard biasa -- pastikan ada supervised prediction component

#### M1: Data Eng (OpenAQ, BMKG, OSM sekolah) | M2: Model (Prophet, LightGBM, LSTM) | M3: Eval (PM2.5 MAE, alert precision, report)

[Full detail ->](#appendix-airguard-sekolah)

## 6. Comparison Matrix & Trade-offs

### 6.1 Quick Reference -- Semua Topik

| Rank | Topik | Score | Pilar K.B. | Risk | GPU | Data | Novelty | Story | Compute |
|:----:|-------|:-----:|------------|:----:|:---:|:----:|:-------:|:-----:|:-------:|
| 1 | **WaterWatch-ID** | **90** | Swasembada Air | Med | Yes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Mod-High |
| 2 | DengueCast-X | 91 | Kesehatan | Med | Yes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Moderate |
| 3 | **TraceFish-ID** | **91** | Ekonomi Biru | Med-High | Yes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Moderate |
| 4 | PanganShock-X | 91 | Swasembada Pangan | **Low** | Opt | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | **Low** |
| 5 | ApiShield-ID | 91 | Kebencanaan | Med | Yes | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Moderate |
| 6 | HydroRisk-ID | 89 | Kebencanaan | Med | Opt | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Moderate |
| 7 | PadiWatch-X | 88 | Swasembada Pangan | Med-High | Yes | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Mod-High |
| 8 | **EduDrop-ID** | **87** | Pendidikan | **Low** | **No** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | **Low** |
| 9 | **WasteWise-ID** | **86** | Ekonomi Hijau | Med | Opt | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Low-Mod |
| 10 | GempaRank-X | 86 | Kebencanaan | Med | **No** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | **Low** |
| 11 | JudolFlow-X | 84 | Keamanan Digital | **High** | Opt | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Moderate |
| 12 | AirGuard | 84 | Kesehatan | **Low** | **No** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | **Low** |

### 6.2 Key Trade-offs

| Topik | Main Strength | Main Risk |
|-------|--------------|-----------|
| **WaterWatch-ID** | Multi-modal (TFT+GAT+ViT); Swasembada Air pillar | Data KLHK sparse secara temporal |
| **DengueCast-X** | Best balance impact + novelty + feasibility | Data DBD kabupaten availability varies |
| **TraceFish-ID** | Ekonomi Biru untouched; novelty tertinggi | Label IUU tidak ada (unsupervised) |
| **PanganShock-X** | Termudah dieksekusi; laporan terbaik | Bisa terasa biasa tanpa angle kuat |
| **ApiShield-ID** | Data melimpah (FIRMS); story kuat | Hotspot labels noisy |
| **PadiWatch-X** | Multimodal (tabular+RS); food security | Crop calendar alignment butuh domain |
| **EduDrop-ID** | Risiko terendah; data Dapodik terstruktur | Novelty medium |
| **WasteWise-ID** | Ekonomi Hijau; data SIPSN publik | Benefit operasional tidak sedramatis kesehatan |
| **GempaRank-X** | Compute terendah; post-event nowcasting | Label scarcity (gempa besar jarang) |
| **JudolFlow-X** | KDD-style; tech wow factor | Execution risk tertinggi; data ethics |
| **AirGuard** | Paling aman; OpenAQ mudah | PM2.5 forecasting sudah sangat umum |

## 7. Decision Engine

### A. By Team Capability

```
GPU strength?
├── GPU KUAT, RS skill ada
│   ├── WaterWatch-ID (TFT+GAT+ViT full pipeline)
│   └── ApiShield-ID (FIRMS + ConvLSTM + GraphSAGE)
├── GPU KUAT, tabular/NLP focus
│   ├── TraceFish-ID (Trajectory Transformer + GNN)
│   ├── DengueCast-X (TFT + GNN + CatBoost)
│   └── JudolFlow-X (retrieval + reranker + GNN) -- HIGH RISK
├── GPU TERBATAS / tanpa GPU
│   ├── EduDrop-ID (XGBoost + Mixed Effects, zero GPU)
│   ├── PanganShock-X (Prophet + LightGBM, GPU optional)
│   └── AirGuard (Prophet + LSTM, zero GPU)
└── GPU TERBATAS, domain expert
    ├── HydroRisk-ID (LightGBM + ConvLSTM)
    ├── GempaRank-X (LightGBM + rules, zero GPU)
    └── WasteWise-ID (N-BEATS + LightGBM)
```

### B. By Risk Appetite

| Appetite | Top Pick | Runner-up | Kenapa |
|----------|----------|-----------|--------|
| **Safe** (90% success rate) | EduDrop-ID | PanganShock-X | Data terstruktur, pipeline sederhana, tanpa GPU |
| **Balanced** (70% success rate) | WaterWatch-ID | DengueCast-X | Novelty tinggi tapi mitigasi jelas; fallback strategy ada |
| **Ambitious** (50% success rate) | TraceFish-ID | JudolFlow-X | Unsupervised problem, pipeline kompleks, data ethics issue |

### C. By Kemandirian Bangsa Pillar

| Prioritas Pilar | Top Pick | Alternative |
|-----------------|----------|-------------|
| Swasembada Air | **WaterWatch-ID** (90) | -- |
| Swasembada Pangan | **PanganShock-X** (91) | PadiWatch-X (88) |
| Ekonomi Biru | **TraceFish-ID** (91) | -- |
| Ekonomi Hijau | **WasteWise-ID** (86) | -- |
| Kesehatan Publik | **DengueCast-X** (91) | AirGuard (84) |
| Pendidikan | **EduDrop-ID** (87) | -- |
| Kebencanaan | **ApiShield-ID** (91) | HydroRisk-ID (89), GempaRank-X (86) |
| Keamanan Digital | **JudolFlow-X** (84) | -- |

### D. Quick Self-Assessment (5 Questions)

Answer yes/no to narrow down:

| # | Question | If YES | If NO |
|---|----------|--------|-------|
| 1 | Tim punya akses GPU untuk training? | Go to Q2 | EduDrop / PanganShock / AirGuard |
| 2 | Ada anggota dengan remote sensing skill? | WaterWatch / ApiShield / PadiWatch | Go to Q3 |
| 3 | Prioritas novelty di atas segalanya? | TraceFish / JudolFlow | Go to Q4 |
| 4 | Ingin dampak sosial paling visible? | DengueCast / EduDrop | PanganShock / HydroRisk |
| 5 | Deadline ketat (< 6 minggu)? | EduDrop / PanganShock / AirGuard | WaterWatch / ApiShield |

## 8. Pipeline Architecture

### Generic Pipeline (WaterWatch / DengueCast / ApiShield / HydroRisk)

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
| **WaterWatch-ID** | KLHK + BMKG + Sentinel-2 + OSM | TFT + GAT + ViT + CatBoost | Ranked DAS priority list | Multi-modal (time + graph + vision) |
| **DengueCast-X** | Kemenkes + BMKG + BPS + OSM | CatBoost + TFT + GNN + News | Ranked district intervention list | Spatiotemporal + public health |
| **TraceFish-ID** | GFW + KKP + BMKG + Pelabuhan | Trajectory TF + XGBoost + GNN + LSTM | IUU risk rank per kapal | Trajectory + graph anomaly |
| **PanganShock-X** | PIHPS + BMKG + BPS + News | Prophet + LightGBM + TFT + Text | Ranked region-commodity alert | Dual objective (reg + class) |
| **ApiShield-ID** | NASA FIRMS + BMKG + Sentinel + OSM | LightGBM + ConvLSTM + GNN | Ranked village patrol list | Remote sensing + hotspot |
| **HydroRisk-ID** | BNPB + BMKG + OSM + DEMNAS | LightGBM + ConvLSTM + Graph exposure | Flood severity rank | Multi-hazard (flood+slide) |
| **PadiWatch-X** | BPS + BMKG + Sentinel-2 | LightGBM + 3D CNN + Multimodal fusion | Anomaly map per season | Multimodal (tabular + RS) |
| **EduDrop-ID** | Dapodik + BPS + OSM | XGBoost + Mixed Effects + K-Prototypes | School risk priority list | Hierarchical + clustering |
| **WasteWise-ID** | SIPSN + BMKG + BPS + OSM | N-BEATS + LightGBM + GNN + ILP | Waste forecast + route optimization | Forecasting + optimization |
| **GempaRank-X** | BMKG + BNPB + OSM + BPS | Rule-based + LightGBM + GNN | First-hour triage dashboard | Post-event nowcasting |
| **JudolFlow-X** | Scraping + OSINT + blocklists | Embedding + Classifier + Reranker + GNN | Risk cluster score | 6-stage retrieval + graph |
| **AirGuard** | OpenAQ + BMKG + BPS | Prophet + LightGBM + LSTM | School-day risk alert | PM2.5 + exposure |

### Experiment Matrix (Wajib untuk Technical Report)

Setiap topik WAJIB memiliki baseline ladder dengan format:

| Level | Model | Target PR-AUC | Recall@Top-10% | Notes |
|:-----:|-------|:-------------:|:--------------:|-------|
| 1 | Naive baseline | 0.50 | 0.10 | DummyClassifier |
| 2 | Simple time-series (Prophet/SARIMA) | 0.62 | 0.25 | Hanya temporal |
| 3 | Strong tabular (LightGBM/CatBoost) | 0.74 | 0.38 | Full feature set |
| 4 | Advanced deep (TFT/ConvLSTM/GNN) | 0.81 | 0.45 | Per branch |
| 5 | **Full pipeline (fusion + calibration)** | **0.85** | **0.52** | **Proposed** |
| 6-8 | Ablations: -GNN, -TFT, -text | 0.80-0.83 | 0.46-0.50 | Kontribusi per branch |

## 9. Decision Checklist

### Screening Questions

| Pertanyaan | Pilihan |
|------------|---------|
| **Data availability** -- Dataset primer bisa didapat dalam **1-2 minggu**? | [✅] Ya -- topik dengan data scoring ⭐⭐⭐⭐+ / [❌] Tidak |
| **Tim skill match** -- Ada anggota yang bisa handle modeling yang direncanakan? | [✅] Ya / [❌] Tidak |
| **Compute adequacy** -- Laptop/GPU cukup untuk training model? | [✅] Ya / [❌] Tidak |
| **Story clarity** -- Problem statement bisa dijelaskan dalam **1 kalimat**? | [✅] Ya / [❌] Tidak |
| **Tim enthusiasm** -- Semua anggota **excited** dengan topik ini? | [✅] Ya / [❌] Tidak |
| **Novelty check** -- Apakah ada publikasi/makalah GEMASTIK sebelumnya yang identik? | [✅] Tidak ada / [❌] Ada -- perlu differentiator |
| **8-week feasibility** -- Pipeline bisa diselesaikan dalam 8 minggu? | [✅] Ya / [❌] Tidak -- perlu scope-down |

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

*Dokumen ini dapat diperbarui setiap kali ada keputusan baru atau informasi tambahan.*

## 10. Appendix: Full Detail per Topik

### Appendix A: WaterWatch-ID

**Data Sources (Complete):**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Parameter kualitas air historis | KLHK / Satu Data Indonesia | DO, BOD, COD, pH, TSS, Nitrat, Fosfat | data.go.id |
| Debit & elevasi sungai | BBWS / Kementerian PUPR | Debit harian, tinggi muka air | Data PUPR |
| Land use catchment area | KLHK / Geospatial Bappenas | Proporsi hutan, sawah, industri, permukiman | geoportal.bappenas |
| Citra satelit optik | Copernicus Sentinel-2 | NDWI, turbidity | Google Earth Engine |
| Curah hujan & iklim | BMKG | Curah hujan harian, intensitas | iklim.bmkg.go.id |
| Graph DAS | Bappenas / OSM | Segmen sungai, anak sungai, muara | Geospasial |

**Preprocessing Steps:**
1. Aggregasi temporal -- rata-rata parameter per minggu per titik sampling
2. Interpolasi sparse -- KNN Imputer + temporal interpolation
3. Fusion data spasial -- join titik monitoring ke segmen DAS terdekat
4. NDWI extraction -- median composite per 2 minggu dari Sentinel-2, cloud-masked
5. Lag features -- rolling window 1, 2, 4, 8 minggu
6. Graph construction -- DAS graph: nodes = segmen sungai, edges = aliran hulu-hilir
7. Train/val/test split -- temporal walk-forward, test set = tahun terbaru

**Full Evaluation Strategy:**

| Metrik | Tujuan |
|--------|--------|
| MAE / RMSE | Primary -- error WQI regresi |
| MAPE | Persentase error untuk interpretasi |
| PR-AUC | Klasifikasi status mutu air (baik/cemar ringan/cemar berat) |
| Recall@Top-K segmen | Operational -- segmen prioritas restorasi tertangkap |
| Spatial consistency | Prediksi konsisten secara spasial (hulu-hilir) |
| Ablation gain | Kontribusi tiap branch terhadap akurasi |

**Full Scoring Justification:**
- **Keaslian 18/20**: Water quality prediction sudah ada, tapi multi-branch fusion (TFT+GAT+ViT) untuk ranking prioritas restorasi DAS sangat orisinal
- **Kebaruan 19/20**: Integrasi time-series parameter kimia + graph DAS + citra satelit (ViT) untuk WQI di Indonesia belum ada
- **Manfaat 19/20**: Air bersih adalah fondasi kemandirian bangsa. Relevan dengan SDG 6
- **Kejelasan 17/20**: Butuh domain knowledge dasar tentang parameter kualitas air
- **Kelengkapan 17/20**: Data KLHK perlu preprocessing sparse, tapi setelah bersih baselines jelas

---

### Appendix B: DengueCast-X

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Kasus DBD historis | Kemenkes / Satu Data Indonesia | Incidence count per district-week | data.go.id |
| Iklim & cuaca | BMKG API | Rainfall, temperature, humidity | iklim.bmkg.go.id |
| Demografi | BPS API | Populasi, density, urbanisasi | webapi.bps.go.id |
| Geospasial | OpenStreetMap | District adjacency, elevasi, sungai | download.geofabrik.de |
| Berita kesehatan (optional) | Google News scraping | Outbreak keywords, sentiment | RSS/NLP pipeline |

**Preprocessing:**
1. Aggregasi mingguan -- dari data harian ke level district-week
2. Rolling lag windows -- 1, 2, 4, 8, 12 minggu
3. Normalisasi per-district -- standarisasi mean/std historis
4. Imputasi missing value -- MICE untuk data cuaca tidak lengkap
5. Outlier handling -- IQR method / Isolation Forest
6. Spatial adjacency matrix -- binary adjacency dari boundary sharing OSM
7. Train/val/test split -- forward-chaining temporal

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| PR-AUC | Primary -- ranking quality dengan class imbalance |
| Recall@Top-10% districts | Operational utility |
| Recall@Top-20% districts | Coverage breadth |
| Temporal backtesting | Walk-forward multi-season validation |
| Lead-time gain | Warning lead time vs baseline |
| Calibration error (ECE) | Probability calibration quality |
| SHAP / attention visualization | Explainability |

---

### Appendix C: TraceFish-ID

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| AIS trajectory kapal | Global Fishing Watch API | Lat, lon, speed, heading, timestamp | globalfishingwatch.org |
| VMS data kapal Indonesia | KKP (pernah dirilis publik) | Kapal >30 GT, tracker wajib | Data terbuka |
| Fishing zone / ZEEI | Bappenas / BIG | Batas ZEEI, kawasan konservasi | Geospasial |
| Data pelabuhan | KKP / BPS | Lokasi pelabuhan, kapasitas | Data publik |
| Cuaca maritim | BMKG Maritim | Gelombang, angin, visibility | bmkg.go.id |

**Preprocessing:**
1. Trajectory resampling -- interpolasi ke interval 10 menit
2. Fishing activity labeling -- speed <3 knot + random heading change; validasi GFW
3. Feature extraction -- speed distribution, turning angle, trip duration, jarak ke ZEEI
4. Port-to-port segmentation -- trajectory per trip
5. Bipartite graph -- nodes: kapal + pelabuhan; edges: frekuensi kunjungan
6. Anomaly score baseline -- isolation forest untuk label proxy
7. Temporal split -- train 2022-2023, val 2024, test 2025

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| PR-AUC | Primary -- IUU sangat rare (<1% trips) |
| Recall@Top-K kapal | Operational kapasitas inspeksi |
| F1 per jenis IUU | transshipment, boundary, gear |
| Cluster purity | Graph community detection quality |
| Temporal backtesting | Konsistensi antar musim |
| Case studies | Validasi kasus IUU terkonfirmasi |

---

### Appendix D: PanganShock-X

**Data Sources:**

| Data | Sumber | Variabel | Akses |
|------|--------|----------|-------|
| Harga harian komoditas | PIHPS BPS | 50+ komoditas | pipps.bps.go.id |
| Inflasi daerah | BPS API | IHK per kota | webapi.bps.go.id |
| Cuaca & iklim | BMKG | Rainfall, temperature, anomaly | iklim.bmkg.go.id |
| Kalender tanam/panen | Kementan | Musim tanam per komoditas | Data terbuka |
| Berita & sentimen | Google News / RSS | Berita pangan regional | Scraping NLP |

**Preprocessing:**
1. Panel time-series construction (region x commodity x date)
2. Spike labeling -- >2 std from 30-day rolling mean
3. Missing price interpolation -- linear (gap <=3 hari), forward-fill (lebih)
4. Rolling features -- mean, std, min, max window 7, 14, 30 hari
5. Holiday & event flags -- puasa, lebaran, natal, pemilu
6. Calendar alignment -- harvest season per region x commodity

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| wMAPE / sMAPE | Weighted/symmetric MAPE untuk regresi harga |
| PR-AUC | Spike/no-spike classification |
| Recall@Top-K alerts | Operational spike detection |
| Directional accuracy | % prediksi arah (naik/turun) benar |
| Calibration plot | Reliability diagram spike probability |

---

### Appendix E: ApiShield-ID

**Data Sources:**

| Data | Sumber | Variabel Kunci |
|------|--------|----------------|
| Hotspot aktif real-time | NASA FIRMS (MODIS/VIIRS) | Latitude, longitude, confidence, FRP |
| Cuaca | BMKG | Curah hujan, kelembaban, suhu, angin |
| Historical fires | BNPB DIBI | Rekaman kebakaran historis |
| Satelit optik | Copernicus Sentinel-2 | NDVI, land cover classification |
| Exposure layers | OpenStreetMap | Pemukiman, jalan, lahan, sungai |

**Preprocessing:**
1. Spatial join -- hotspot -> grid desa/kecamatan (1 km2)
2. Rainfall deficit -- SPI 1, 3, 6 bulan
3. Lag features -- hotspot count 1, 3, 7, 14, 30 hari
4. Land cover aggregation -- proporsi peat, forest, plantation
5. Temporal split -- forward-chaining; exclusion El Nino
6. Class balancing -- positive class (~1-5%)

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| PR-AUC | Primary -- class imbalance ekstrem |
| Recall@Top-K villages | Operational patrol prioritization |
| Lead-time gain | Hari lebih awal dibanding baseline |
| Calibration error | Uncertainty reliability |
| Spatial stress test | Province-wise evaluation |

---

### Appendix F: HydroRisk-ID

**Data Sources:**

| Data | Sumber |
|------|--------|
| Banjir/longsor historis | BNPB DIBI |
| Curah hujan harian, prakiraan 3-7 hari | BMKG |
| DEM / topography / kemiringan lereng | Copernicus / DEMNAS |
| Land use, DAS | KLHK / Geospatial Bappenas |
| Populasi, bangunan, infrastruktur vital | BPS + OSM |

**Preprocessing:**
1. Event aggregation per subdistrict per day -> binary + severity multi-class
2. Rainfall accumulation -- cumulative 1, 3, 7 hari
3. Topography features -- slope, elevation, distance to river
4. Exposure weighting -- population x building density
5. Temporal split -- forward-chaining
6. Address label lag & underreporting -- explicit section

---

### Appendix G: PadiWatch-X

**Data Sources:**

| Data | Sumber |
|------|--------|
| Hasil panen per kabupaten/musim | BPS (Ubinan / KSA) |
| Climate indices (SPI, NDVI anomaly) | BMKG + Copernicus |
| Citra satelit NDVI/EVI | Sentinel-2 / MODIS (GEE) |
| Peta lahan sawah | Kementan / Geospatial |
| Kalender tanam | Kementan (per provinsi) |

**Preprocessing:**
1. Seasonal aggregation -- MT1 (Okt-Mar), MT2 (Apr-Sep)
2. NDVI temporal profiles -- cloud masking -> median composite 16 hari
3. Climate anomaly indices -- SPI 1, 3, 6 bulan; temperature anomaly
4. Crop calendar alignment -- berbeda per provinsi

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| MAE, R2 | Regresi yield |
| Directional accuracy on anomalies | Arah anomali benar |
| Per-province robustness | Generalisasi ke unseen provinces |
| Ablation: climate-only vs multimodal | Kontribusi RS |

---

### Appendix H: EduDrop-ID

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Data pokok pendidikan (Dapodik) | Kemendikdasmen | Siswa, guru, rombel, putus sekolah, akreditasi | dapodik.kemdikbud.go.id |
| Data kemiskinan | BPS | % kemiskinan, PDRB per kapita | bps.go.id |
| Infrastruktur sekolah | Dapodik + OSM | Listrik, air, toilet, jarak | dapodik + osm.org |
| Program bantuan | Puslapdik | Penerima BOS, PIP, KIP | Data publik |

**Preprocessing:**
1. School-level aggregation per tahun
2. Target definition -- % putus sekolah per tahun (atau binary threshold)
3. Lag features -- tren 2-3 tahun, delta enrollment, rasio guru/siswa
4. Spatial features -- kemiskinan, akses transportasi per kecamatan
5. Categorical encoding -- provinsi/kabupaten sebagai hierarchical group
6. Train/val/test split -- temporal: train 2020-2022, val 2023, test 2024
7. Imbalance handling -- fokus ke sekolah risiko tinggi

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| PR-AUC | Primary -- dropout class minoritas |
| Recall@Top-K sekolah | Operational prioritization |
| F1-score | Balanced precision-recall |
| RMSE | Regresi persentase putus sekolah |
| CV by province | Generalisasi ke unseen provinces |

---

### Appendix I: WasteWise-ID

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| Timbulan sampah historis | SIPSN KLHK | Tonase per hari per kab/kota | sipsn.menlhk.go.id |
| Demografi & kepadatan | BPS | Penduduk, kepadatan, PDRB | bps.go.id |
| Data cuaca | BMKG | Curah hujan, suhu | iklim.bmkg.go.id |
| Hari libur & event | Kemenko PMK | Libur nasional, hari besar, event | Data publik |
| TPS/TPA location | OpenStreetMap | Lokasi TPS, TPA, jarak | osm.org |

**Preprocessing:**
1. Daily aggregation -- tonase per kecamatan per hari
2. Holiday feature -- binary flags
3. Weather features -- curah hujan kumulatif 1, 3, 7 hari
4. Lag features -- timbulan 1, 2, 3, 7 hari sebelumnya
5. Population normalization -- tonase per 1000 penduduk
6. Spatial adjacency -- graph kecamatan
7. Temporal walk-forward split

---

### Appendix J: GempaRank-X

**Data Sources:**

| Data | Sumber |
|------|--------|
| Katalog gempa (magnitudo, depth, lokasi, waktu) | BMKG |
| Historical damage reports | BNPB DIBI |
| Buildings, roads, health facilities | OpenStreetMap |
| Populasi per desa/kecamatan | BPS |
| Topografi / soil type (liquefaction risk) | Copernicus / DEMNAS |

**Preprocessing:**
1. Define impact target -- affected population / building damage proxy
2. Exposure layer -- building count, road density, facility count per district
3. Graph -- district connectivity + travel time to hospitals
4. Scenario backtests -- simulate historical earthquakes

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| NDCG@K, Recall@Top-K | Ranking quality of impacted districts |
| MAE on affected population | Impact magnitude accuracy |
| Scenario backtests | On historical earthquake events |
| Ablation | Rule-based vs learned, +/- graph |

---

### Appendix K: JudolFlow-X

**Data Sources & Preprocessing:**
1. Scraping dari platform publik (medsos, Telegram publik) -- etis, data publik
2. URL canonicalization -- resolve shortlinks
3. Entity extraction -- domain, handle, phone, payment alias
4. Slang normalization -- "gacor", "maxwin", "bonanza"
5. Graph construction -- nodes: user, domain, handle; edges: co-occurrence
6. Weak labeling -- rule-based dari keyword + OSINT lists

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| Macro F1 | Suspicious content classification |
| PR-AUC | Imbalanced labels |
| Entity extraction F1 | Per entity type |
| Cluster purity / NMI | Graph clustering quality |
| Precision@K | Suspicious cluster ranking |
| Case study | Qualitative evaluation |

---

### Appendix L: AirGuard Sekolah

**Data Sources:**

| Data | Sumber Utama | Variabel Kunci | Akses |
|------|-------------|----------------|-------|
| PM2.5 real-time & historis | OpenAQ | PM2.5, PM10, O3, NO2 | openaq.org |
| Cuaca & iklim | BMKG | Suhu, kelembaban, kecepatan angin | iklim.bmkg.go.id |
| Lokasi sekolah | OSM / Dapodik | Koordinat sekolah, jenjang | osm.org |
| Kalender akademik | Kemendikdasmen | Hari sekolah, libur, ujian | Data publik |

**Preprocessing:**
1. Hourly PM2.5 aggregation -> daily mean per stasiun
2. Spatial interpolation -- inverse distance weighting ke lokasi sekolah
3. Lag features -- PM2.5 1, 2, 3 hari sebelumnya
4. Meteorological features -- suhu, kelembaban, wind speed
5. Holiday flags -- hari sekolah, libur nasional
6. Train/val/test split -- temporal

**Full Evaluation:**

| Metrik | Tujuan |
|--------|--------|
| MAE / RMSE | PM2.5 forecast error |
| Alert precision | School-day risk alert accuracy |
| Peak detection | High pollution day detection |
| Spatial CV | Generalisasi antar kota |
