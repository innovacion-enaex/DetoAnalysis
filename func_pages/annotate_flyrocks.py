import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Obtener flyrocks")
st.caption("Una vez realizadas las configuraciones, el usuario podrá anotar un archivo con los máximas trayectorias de flyrock.")