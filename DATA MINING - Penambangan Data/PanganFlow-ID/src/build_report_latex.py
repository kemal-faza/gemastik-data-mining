#!/usr/bin/env python3
"""
build_report_latex.py -- Generate GEMASTIK technical report in LaTeX (.tex).
Reads CSV data from reports/tables/, populates tables and figures,
outputs a self-contained .tex file ready for manual editing or Overleaf.

Usage:
  python src/build_report_latex.py [--team-id ID] [--team-name NAME]
                                   [--member1 "Nama"] [--member2 "Nama"]
                                   [--member3 "Nama"] [--pembimbing "Nama"]
                                   [--output reports/panganflow_report.tex]
"""

from __future__ import annotations
import argparse, json, math, re, textwrap
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "reports" / "tables"
FIGURE_DIR = ROOT / "reports" / "figures"

# === GLOBALS (overridable via CLI) ===
TEAM_ID = "ID_TIM"
TEAM_NAME = "NAMA_TIM"
MEMBER_1 = "Nama Ketua Tim"
MEMBER_2 = "Nama Anggota 2"
MEMBER_3 = "Nama Anggota 3"
PEMBIMBING = "Nama Pembimbing"

# === HELPERS ===
def fmt(v: Any, decimals: int = 3) -> str:
    """Format a value for LaTeX table cell."""
    if isinstance(v, float):
        if abs(v) >= 1000:
            return f"{v:,.0f}"
        return f"{v:.{decimals}f}"
    return str(v).replace("%", "\\%").replace("_", "\\_").replace("&", "\\&")


def escape_tex(text: str) -> str:
    """Escape special LaTeX characters."""
    return text.replace("\\", "\\\\").replace("&", "\\&") \
               .replace("%", "\\%").replace("_", "\\_") \
               .replace("{", "\\{").replace("}", "\\}") \
               .replace("#", "\\#").replace("$", "\\$") \
               .replace("~", "\\textasciitilde{}")


def load_df(name: str) -> pd.DataFrame:
    path = TABLE_DIR / name
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def df_to_latex_table(df: pd.DataFrame, caption: str, label: str,
                       max_rows: int | None = None,
                       font_size: str = "\\footnotesize",
                       col_format: str | None = None) -> str:
    """Convert a DataFrame to a LaTeX table environment."""
    if df.empty:
        return f"% Table {label}: no data\\n"
    if max_rows and len(df) > max_rows:
        df = df.head(max_rows)

    cols = list(df.columns)
    if col_format is None:
        col_format = "l" + "r" * (len(cols) - 1)

    lines = [f"  {font_size}", f"  \\caption{{{escape_tex(caption)}}}", f"  \\label{{{label}}}",
             f"  \\begin{{tabular}}{{{col_format}}}",
             "    \\toprule",
             "    " + " & ".join(escape_tex(str(c)) for c in cols) + " \\\\",
             "    \\midrule"]
    for _, row in df.iterrows():
        row_str = " & ".join(fmt(row[c]) for c in cols)
        lines.append("    " + row_str + " \\\\")
    lines.append("    \\bottomrule")
    lines.append("  \\end{tabular}")
    return "\\begin{table}[t]\n" + "\n".join(lines) + "\n\\end{table}\n"


def figure_cmd(path: Path, caption: str, label: str, width: str = "0.48\\columnwidth") -> str:
    if not path.exists():
        return f"% Figure {label}: {path.name} not found\n"
    # figures/ direktori sama dengan lokasi .tex (reports/)
    from_report = "figures/" + path.name
    return (
        f"\\begin{{figure}}[t]\n"
        f"  \\centering\n"
        f"  \\includegraphics[width={width}]{{{from_report}}}\n"
        f"  \\caption{{{escape_tex(caption)}}}\n"
        f"  \\label{{{label}}}\n"
        f"\\end{{figure}}\n"
    )


def section(title: str, content: str) -> str:
    return f"\\section{{{title}}}\n{content}\n"


# === DATA LOADING ===

def load_inputs() -> dict[str, pd.DataFrame | dict]:
    data: dict[str, Any] = {}
    data["dataset_summary"] = load_df("dataset_summary.csv")
    data["metrics"] = load_df("metrics_summary.csv")
    data["ranking"] = load_df("ranking_snapshot.csv")
    data["flows"] = load_df("flow_recommendations.csv")
    data["ablation"] = load_df("feature_ablation.csv")
    data["clusters"] = load_df("cluster_summary.csv")
    data["fairness"] = load_df("subgroup_fairness.csv")
    data["stability"] = load_df("ranking_stability.csv")
    data["cases"] = load_df("case_studies.csv")
    data["err_region"] = load_df("error_analysis_region.csv")
    data["err_province"] = load_df("error_analysis_province.csv")
    data["source_status"] = load_df("source_status.csv")
    data["importance"] = load_df("feature_importance.csv")

    # Load JSON summary
    json_path = TABLE_DIR / "dataset_summary.json"
    if json_path.exists():
        with open(json_path) as f:
            data["summary_json"] = json.load(f)
    else:
        data["summary_json"] = {}

    return data


