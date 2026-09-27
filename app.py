import pandas as pd  # Impotación de pandas como pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st  # Importación de streamlit como st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear una casilla de verificación en la aplicación Streamlit
hist_checkbox = st.checkbox('Construir histograma')

# Crear una casilla de verificación en la aplicación Streamlit
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_checkbox:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig = go.Figure(data=go.Scatter(
        x=car_data['model_year'], y=car_data['price'], mode='markers'))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Precio vs Año del Vehículo')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
