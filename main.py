import streamlit as st
from PIL import Image

image = Image.open("./assets/kirby_nerd.jpg")

st.markdown(
    """
# Diccionario Métodos Numéricos II
**Proyecto final**

---

## Integrantes:
- Araujo Palestina Claudio Hassiel
- Hernández Rodríguez Alejandro
- Torreblanca Cespedes Aldo E

## Temas:
- Newton
- Casi-Newton
- Gradiente 
"""
)

st.image(image, caption="Nosotros comprendiendo Newton", width=240)

# Texto que aparece en la barra lateral
st.sidebar.markdown(
    """
# Diccionario

**Proyecto final de metodos numericos 2**
- Araujo Palestina Claudio Hassiel
- Hernández Rodríguez Alejandro
- Torreblanca Cespedes Aldo E
"""
)
