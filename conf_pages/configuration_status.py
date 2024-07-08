import streamlit as st
from scripts import initial_configuration

initial_configuration.set_initial_configuration()

st.title("Estado de la configuración")

# Pixel conversion
pixel_conversion_text = "Conversión de pixeles a metros: "
if st.session_state.pixel_conversion:
    pixel_conversion_text += "_Realizada_"
else:
    pixel_conversion_text += "_No realizada_"

# Load files
files_loaded_text = "Archivos cargados: "
if st.session_state.files_loaded:
    files_loaded_text += "_Sí_"
else:
    files_loaded_text += "_No_"

# Load mesh
mesh_loaded_text = "Malla cargada: "
if st.session_state.mesh_loaded:
    mesh_loaded_text += "_Sí_"
else:
    mesh_loaded_text += "_No_"

# Mesh projection
mesh_projection_text = "Proyección de malla: "
if st.session_state.mesh_projection:
    mesh_projection_text += "_Realizada_"
else:
    mesh_projection_text += "_No realizada_"

# Write the content
status_text = f"* {pixel_conversion_text}\n* {files_loaded_text}\n* {mesh_loaded_text}\n* {mesh_projection_text}"
st.write(status_text)