# === SECTION GENERATORS ===

def gen_header() -> str:
    lines = [
        "\\documentclass[journal, a4paper]{IEEEtran}",
        "\\IEEEoverridecommandlockouts",
        "\\usepackage{graphicx}",
        "\\usepackage{booktabs}",
        "\\usepackage{times}",
        "\\usepackage{amsmath}",
        "\\usepackage{hyperref}",
        "\\usepackage[tableposition=top]{caption}",
        f"\\hypersetup{{pdfauthor={{{escape_tex(MEMBER_1)}, {escape_tex(MEMBER_2)}, {escape_tex(MEMBER_3)}}}, pdfsubject={{GEMASTIK XVIII Data Mining}}, colorlinks=true, citecolor=blue, urlcolor=blue}}",
        "\\graphicspath{{./}}",
        "\\setlength{\\parindent}{1em}",
        "\\setlength{\\parskip}{0.5ex}",
        "",
        "\\begin{document}",
        "",
        "\\title{PanganFlow.ID: Penambangan Pola Surplus-Defisit dan Rekomendasi",
        "       Redistribusi Beras Antarprovinsi Berbasis Disparitas Harga,",
        "       Produksi, dan Konsumsi}",
        "",
        f"\\author{{{escape_tex(MEMBER_1)}$^{{1}}$, {escape_tex(MEMBER_2)}$^{{2}}$, {escape_tex(MEMBER_3)}$^{{3}}$,",
        f"    {escape_tex(PEMBIMBING)}$^{{4}}$",
        "\\thanks{Corresponding author: " + escape_tex(MEMBER_1) + ", email: email@institusi.ac.id}}",
        "\\maketitle",
        "",
    ]
    return "\n".join(lines)


def gen_abstract(summary: pd.DataFrame, summary_json: dict) -> str:
    row = summary.iloc[0] if not summary.empty else {}
    rows = int(row.get("rows", summary_json.get("rows", 0)))
    provinces = int(row.get("province_count", summary_json.get("province_count", 0)))
    date_min = str(row.get("date_min", summary_json.get("date_min", "")))
    date_max = str(row.get("date_max", summary_json.get("date_max", "")))
    lines = [
        "\\begin{abstract}",
        f"  \\textbf{{Intisari---}}Ketahanan pangan tidak hanya ditentukan oleh kecukupan stok nasional, "
        f"tetapi juga oleh ketimpangan harga, produksi, kebutuhan, dan akses antarwilayah. "
        f"Penelitian ini mengusulkan PanganFlow.ID, sistem penambangan data untuk mendeteksi "
        f"provinsi dengan tekanan pasokan beras dan menyusun prioritas aliran redistribusi "
        f"antarprovinsi. Dataset yang dibangun mencakup {rows:,} baris panel provinsi-bulan "
        f"untuk {provinces} provinsi pada periode {date_min} sampai {date_max}. "
        f"Metode yang digunakan meliputi deteksi anomali (Isolation Forest), estimasi surplus-defisit, "
        f"Random Forest ranking, K-Means clustering, dan graph-based redistribution scoring. "
        f"Hasil sistem berupa ranking provinsi prioritas, tipologi wilayah, serta rekomendasi "
        f"pasangan provinsi surplus menuju provinsi defisit yang dapat dipakai sebagai bahan "
        f"tinjauan kebijakan.",
        "\\end{abstract}",
        "",
        "\\textbf{\\textit{Kata kunci -- Data Mining, Beras, Ketahanan Pangan, ",
        "Redistribusi, Anomaly Detection, Ranking.}}",
        "",
    ]
    return "\n".join(lines)

