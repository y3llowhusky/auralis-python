import os
import json
from db import executar_comando

usuario = {
    "nome": None,
    "email": None,
    "senha": None,
    "genero": None,
    "data nascimento": None
}

# função para cadastro de usuário no banco de dados
def cadastrar_usuario(email: str, senha: str) -> bool:
    select = "SELECT * FROM auralis_usuarios WHERE email = :1"
    resultado = executar_comando(select, {"1": email}, fetch=True)

    if resultado:
        return False
    else:
        sql = "INSERT INTO auralis_usuarios (email, senha) VALUES (:1, :2)"
        executar_comando(sql, {"1": email, "2": senha}, fetch=False)
        return True

# função para apagar um usuário do banco, através da opção 3 do menu de email no sistema principal. Retorna booleano de acordo com sucesso ou fracasso da solicitação
def apagar_usuario(email, senha) -> bool:
    select = "SELECT id_usuario FROM auralis_usuarios WHERE email = :1 AND senha = :2"
    resultado = executar_comando(select, {"1": email, "2": senha}, fetch=True)
    
    if not resultado:
        return False

    id_usuario = resultado[0][0]
    
    delete = "DELETE FROM auralis_usuarios WHERE id_usuario = :1"
    executar_comando(delete, {"1": id_usuario}, fetch=False)

    return True

# função para verificar se email e senha digitados correspondem a algum valor no banco de dados
def verificar_login(email: str, senha: str) -> int | None:
    sql = "SELECT * FROM auralis_usuarios WHERE email = :1 AND senha = :2"
    resultado = executar_comando(sql, {"1": email, "2": senha}, fetch=True)

    # verifica se query retornou um usuário, se sim instancia variável para guardar id do usuário, se não retorna falso.
    if resultado:
        global usuario_logado_id
        usuario_logado_id = resultado[0][0]
        return usuario_logado_id
    return None

# função para apagar dados do usuário do banco de dados
def apagar_dados_usuario(id_usuario) -> None:
    executar_comando("DELETE FROM auralis_registros WHERE id_usuario = :1", {"1": id_usuario})
    executar_comando("DELETE FROM auralis_feedbacks WHERE id_usuario = :1", {"1": id_usuario})
    executar_comando("DELETE FROM auralis_inscricoes WHERE id_usuario = :1", {"1": id_usuario})

# função para atualizar a senha do usuário no banco de dados
def atualizar_senha(id_usuario: int, senha_atual: str, nova_senha: str) -> None:
    sql_verifica = "SELECT senha FROM auralis_usuarios WHERE id_usuario = :1"
    resultado = executar_comando(sql_verifica, {"1": id_usuario}, fetch=True)

    # verifica se senha atual está correta
    if not resultado or resultado[0][0] != senha_atual:
        return False
    else:
        sql_atualiza = "UPDATE auralis_usuarios SET senha = :1 WHERE id_usuario = :2"
        executar_comando(sql_atualiza, {"1": nova_senha, "2": id_usuario}, fetch=False)
        return True