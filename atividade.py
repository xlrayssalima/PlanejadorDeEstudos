from constantes import ARQUIVO_ATIVIDADES, ARQUIVO_IDS
from utils import carregar_dados, salvar_dados, clearTerminal

def carrega_atividades():
    return carregar_dados(ARQUIVO_ATIVIDADES)

def carrega_ids():
    return carregar_dados(ARQUIVO_IDS)

def cadastrar_atividade(atividades, idUsuario):
    clearTerminal()

    ids = carrega_ids()
    idAtividade = ids["id_atividade"] + 1
    ids["id_atividade"] = idAtividade


    titulo = input("Título da Atividade: ")
    descricao = input("Descrição da Atividade: ")
    inicial = input("Data Inicial da Atividade (dia/mês): ")
    final = input("Data Final da Atividade (dia/mês): ")
    hora_est = input("Horário de Estudo: ")

    try:
        nivel = input("Nível de prioridade: 1 - Alta, 2 - Média ou 3 - Baixa: ")
        if nivel == 1:
            nivel_prior = 'Alta'
        elif nivel == 2:
            nivel_prior = 'Média'
        elif nivel == 3:
            nivel_prior = 'Baixa'
        else:
            print('Nível informado não corresponde a um nível válido')
    except ValueError:
        print('Escolha o nível pelo seu respectivo número')

    if (titulo == '' or descricao == '' or inicial == '' or final == ''):
        clearTerminal()
        print('\nA atividade deve ter pelo menos titulo, descrição, data inicial e data final')
    else:
        # dicionario c/ dados da nova atividade
        nova_atividade = {
            'id_usuario': idUsuario,
            'id_atividade': idAtividade,
            'titulo': titulo,
            'descricao': descricao,
            'data_inicio': inicial,
            'data_fim': final,
            'hora_est': hora_est,
            'nivel_prior': nivel_prior,
        }

        # add nova atividade na lista de atividades
        atividades.append(nova_atividade)
        salvar_dados('atividades.json', atividades)
        salvar_dados('ids.json', ids)

        clearTerminal()
        print("\nAtividade cadastrada com sucesso ^^!")

def listar_atividades(idUsuario):
    clearTerminal()
    atividades = carrega_atividades()
    print('--- ATIVIDADES CADASTRADAS ---')
    print(f"ID | Título | Descrição | Data Inicial | Data Final | Horário de Estudo | Nível de Prioridade")
    print(f"---------------------------------------------------------------------------------------------")
    for atividade in atividades:
        if (atividade['id_usuario'] == idUsuario): 
            print(f"{atividade['id_atividade']} | {atividade['titulo']} | {atividade['descricao']} | {atividade['data_inicio']} | {atividade['data_fim']} | {atividade['hora_est']} | {atividade['nivel_prior']}")

def excluir_atividade(idUsuario):
    clearTerminal()
    listar_atividades(idUsuario)
    atividades = carrega_atividades()
    encontrou = False

    try:
        id_atividade = int(input("\nDigite o ID da atividade a ser excluída: "))

        for atividade in atividades:
            if atividade['id_atividade'] == id_atividade and atividade['id_usuario'] == idUsuario:
                encontrou = True

                confirmacao = input('Tem certeza que deseja apagar a atividade? (S - SIM) (Outra tecla para cancelar)')
                if (confirmacao == 'S' or confirmacao == 's'):
                    atividades.remove(atividade)
                    salvar_dados('atividades.json', atividades)
                    print("\nAtividade excluída com sucesso! :)")
                    return
        if not encontrou:
            print("\nID inválido!Tente novamente :(")
    except ValueError:
        print('Digite o número do ID!')
    except KeyboardInterrupt:
        return None

def editar_atividade(idUsuario):
    clearTerminal()
    listar_atividades(idUsuario)
    atividades = carrega_atividades()

    try:
        id_atividade = int(input("\nDigite o ID da atividade a ser editada: "))

        editou = False
    
        for atividade in atividades:
            if atividade['id_atividade'] == id_atividade and atividade['id_usuario'] == idUsuario:
                clearTerminal()
                titulo = input("Novo Título da Atividade: ")
                descricao = input("Nova Descrição da Atividade: ")
                inicial = input("Nova Data Inicial da Atividade (dia/mês): ")
                final = input("Nova Data Final da Atividade (dia/mês): ")
                hora_est = input("Novo Horário de Estudo: ")
                nivel_prior = input("Novo Nível de prioridade: ")

                atividade['titulo'] = titulo
                atividade['descricao'] = descricao
                atividade['data_inicio'] = inicial
                atividade['data_fim'] = final
                atividade['hora_est'] = hora_est
                atividade['nivel_prior'] = nivel_prior

                editou = True
                break

        if editou:
            salvar_dados('atividades.json', atividades)
            print("\nAtividade editada com sucesso!")
        
        print("\nID inválido!")
    except ValueError:
        print('Digite o número do ID!')
    except KeyboardInterrupt:
        return None

def listar_atividades_por_nivel(idUsuario):
    clearTerminal()
    atividades = carrega_atividades()
    
    try:
        nivel = input("Nível de prioridade: 1 - Alta, 2 - Média ou 3 - Baixa: ")
        if nivel == '1':
            nivel_prior = 'Alta'
        elif nivel == '2':
            nivel_prior = 'Média'
        elif nivel == '3':
            nivel_prior = 'Baixa'
        else:
            print('Nível informado não corresponde a um nível válido')
        
        print(f'--- ATIVIDADES CADASTRADAS - PRIORIDADE {nivel_prior} ---')
        print(f"ID | Título | Descrição | Data Inicial | Data Final | Horário de Estudo | Nível de Prioridade")
        print(f"---------------------------------------------------------------------------------------------")
        for atividade in atividades:
            if (atividade['id_usuario'] == idUsuario and atividade['nivel_prior'] == nivel_prior): 
                print(f"{atividade['id_atividade']} | {atividade['titulo']} | {atividade['descricao']} | {atividade['data_inicio']} | {atividade['data_fim']} | {atividade['hora_est']} | {atividade['nivel_prior']}")
    except ValueError:
        print('Escolha o nível pelo seu respectivo número')