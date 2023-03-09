import streamlit as st
import pandas as pd
from google.cloud import firestore
from google.oauth2 import service_account

##db = firestore.Client.from_service_account_json("names-project-demo2-fverac78.json")
##dbNames = db.collection("names")

import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="names-project-demo2-fverac78")

dbNames = db.collection("projects")

st.set_page_config(
    page_title="SS Tec de Mty 🐶",
    page_icon="🐶",
    initial_sidebar_state="expanded"
)
st.image("./índice.png", width=100)
st.title("Proyectos solidarios 🐶")
st.caption("Eliga su tipo de usuario a la izquierda")
#Algo para que seleccionen que persona son y poder darles acceso a diferentes secciones

usuario = st.sidebar.selectbox("Soy: ", ("Alumno", "SS", "Organización"))

if (usuario == "Organización"):
    st.header("Registro de proyectos solidarios")
    st.subheader("Si eres una organización de la sociedad civil interesada en reclutar alumnos del Tecnológico de Monterrey para tus proyectos, estás en el lugar indicado!")
    st.text("\n")
    st.markdown("Por favor introdusca los siguientes datos")
    correo = st.text_input("Correo electrónico de contacto")
    osf = st.text_input("Nombre de su Organización")
    proyecto = st.text_input("Nombre de su proyecto")
    desc = st.text_input("Descripción del proyecto")
    duracion = st.radio("Seleccione la duración del proyecto", ("5 semanas", "10 semanas", "15 semanas"))
    cupo = st.text_input("Indique el cupo máximo de alumnos para su proyecto")
    modalidad = st.selectbox("Seleccione la modalidad del proyecto", ("Remota", "Híbrida", "Presencial"))
    entrevista = st.checkbox("¿Requiere entrevista previa con los interesados?")

    submit = st.button("Crear nuevo registro")

    if submit and correo and osf and proyecto and desc and duracion and cupo and modalidad and entrevista:
        doc_ref = db.collection("projects").document(proyecto)
        doc_ref.set({"correo" : correo, "osf" : osf, "proyecto" : proyecto, "desc" : desc, "duracion" : duracion, "cupo" : cupo, "modalidad" : modalidad, "entrevista" : entrevista})
        st.sidebar.write("Registro insertado correctamente")

    project_ref = list(db.collection(u'projects').stream())
    project_dict = list(map(lambda x: x.to_dict(), project_ref))
    project_dataframe = pd.DataFrame(project_dict)
    st.dataframe(project_dataframe)

    def loadByName(project):
        project_ref = dbNames.where(u'proyecto', u'==', proyecto)
        currentName = None
        for myproj in project_ref.stream():
            currentName = myproj
        return currentName

    st.sidebar.subheader('Buscar proyecto')
    nameSearch = st.sidebar.text_input("Nombre del proyecto")
    btnFiltrar = st.sidebar.button("Buscar")

    if nameSearch and btnFiltrar:
        doc = loadByName(nameSearch)
        if doc is None:
            st.sidebar.write("Nombre no existe")
        else:
            st.sidebar.write(doc.to_dict())

    #st.sidebar.markdown("""___""")
    #btnEliminar = st.sidebar.button("Eliminar")

    #if btnEliminar:
    #    deletename = loadByName(nameSearch)
    #    if deletename is None:
    #        st.sidebar.write(f"{nameSearch} no existe")
    #    else:
    #        dbNames.document(deletename.id).delete()
    #        st.sidebar.write(f"{nameSearch} eliminado")

    #st.sidebar.markdown("""___""")
    #newname = st.sidebar.text_input("Actualizar nombre")
    #btnActualizar = st.sidebar.button("Actualizar")

    #if btnActualizar:
    #    updatename = loadByName(nameSearch)
    #    if updatename is None:
    #        st.write(f"{nameSearch} no existe")
    #    else:
    #        myupdatename = dbNames.document(updatename.id)
    #        myupdatename.update( { "name": newname })
    #        st.write(f"{nameSearch} actualizado con {newname}")
            