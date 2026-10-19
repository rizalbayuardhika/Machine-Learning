import streamlit as st
import joblib
import numpy as np

# Header
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    page_icon="",
    layout="centered"
)

# Load model
model = joblib.load('model_rumah.pkl')

# Judul Utama
st.title(" Prediksi Harga Rumah")
st.markdown("---")
st.markdown(
    "Aplikasi ini menggunakan model *Machine Learning* (**Linear Regression**) "
    "untuk mengestimasi harga properti berdasarkan spesifikasi fisik dan lokasinya."
)

# Form Input
st.subheader("Masukkan Spesifikasi Rumah")

# Kolom
col1, col2 = st.columns(2)

with col1:
    luas_m2 = st.number_input('Luas Bangunan (m²)', min_value=0.0, value=0.0, step=5.0)
    kamar = st.number_input('Jumlah Kamar Tidur', min_value=0, max_value=10, value=0)
    kamar_mandi = st.number_input('Jumlah Kamar Mandi', min_value=0, max_value=10, value=0)

with col2:
    usia_rumah = st.number_input('Usia Rumah (Tahun)', min_value=0, max_value=100, value=0)
    jarak_kota_km = st.number_input('Jarak ke Pusat Kota (km)', min_value=0.0, value=0.0, step=0.5)

st.markdown("---")

# Tombol Prediksi
st.markdown("<br>", unsafe_allow_html=True)

# Tombol Tengah
if st.button('🚀 Hitung Estimasi Harga Rumah', use_container_width=True):
    # Menyusun input ke array
    data_baru = np.array([[luas_m2, kamar, kamar_mandi, usia_rumah, jarak_kota_km]])
    
    # Prediksi harga
    hasil_prediksi = model.predict(data_baru)
    
    st.markdown("### Hasil Prediksi:")
    st.success(f"Estimasi Harga Properti: **Rp {hasil_prediksi[0]:,.2f} Juta**")
    st.snow()
# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'> Kelompok 10</p>", unsafe_allow_html=True)