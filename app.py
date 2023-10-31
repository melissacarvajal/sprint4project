#build the web app here with sreamlit

import streamlit as st
import pandas as pd
import plotly_express as px

# Leemos el conjunto de datos sobre los anuncios de ventas de coches
df_ads = pd.read_csv(r'C:\Users\david\Documents\Programacion\Web_App_Coin_Tosser\sprint4project\vehicles_us.csv')

st.header('¡Bienvenidx! Aquí encontrarás información sobre los coches que anunciamos')

hist_button = st.button('Construir histograma') # crear un botón para histograma
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(df_ads, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Mostrar un gráfico de dispersión') # crea un botón para gráfico dispersión

if disp_button:
    st.write('Creando un gráfico de dispersión para los anuncios de ventas de coches')
    fig_2 = px.scatter(df_ads, x='model_year', y='condition')
    st.plotly_chart(fig_2, use_container_width=True)