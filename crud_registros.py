from db import executar_comando
from biblioteca import salvar_dados
from datetime import datetime

registro_diario = {
    "hidratacao (ml)": None,
    "tempo sol (min)": None,
    "nivel estresse (1 a 10)": None,
    "sono (horas)": None,
    "tempo tela (horas)": None,
    "trabalho (horas)": None,
    "atividade fisica (min)": None,
}

def calcular_score(dados: dict) -> int:
    # transforma os dados inseridos em valores de 0 a 1
    hidr = min(dados["hidratacao (ml)"] / 2500, 1)
    sol = min(dados["tempo sol (min)"] / 45, 1)
    estresse = 1 - min(dados["nivel estresse (1 a 10)"] / 10, 1)
    sono = min(dados["sono (horas)"] / 8, 1)
    tela = 1 - min(dados["tempo tela (horas)"] / 8, 1)
    trabalho = 1 - abs((dados["trabalho (horas)"] - 7) / 7)
    atividade = min(dados["atividade fisica (min)"] / 60, 1)

    # instancia o peso de cada índice baseado na sua importância no bem-estar do usuário
    pesos = {
        "hidr": 0.15,
        "sol": 0.10,
        "estresse": 0.20,
        "sono": 0.25,
        "tela": 0.10,
        "trabalho": 0.10,
        "atividade": 0.10
    }

    # calcula o score final baseado no índice e seu respectivo peso
    score = (
        hidr * pesos["hidr"]
        + sol * pesos["sol"]
        + estresse * pesos["estresse"]
        + sono * pesos["sono"]
        + tela * pesos["tela"]
        + trabalho * pesos["trabalho"]
        + atividade * pesos["atividade"]
    ) * 100

    # retorna o score arredondado
    return round(max(0, min(score, 100)))

def salvar_registro(registro: dict, id_usuario: int) -> bool:
    sql = """INSERT INTO auralis_registros (id_usuario, hidratacao_ml, tempo_sol_min, nivel_estresse, sono_horas, tempo_tela_horas, 
            trabalho_horas, atividade_fisica_min, score, data_registro) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, TO_DATE(:10, 'DD/MM/YYYY'))"""
    
    dados_registro = {
        "1": id_usuario,
        "2": registro["hidratacao (ml)"],
        "3": registro["tempo sol (min)"],
        "4": registro["nivel estresse (1 a 10)"],
        "5": registro["sono (horas)"],
        "6": registro["tempo tela (horas)"],
        "7": registro["trabalho (horas)"],
        "8": registro["atividade fisica (min)"],
        "9": calcular_score(registro),
        "10": datetime.now().strftime("%d/%m/%Y")
    }

    try:
        salvar_dados(sql, dados_registro)
        return True
    except Exception as e:
        return False

def verificar_registro_hoje(id_usuario: int) -> bool:
    sql = "SELECT * FROM auralis_registros WHERE id_usuario = :1 AND data_registro = TO_DATE(:2, 'DD/MM/YYYY')"
    dados = {
        "1": id_usuario,
        "2": datetime.now().strftime("%d/%m/%Y")
    }
    resultado = executar_comando(sql, dados, fetch=True)
    return bool(resultado)