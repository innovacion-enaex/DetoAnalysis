import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Crear perímetro de seguridad")
st.caption("Una vez realizadas las configuraciones, el usuario podrá generar una imagen anotada con el perímetro de seguridad.")