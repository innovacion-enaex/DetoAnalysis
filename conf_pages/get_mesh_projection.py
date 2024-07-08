import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Conversión de pixeles a metros")
st.caption("En esta página el usuario interactuará con la malla y una imagen para obtener la matriz de proyección de la imagen.")