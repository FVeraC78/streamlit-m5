import streamlit as st
import pandas as pd

@st.cache
def load_data(nrows):
    datos = pd.read_csv('movies.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    datos.rename(lowercase, axis='columns', inplace=True)
    
    return datos

st.title('Netflix app')
st.markdown('Done using st.cache')

datos = load_data(500)

mostrar_but = st.sidebar.checkbox('Mostrar todos los filmes')
if (mostrar_but):
    st.header('Todos los filmes')
    st.dataframe(datos)

def search_movie(nombre_peli):
    st.header('Título del filme')
    pelis = datos[datos['name'].str.lower().str.contains(nombre_peli)]
    st.dataframe(pelis)

def filter_director(director):
    st.header('Filtrado por director')
    pelis_dire = datos[datos['director'].str.contains(director)]
    st.dataframe(pelis_dire)

nombre_peli = st.sidebar.text_input('Título del filme')
nombre_peli = nombre_peli.lower()
buscarpeli_but = st.sidebar.button('Buscar filmes')

if (buscarpeli_but):
    search_movie(nombre_peli)

nombre_dire = st.sidebar.selectbox('Selecciona director', datos['director'].unique())
dire_but = st.sidebar.button('Filtrar por director')

if (dire_but):
    filter_director(nombre_dire)