def gen_section_pendahuluan() -> str:
    return section("Pendahuluan", textwrap.dedent("""\
    Indonesia secara nasional memiliki kecukupan beras, namun disparitas harga antarprovinsi
    menunjukkan bahwa distribusi pangan tidak merata. Data Bapanas periode 2021--2025
    mencatat harga beras medium di Papua Pegunungan mencapai Rp25.500/kg, hampir dua kali
    lipat harga di Jawa Timur yang hanya Rp12.742/kg. Selisih ini tidak dapat dijelaskan
    oleh biaya transportasi semata, melainkan mencerminkan ketimpangan struktural antara
    provinsi surplus dan defisit produksi.

    Dari 38 provinsi yang dipantau, 14 provinsi mencatat surplus produksi beras
    (didominasi Jawa dan Sulawesi Selatan), sementara 24 provinsi lainnya mengalami defisit.
    Wilayah Maluku-Papua menjadi yang paling rentan: dari 8 provinsi di region tersebut,
    seluruhnya mencatat defisit produksi dengan harga di atas median nasional.
    Kondisi kepulauan Indonesia membuat ketimpangan pasokan ini menjadi masalah spasial
    sekaligus temporal yang memerlukan pendekatan data mining multi-sumber.

    Tujuan penelitian ini adalah membangun sistem data mining yang menjawab tiga pertanyaan:
    (1) provinsi mana yang menunjukkan tekanan pasokan beras tertinggi, (2) provinsi mana
    yang relatif surplus dan berpotensi sebagai sumber redistribusi, serta (3) pasangan
    asal-tujuan mana yang layak ditinjau lebih dulu untuk aliran redistribusi. Manfaat
    praktisnya adalah menyediakan ranking prioritas dan rekomendasi aliran yang dapat
    digunakan sebagai bahan tinjauan kebijakan oleh analis ketahanan pangan.

    Batasan penelitian ini meliputi: (1) komoditas dibatasi pada Beras Medium agar
    estimasi surplus-defisit konsisten dengan data produksi BPS; (2) neraca surplus-defisit
    merupakan proxy struktural dari data tahunan produksi dan konsumsi, bukan mencerminkan
    stok aktual bulanan; (3) rekomendasi aliran adalah prioritas tinjauan kebijakan, bukan
    keputusan distribusi final.
    """))

def gen_section_kajian_terkait() -> str:
    return section("Kajian Terkait", textwrap.dedent("""\
    Prediksi harga pangan dan deteksi anomali telah banyak diteliti dalam literatur data mining.
    Sediyono dan Hartomo (2025) mengembangkan integrated framework untuk multi-commodity
    agricultural price forecasting dan anomaly detection menggunakan Transformer-based models
    dengan attention-boosted LSTM-VAE [1]. Pendekatan serupa dengan semantic dan temporal fusion
    untuk commodity price shock early warning juga telah dieksplorasi menggunakan agentic
    generative AI [2].

    Di Indonesia, beberapa studi membandingkan model LSTM, Random Forest, dan SVR untuk
    prediksi harga beras di Sumatera Selatan, dengan hasil bahwa LSTM unggul untuk data
    time-series [3]. Di Jawa Barat, perbandingan ARIMA, Regresi Linear, Random Forest, dan
    LSTM untuk harga beras medium harian menemukan bahwa ensemble methods memberikan
    keseimbangan akurasi dan interpretabilitas [4]. Pengaruh cuaca terhadap harga beras di
    Jawa Timur juga telah dimodelkan menggunakan LSTM, menunjukkan bahwa fitur meteorologis
    meningkatkan akurasi prediksi [5].

    Dari sisi ensemble learning, stacking untuk prediksi harga beras nasional menunjukkan
    bahwa kombinasi model dapat mengungguli model tunggal [6]. Sementara itu, deep learning
    hybrid untuk forecasting produksi beras di Indonesia memberikan perspektif berbeda karena
    berfokus pada ketersediaan pasokan, bukan harga [7]. Di tingkat distribusi, analisis
    spasial-temporal untuk logistik rantai dingin produk pertanian menunjukkan pentingnya
    faktor geografis dalam perencanaan distribusi pangan [8]. Penelitian crop redistribution
    secara global menunjukkan bahwa optimasi spasial dapat meningkatkan produksi sambil
    mengurangi tekanan sumber daya [9]. Model spatial equilibrium untuk perdagangan
    antarwilayah pada distribusi gandum menunjukkan bahwa price signal dan biaya transportasi
    adalah faktor kunci dalam aliran komoditas [10].

    Kesenjangan utama dalam literatur yang ada adalah: (1) sebagian besar studi fokus pada
    prediksi harga titik (point forecasting) di satu provinsi, bukan ranking prioritas
    multi-provinsi; (2) belum ada penelitian yang mengintegrasikan sinyal harga, neraca
    produksi-konsumsi, dan jarak geografis ke dalam satu sistem rekomendasi aliran
    redistribusi untuk pangan Indonesia; (3) belum ada studi data mining di Indonesia yang
    membingkai masalah pangan sebagai ranking prioritas intervensi. PanganFlow.ID mengisi
    kesenjangan ini dengan menggabungkan anomaly detection, surplus-deficit proxy estimation,
    Random Forest ranking, dan graph-based redistribution scoring menjadi pipeline terpadu.
    """))

