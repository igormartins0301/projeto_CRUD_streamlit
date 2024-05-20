import streamlit as st
import requests

def fazer_requisicao(form_data):
    url = 'http://127.0.0.1:8000/login/access-token/'
    response = requests.post(url, data=form_data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None


def show_login():
    st.title('Bem-vindo!')

    with st.form(key='login_form'):
        email = st.text_input('Email')
        senha = st.text_input('Senha', type='password')
        submit_button = st.form_submit_button('Entrar')

    if submit_button:
        form_data = {
            'username': email,
            'password': senha
        }
        token = fazer_requisicao(form_data)
        
        if token:
            st.session_state.token = token
            st.rerun()
        else:
            st.error('Credenciais inválidas. Tente novamente.')
