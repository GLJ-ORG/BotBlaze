import requests
import json
import time

#variaveis globais
rodada = 0
lista_color = []
lista_roll = []
soma_color = 0
soma_roll = 0
comparar_color = 0
comparar_roll = []
soma_color_back = 0
soma_roll_back = [0, 0]
num_guardado = 0
rolo1 = 0
rolo2 = 0

num1 = 0
num2 = 0
roll1 = 0
roll2 = 0
previsao = 0
somas = 0
total_partidas = 0
resultado_divisao = int(0)
#informações usuario

banca_inicial = 100 #(input('Qual o valor da sua banca?'))
tipo_conta = int(0) #int(input('Deseja operar em conta REAL(1) ou Treinamento(2)? (1 ou 2)'))
entrada = int(50) #int(input('Qual valor da sua primeira entrada?'))
stop_loss = 0 #int(input('Quantos loss você aceita tomar?'))30
stop_gain = 0 #int(input('Qual sua meta de vitória em porcentagem(%)?'))
quantidade_gales = 3 #int(input('Quantos gales você quer?'))
multiplicador = 2 #int(input('Qual será seu fator multiplicador de gale?'))


while rodada == 0:
# Receber dados da api OK
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista_color = [x['color'] for x in resultado]

    dados2 = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado2 = json.loads(dados2.content)
    lista_roll = [y['roll'] for y in resultado2]

    soma_roll_back.insert(0, int(soma_roll))
    time.sleep(2)
    #soma_roll_back.remove()

# Pegar numeros separadamente da lista
    num1, num2, *outras_lista = lista_color
    roll1, roll2, *outras_lista2 = lista_roll
    rolo1, rolo2, *outras_lista3 = soma_roll_back



    soma_roll = sum(lista_roll)
    #time.sleep(2)
    #print()
    #print(soma_roll_back)
    #print(roll1, roll2, rolo1, rolo2)

    if rolo1 != rolo2:
        print(lista_roll)
        #print(soma_roll_back)

        #Calculo de previsão
        a = (num1)
        somas += a
        dividir_somas = somas
        resultado_divisao = int(dividir_somas / 2)
        total_partidas = total_partidas + 1

        print(f'Partida Nº{total_partidas}', f'Divisão:{resultado_divisao}')
        #previsão da partida
        if resultado_divisao % 2 == 0:
            previsao = 1
            prev_text = 'Preto'
        else:
            previsao = 2
            prev_text = 'Vermelho'
        print(f'Cor prevista para prox rodada: {prev_text}')
        print()
        #contadores de partida, vitorias e derotas

















# calculo para logica da previsao OK
#a = num1
#somas += a
#dividir_somas = somas
#resultado_divisao = int(dividir_somas / 2)
#total_rodadas = total_rodadas + 1

# condição de previsão OK
#if resultado_divisao % 2 == 0:
    # Preto padrão API numero Par OK
 #   previsao = 1
#else:
    # Vermelho padrão API numero Impar OK
 #   previsao = 2

# Gerar lista de previsoes e recentes OK
#lista_previsoes.insert(0, int(previsao))
#lista_recents.insert(0, int(num_recent))

#prev1, prev2, *outras_previsoes = lista_previsoes
#rece1, rece2, *outras_recentes = lista_recents


    #print(num_guardado, soma_roll)
    #print(soma_roll_back)