def gen_section_dataset(summary: pd.DataFrame, source_status: pd.DataFrame) -> str:
    row = summary.iloc[0] if not summary.empty else {}
    content = ""
    content += (
        f"Dataset final berbentuk panel provinsi-bulan-komoditas sebanyak "
        f"{int(row.get('rows', 0)):,} baris, mencakup {int(row.get('province_count', 0))} "
        f"provinsi dan periode {row.get('date_min', '')} sampai {row.get('date_max', '')}. "
        f"Komoditas v1 dibatasi pada Beras Medium agar perhitungan surplus-defisit konsisten "
        f"dengan data produksi beras BPS dan konsumsi beras per kapita.\n\n"
    )
    content += df_to_latex_table(
        source_status[["source", "status", "rows"]].head(6) if not source_status.empty else pd.DataFrame(),
        "Status sumber data resmi dan snapshot.",
        "tab:source_status", font_size="\\scriptsize"
    )
    content += "\n"
    content += (
        "Kebutuhan beras diproksikan sebagai populasi dikalikan konsumsi beras per kapita "
        "tahunan. Surplus proxy dihitung sebagai produksi beras tahunan dikurangi kebutuhan "
        "tahunan. Karena stok awal, arus masuk, arus keluar, dan cadangan tidak selalu tersedia "
        "terbuka pada resolusi provinsi-bulan, nilai ini diperlakukan sebagai proxy struktural.\n"
    )
    return section("Dataset dan Formulasi Masalah", content)


def gen_section_metodologi() -> str:
    return section("Metodologi", textwrap.dedent("""\
    Pipeline PanganFlow.ID terdiri atas enam tahap. Pertama, harga beras medium dari Bapanas
    diproses menjadi fitur gap terhadap median nasional, perubahan harga 1 dan 3 bulan,
    rolling mean 3 bulan, rolling standard deviation 6 bulan, dan z-score historis 6 bulan.
    Kedua, data produksi beras BPS dikombinasikan dengan estimasi kebutuhan (populasi x
    konsumsi per kapita 81,23 kg/tahun) untuk menghasilkan skor defisit dan skor surplus
    per provinsi. Ketiga, Isolation Forest dengan contamination 18\\% digunakan untuk
    mendeteksi provinsi dengan sinyal anomali harga.

    Keempat, Random Forest (n\\textunderscore{}estimators=260, min\\textunderscore{}samples\\textunderscore{}leaf=3,
    random\\textunderscore{}state=42) mempelajari prioritas pemantauan bulan berikutnya dari fitur
    bulan berjalan menggunakan temporal split (15\\% terakhir sebagai holdout). Kelima,
    K-Means (k=4, 20 init) dengan PCA 2 komponen digunakan untuk memetakan tipologi provinsi
    berdasarkan skor harga dan neraca. Keenam, setiap pasangan provinsi surplus-defisit
    diberi skor graf dengan formula:

    \\begin{equation}
    \\begin{aligned}
    \\text{priority\\_score} =\\ & 0.31 \\times \\text{price\\_gap} + 0.27 \\times \\text{deficit} \\\\
    & + 0.23 \\times \\text{surplus} + 0.14 \\times \\text{model} \\\\
    & + 0.10 \\times \\text{anomaly} - 0.15 \\times \\text{distance}
    \\end{aligned}
    \\end{equation}

    Model akhir menggabungkan weighted priority index transparan dengan prediksi Random
    Forest melalui formula hybrid: $\\text{score} = 0.72 \\times \\text{weighted\\_index} + 0.28
    \\times \\text{rf\\_prediction\\_norm}$.

    Lima baseline digunakan sebagai pembanding:
    \\begin{enumerate}
        \\item Ranking acak sebagai batas bawah.
        \\item Price-gap ranking untuk efek disparitas harga.
        \\item Deficit ranking untuk efek neraca.
        \\item Weighted priority index transparan.
        \\item Random Forest ranker dengan split temporal.
    \\end{enumerate}
    """))

