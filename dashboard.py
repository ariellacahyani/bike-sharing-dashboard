import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Setting
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load Dataset
df = pd.read_csv('https://raw.githubusercontent.com/ariellacahyani/bike-sharing-dashboard/refs/heads/main/day.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/ariellacahyani/bike-sharing-dashboard/refs/heads/main/hour.csv')


# Kolom nama musim
df['season_corrected'] = df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Dashboard Title
st.title("📊 Dashboard Analisis Data Penyewaan Sepeda 🚴")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect(
    "Pilih Musim:",
    options=df['season_corrected'].unique(),
    default=df['season_corrected'].unique()
)

selected_month = st.sidebar.slider(
    "Pilih Bulan:",
    min_value=int(df['mnth'].min()),
    max_value=int(df['mnth'].max()),
    value=(int(df['mnth'].min()), int(df['mnth'].max()))
)

# Sidebar untuk filter dataset hourly
st.sidebar.header("Filter Data Hourly")
selected_hour_season = st.sidebar.multiselect(
    "Pilih Musim (Hourly):",
    options=hour_df['season_corrected'].unique(),
    default=hour_df['season_corrected'].unique()
)

selected_hour = st.sidebar.slider(
    "Pilih Jam:",
    min_value=int(hour_df['hr'].min()),
    max_value=int(hour_df['hr'].max()),
    value=(int(hour_df['hr'].min()), int(hour_df['hr'].max()))
)

# Filter Data
filtered_df = df[(df['season_corrected'].isin(selected_season)) & 
                 (df['mnth'] >= selected_month[0]) & 
                 (df['mnth'] <= selected_month[1])]

# Statistik
st.markdown("## **Statistik Utama**")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Permintaan Sepeda", int(filtered_df['cnt'].sum()))
with col2:
    st.metric("Rata-Rata Suhu", round(filtered_df['temp'].mean(), 2))
with col3:
    st.metric("Rata-Rata Kelembapan", round(filtered_df['hum'].mean(), 2))

# Visualisasi 1: Permintaan Sepeda Berdasarkan Musim
st.markdown("### **Permintaan Sepeda Berdasarkan Musim**")
season_summary = filtered_df.groupby('season_corrected')['cnt'].sum().reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x='season_corrected', y='cnt', data=season_summary, palette='coolwarm', ax=ax1)
ax1.set_title("Total Permintaan Sepeda Berdasarkan Musim", fontsize=14)
ax1.set_xlabel("Musim", fontsize=12)
ax1.set_ylabel("Total Permintaan Sepeda (cnt)", fontsize=12)
st.pyplot(fig1)

# Visualisasi 2: Hubungan Suhu dan Permintaan Sepeda
st.markdown("### **Hubungan Suhu dan Permintaan Sepeda**")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(x='temp', y='cnt', data=filtered_df, color='blue', alpha=0.5, ax=ax2)
sns.regplot(x='temp', y='cnt', data=filtered_df, scatter=False, color='red', ax=ax2)
ax2.set_title("Hubungan Suhu dan Permintaan Sepeda", fontsize=14)
ax2.set_xlabel("Suhu Normalized (temp)", fontsize=12)
ax2.set_ylabel("Total Permintaan Sepeda (cnt)", fontsize=12)
st.pyplot(fig2)

# Visualisasi 3: Permintaan Berdasarkan Bulan
st.markdown("### **Permintaan Sepeda Berdasarkan Bulan**")
month_summary = filtered_df.groupby('mnth')['cnt'].sum().reset_index()
fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.lineplot(x='mnth', y='cnt', data=month_summary, marker="o", ax=ax3)
ax3.set_title("Total Permintaan Sepeda Berdasarkan Bulan", fontsize=14)
ax3.set_xlabel("Bulan", fontsize=12)
ax3.set_ylabel("Total Permintaan Sepeda (cnt)", fontsize=12)
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig3)

# Visualisasi 4: Hubungan Kelembapan dan Permintaan
st.markdown("### **Hubungan Kelembapan dan Permintaan Sepeda**")
fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.scatterplot(x='hum', y='cnt', data=filtered_df, color='green', alpha=0.5, ax=ax4)
sns.regplot(x='hum', y='cnt', data=filtered_df, scatter=False, color='red', ax=ax4)
ax4.set_title("Hubungan Kelembapan dan Permintaan Sepeda", fontsize=14)
ax4.set_xlabel("Kelembapan Normalized (hum)", fontsize=12)
ax4.set_ylabel("Total Permintaan Sepeda (cnt)", fontsize=12)
st.pyplot(fig4)

# Informasi Tambahan
st.sidebar.markdown("### **Catatan**")
st.sidebar.info("""
Dashboard ini memberikan analisis interaktif berdasarkan data penyewaan sepeda.
Gunakan filter di sidebar untuk menyesuaikan visualisasi sesuai kebutuhan Anda.
""")

