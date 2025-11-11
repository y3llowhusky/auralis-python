import os
import json
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