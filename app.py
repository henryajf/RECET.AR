import streamlit as st
import streamlit.components.v1 as components

# 1. Configurar layout a lo ancho completo
st.set_page_config(page_title="RECET.AR", layout="wide", initial_sidebar_state="collapsed")

# 2. Inyectar CSS para ocultar bordes, menú superior y el padding nativo de Streamlit
st.markdown("""
    <style>
        /* Eliminar espacio blanco alrededor del iframe */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        /* Ocultar elementos de la interfaz de Streamlit */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

with open("receta.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 3. Mostrar HTML incrustado. 
# Bajar a 800-850 asegura que no se genere el scroll principal de la ventana del navegador.
components.html(html_data, height=800, scrolling=True)