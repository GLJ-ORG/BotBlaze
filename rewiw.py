from datetime import datetime
import requests
import json
import Log
#import funcao

#variaveis globais
rodada = 0
lista_color = []
lista_roll = []
lista_previsoes = [0, 0]

soma_color = 0
soma_roll = 0
comparar_color = 0
comparar_roll = []
soma_color_back = 0
soma_roll_back = [0, 0]
num_guardado = 0
rolo1 = 0
rolo2 = 0
prev1 = 0
prev2 = 0
contador_loss = 0
contador_gain = 0
zerador_loss = 0
gain = 0
loss = 0
coringa = 0

rev_previsao = int(0)
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


while 'true':
# Receber dados da api OK
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista_color = [x['color'] for x in resultado]

    dados2 = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado2 = json.loads(dados2.content)
    lista_roll = [y['roll'] for y in resultado2]


    soma_roll_back.insert(0, int(soma_roll))
    #time.sleep(1)
    soma_roll_back.pop()


# Pegar numeros separadamente da lista
    num1, num2, *outras_lista = lista_color
    roll1, roll2, *outras_lista2 = lista_roll
    rolo1, rolo2, *outras_lista3 = soma_roll_back



    soma_roll = sum(lista_roll)
#prints antes da trava de atualização

    #time.sleep(2)
    #print(previsao, resultados, lista_previsoes)
    #print(soma_roll_back)
    #print(roll1, roll2, rolo1, rolo2)

    #roll_recent = funcao.numero_roll()
    #print(roll_recent)

    if rolo1 != rolo2:
        #print(lista_roll)
        #print(soma_roll_back)
        Log.PreencheLog(str(lista_roll))
        #Calculo de previsão

   # def rev_num(num1):
    #    numero = 0
     #   if num1 == 1:
      #          numero = 2
       # elif num1 == 2:
        #        numero = 1
       # else:
        #        numero = 1
        #return num1

        a = num1
        somas += a
        dividir_somas = somas
        resultado_divisao = int(dividir_somas / 2)
        total_partidas = total_partidas + 1





        #previsão da partida
        if resultado_divisao % 2 == 0:
            previsao = 1
            prev_text = 'Vermelho'
        else:
            previsao = 2
            prev_text = 'Preto'


        #def rev_previsao(previsao):
         #   if previsao == 1:
          #      previsao = 2
           # elif previsao == 2:
            #    previsao = 1
            #else:
             #   previsao = 1
            #return previsao


        #res = rev_previsao(previsao)
        #lista_previsoes.insert(0, int(res)

        #lista_previsoes.pop()

        #print(res, previsao,  rev_previsao(previsao))


        lista_previsoes.insert(0, int(previsao))
        lista_previsoes.pop()
        prev1, prev2, *outras_previsoes = lista_previsoes

            #contadores
        if num1 == prev2 & prev2 > 0 or num1 == 0:
            gain += 1
            contador_gain += 1
            contador_loss = 0
            zerador_loss = 0

        elif prev2 > 0:
            contador_loss += 1
            zerador_loss += 1

        if contador_loss == 3:
            loss += 1
            contador_losses = 0
            zerador_losses = 0

        if num1 == 0:
            coringa +=1

        def cor_rodada(num1):
            if num1 == 1:
                return "vermelho"
            elif num1 == 2:
                return "preto"
            elif num1 == 0:
                return "coringa"


        print(f'Gain: {gain} Loss: {loss} Coringa: {coringa}')

        print(f'Entrar na Cor: ~~{prev_text}~~')
        Log.PreencheLog(f'Cor prevista para prox rodada: {prev_text}')

        print(f'Cor da Rodada:{[roll1]} {cor_rodada(num1)}')

        print(f'Partida Nº{total_partidas}', f'Divisão:{datetime.now()}')
        Log.PreencheLog(str(f'Partida Nº{total_partidas} D|H Atual:{resultado_divisao}'))

        hora_atual = float(0)
        hora_atual = total_partidas * 0.3 / 0.6
        print('Tempo de trabalho: {} mim'.format(hora_atual, 2))

        # print dados para analise
        print(num1, prev2, lista_previsoes)
        print(gain, loss)
        print(contador_gain, contador_loss, zerador_loss)
        print()


        #contadores de partida, vitorias e derotas


        #print(lista_previsoes)
        #valor_entrada()


















