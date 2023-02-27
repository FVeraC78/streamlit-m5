import streamlit as st 

st.title('App con sidebar')

sidebar = st.sidebar
sidebar.title ("Titulo de barra lateral")
sidebar.write ("Aca van los elementos del sidebar")

st.header ("Header 1")
st.header ("Header 2")
st.write ("aca va la informaccion de la seccion principal")