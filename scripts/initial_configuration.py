import streamlit as st

def set_initial_configuration():
    # Wide layout
    try:
        st.set_page_config(layout="wide")
    except:
        pass
    # Setup the initial state of the app
    st.session_state.pixel_conversion = False
    st.session_state.files_loaded = False
    st.session_state.mesh_loaded = False
    st.session_state.mesh_projection = False    
