import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo

add_logo("http://placekitten.com/150/150")
st.snow()
st.markdown("# Home")
st.text("""
         Nama   : Ahmad Rosyihuddin
         NIM    : 200411100126
         Kelas  : Pencarian Dan Penambangan WEB
         """)
st.write("""
         Email  : arosyihuddin6@gmail.com\n
         Github : [Github Repositori](https://github.com/arosyihuddin/streamlit-pta-trunojoyo)
         """)

st.markdown("# Klasisfikasi Abstrak Tugas Akhir Universitas Trunojoyo Madura")

# Load Dataset
df = pd.read_csv("data/crawling_pta_labeled.csv")
st.write(df)
