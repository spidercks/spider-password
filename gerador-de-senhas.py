from funcoes import * 
from interface import *

cabecalho("SPIDER-GERADOR")

quant = quant_senhas()
tam = tam_senhas()

senhas = gerador_senhas(quant, tam)

cabecalho("SAINDO...")