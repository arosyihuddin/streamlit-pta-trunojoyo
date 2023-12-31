import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo


add_logo("http://placekitten.com/150/150")
st.markdown("# Pengolahan Data")
selected = option_menu(
    menu_title="Pencarian dan Penambangan WEB",
    options=["Crawling", "Preprocessing", "VSM", "LDA", "Implementation"],
    icons=["data", "Process", "model", "implemen", "Test", "sa"],
    orientation="horizontal",
)
if "df" not in st.session_state:
    print("OKE")
    st.session_state.df = pd.read_csv("data/data_preprocessing.csv")
    st.session_state.df_onehot = pd.read_csv("data/OneHotEncoder.csv")
    st.session_state.df_tf_idf = pd.read_csv("data/TF IDF.csv")
    st.session_state.df_tf = pd.read_csv("data/Term Frequensi.csv")
    st.session_state.df_lf = pd.read_csv("data/Logarithm Frequensi.csv")
    st.session_state.df_lda = pd.read_csv('data/reduksi dimensi.csv')

if selected == "Crawling":
    st.write(
        'Dataset yang di ambil dari website pta.trunojoyo.ac.id dengan proses pengambilan menggunakan metode Crawling berikut adalah link colab untukk Cerawling datasetnya [Link Colab](https://colab.research.google.com/drive/1vHaVvp_g6eTXenmv8A44eJ0F8Zb3vCuz?usp=sharing)')

elif selected == "Preprocessing":
    st.write('pada tahap ini data dilakukan preprocessing dengan menggunakan beberapa tahap di antaranya')
    st.write("""
             1. Cleaning
             2. Tokenizing
             3. Stopword Removal
             4. Stemming (Opsional)""")
    st.write("berikut hasil dari proses preprocesing:")
    st.write(st.session_state.df)

elif selected == "VSM":
    onehot, tf_idf, tf, lf = st.tabs(['One Hot Encoding', 'TF IDF',
                                      'Term Frequensi', 'Logaritm Frequency'])

    with onehot:
        st.dataframe(st.session_state.df_onehot)

    with tf_idf:
        st.dataframe(st.session_state.df_tf_idf)

    with tf:
        st.dataframe(st.session_state.df_tf)

    with lf:
        st.dataframe(st.session_state.df_lf)

elif selected == "LDA":
    st.write("hasil reduksi dimensi :")
    st.dataframe(st.session_state.df_lda)

else:
    model = joblib.load("model/naive bayes.pkl")
    lda = joblib.load("model/lda.pkl")
    vectorizer = joblib.load("model/tf_vectorizer.pkl")

    abstrak = [st.text_input("Masukkan Abstrak")]
    button = st.button("Klasifikasikan")

    if button:
        x_new = vectorizer.transform(abstrak).toarray()
        lda_x = lda.transform(x_new)
        predictions = model.predict(lda_x)
        st.write("Abstrak termasuk dalam Kategori : ", predictions[0])
