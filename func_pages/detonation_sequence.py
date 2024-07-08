import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Secuencia de detonación")
st.caption("Una vez realizadas las configuraciones, el usuario podrá obtener un video/imagenes del secuenciamiento de la detonación.")
