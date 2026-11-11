# Bike Sharing Dashboard

Dashboard ini dibuat menggunakan Streamlit untuk memvisualisasikan data penyewaan sepeda (Bike Sharing Dataset). Dashboard ini berfokus pada analisis tren musiman dan segmentasi suhu udara terhadap jumlah penyewaan sepeda harian.

## Setup Environment

### Opsi 1: Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Opsi 2: Menggunakan Terminal/Command Prompt (venv bawaan Python)
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
python -m venv main-ds
.\main-ds\Scripts\activate
pip install -r requirements.txt
```

## Cara Menjalankan Dashboard (Run Streamlit App)

Pastikan Anda sudah berada di dalam virtual environment (main-ds), lalu jalankan perintah berikut di terminal:
```bash
streamlit run dashboard.py
```