def gen_section_eksperimen(metrics: pd.DataFrame, ablation: pd.DataFrame,
                           importance: pd.DataFrame, err_region: pd.DataFrame,
                           err_province: pd.DataFrame) -> str:
    content = ""
    content += textwrap.dedent("""\
    Untuk mengevaluasi performa model, lima baseline digunakan sebagai pembanding:
    random ranking, price-gap baseline, deficit baseline, weighted priority index,
    dan model hybrid PanganFlow. Metrik utama adalah NDCG@10 yang mengukur kualitas
    ranking provinsi prioritas. Precision@10 dan Recall@10 melengkapi sebagai metrik
    operasional yang menunjukkan seberapa akurat peringkat teratas.

    Tabel \\ref{tab:metrics} dan Gambar \\ref{fig:model_comparison} menunjukkan
    bahwa model hybrid PanganFlow mencapai NDCG@10 sebesar 0,937, mengungguli
    weighted index (0,929) dan seluruh baseline lainnya. Meskipun lift terhadap
    weighted index relatif kecil (0,9\\%), Random Forest menangkap interaksi non-linear
    antar fitur yang tidak dapat ditangkap oleh indeks linear transparan.

    Tabel \\ref{tab:ablation} menyajikan kontribusi masing-masing kelompok fitur.
    Fitur neraca (balance) adalah kontributor terbesar -- tanpa fitur ini NDCG@10
    turun dari 0,905 menjadi 0,880. Fitur spasial memberikan kontribusi paling kecil,
    karena efek kedekatan geografis sudah tercakup oleh region grouping.

    Gambar \\ref{fig:feature_importance} dan Gambar \\ref{fig:shap_summary}
    mengonfirmasi bahwa fitur harga dan neraca mendominasi prediksi model, dengan
    surplus\\_proxy\\_ton dan price\\_gap\\_score sebagai dua fitur paling penting.
    Analisis error (Tabel \\ref{tab:error}) menunjukkan bahwa provinsi di region
    Maluku-Papua memiliki error tertinggi, mencerminkan volatilitas data yang lebih
    tinggi di wilayah timur Indonesia.
    """)

    # Metrics table
    if not metrics.empty:
        m = metrics[["model", "ndcg_at_k", "precision_at_k", "recall_at_k"]].copy()
        m["model"] = m["model"].str.replace("Weighted priority index", "Weighted index")
        m["model"] = m["model"].str.replace("PanganFlow hybrid model", "PanganFlow")
        content += df_to_latex_table(m, "Hasil evaluasi ranking provinsi prioritas.",
                                     "tab:metrics") + "\n"

    # Model comparison figure
    content += figure_cmd(FIGURE_DIR / "model_comparison.png",
                          "Perbandingan NDCG@10 antar model.", "fig:model_comparison") + "\n"

    # Ablation table
    if not ablation.empty:
        content += df_to_latex_table(ablation, "Ablation study keluarga fitur.",
                                     "tab:ablation") + "\n"

    # Feature importance figure
    content += figure_cmd(FIGURE_DIR / "feature_importance.png",
                          "Feature importance model prioritas.", "fig:feature_importance") + "\n"

    # SHAP figure
    content += figure_cmd(FIGURE_DIR / "shap_summary.png",
                          "SHAP summary plot -- kontribusi fitur terhadap output model.",
                          "fig:shap_summary") + "\n"

    # Error analysis table
    if not err_province.empty:
        ep = err_province[["province", "region", "mae", "rmse"]].head(5)
        content += df_to_latex_table(ep, "Top-5 provinsi dengan error tertinggi.",
                                     "tab:error") + "\n"

    return section("Eksperimen dan Hasil", content)


