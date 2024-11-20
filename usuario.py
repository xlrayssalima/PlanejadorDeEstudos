from utils import salvar_dados, carregar_dados, clearTerminal
from constantes import ARQUIVO_USUARIOS, ARQUIVO_IDS

def carrega_usuarios():
    return carregar_dados(ARQUIVO_USUARIOS)

def carrega_ids():
    return carregar_dados(ARQUIVO_IDS)

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    clearTerminal()
    
    ids = carrega_ids()
    idUsuario = ids["id_usuario"] + 1
    ids["id_usuario"] = idUsuario

    print('--- CADASTRO ---')
    nome = input("\nDigite o nome de usuário: ")
    senha = input("Digite a senha: ")

    usuario = {
        "id_usuario": idUsuario,
        "nome": nome,
        "senha": senha
    }
    usuarios.append(usuario)

    salvar_dados('usuarios.json', usuarios)
    salvar_dados('ids.json', ids)
    print("\nUsuário cadastrado com sucesso!")
    
    clearTerminal()
    return login()

def login():
    usuarios = carrega_usuarios()

    while True:
        print('--- LOGIN ---')
        nome = input("\nDigite o nome de usuário: ")
        senha = input("Digite a senha: ")

        for usuario in usuarios:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                clearTerminal()
                print("\nLogin bem-sucedido!")
                return usuario
            
        print("\nUsuário ou senha incorretos.")
        irParaCadastro = input('\nCadastrar novo usuário? (S - Sim) (Enter para tentar novamente)')
        if (irParaCadastro == 'S' or irParaCadastro == 's'):
            cadastrar_usuario(usuarios)
