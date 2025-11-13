from db import executar_comando
from biblioteca import *
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

def listar_registros(id_usuario: int, nome_usuario: str) -> None:
    sql = "SELECT id_registro, id_usuario, hidratacao_ml, tempo_sol_min, nivel_estresse," \
    "sono_horas, tempo_tela_horas, trabalho_horas, atividade_fisica_min, score, data_registro" \
    " FROM auralis_registros WHERE id_usuario = :1 ORDER BY data_registro"

    dados_registro = {"1": id_usuario}
    resultado = executar_comando(sql, dados_registro, fetch=True)

    print(f"Histórico de registros de {nome_usuario}\n")

    if not resultado:
        print("Nenhum registro encontrado.")
    else:
        registros = []
        for registro in resultado:
            data = registro[10].strftime("%d/%m/%Y")
            exibir_titulo(f"registro diário - {data}")
            print(f"""Hidratação (ml): {registro[2]}
Tempo ao sol: {registro[3]} min
Nível de estresse (1 a 10): {registro[4]}
Sono: {registro[5]} horas
Tempo de tela: {registro[6]} horas
Tempo de trabalho: {registro[7]} horas
Atividade física: {registro[8]} min
-----\nScore do dia: {registro[9]}""")
            print("")

            registros.append({
                "data_registro": registro[10].strftime("%d/%m/%Y"),
                "hidratacao_ml": registro[2],
                "tempo_sol_min": registro[3],
                "nivel_estresse": registro[4],
                "sono_horas": registro[5],
                "tempo_tela_horas": registro[6],
                "trabalho_horas": registro[7],
                "atividade_fisica_min": registro[8],
                "score": registro[9]})

        print(f"Total de registros diários: {len(resultado)}")
        exportar = input("Deseja exportar os registros para um arquivo de texto? (s/n): ").strip().lower()
        if exportar == "s":
            exportar_json("historico_registros", registros)