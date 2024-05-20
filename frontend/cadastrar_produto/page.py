import streamlit as st
import requests

def cadastrar_produto(produto_data):
    url = 'http://127.0.0.1:8000/products/'
    response = requests.post(url, json=produto_data)
    
    if response.status_code == 200:
        return 'Produto cadastrado'
    else:
        return None
    
    
def pagina_cadastro():
    st.title('Cadastro de Produto')

    with st.form(key='cadastro_produto_form'):
        produto = st.text_input('Nome do Produto')
        preco = st.number_input('Preço', value=0.0)
        vendedor = st.text_input('Nome do Vendedor')
        descricao = st.text_area('Descrição')
        quantidade = st.number_input('Quantidade', value=0)
        
        submit_button = st.form_submit_button('Cadastrar Produto')

    if submit_button:
        produto_data = {
            'produto': produto,
            'preco': preco,
            'vendedor': vendedor,
            'descricao': descricao,
            'quantidade': quantidade
        }
        
        message = cadastrar_produto(produto_data)
        
        if message:
            st.success(message)
        else:
            st.error('Erro ao cadastrar o produto. Tente novamente.')