def gen_section_analisis_spasial(flows: pd.DataFrame) -> str:
    content = ""
    content += textwrap.dedent("""\
    Ranking provinsi dan rekomendasi aliran dihasilkan melalui graph-based scoring yang
    mempertimbangkan price gap, surplus asal, defisit tujuan, dan jarak logistik.
    Sistem tidak mengklaim rute operasional final; keluaran adalah antrian review
    untuk melihat provinsi yang layak diperiksa lebih dulu.

    Hasil menunjukkan bahwa Papua Pegunungan menjadi tujuan pada 5 dari 6 flow
    prioritas tertinggi. Hal ini dapat dijelaskan oleh kombinasi harga tertinggi
    nasional (Rp25.500/kg), defisit produksi proxy sebesar 0,12 juta ton, dan
    anomaly score 0,102 -- menjadikannya provinsi paling kritis secara objektif.
    Sulawesi Selatan menempati peringkat pertama sebagai asal karena surplus
    produksi terbesar (2,31 juta ton) dengan harga relatif rendah (Rp12.919/kg).

    Pola yang menarik adalah dominasi provinsi dari region Maluku-Papua dalam
    peringkat prioritas: 7 dari 10 provinsi prioritas tertinggi berasal dari region
    ini. Ini bukan artefak bias model, melainkan cerminan objektif kondisi
    lapangan: seluruh provinsi di Maluku-Papua mencatat defisit produksi dan harga
    di atas median nasional, dengan jarak yang sangat jauh dari sentra produksi
    di Jawa dan Sulawesi.

    Untuk flow lintas region seperti Sulawesi menuju Papua, jarak yang mencapai
    ribuan kilometer tercermin dalam penalti $distance\\_penalty$ (-0,15) pada
    formula scoring. Dalam kasus ini, price gap yang sangat besar (Rp12.581/kg)
    dan surplus asal yang melimpah (2,31 juta ton) masih cukup untuk mengkompensasi
    jarak, menjadikan Sulawesi Selatan-Papua Pegunungan sebagai flow skor tertinggi.
    """)
    if not flows.empty:
        fv = flows[["rank", "origin_province", "destination_province",
                     "priority_score"]].head(6)
        content += df_to_latex_table(fv, "Top rekomendasi aliran beras.",
                                     "tab:flows") + "\n"

        for _, flow in flows.head(3).iterrows():
            reasons = str(flow.get("top_reasons", ""))
            content += (
                f"Flow peringkat {int(flow['rank'])}: {flow['origin_province']} menuju "
                f"{flow['destination_province']} memperoleh skor "
                f"{float(flow['priority_score']):.1f}. Alasan utama: {escape_tex(reasons)}.\n"
            )

    content += "\n" + figure_cmd(FIGURE_DIR / "pressure_centroid_map.png",
"Peta centroid tekanan beras nasional.",
"fig:pressure_map") + "\n"
    content += figure_cmd(FIGURE_DIR / "flow_network.png",
"Visualisasi graph recommendation antarprovinsi.",
"fig:flow_network") + "\n"
    content += figure_cmd(FIGURE_DIR / "top_flow_recommendations.png",
"Top-10 rekomendasi aliran beras.",
"fig:top_flows") + "\n"

    # Merge: Dashboard content
    content += textwrap.dedent("""\
    \\textbf{Implementasi Dashboard.} PanganFlow.ID dilengkapi dashboard berbasis
    Streamlit sebagai alat eksplorasi dan presentasi hasil. Dashboard terdiri dari
    lima panel: peta centroid tekanan beras, daftar peringkat provinsi, rekomendasi
    flow dengan panah asal-tujuan, profil detail provinsi, dan panel validasi dataset.
    Setiap flow dilengkapi alasan tekstual seperti ``selisih harga Rp12.581/kg; asal
    surplus proxy 2,31 juta ton'' untuk memudahkan interpretasi. Dashboard dapat
    dijalankan dengan perintah:
    \\texttt{python dashboard/app.py}.
    """)
    content += figure_cmd(FIGURE_DIR / "dashboard_preview.png",
                          "Pratinjau dashboard PanganFlow.ID.",
                          "fig:dashboard", width="0.45\\columnwidth")

    return section("Analisis Spasial dan Rekomendasi Flow", content)

def gen_section_clustering(clusters: pd.DataFrame, fairness: pd.DataFrame, cases: pd.DataFrame,
                            stability: pd.DataFrame) -> str:
    content = ""

    if not clusters.empty:
        cv = clusters[["cluster_label", "province_count", "avg_deficit_score",
                        "avg_surplus_score"]].copy()
        content += df_to_latex_table(cv, "Ringkasan cluster provinsi.", "tab:clusters") + "\n"

    content += figure_cmd(FIGURE_DIR / "cluster_pca.png",
                           "PCA cluster provinsi.", "fig:cluster_pca") + "\n"

    if not fairness.empty:
        fv = fairness[["region", "top10_count", "top10_share", "avg_priority_score"]]
        content += df_to_latex_table(fv, "Pemeriksaan subgroup berdasarkan region.",
                                     "tab:fairness") + "\n"

    if not cases.empty:
        cv2 = cases[["province", "recommended_origin", "interpretation"]]
        content += df_to_latex_table(cv2, "Studi kasus provinsi prioritas.",
                                     "tab:cases", font_size="\\scriptsize") + "\n"

    if not stability.empty:
        overlap = stability["mean_top10_overlap"].iloc[0]
        content += (
            f"Stability check dengan perturbasi skor menghasilkan rata-rata overlap Top-10 "
            f"sebesar {overlap:.3f}. Nilai ini menunjukkan ranking relatif stabil.\n"
        )

    return section("Clustering, Fairness, dan Studi Kasus", content)


def gen_section_dashboard() -> str:
    content = textwrap.dedent("""\
    Dashboard PanganFlow.ID dibangun menggunakan Streamlit sebagai alat eksplorasi
    dan presentasi hasil. Tampilan utama terdiri dari lima panel: (1) peta
    centroid tekanan beras nasional dengan skor prioritas sebagai kode warna;
    (2) daftar peringkat provinsi prioritas dengan alasan tekstual; (3) rekomendasi
    flow dengan panah asal-tujuan; (4) profil detail setiap provinsi mencakup harga,
    skor defisit, skor surplus, dan anomaly score; serta (5) panel validasi dataset
    yang menampilkan source status dan validation checks.

    Desain dashboard menempatkan rekomendasi sebagai prioritas review manusia,
    bukan instruksi distribusi otomatis. Setiap flow dilengkapi alasan tekstual
    seperti \"selisih harga Rp12.581/kg; asal surplus proxy 2,31 juta ton\" untuk
    memudahkan interpretasi oleh pengguna non-teknis. Dashboard dapat dijalankan
    dengan perintah:\\newline
    \\texttt{python dashboard/app.py}.
    """)
    content += figure_cmd(FIGURE_DIR / "dashboard_preview.png",
                                  "Pratinjau dashboard PanganFlow.ID.",
                                  "fig:dashboard", width="0.45\\columnwidth")
    return section("Dashboard dan Implementasi", content)

