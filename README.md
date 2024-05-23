# Projeto CRUD Fullstack

![image](/pic/foto.png)

## Pré-requisitos
1. Banco de Dados Postgres no render, passo a passo no link (https://www.linkedin.com/feed/update/urn:li:activity:7136743523554373632/) 
2. MongoDBCompass

## Passos para executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/igormartins0301/projeto_CRUD_streamlit.git
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.3
pyenv local 3.12.3
```

3. Crie um ambiente virtual para o projeto:

```bash
python -m venv venv
venv/scripts/activate
```

4. Instale as dependencias do projeto:

```bash
python.exe -m pip install --upgrade pip

pip install -r requirements.txt
```

5. Crie o seu banco de dados postgres no Render ou Local e preencha o .env conforme o exemplo

6. Suba o servidor backend com o comando 

```bash
cd backend
uvicorn main:app --reload
```

7. Suba o frontend com o comando 
```bash
cd frontend
streamlit run app.py
```

8. Acesse o endpoint http://127.0.0.1:8000/docs
- Vá até a opção de POST /users/ Create User Route
- Try it out
- Crie um usuário

9. Acesse o endpoint do streamlit e faça login com o usuário e senha criado e utilize os métodos existentes.

