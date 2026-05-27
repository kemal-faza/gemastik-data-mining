# PanganFlow.ID

**GEMASTIK XVIII (2025) -- Divisi Penambangan Data**

Sistem penambangan data spatio-temporal untuk mendeteksi ketimpangan pasokan beras antarprovinsi dan menyusun rekomendasi prioritas aliran redistribusi berbasis disparitas harga, produksi, estimasi kebutuhan, dan jarak logistik.

**Skor Evaluasi Internal:** 91/100 (Rubrik Keaslian, Kebaruan, Manfaat, Kejelasan, Kelengkapan) -- Lihat [PLAN.md](PLAN.md) untuk detail scoring dan decision engine.

**Status:** Technical report selesai, dashboard fungsional, siap submisi.

---

## Navigasi Cepat

| Tujuan | Path |
|--------|------|
| Kode & pipeline utama | [`DATA MINING - Penambangan Data/PanganFlow-ID/`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/) |
| Paper LaTeX | [`.../reports/panganflow_report.tex`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/reports/panganflow_report.tex) |
| PDF final | [`.../reports/GEMASTIK XVIII - PanganFlow.ID.pdf`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/reports/GEMASTIK%20XVIII%20-%20PanganFlow.ID.pdf) |
| Dashboard | [`.../dashboard/app.py`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/dashboard/app.py) |
| Spesifikasi riset | [`.../panganflow-spec.md`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/panganflow-spec.md) |
| Dokumen perencanaan | [`PLAN.md`](PLAN.md) |
| Panduan GEMASTIK | [`Panduan-GEMASTIK-2025-Data-Mining.pdf`](Panduan-GEMASTIK-2025-Data-Mining.pdf) |

---

## Struktur Proyek

```
.
├── Panduan-GEMASTIK-2025-Data-Mining.pdf   # Panduan resmi GEMASTIK XVIII
├── Winner-Level GEMASTIK Data Mining Playbook-1.pdf  # Playbook strategi
├── PLAN.md                                  # Decision engine & scoring (8 topik)
├── PLAN-JUDOL.md                            # Variasi plan DengueCast + JudolFlow
├── possible-idea.md                         # Brainstorming 7 ide awal + rekomendasi
│
└── DATA MINING - Penambangan Data/
    └── PanganFlow-ID/
        ├── data/
        │   ├── raw/                          # Snapshot data mentah dari sumber resmi
        │   │   ├── bapanas_harga_pangan_bulanan_konsumen_provinsi.csv
        │   │   ├── bps_rice_balance_snapshot.csv
        │   │   ├── bi_pihps_provinces.json
        │   │   └── bi_pihps_commodities.json
        │   └── processed/                    # Hasil pipeline: panel & rekomendasi
        │       ├── province_commodity_panel.csv
        │       ├── province_distance_matrix.csv
        │       ├── flow_recommendations.csv
        │       └── latest_province_snapshot.csv
        │
        ├── reports/
        │   ├── panganflow_report.tex         # LaTeX paper (bisa diedit langsung)
        │   ├── compile_report.sh             # Compile .tex ke PDF (pdflatex)
        │   ├── tables/                       # CSV hasil evaluasi (dibaca build_report_latex.py)
        │   │   ├── metrics_summary.csv
        │   │   ├── feature_ablation.csv
        │   │   ├── flow_recommendations.csv
        │   │   ├── cluster_summary.csv
        │   │   ├── subgroup_fairness.csv
        │   │   ├── ranking_stability.csv
        │   │   ├── case_studies.csv
        │   │   ├── error_analysis_region.csv
        │   │   ├── error_analysis_province.csv
        │   │   ├── source_status.csv
        │   │   ├── dataset_summary.csv
        │   │   └── dataset_summary.json
        │   └── figures/                      # Gambar untuk paper (PNG)
        │       ├── model_comparison.png
        │       ├── feature_importance.png
        │       ├── shap_summary.png
        │       ├── pressure_centroid_map.png
        │       ├── flow_network.png
        │       ├── top_flow_recommendations.png
        │       ├── cluster_pca.png
        │       └── dashboard_preview.png
        │
        ├── src/
        │   ├── build_dataset.py              # Ambil data dari API/snapshot, bangun panel
        │   ├── train_panganflow.py           # Modeling: Isolation Forest, Random Forest, K-Means, scoring
        │   ├── build_formal_report.py        # Generate DOCX technical report
        │   └── build_report_latex.py         # Generate .tex dari data CSV di reports/tables/
        │
        ├── notebooks/
        │   └── PanganFlow-ID-analysis.ipynb  # Eksplorasi data & prototyping
        │
        ├── dashboard/
        │   ├── app.py                        # Dashboard Streamlit (peta, ranking, flow, profil)
        │   └── static_preview.html           # Preview statis dashboard
        │
        ├── panganflow-spec.md                # Spesifikasi riset lengkap
        ├── pyproject.toml                    # Konfigurasi uv + dependensi
        ├── requirements.txt                  # Dependensi (alternatif pip)
        └── uv.lock                           # Lock file uv
```