def gen_section_keterbatasan() -> str:
    return section("Keterbatasan", textwrap.dedent("""\
    \\begin{itemize}
        \\item Neraca surplus-defisit memakai proxy tahunan; stok awal, cadangan, arus
              masuk, dan arus keluar belum dimodelkan penuh.
        \\item Harga Bapanas bulanan lebih stabil untuk reproduksi, tetapi tidak sedetail
              harga harian PIHPS.
        \\item Jarak centroid hanya proxy biaya logistik; moda transportasi, pelabuhan,
              gudang, dan kapasitas distribusi belum masuk.
        \\item Model ranking mempelajari proxy prioritas, bukan ground-truth kebijakan resmi.
    \\end{itemize}
    """))

def gen_section_kesimpulan() -> str:
    return section("Kesimpulan", textwrap.dedent("""\
    PanganFlow.ID berhasil menunjukkan bahwa data harga, produksi, konsumsi, dan spasial
    dapat diintegrasikan menjadi sistem data mining yang menghasilkan output lebih kaya
    daripada prediksi harga tunggal. Model hybrid PanganFlow mencapai NDCG@10 sebesar
    0,937, mengungguli keempat baseline (random, price-gap, deficit, dan weighted index).

    Ablation study mengungkapkan bahwa fitur neraca (balance) adalah kontributor terbesar
    terhadap performa model -- tanpa fitur ini, NDCG@10 turun dari 0,905 menjadi 0,880
    (penurunan 2,8\\%). Fitur spasial memberikan kontribusi paling kecil (tanpa spatial:
    NDCG@10=0,912), yang dapat dijelaskan karena adjacency effect sudah sebagian
    tercakup oleh nested region grouping.

    Analisis error menunjukkan bahwa Maluku-Papua memiliki MAE tertinggi (0,098),
    dengan Papua Pegunungan sebagai provinsi paling sulit diprediksi (MAE=0,202).
    Ini wajar mengingat volatilitas harga dan ketimpangan data di region timur
    Indonesia. Stabilitas ranking diverifikasi dengan bootstrap 120 run, menghasilkan
    rata-rata overlap Top-10 sebesar 0,863.

    Pengembangan lanjutan dapat mencakup penambahan data stok riil, cadangan
    pemerintah, kalender panen, dan indikator gangguan transportasi untuk
    meningkatkan akurasi rekomendasi flow. Multi-komoditas (cabai, bawang, telur)
    juga dapat ditambahkan setelah data produksi dan konsumsi yang konsisten tersedia.

    Keterbatasan penelitian ini meliputi: (1) neraca surplus-defisit merupakan proxy
    tahunan dari data BPS, bukan mencerminkan stok aktual bulanan; (2) harga Bapanas
    bulanan lebih stabil untuk reproduksi tetapi tidak sedetail harga harian PIHPS;
    (3) jarak centroid hanya proxy biaya logistik, belum mempertimbangkan moda
    transportasi, pelabuhan, dan kapasitas gudang; (4) model ranking mempelajari
    proxy prioritas berbasis data historis, bukan ground-truth kebijakan resmi.
    """))
