#!/bin/python3

#importando bibliotecas para verificar a plataforma e os modulos para gerar a gui
import platform
from src import gui

#verificando o modelo do processador do computador para verificar qual dispositivo utilizar,possivel má escolha pois o raspberry pi e os macbooks utilizam processadores ARM em seus computadores 
#colocar uma segunda verficação para rodar em macbooks e raspberry pi's
version = platform.machine()
sistema = platform.system()
def start():
    if version == 'AMD64' or 'i386':
        if sistema == 'Windows' or 'Linux':
            gui.term_gui()
    if version == 'armv71':
        if sistema == 'Android':
            gui.mbl_term_gui()
        gui.term_gui()
pass

start()
