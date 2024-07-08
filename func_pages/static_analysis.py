import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Análisis estático")
st.caption("Una vez realizadas las configuraciones, el usuario podrá obtener imágenes con ciertos análisis estáticos.")
