import streamlit as st
from cadastrar_produto.page import pagina_cadastro
from visualizar_produtos.page import pagina_visualizar_produtos
from login import show_login

def main():

    if 'token' not in st.session_state:
        show_login()
    else:
        menu = st.sidebar.selectbox('Selecione uma função:', 
                                    ['Cadastrar Produto', 'Visualizar Produtos'])

        if menu == 'Cadastrar Produto':
            pagina_cadastro()
        elif menu == 'Visualizar Produtos':
            pagina_visualizar_produtos()
    
if __name__ == '__main__':
    main()


