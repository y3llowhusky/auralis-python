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
        
# procedimento para preencher um dicionario e adiciona-lo a lista de dicionarios
def preencher_dicionario(dicionario: dict) -> None:
    # preenche os values dos items do dicionario e adiciona o dicionario preenchido na lista de dicionarios
    for campo, valor in dicionario.items():
        campo_valido = False
        while not campo_valido:
            valor = input(f'{campo.upper()}: ')

            # verifica se valor digitado é vazio
            if valor.strip() == '':
                print('Campo em branco! Digite um valor válido.')
            else:
                tipo = verificar_tipo(campo)
                
                # converte conteudo digitado para o tipo esperado para aquele campo, se possivel
                try:
                    # converte o conteúdo do campo para o tipo esperado dele
                    valor = tipo(valor)
                    
                    # verifica se campo é válido através do retorno da função validar_campo (bool)
                    campo_valido = validar_campo(campo, valor)
                    
                    # se campo não for valido, permanece no loop, se for valido, flag é automaticamente desativada
                    if not campo_valido:
                        print(f'Digite valor válido para {campo}!')
                    
                except ValueError:
                    print(f'Digite valor válido para {campo}!')
        
        # atribui conteudo do campo ao valor do item no dicionario
        dicionario[campo] = valor

# função para validar dados inseridos pelo usuário de acordo com o campo
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
        case "hidratacao (ml)":
            return valor >= 0 and valor <= 10000
        case "tempo sol (min)":
            return valor >= 0 and valor <= 1440
        case "nivel estresse (1 a 10)":
            return valor >= 1 and valor <= 10
        case "sono (horas)":
            return valor >= 0 and valor <= 24
        case "tempo tela (horas)":
            return valor >= 0 and valor <= 24
        case "trabalho (horas)":
            return valor >= 0 and valor <= 24
        case "atividade fisica (min)":
            return valor >= 0 and valor <= 1440
        case "nota feedback (1 a 5)":
            return valor >= 1 and valor <= 5
        case _:
            return True

# função para verificar se data está em formato e intervalo válidos
def verificar_data(data_texto: str) -> bool:
    try:
        data_valida = datetime.strptime(data_texto, "%d/%m/%Y")
        if data_valida < datetime.now() and data_valida.year > 1900:
            return True
        return False
    except ValueError:
        return False

# função para verificar o tipo esperado do conteúdo de um campo, retorna o tipo esperado
def verificar_tipo(campo: str) -> type:
    # verifica qual o conteúdo do campo, e instancia tipo esperado de acordo com ele
    if campo.lower() == 'hidratacao (ml)' or campo.lower() == 'tempo sol (min)' or campo.lower() == 'atividade fisica (min)' or \
    campo.lower() == 'nota feedback (1 a 5)':
        tipo_esperado = int
    elif campo.lower() == 'sono (horas)' or  campo.lower() == 'tempo tela (horas)' or \
    campo.lower() == 'trabalho (horas)' or campo.lower() == 'nivel estresse (1 a 10)':
        tipo_esperado = float
    else:
        tipo_esperado = str
    
    return tipo_esperado

def exportar_json(nome_arq: str, dados: list[dict]) -> None:
    try:
        pasta_exportacoes = "exportacoes"
        os.makedirs(pasta_exportacoes, exist_ok=True)

        caminho_arquivo = os.path.join(pasta_exportacoes, f"{nome_arq}.json")

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print(f"\nDados exportados com sucesso para '{caminho_arquivo}'!\n")
    except Exception as e:
        print(f"Erro ao exportar dados para JSON: {e}")

def salvar_dados(sql: str, dados: dict) -> None:
    executar_comando(sql, dados, fetch=False)

def verificar_cadastro_hoje(id_usuario: int, tabela: str) -> bool:
    sql = f"SELECT * FROM auralis_{tabela}s WHERE id_usuario = :1 AND data_{tabela} = TO_DATE(:2, 'DD/MM/YYYY')"
    dados = {
        "1": id_usuario,
        "2": datetime.now().strftime("%d/%m/%Y")
    }
    resultado = executar_comando(sql, dados, fetch=True)
    return bool(resultado)