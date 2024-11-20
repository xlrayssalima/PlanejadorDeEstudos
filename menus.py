from utils import clearTerminal 
from constantes import *
from usuario import *
from atividade import *

def menuLogin(usuarios):
    while True:
        print('1 - Fazer Login')
        print('2 - Cadastrar Novo Usuário\n')

        try:
            opcaoMenuInicial = int(input('Escolha uma das opções acima: '))
        except ValueError:
            clearTerminal()
            print('Escollha o número da opção!')
            continue
        except KeyboardInterrupt:
            break

        if (opcaoMenuInicial == LOGIN):
            clearTerminal()
            return login()
        elif (opcaoMenuInicial == CADASTRAR_NOVO_USUARIO):
            clearTerminal()
            return cadastrar_usuario(usuarios)
        else:
            clearTerminal()
            print('Opção inválida, tente novamente!\n')

def menuAtividades(atividades, idUsuario):
    while True:
        print("\n--- Cadastro de Atividades ---")
        print("1. Cadastrar Nova Atividade")
        print("2. Listar Atividades")
        print("3. Editar Atividade")
        print("4. Excluir Atividade")
        print("5. Listar Atividades por Nível de Prioridade")
        print("6. Sair")

        try:
            escolha = input("Escolha uma opção: ")
        except ValueError:
            clearTerminal()
            print('Escollha o número da opção!')
            continue
        except KeyboardInterrupt:
            break

        if escolha == '1':
            atividades = cadastrar_atividade(atividades, idUsuario)
        elif escolha == '2':
            listar_atividades(idUsuario)
        elif escolha == '3':
            editar_atividade(idUsuario)
        elif escolha == '4':
            excluir_atividade(idUsuario)
        elif escolha == '5':
            listar_atividades_por_nivel(idUsuario)
        elif escolha == '6':
            print("\nSaindo, tchauzinho ^^...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")