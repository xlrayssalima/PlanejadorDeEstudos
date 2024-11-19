from utils import clearTerminal 
from menus import menuLogin

clearTerminal()
print('Bem-vindo ao Planejador de Estudos!\n')
opcaoLogin = menuLogin()

print(opcaoLogin)