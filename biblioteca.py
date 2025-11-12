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

def verificar_data(data_texto: str) -> bool:
    try:
        data_valida = datetime.strptime(data_texto, "%d/%m/%Y")
        if data_valida < datetime.now() and data_valida.year > 1900:
            return True
        return False
    except ValueError:
        return False
    
def validar_campo(campo: str, valor: str) -> bool:
    match campo:
        case "email":
            return "@" in valor and "." in valor
        case "senha":
            return len(valor) >= 6
        case "nome":
            return len(valor) > 1
        case "genero":
            return valor.upper() in ["M", "F", "O"]
        case "data_nascimento":
            return verificar_data(valor)