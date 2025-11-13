from db import executar_comando
from biblioteca import salvar_dados
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