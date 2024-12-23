# Dashboard Penyewaan Sepeda ✨

## Deskripsi
Dashboard ini menyediakan analisis interaktif mengenai data penyewaan sepeda, termasuk statistik utama dan visualisasi berdasarkan musim, bulan, jam, dan faktor lainnya.

## Fitur Utama
* **Analisis Musiman:** Bandingkan penggunaan sepeda di setiap musim.
* **Tren Harian:** Visualisasi penggunaan sepeda per jam setiap hari.
* **Segmentasi Pengguna:** Analisis penggunaan sepeda berdasarkan tipe pengguna (anggota, pengunjung).
* **Filter Interaktif:** Sesuaikan tampilan dashboard berdasarkan kriteria yang Anda inginkan.

## Prasyarat
Pastikan Anda telah menginstal Python versi 3.7 atau lebih baru. Selain itu, Anda memerlukan beberapa pustaka Python berikut:
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Instalasi
1. **Clone repositori ini**:
   ```bash
git clone https://github.com/ariellacahyani/bike-sharing-dashboard
cd bike-sharing-dashboard

python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate     # Untuk Windows
pip install -r requirements.txt



## Run steamlit app
```
streamlit run dashboard.py
```