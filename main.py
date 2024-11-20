from utils import clearTerminal
from menus import menuLogin, menuAtividades
from usuario import *
from constantes import ARQUIVO_ATIVIDADES

clearTerminal()
print('Bem-vindo ao Planejador de Estudos!\n')

usuarios = carrega_usuarios()
atividades = carregar_dados(ARQUIVO_ATIVIDADES)

usuario = menuLogin(usuarios)

menuAtividades(atividades, usuario['id_usuario'])
