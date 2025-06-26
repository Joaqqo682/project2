import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analisis de anuncios de venta de coches")
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') 
     
if hist_button: 
    st.write("Creacion de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir grafico de dispersión')
if scatter_button:
    st.write("Grafico de dispersion: precio vs año")
    fig2 = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig2, use_container_width=True)
    