---

## Quick Start -- Menjalankan Pipeline

### Prasyarat

- Python 3.12 atau lebih baru
- `uv` (recommended) atau `pip`
- `pdflatex` (untuk kompilasi LaTeX)

  - Fedora: `sudo dnf install texlive texlive-ieeetran texlive-booktabs texlive-caption texlive-hyperref`
  - Ubuntu/Debian: `sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended`

### Setup

```bash
# Masuk ke direktori proyek
cd "DATA MINING - Penambangan Data/PanganFlow-ID"

# Install dependensi dengan uv (otomatis buat venv)
uv sync

# Atau dengan pip
pip install -r requirements.txt
```

### Jalankan Pipeline (4 Langkah)

```bash
# Langkah 1: Ambil data dari Bapanas/BPS/PIHPS, bangun panel provinsi-bulan
uv run python src/build_dataset.py

# Langkah 2: Modeling (anomaly detection, Random Forest, K-Means, flow scoring)
uv run python src/train_panganflow.py

# Langkah 3: Generate technical report (DOCX)
uv run python src/build_formal_report.py

# Langkah 4: Jalankan dashboard interaktif
uv run streamlit run dashboard/app.py
```

### Output Utama

- `data/processed/province_commodity_panel.csv` -- panel 1.904 baris x 38 provinsi
- `data/processed/flow_recommendations.csv` -- rekomendasi pasangan asal-tujuan
- `reports/GEMASTIK XVIII Penambangan Data - <ID_TIM> - <NAMA_TIM> - PanganFlow.ID.docx`

---

## Data & Metodologi

### Sumber Data

