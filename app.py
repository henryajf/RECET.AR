import streamlit as st
import streamlit.components.v1 as components

# Configurar la página de Streamlit
st.set_page_config(page_title="RECET.AR", layout="wide")

# Leer tu archivo HTML
with open("receta.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Mostrar el HTML incrustado
# El parámetro height asegura que la hoja A4 tenga espacio suficiente en la pantalla
components.html(html_data, height=1200, scrolling=True)
