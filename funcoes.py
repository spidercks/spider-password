from interface import * 
from random import choice
from time import sleep 

senha = [] 


def leiaInt(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")
            continue
        else:
            return inteiro
            break


def quant_senhas():
    quant = leiaInt("Quantidade: ")
    return quant


def tam_senhas():
    tam = leiaInt("Tamanho: ")
    return tam


def gerador_senhas(quant, tam):
    cabecalho("GERANDO SENHAS...")
    sleep(1)

    strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")

    for senha_gerada in range(0, int(quant)):
        for string in range(0, int(tam)):
            senha.append(choice(strings))

        for caracter in senha:
            print(caracter, end="")

        print("")
        senha.clear()
        sleep(1)