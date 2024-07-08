import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Cargar malla")
st.caption("En esta página el usuario carga la malla de la tronadura")

# Load files
file_mesh = st.file_uploader("Archivo de la malla", type=["txt"])