def gen_daftar_pustaka() -> str:
    refs = [
        "E. Sediyono and D. Hartomo, ``An Integrated Framework for Multi-Commodity Agricultural Price Forecasting and Anomaly Detection,'' Semantic Scholar, 2025.",
        "``Temporal and Semantic Fusion with Agentic AI for Commodity Price Shock Forecasting,'' \\href{https://arxiv.org/abs/2508.06497}{arXiv:2508.06497}, 2025.",
        "``Perbandingan Kinerja LSTM, Random Forest, dan SVR untuk Prediksi Harga Beras,'' JURIKOM, 2024.",
        "``Komparasi Model ARIMA, Regresi Linear, Random Forest, dan LSTM untuk Prediksi Harga Beras,'' JIT Nurulfikri, 2024.",
        "``Rice Price Prediction in East Java Based on Weather Using LSTM,'' JAIC Polibatam, 2025.",
        "``Performance Evaluation of Ensemble Learning Stacking in Rice Price Prediction,'' \\href{https://doi.org/10.1109/10957374}{IEEE, 2024}.",
        "``Advanced Deep Learning and Hybrid Models for Forecasting Rice Production in Indonesia,'' ITS Scholar, 2024.",
        "``Forecasting and Spatial Distribution Analysis of Cold Chain Logistics,'' \\href{https://doi.org/10.1007/s10668-025-06969-9}{Springer, 2025}.",
        "``Crop Redistribution Increases Regional Production While Reducing Resource Use,'' MDPI Agronomy, 15(9), 2148, 2025.",
        "``Spatial Equilibrium Model-Based Optimization for Inter-Regional Grain Trade,'' Water Supply, 22(5), 5393, \\href{https://iwaponline.com/ws/article/22/5/5393}{2022}.",
        "L. Breiman, ``Random Forests,'' Machine Learning, 45(1), 5--32, \\href{https://doi.org/10.1023/A:1010933404324}{2001}.",
        "F. T. Liu, K. M. Ting, and Z. H. Zhou, ``Isolation Forest,'' \\href{https://doi.org/10.1109/ICDM.2008.17}{ICDM, 2008}.",
        "J. MacQueen, ``Some Methods for Classification and Analysis of Multivariate Observations,'' \\href{https://projecteuclid.org/euclid.bsmsp/1200512992}{Berkeley Symposium, 1967}.",
        "Bank Indonesia, ``Pusat Informasi Harga Pangan Strategis Nasional,'' \\href{https://www.bi.go.id/hargapangan}{bi.go.id/hargapangan}.",
        "Badan Pangan Nasional, ``Rata-rata Harga Pangan Bulanan Tingkat Konsumen Provinsi,'' \\href{https://satudata.badanpangan.go.id}{satudata.badanpangan.go.id}.",
        "Badan Pusat Statistik, ``Produksi Padi dan Beras Menurut Provinsi,'' \\href{https://www.bps.go.id}{bps.go.id}, 2024.",
        "Badan Pusat Statistik, ``Pengeluaran untuk Konsumsi Penduduk Indonesia per Provinsi,'' \\href{https://www.bps.go.id}{bps.go.id}, 2024.",
    ]
    lines = ["\\begin{thebibliography}{99}"]
    for i, ref in enumerate(refs, start=1):
        lines.append(f"  \\bibitem{{{i}}} {ref}")
    lines.append("\\end{thebibliography}")
    return "\n".join(lines) + "\n"


# === MAIN GENERATOR ===

def generate_report(output_path: Path) -> None:
    data = load_inputs()
    summary = data.get("dataset_summary", pd.DataFrame())
    summary_json = data.get("summary_json", {})
    metrics = data.get("metrics", pd.DataFrame())
    ablation = data.get("ablation", pd.DataFrame())
    flows = data.get("flows", pd.DataFrame())
    clusters = data.get("clusters", pd.DataFrame())
    fairness = data.get("fairness", pd.DataFrame())
    cases = data.get("cases", pd.DataFrame())
    stability = data.get("stability", pd.DataFrame())
    err_region = data.get("err_region", pd.DataFrame())
    err_province = data.get("err_province", pd.DataFrame())
    source_status = data.get("source_status", pd.DataFrame())
    importance = data.get("importance", pd.DataFrame())

    parts = []
    parts.append(gen_header())
    parts.append(gen_abstract(summary, summary_json))
    parts.append(gen_section_pendahuluan())
    parts.append(gen_section_kajian_terkait())
    parts.append(gen_section_dataset(summary, source_status))
    parts.append(gen_section_metodologi())
    parts.append(gen_section_eksperimen(metrics, ablation, importance, err_region, err_province))
    parts.append(gen_section_analisis_spasial(flows))
    parts.append(gen_section_clustering(clusters, fairness, cases, stability))
    parts.append(gen_section_kesimpulan())
    parts.append(gen_daftar_pustaka())
    parts.append("\\end{document}\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n\n".join(parts), encoding="utf-8")
    print(f"Report written: {output_path} ({output_path.stat().st_size:,} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GEMASTIK report in LaTeX.")
    parser.add_argument("--team-id", default="ID_TIM")
    parser.add_argument("--team-name", default="NAMA_TIM")
    parser.add_argument("--member1", default="Nama Ketua Tim")
    parser.add_argument("--member2", default="Nama Anggota 2")
    parser.add_argument("--member3", default="Nama Anggota 3")
    parser.add_argument("--pembimbing", default="Nama Pembimbing")
    parser.add_argument("--output", default=str(ROOT / "reports" / "panganflow_report.tex"))
    args = parser.parse_args()

    global TEAM_ID, TEAM_NAME, MEMBER_1, MEMBER_2, MEMBER_3, PEMBIMBING
    TEAM_ID = args.team_id
    TEAM_NAME = args.team_name
    MEMBER_1 = args.member1
    MEMBER_2 = args.member2
    MEMBER_3 = args.member3
    PEMBIMBING = args.pembimbing

    generate_report(Path(args.output))


if __name__ == "__main__":
    main()
