import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ==========================================
# 1. CARGA Y LIMPIEZA DE DATOS (PROCESAMIENTO)
# ==========================================


@st.cache_data  # Mantiene los datos en memoria para que la app cargue rápido
def load_and_clean_data():
    # Leer los datos originales
    df = pd.read_csv('vehicles_us.csv')

    # Ajuste de tipos de datos iniciales
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)

    # Manejo de categorías en paint_color
    df['paint_color'] = df['paint_color'].astype('category')
    if 'unknown' not in df['paint_color'].cat.categories:
        df['paint_color'] = df['paint_color'].cat.add_categories('unknown')
    df['paint_color'] = df['paint_color'].fillna('unknown')

    # Manejo de nulos: Medianas y Modas redondeadas por modelo
    df['model_year'] = df.groupby('model')['model_year'].transform(
        lambda x: x.fillna(
            round(x.median()) if not pd.isna(x.median()) else 2010)
    ).astype('Int64')

    df['cylinders'] = df.groupby('model')['cylinders'].transform(
        lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 6)
    ).astype('Int64')

    df['odometer'] = df.groupby('model_year')['odometer'].transform(
        lambda x: x.fillna(x.median()))
    df['odometer'] = df['odometer'].fillna(df['odometer'].median())

    # Filtro de outliers y valores extremos para un análisis más realista
    df_clean = df[(df['price'] >= 500) & (df['price'] <= 100000)]
    df_clean = df_clean[(df_clean['odometer'] <= 300000) &
                        (df_clean['model_year'] >= 1995)]

    return df_clean


# Cargamos el dataset procesado
car_data_clean = load_and_clean_data()


# ==========================================
# 2. INTERFAZ DE USUARIO EN STREAMLIT
# ==========================================

st.title('Anuncios de Vehículos Usados')


# Crear las casillas de verificación
hist_checkbox = st.checkbox('Mostrar Distribución de Precios')
scatter_checkbox = st.checkbox('Mostrar Kilometraje vs. Precio')
box_checkbox = st.checkbox('Mostrar Precios por Condición')

# --- LÓGICA DEL HISTOGRAMA ---
if hist_checkbox:
    st.subheader('Distribución de Precios de Venta')

    fig_hist = go.Figure()
    fig_hist.add_trace(go.Histogram(
        x=car_data_clean['price'],
        nbinsx=50,
        marker_color='#1f77b4',
        opacity=0.75
    ))
    fig_hist.update_layout(
        title='<b>¿Cómo se distribuyen los precios de venta de los autos?</b>',
        xaxis_title='Precio ($)',
        yaxis_title='Cantidad de Anuncios',
        template='plotly_white',
        bargap=0.05
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# --- LÓGICA DEL SCATTER PLOT ---
if scatter_checkbox:
    st.subheader('Análisis de Devaluación (Kilometraje vs Precio)')

    # Muestreo de rendimiento para que Plotly no sature el navegador web del usuario
    df_sample = car_data_clean.sample(
        n=min(2000, len(car_data_clean)), random_state=42)

    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(
        x=df_sample['odometer'],
        y=df_sample['price'],
        mode='markers',
        marker=dict(
            size=7,
            # Convertido a float para la escala de color de Plotly
            color=df_sample['model_year'].astype(float),
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Año del Modelo")
        ),
        text=df_sample['model']
    ))
    fig_scatter.update_layout(
        title='<b>Relación entre Kilometraje (Odometer) y Precio</b>',
        xaxis_title='Kilometraje Recorrido',
        yaxis_title='Precio ($)',
        template='plotly_white'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- LÓGICA DEL BOXPLOT ---
if box_checkbox:
    st.subheader('Análisis de Rangos por Estado del Vehículo')

    fig_box = go.Figure()
    condiciones_ordenadas = ['new', 'like new',
                             'excellent', 'good', 'fair', 'salvage']

    for condicion in condiciones_ordenadas:
        df_cond = car_data_clean[car_data_clean['condition'] == condicion]
        fig_box.add_trace(go.Box(
            y=df_cond['price'],
            name=condicion,
            boxpoints='outliers',
            marker=dict(size=4)
        ))

    fig_box.update_layout(
        title='<b>Distribución y Rangos de Precios según la Condición del Auto</b>',
        xaxis_title='Condición Declarada',
        yaxis_title='Precio ($)',
        template='plotly_white',
        showlegend=False
    )
    st.plotly_chart(fig_box, use_container_width=True)