| Sumber | Data | Akses |
|--------|------|-------|
| Bapanas Satu Data | Harga bulanan konsumen provinsi | [satudata.badanpangan.go.id](https://satudata.badanpangan.go.id) |
| BPS | Produksi beras, konsumsi per kapita | [bps.go.id](https://bps.go.id) |
| PIHPS BI | Referensi provinsi/komoditas | [bi.go.id/hargapangan](https://www.bi.go.id/hargapangan) |

### Pipeline Analisis

1. **Deteksi Anomali** -- Isolation Forest untuk sinyal lonjakan harga (contamination 18%)
2. **Estimasi Surplus-Defisit** -- proxy produksi dikurangi estimasi kebutuhan (populasi x 81,23 kg/kapita/tahun)
3. **Ranking Prioritas** -- Random Forest (n_estimators=260, min_samples_leaf=3) untuk mempelajari prioritas intervensi
4. **Klasterisasi** -- K-Means (k=4, n_init=20) + PCA 2 komponen untuk tipologi provinsi
5. **Graph Scoring** -- semua pasangan asal-tujuan diskor berdasarkan price gap, surplus, defisit, dan penalti jarak
6. **Evaluasi** -- NDCG@K, Precision@K, Recall@K, ablation study, subgroup fairness, stability check

Detail lengkap: [`panganflow-spec.md`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/panganflow-spec.md)

---

## Paper / Technical Report

Paper GEMASTIK dihasilkan dalam dua format: **DOCX** (via `build_formal_report.py`) dan **LaTeX** (via `build_report_latex.py` + `compile_report.sh`).

Paper LaTeX **direkomendasikan** karena:
- Format IEEE 2-column yang rapi dan profesional
- Kolaborasi real-time via Overleaf
- Bibliografi terstruktur dengan `thebibliography`
- Persamaan matematika yang presisi (formula priority scoring)

---

### Alur A: Generate .tex dari Data Pipeline

File `.tex` dihasilkan secara otomatis dari data CSV di `reports/tables/`. Jalankan ini **setiap kali ada perubahan data atau hasil modeling**.

```bash
cd "DATA MINING - Penambangan Data/PanganFlow-ID"

uv run python src/build_report_latex.py \
    --team-id "TST001" \
    --team-name "PanganFlowTeam" \
    --member1 "Muhamad Kemal Faza" \
    --member2 "Muchammad Yuda Tri Ananda" \
    --member3 "Muhammad Akmal Fazli Riyadi" \
    --pembimbing "Henri Tantyoko"
```

**Apa yang terjadi:**
1. Script membaca semua CSV di `reports/tables/` (metrics_summary.csv, feature_ablation.csv, flow_recommendations.csv, cluster_summary.csv, dll.)
2. Mengisi template dengan data aktual (tabel evaluasi, tabel ablasi, daftar flow, ringkasan cluster, dll.)
3. Mengekspor ke `reports/panganflow_report.tex`

**Argumen CLI:**

| Argumen | Default | Keterangan |
|---------|---------|------------|
| `--team-id` | `ID_TIM` | ID tim dari registrasi GEMASTIK |
| `--team-name` | `NAMA_TIM` | Nama tim |
| `--member1` | `Nama Ketua Tim` | Ketua tim (corresponding author) |
| `--member2` | `Nama Anggota 2` | Anggota 2 |
| `--member3` | `Nama Anggota 3` | Anggota 3 |
| `--pembimbing` | `Nama Pembimbing` | Dosen pembimbing |
| `--output` | `reports/panganflow_report.tex` | Path output |

---

### Alur B: Compile .tex ke PDF (Lokal)

Setelah `.tex` dihasilkan, compile dengan `pdflatex`:

```bash
cd reports
bash compile_report.sh
```

Script ini menjalankan `pdflatex` dua kali (untuk resolve referensi silang) dan menghasilkan PDF.

Output: `reports/panganflow_report.pdf`

---

### Alur C: Upload ke Overleaf (Kolaborasi Real-Time)

1. Generate `.tex` dengan `build_report_latex.py` (Alur A).
2. Buka [Overleaf](https://overleaf.com), buat project baru > Upload.
3. Upload semua file berikut:
   - `reports/panganflow_report.tex`
   - Semua file PNG di `reports/figures/` (model_comparison.png, feature_importance.png, shap_summary.png, pressure_centroid_map.png, flow_network.png, top_flow_recommendations.png, cluster_pca.png, dashboard_preview.png)
4. Di Overleaf, set compiler ke **pdfLaTeX**.
5. Klik **Recompile** -- PDF akan dihasilkan di browser.
6. Download PDF dari Overleaf, rename sesuai format submisi: `GEMASTIK XVIII Penambangan Data - <ID Tim> - <Nama Tim> - <Judul>.pdf`

> **Catatan:** Jika Overleaf mendeteksi error "file not found" untuk gambar, pastikan semua file PNG dari `reports/figures/` sudah diupload. Path gambar di `.tex` menggunakan `figures/` sebagai prefix relatif.

---

## Cara Melakukan Perubahan pada Paper

### Skenario 1: Ubah Data (Angka / Tabel)

Jika hasil modeling berubah (setelah tuning hyperparameter, ganti dataset, dll.):

```bash
cd "DATA MINING - Penambangan Data/PanganFlow-ID"

# 1. Jalankan ulang modeling untuk update CSV di reports/tables/
uv run python src/train_panganflow.py

# 2. Regenerate .tex (membaca CSV yang baru)
uv run python src/build_report_latex.py \
    --team-id "TST001" --team-name "PanganFlowTeam" \
    --member1 "Muhamad Kemal Faza" \
    --member2 "Muchammad Yuda Tri Ananda" \
    --member3 "Muhammad Akmal Fazli Riyadi" \
    --pembimbing "Henri Tantyoko"

# 3. Recompile PDF
bash reports/compile_report.sh
```

**File yang berubah otomatis:** Semua tabel numerik (metrics, ablation, flows, clusters, error, fairness, source status).

**File yang TIDAK berubah:** Konten naratif, gambar (kecuali jika `train_panganflow.py` menghasilkan figure baru).

---

### Skenario 2: Ubah Konten Naratif (Teks Manual)

Untuk mengubah bagian yang **tidak di-generate otomatis** (pendahuluan, kajian terkait, analisis manual, kesimpulan):

1. **Edit langsung** `reports/panganflow_report.tex` dengan text editor.
2. Cari section yang relevan:

   | Section | Isi |
   |---------|-----|
   | `\section{Pendahuluan}` | Latar belakang, tujuan, batasan |
   | `\section{Kajian Terkait}` | Literature review + research gap |
   | `\section{Dataset dan Formulasi Masalah}` | Deskripsi dataset & fitur |
   | `\section{Metodologi}` | Penjelasan pipeline & formula |
   | `\section{Eksperimen dan Hasil}` | Baseline ladder, evaluasi |
   | `\section{Analisis Spasial dan Rekomendasi Flow}` | Interpretasi spasial & studi kasus |
   | `\section{Clustering, Fairness, dan Studi Kasus}` | Klaster & subgroup analysis |
   | `\section{Kesimpulan}` | Temuan utama, keterbatasan, saran |

3. Simpan, lalu recompile:
   ```bash
   bash reports/compile_report.sh
   ```

> **PERINGATAN:** Jika kamu regenerate `.tex` via `build_report_latex.py` setelah edit manual, semua perubahan manual akan **tertimpa**. Simpan salinan cadangan jika perlu, atau edit langsung kode generator (Skenario 3).

---

### Skenario 3: Ubah Struktur / Template (Kode Generator)

Untuk perubahan struktural (tambah section baru, ubah format tabel, tambah gambar, ubah urutan):

1. **Edit** `src/build_report_latex.py` -- cari fungsi yang relevan:

   | Fungsi | Menghasilkan |
   |--------|-------------|
   | `gen_header()` | Preamble LaTeX + title/author |
   | `gen_abstract()` | Abstrak + kata kunci |
   | `gen_section_pendahuluan()` | Section Pendahuluan |
   | `gen_section_kajian_terkait()` | Section Kajian Terkait |
   | `gen_section_dataset()` | Section Dataset + tabel source_status |
   | `gen_section_metodologi()` | Section Metodologi + formula |
   | `gen_section_eksperimen()` | Section Eksperimen + gambar/model comparison |
   | `gen_section_analisis_spasial()` | Section Analisis Spasial + tabel flows |
   | `gen_section_clustering()` | Section Clustering + Fairness + Studi Kasus |
   | `gen_section_kesimpulan()` | Section Kesimpulan |
   | `gen_daftar_pustaka()` | Bibliografi |
   | `df_to_latex_table()` | Helper: konversi DataFrame ke LaTeX table |
   | `figure_cmd()` | Helper: generate `\includegraphics` |

2. Setelah edit, regenerate + recompile:
   ```bash
   uv run python src/build_report_latex.py --team-id "..." ...
   bash reports/compile_report.sh
   ```

---

### Skenario 4: Ubah Metadata Tim (Identitas)

Hanya ganti nama tim, anggota, pembimbing, tanpa mengubah konten paper:

```bash
cd "DATA MINING - Penambangan Data/PanganFlow-ID"

uv run python src/build_report_latex.py \
    --team-id "TST002" \
    --team-name "NamaTimBaru" \
    --member1 "Nama Baru 1" \
    --member2 "Nama Baru 2" \
    --member3 "Nama Baru 3" \
    --pembimbing "Pembimbing Baru"

bash reports/compile_report.sh
```

Semua konten tetap sama, hanya header + author block yang berubah.

---

### Skenario Alternatif: Paper DOCX (Non-LaTeX)

Jika tidak ingin menggunakan LaTeX:

```bash
cd "DATA MINING - Penambangan Data/PanganFlow-ID"
uv run python src/build_formal_report.py
```

Output: `reports/GEMASTIK XVIII Penambangan Data - ID_TIM - NAMA_TIM - PanganFlow.ID.docx`

File DOCX ini juga bisa dikonversi ke PDF via Microsoft Word / LibreOffice.

---

## Dashboard

PanganFlow.ID Watchboard -- dashboard interaktif berbasis Streamlit dengan 5 panel:

```bash
cd "DATA MINING - Penambangan Data/PanganFlow-ID"
uv run streamlit run dashboard/app.py
```

**5 Panel Dashboard:**
1. **Peta** centroid tekanan beras nasional dengan kode warna prioritas
2. **Ranking** provinsi prioritas dengan alasan tekstual
3. **Flow** rekomendasi panah asal-tujuan dengan skor prioritas
4. **Profil** detail provinsi (harga, defisit, surplus, anomaly score)
5. **Validasi** status sumber data & pengecekan kualitas

---

## Dokumen Perencanaan

| File | Deskripsi |
|------|-----------|
| [`PLAN.md`](PLAN.md) | Decision engine, scoring rubrik, topic cards (DengueCast-X 91, EduDrop-ID 87, JudolFlow-X 84), pipeline architecture, decision checklist |
| [`PLAN-JUDOL.md`](PLAN-JUDOL.md) | Variasi plan spesifik untuk DengueCast-X + JudolFlow-X |
| [`possible-idea.md`](possible-idea.md) | Brainstorming awal: 7 ide topik dengan scoring detail + rekomendasi final |
| [`PanganFlow-ID/panganflow-spec.md`](DATA%20MINING%20-%20Penambangan%20Data/PanganFlow-ID/panganflow-spec.md) | Spesifikasi riset final: judul, masalah, dataset, formulasi fitur, metode, evaluasi, dashboard, batasan |
| [`Panduan-GEMASTIK-2025-Data-Mining.pdf`](Panduan-GEMASTIK-2025-Data-Mining.pdf) | Panduan resmi GEMASTIK XVIII Divisi Data Mining |
| [`Winner-Level GEMASTIK Data Mining Playbook-1.pdf`](Winner-Level%20GEMASTIK%20Data%20Mining%20Playbook-1.pdf) | Playbook strategi pemenang historis |

---

## Tim

| Anggota | Peran | Institusi |
|---------|-------|-----------|
| Muhamad Kemal Faza | Ketua Tim (Corresponding Author) | FSM Universitas Diponegoro |
| Muchammad Yuda Tri Ananda | Anggota | FSM Universitas Diponegoro |
| Muhammad Akmal Fazli Riyadi | Anggota | FSM Universitas Diponegoro |
| Henri Tantyoko | Dosen Pembimbing | FSM Universitas Diponegoro |

---

## Environment & Tools

| Tool | Versi | Kegunaan |
|------|-------|----------|
| Python | 3.12+ | Runtime |
| uv | latest | Package manager (recommended) |
| pandas | 2.2+ | Data wrangling |
| scikit-learn | 1.6+ | Random Forest, Isolation Forest, K-Means, PCA |
| matplotlib | 3.10+ | Visualisasi statis |
| plotly | 6.0+ | Visualisasi peta interaktif |
| streamlit | 1.45+ | Dashboard interaktif |
| shap | 0.46+ | Explainability (SHAP values) |
| python-docx | 1.1+ | Generate DOCX report |
| pdflatex | (system) | Compile LaTeX ke PDF |

---

## Catatan Penting

- Pipeline menggunakan **uv** sebagai package manager. Jika pakai `pip`, gunakan `requirements.txt`.
- Data snapshot di `data/raw/` adalah fallback jika API publik tidak tersedia. Status snapshot dicatat di `reports/tables/source_status.csv`.
- Paper PDF final HARUS diberi nama sesuai format GEMASTIK:
  `GEMASTIK XVIII Penambangan Data - <ID Tim> - <Nama Tim> - <Judul>.pdf`
- Maksimum ukuran file: 10 MB.
- Paper WAJIB orisinal (bukan GenAI murni), belum pernah dipublikasikan termasuk untuk kompetisi lain.
- Tools / library / framework / Generative AI **diperbolehkan** sebagai alat bantu.
