import os
import json
from db import executar_comando
from datetime import *

# limpa a tela do terminal
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")

# procedimento para exibir titulo formatado
def exibir_titulo(title: str) -> None:
    largura = len(title) * 2
    print("=" * largura)
    print(title.center(largura).upper())
    print("=" * largura)

# função para cadastro de usuário no banco de dados
def cadastrar_usuario(login: str, senha: str) -> bool:
    select = "SELECT * FROM challenge_python_usuarios WHERE login = :1"
    resultado = executar_comando(select, {"1": login}, fetch=True)

    if resultado:
        return False
    else:
        sql = "INSERT INTO challenge_python_usuarios (login, senha) VALUES (:1, :2)"
        executar_comando(sql, {"1": login, "2": senha}, fetch=False)
        return True

# função para apagar um usuário do banco, através da opção 3 do menu de login no sistema principal. Retorna booleano de acordo com sucesso ou fracasso da solicitação
def apagar_usuario(email, senha) -> bool:
    select = "SELECT id_usuario FROM auralis_usuarios WHERE email = :1 AND senha = :2"
    resultado = executar_comando(select, {"1": email, "2": senha}, fetch=True)
    
    if not resultado:
        return False

    id_usuario = resultado[0][0]
    
    delete = "DELETE FROM auralis_usuarios WHERE id_usuario = :1"
    executar_comando(delete, {"1": id_usuario}, fetch=False)

    return True