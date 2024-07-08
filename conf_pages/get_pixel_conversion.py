import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Conversión de pixeles a metros")
st.caption("En esta página el usuario interactuará con una imagen para realizar la conversión de pixeles a metros.")