import requests
import json
import time

#variaveis globais


#informações usuario

banca_inicial = (input('Qual o valor da sua banca?'))
tipo_conta = int(0) #int(input('Deseja operar em conta REAL(1) ou Treinamento(2)? (1 ou 2)'))
valor_banca = int(1000) #int(input('Qual o valor da sua banca?'))
entrada = int(50) #int(input('Qual valor da sua primeira entrada?'))
stop_loss = 0 #int(input('Quantos loss você aceita tomar?'))
stop_gain = 0 #int(input('Qual sua meta de vitória em porcentagem(%)?'))
quantidade_gales = 0 #int(input('Quantos gales você quer?'))
multiplicador = int(2) #int(input('Qual será seu fator multiplicador de gale?'))
