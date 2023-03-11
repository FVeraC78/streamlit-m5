import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("App New York City - Fernando Vera A01625282")
@st.cache
def load_data(nrows):
    data = pd.read_csv('citibike-tripdata.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['started_at'] = pd.to_datetime(data['started_at'])
    return data

datos = load_data(500)

mostrartodo = st.sidebar.checkbox('Mostrar todos los registros')
if (mostrartodo):
    st.dataframe(datos)

mostrarhisto = st.sidebar.checkbox('Mostrar número de viajes por hora')
if (mostrarhisto):
    fig, ax = plt.subplots()
    ax.hist(datos['started_at'].dt.hour, bins=24,range=(0,24))
    st.header("Viajes comenzados por hora")
    st.pyplot(fig)
    st.markdown("___")

mostrarmapa = st.sidebar.checkbox('Mostrar mapa de viajes por hora')
if(mostrarmapa):
    datos.rename(columns={"start_lat": "lat", "start_lng": "lon"}, inplace = True)
    #Some number in the range 0-23
    hour_to_filter = st.slider('Hora', 0, 23, 17)
    filtered_data = datos[datos['started_at'].dt.hour == hour_to_filter]
    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)
