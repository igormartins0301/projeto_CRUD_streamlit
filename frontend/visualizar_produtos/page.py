import streamlit as st
import requests
import pandas as pd

def obter_produtos():
    url = 'http://127.0.0.1:8000/products/'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def pagina_visualizar_produtos():
    st.title('Lista de Produtos')
    produtos = obter_produtos()

    if produtos:
        st.write('Produtos Cadastrados:')
        st.write('---')
        
        # Transformar a resposta JSON em um DataFrame do Pandas
        df = pd.DataFrame(produtos)
        st.write(df)
    else:
        st.error('Erro ao obter a lista de produtos. Tente novamente.')

