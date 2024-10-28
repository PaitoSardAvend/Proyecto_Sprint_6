import streamlit as st
import pandas as pd
import plotly.express as px
# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('D:/PS/ANALISIS DE DATOS/SPRINT 5/Proyecto_sprint_6/vehicles_us.csv')
# Crear un encabezado
st.header("Análisis de Datos de Vehículos")

# Casillas de verificación para seleccionar gráficos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Si la casilla de verificación para el histograma está seleccionada
if build_histogram:
    st.write('Construyendo un histograma para la columna odómetro')
    fig_histogram = px.histogram(car_data, x="odometer")  # Cambia "odometer" por la columna que quieras visualizar
    st.plotly_chart(fig_histogram)

# Si la casilla de verificación para el gráfico de dispersión está seleccionada
if build_scatter:
    st.write('Construyendo un gráfico de dispersión')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")  # Cambia "price" por la columna que quieras visualizar
    st.plotly_chart(fig_scatter)