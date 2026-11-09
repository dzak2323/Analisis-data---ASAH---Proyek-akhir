import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")

# Fungsi untuk memuat dan membersihkan data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season'] = df['season'].map(season_mapping)
    df['temp_group'] = pd.cut(df['temp'], bins=3, labels=['Rendah', 'Sedang', 'Tinggi'])
    # Menambahkan kolom tahun untuk filter interaktif
    df['year'] = df['yr'].map({0: '2011', 1: '2012'})
    return df

day_df = load_data()

# --- SIDEBAR (FITUR INTERAKTIF) ---
st.sidebar.title("🚲 Filter Data")
st.sidebar.markdown("Gunakan filter di bawah ini untuk berinteraksi dengan dashboard:")
# Fitur interaktif: Filter berdasarkan Tahun
selected_year = st.sidebar.selectbox(
    "Pilih Tahun:", 
    ["Semua Tahun", "2011", "2012"]
)

# Logika Filter
if selected_year == "Semua Tahun":
    filtered_df = day_df
else:
    filtered_df = day_df[day_df['year'] == selected_year]

# --- MAIN DASHBOARD ---
st.title("🚲 Dashboard Analisis Penyewaan Sepeda")
st.markdown("**Oleh:** Muhammad Dzaki Rifa'I (DS-01)")
st.markdown(f"**Menampilkan data untuk:** {selected_year}")
st.markdown("---")

tab1, tab2 = st.tabs(["Tren Musim", "Segmentasi Suhu"])

with tab1:
    st.subheader(f"Rata-rata Penyewaan Sepeda Berdasarkan Musim ({selected_year})")
    season_summary = filtered_df.groupby('season', observed=False)['cnt'].mean().reset_index().sort_values(by='cnt', ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=season_summary, palette="Blues_d", ax=ax)
    ax.set_xlabel("Musim", fontsize=12)
    ax.set_ylabel("Rata-rata Penyewaan", fontsize=12)
    st.pyplot(fig)

with tab2:
    st.subheader(f"Rata-rata Penyewaan Berdasarkan Kategori Suhu ({selected_year})")
    temp_summary = filtered_df.groupby('temp_group', observed=False)['cnt'].mean().reset_index().sort_values(by='cnt', ascending=False)
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(x='temp_group', y='cnt', data=temp_summary, palette="YlOrBr_r", ax=ax2)
    ax2.set_xlabel("Kategori Suhu", fontsize=12)
    ax2.set_ylabel("Rata-rata Penyewaan", fontsize=12)
    st.pyplot(fig2)