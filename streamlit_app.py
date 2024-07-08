"""
Files:
conf_pages conf_pages/configuration_status.py conf_pages/get_mesh_projection.py conf_pages/get_pixel_conversion.py conf_pages/load_files.py conf_pages/load_mesh.py func_pages func_pages/annotate_flyrocks.py func_pages/create_safety_perimeter.py func_pages/detonation_sequence.py func_pages/static_analysis.py
# List of material icons: https://material.io/resources/icons/?style=baseline
"""
import streamlit as st

pages_dict = {
    "Configuración":[
        st.Page("conf_pages/configuration_status.py", title="Status"), #, icon=":material/verified:"),
        st.Page("conf_pages/get_pixel_conversion.py", title="Pixel a metros"), #, icon=":material/flutter_dash:"),
        st.Page("conf_pages/load_files.py", title="Cargar archivos"), #, icon=":material/flutter_dash:"),
        st.Page("conf_pages/load_mesh.py", title="Cargar malla"), #, icon=":material/flutter_dash:"),
        st.Page("conf_pages/get_mesh_projection.py", title="Proyección de malla"), #, icon=":material/flutter_dash:"),
        ],
    "Funcionalidades":[
        st.Page("func_pages/create_safety_perimeter.py", title="Crear perímetro de seguridad"), #, icon=":material/label:"),
        st.Page("func_pages/annotate_flyrocks.py", title="Anotar flyrocks"), #, icon=":material/label:"),
        st.Page("func_pages/detonation_sequence.py", title="Secuencia de detonación"), #, icon=":material/label:"),
        st.Page("func_pages/static_analysis.py", title="Análisis estático"), #, icon=":material/label:"),
        ],
}

pg = st.navigation(pages_dict)
pg.run()