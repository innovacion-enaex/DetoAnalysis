import streamlit as st

is_admin = st.checkbox("Admin mode")

# Using a dict of pages
# List of material icons: https://material.io/resources/icons/?style=baseline
pages_dict = {
    "English":[
        st.Page("pages/page_1.py"),
        st.Page("pages/page_2.py", title="A name for the page 2", icon="🔥"),
        ],
    "Español":[
        st.Page("paginas/pagina_1.py", icon=":material/flutter_dash:"),
        ],
}

if is_admin:
    pages_dict["Admin"] = [
        st.Page("pages/admin_page.py", icon=":material/lock_open:"),
    ]

pg = st.navigation(pages_dict)
pg.run()

# Improvements:
# - Pages can be grouped by language or any other criteria.
# - The pages can be defined dynamically