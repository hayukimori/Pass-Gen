from src import passgen
import sys
 
def term_gui():
    #desenho da gui
    gui0 = '_'*39+'\n'
    gui1 = '_'*15+' PASS-GENERATOR '+'_'*8+'\n \n'
    gui2 = 'digite o número da função a qual será utilizada \n 1- Gerar Senha \n 2- Créditos \n 3- Sair \n'
    gui3 = '_'*39+'\n'
    gui4 = '_'*39+'\n'
    gui = gui0+gui1+gui2+gui3+gui4
    print(gui)
    #verificando escolha do usuario e de definindo as funções pelos modulos
    user_choose = int(input('Digite o número da opção desejada: '))
    if user_choose == 1:
        passgen.gen_function()
    elif user_choose == 2:
        passgen.gen_credits()
    elif user_choose == 3:
        sys.exit()
    pass