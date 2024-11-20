import os
import json
from datetime import datetime

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# aqui é a funções para manipulação de arquivos JSON
def guardar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo está corrompido.")
        return []