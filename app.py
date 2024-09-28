# Mengimpor libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as sns  
import io

# Page Configuration
st.set_page_config(
    page_title="Dashboard Data Diabetes Sheila",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# Load Data
data_diabetes = pd.read_csv('diabetes.csv')

# Sidebar untuk memilih tampilan
st.sidebar.title("Pilih Tampilan Data")
options = ["Keseluruhan Data", "Info Data", "Deskripsi Data", "Heatmap", "Distribusi Usia", "Visualisasi Outcome"]
selected_option = st.sidebar.selectbox("Silahkan pilih salah satu:", options)

# Menampilkan konten berdasarkan pilihan
if selected_option == "Keseluruhan Data":
    st.title('Data Diabetes')
    st.write("Tampilkan 15 baris pertama dari dataset:")
    st.dataframe(data_diabetes.head(15)) 

elif selected_option == "Info Data":
    st.title('Info Data Diabetes')
    st.write("Informasi tentang dataset:")
    buffer = io.StringIO()  
    data_diabetes.info(buf=buffer) 
    s = buffer.getvalue()  
    st.text(s)  

elif selected_option == "Deskripsi Data":
    st.title('Ringkasan Statistik Data Diabetes')
    st.write("Statistik deskriptif dari dataset:")
    st.dataframe(data_diabetes.describe()) 

elif selected_option == "Heatmap":
    st.title('Heatmap Correlation of Data Diabetes')
    fig, ax = plt.subplots()
    sns.heatmap(data_diabetes.corr(), annot=True, ax=ax)
    st.pyplot(fig)

elif selected_option == "Distribusi Usia":
    st.title('Histogram Distribusi Usia')
    plt.figure(figsize=(3, 2)) 
    sns.histplot(data=data_diabetes, x='Age', bins=20)
    plt.title('Distribusi Usia')
    plt.xlabel('Usia')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)  # Menampilkan plot di Streamlit

elif selected_option == "Visualisasi Outcome":
    st.title('Pie Chart dari Outcome Diabetes')
    outcome_counts = data_diabetes['Outcome'].value_counts()
    plt.figure(figsize=(4, 3)) 
    plt.pie(outcome_counts, labels=outcome_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribusi Outcome Diabetes')
    st.pyplot(plt) 
    plt.clf()
