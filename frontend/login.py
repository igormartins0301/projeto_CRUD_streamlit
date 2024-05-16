import streamlit as st
import requests

# Função para fazer a requisição à API
def fazer_requisicao(email, senha):
    url = 'https://exemplo.com/api/login'
    payload = {'email': email, 'password': senha}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None

@st.cache
def salvar_token(token):
    return token

# Configuração da página
st.title('Bem-vindo!')

# Inputs para email e senha
email = st.text_input('Email')
senha = st.text_input('Senha', type='password')

# Botão de entrar
if st.button('Entrar'):
    token = fazer_requisicao(email, senha)
    # Salvar o token
    if token:
        salvar_token(token)
        st.success('Login bem-sucedido! Token salvo no cache.')
    else:
        st.error('Credenciais inválidas. Tente novamente.')
