import streamlit as st

def bienvenida(nombre):
    mimensaje = 'Bienvenido/a : ' + nombre
    return mimensaje

myname = st.text_input("Nombre : ")

if (myname):
    mensaje = bienvenida(myname)
    st.write(f" Resultado : {mensaje}")


