from db import executar_comando
from biblioteca import *
from datetime import datetime

feedback = {
    "nota feedback (1 a 5)": None,
    "mensagem": None
}

def salvar_feedback(feedback: dict, id_usuario: int) -> bool:
    sql = """INSERT INTO auralis_feedbacks (id_usuario, mensagem, nota_feedback, data_feedback) VALUES (:1, :2, :3, TO_DATE(:4, 'DD/MM/YYYY'))"""
    
    dados_feedback = {
        "1": id_usuario,
        "2": feedback["mensagem"],
        "3": feedback["nota feedback (1 a 5)"],
        "4": datetime.now().strftime("%d/%m/%Y"),
    }

    try:
        salvar_dados(sql, dados_feedback)
        return True
    except Exception as e:
        return False
    
def listar_feedbacks(id_usuario: int, nome_usuario: str) -> None:
    sql = "SELECT * FROM auralis_feedbacks WHERE id_usuario = :1 ORDER BY data_feedback"

    dados_feedback = {"1": id_usuario}
    resultado = executar_comando(sql, dados_feedback, fetch=True)

    print(f"Histórico de feedbacks de {nome_usuario}\n")

    if not resultado:
        print("Nenhum feedback encontrado.")
    else:
        feedbacks = []
        for feedback in resultado:
            data = feedback[4].strftime("%d/%m/%Y")
            exibir_titulo(f"feedback - {data}")
            print(f"""Nota do feedback (1 a 5): {feedback[3]}
Mensagem: {feedback[2]}""")
            print("")

            feedbacks.append({
                "data_feedback": data,
                "mensagem": feedback[2],
                "nota_feedback": feedback[3],})

        print(f"=====\nTotal de registros diários: {len(resultado)}\n=====")
        exportar = input("Deseja exportar os feedbacks para um arquivo de texto? (s/n): ").strip().lower()
        if exportar == "s":
            exportar_json("historico_feedbacks", feedbacks)