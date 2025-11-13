from db import executar_comando
from biblioteca import *
from datetime import datetime

inscricao = {
    "receber whatsapp (s/n)": None,
    "receber email (s/n)": None,
}

def verificar_inscricao(id_usuario: int):
    sql = "SELECT status FROM auralis_inscricoes WHERE id_usuario = :id_usuario"
    dados_inscricao = {"id_usuario": id_usuario}
    resultado = executar_comando(sql, dados_inscricao, fetch=True)

    return resultado[0][0] if resultado else None

def salvar_inscricao(inscricao: dict, id_usuario: int) -> bool:
    sql = """INSERT INTO auralis_inscricoes (id_usuario, recebe_whatsapp, recebe_email, status) 
            VALUES (:1, :2, :3, :4)"""
    
    dados_inscricao = {
        "1": id_usuario,
        "2": inscricao["receber whatsapp (s/n)"].upper(),
        "3": inscricao["receber email (s/n)"].upper(),
        "4": "A"
    }

    try:
        salvar_dados(sql, dados_inscricao)
        return True
    except Exception as e:
        return False
    
def atualizar_inscricao(id_usuario: int, whatsapp: str, email: str, status: str) -> bool:
    sql = """UPDATE auralis_inscricoes SET recebe_whatsapp = :whatsapp, recebe_email = :email, status = :status WHERE id_usuario = :id_usuario"""
    
    dados_inscricao = {
        "whatsapp": whatsapp.upper(),
        "email": email.upper(),
        "status": status,
        "id_usuario": id_usuario
    }

    try:
        salvar_dados(sql, dados_inscricao)
        return True
    except Exception:
        return False
    
def desativar_inscricao(id_usuario: int) -> bool:
    sql = "UPDATE auralis_inscricoes SET status = 'I' WHERE id_usuario = :id_usuario"
    
    dados_inscricao = {
        "id_usuario": id_usuario
    }

    try:
        salvar_dados(sql, dados_inscricao)
        return True
    except Exception:
        return False