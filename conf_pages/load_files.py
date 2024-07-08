import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Cargar archivos")
st.caption("En esta página el usuario carga 2 archivos de configuración de tronadura")

# Load files
file_1 = st.file_uploader("Archivo de configuración 1", type=["txt"])

file_2 = st.file_uploader("Archivo de configuración 2", type=["txt"])