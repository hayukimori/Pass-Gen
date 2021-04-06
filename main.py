#!/bin/python3

#importando bibliotecas para verificar a plataforma e os modulos para gerar a gui
import platform
import sys
from src import gui

#verificando o modelo do processador do computador e qual sistema rodado
version = platform.machine()
sistema = platform.system()

#função start iniciando o modulo gui e verificando a versão no qual roda o programa
def start():
    if version == 'AMD64' or 'i386':
        if sistema == 'Windows' or 'Linux' or 'Darwin' or 'Java':
            gui.term_gui()
        if sistema == ' ':
            gui.term_gui()
    if version == 'armv71':
        if sistema == 'Darwin' or 'Linux':
            gui.term_gui()
        
    else:
        sys.exit()
pass

start()
