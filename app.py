
import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 🔗 API oficial - Estación Quinta Normal
url = 'https://climatologia.meteochile.gob.cl/application/productos/emaResumenDiario/330020'
response = requests.get(url)

st.write('Status code:', response.status_code)

if response.status_code == 200:
    data = response.json()
    valores = data['datos']['valoresMasRecientes']
    df = pd.DataFrame([valores])
    df['momento'] = pd.to_datetime(df['momento'])
    df = df.set_index('momento')
else:
    df = pd.DataFrame()
    st.error("Error al obtener datos desde la API")

# 📊 Visualización
st.title("🌦️ Últimos datos de la Estación Quinta Normal (Santiago)")

if not df.empty:
    st.dataframe(df.T)

    if 'temperatura' in df.columns:
        st.metric(label="🌡️ Temperatura actual", value=f"{df['temperatura'].iloc[0]} °C")

    if 'humedadRelativa' in df.columns:
        st.metric(label="💧 Humedad relativa", value=f"{df['humedadRelativa'].iloc[0]} %")

    if 'presion' in df.columns:
        st.metric(label="🌬️ Presión atmosférica", value=f"{df['presion'].iloc[0]} hPa")
else:
    st.warning("No hay datos disponibles para mostrar.")
