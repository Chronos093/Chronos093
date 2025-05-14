#!/bin/bash
# Script para ligar os leds do teclado
# ver. 0.01 - primeira versão do script
# ver. 0.02 - adiciona condição para ligar e desligar o led, e renomeado o nome do arquivo para main
# ver. 0.03 - verifica se o pacote BRINGHTNESSCTL está instalado, caso não o instala.

# Importa modulos do sistema
import os
import getpass
import time


# Função que verifica se o pacote está instalado
def checkPack():
    packaget = os.popen("which brightnessctl").read().rstrip('\n')    # verifica o pacote

    if packaget == "":    # válida se a variável packaget está vazia
        os.system("clear")

        print("O seguinte pacote será instalado: Brightnessctl")
        time.sleep(5.5)    # Pausa a execução por 5.5 secundos
        os.system("clear")

        # Solicita a senha sudo para rodar os comandos com elevação
        password = getpass.getpass("Digite a senha de super usuário: ")

        os.system("echo " + password + " | sudo -S apt install brightnessctl")    # instala o pacote

        time.sleep(3.0)    # Pausa a execução por 3.0 secundos
        os.system("clear")
        print("Pacote instalado com sucesso! Execute o script novamente.")
        time.sleep(5.5)    # Pausa a execução por 5.5 secundos

        exit()        
    else:
        os.system("clear")

        function = switch(case=cond)
        function()


# Função para ligar as luzes
def functionUp():
# Solicita a senha sudo para rodar os comandos com elevação
    password = getpass.getpass("Digite a senha de super usuário: ")

# Resgata o dispositivo que está associado ao led
    commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
    inputLed = commandLed.read().rstrip('\n')

# Passa a senha sudo, e o device para o comando que liga as luzes do teclado
    os.system("echo " + password + " | sudo -S brightnessctl --device='" + inputLed + "::scrolllock' set 1")


# Função para desligar as luzes
def functionDown():
# Solicita a senha sudo para rodar os comandos com elevação
    password = getpass.getpass("Digite a senha de super usuário: ")

# Resgata o dispositivo que está associado ao led
    commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
    inputLed = commandLed.read().rstrip('\n')

# Passa a senha sudo, e o device para o comando que desliga as luzes do teclado
    os.system("echo " + password + " | sudo -S brightnessctl --device='" + inputLed + "::scrolllock' set 0")    


def default():
    print("Erro ao consultar o estado do led.")

def switch(case):
    if case == "0":
        return functionUp
    elif case == "1":
        return functionDown
    else:
        return default


if __name__ == "__main__":
# Resgata o dispositivo que está associado ao led
    commandLed = os.popen("brightnessctl | grep Device | awk '{print $2}' | cut -d ':' -f 1 | cut -c2-")
# Utiliza o rstrip para remover a quebra de linha no final do comando anterior
    inputLed = commandLed.read().rstrip('\n')

    cond = os.popen("sudo brightnessctl --device '" + inputLed + "::scrolllock' get").read().rstrip('\n')
    
    checkPack()