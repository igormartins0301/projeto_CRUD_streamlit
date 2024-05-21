import streamlit as st
import requests
import pandas as pd

def obter_produtos():
    url = 'http://127.0.0.1:8000/protected/'
    headers = {
    "Authorization": f"Bearer {st.session_state.token}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def pagina_protegido():
    st.title('protegido')
    produtos = obter_produtos()

    if produtos:
        st.text(produtos)
    else:
        st.error('Erro ao obter a lista de produtos. Tente novamente.')
