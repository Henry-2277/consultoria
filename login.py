import sqlite3
import base64
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

# Substitua 'seu_usuario' pelo seu nome de usuário e 'sua_senha' pela sua senha
nome = "teste"
senha = "12"

# Concatene o username e a senha separados por ':' conforme o formato "username:password"
credentials = f"{nome}:{senha}"

# Codifique as credenciais em Base64
base64_encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Imprima o resultado
print(base64_encoded_credentials)

# Função para conectar ao banco de dados SQLite
def get_db_conn():
    conn = sqlite3.connect("login.db")  # Alteração do nome do banco de dados
    return conn

security = HTTPBasic()

class arealogin(BaseModel):
    nome: str
    senha: str

def get_current_user(credentials: HTTPBasicCredentials = Depends(security), conn = Depends(get_db_conn)):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM arealogin WHERE nome=? AND senha=?", (credentials.username, credentials.password))
    user_data = cursor.fetchone()

    if user_data is None or user_data[2] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário inválido",
            headers={"WWW-Authenticate": "Basic"},
        )

    return arealogin(nome=user_data[1], senha=user_data[2])

@app.post("/registro/", status_code=status.HTTP_201_CREATED)
def registro_user(user: arealogin, conn = Depends(get_db_conn)):
    cursor = conn.cursor()

    # Verificar se o nome de usuário já existe no banco de dados
    cursor.execute("SELECT * FROM arealogin WHERE nome=?", (user.nome,))
    existing_user = cursor.fetchone()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário já existe",
        )

    # Inserir o novo usuário no banco de dados
    cursor.execute("INSERT INTO arealogin (nome, senha) VALUES (?, ?)", (user.nome, user.senha))
    conn.commit()
    return {"message": "Usuário criado com sucesso"}

@app.get("/login")
def login(user: arealogin = Depends(get_current_user)):
    return {"message": f"Bem-vindo, {user.nome}! Agora você está logado."}




