from utils import clearTerminal 
from constantes import *

def menuLogin():
    while True:
        print('1 - Fazer Login')
        print('2 - Cadastrar Novo Usuário\n')

        opcaoMenuInicial = int(input('Escolha uma das opções acima: '))

        if (opcaoMenuInicial == LOGIN):
            print('FAÇA LOGIN')
            clearTerminal()
            break
        elif (opcaoMenuInicial == CADASTRAR_NOVO_USUARIO):
            print('CADASTRE NOVO USUÁRIO')
            clearTerminal()
            break
        else:
            clearTerminal()
            print('Opção inválida, tente novamente!\n')
    
    return opcaoMenuInicial