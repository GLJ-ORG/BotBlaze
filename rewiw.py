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

banca = int(100)
gale = int(0)
somas_gale = int(0)

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


    if rolo1 != rolo2:

    #Calculo de previsão
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

        lista_previsoes.insert(0, int(previsao))
        lista_previsoes.pop()
        prev1, prev2, *outras_previsoes = lista_previsoes

    #contadores de vitorias e derrotas
        if num1 == prev2 & prev2 > 0 or num1 == 0:
            gain += 1
            contador_gain += 1
            contador_loss = 0
            zerador_loss = 0

        elif prev2 > 0:
            contador_loss += 1
            zerador_loss += 1

        if contador_loss == 4:
            loss += 1
            contador_loss = 0
            zerador_loss = 0
            somas_gale = 0

        if num1 == 0:
            coringa +=1

        def cor_rodada(num1):
            if num1 == 1:
                return "Vermelho"
            elif num1 == 2:
                return "Preto"
            elif num1 == 0:
                return "CORINGA"


        #def tempo_trabalhado():
        tempo_trabalho = float(0)
        tempo_trabalho = total_partidas * 0.3 / 0.6
        #return Tempo_trabalhado

    #Simulador de banca

        valor_entrada = banca * 0.01
        if valor_entrada < 1.1:
            valor_entrada = 1.1

        branco = valor_entrada * 0.15
        if branco < 1.1:
            branco = 1.1

        g = valor_entrada + (branco * 2)
        g1 = (g * 2) + branco
        g2 = (g1 * 2) + branco
        g3 = (g2 * 2) + branco
        g4 = (g3 * 2) + branco
        g5 = (g4 * 2) + branco

        if contador_loss == 0:
            gale = g
            somas_gale += g
        elif contador_loss == 1:
            gale = g1
            somas_gale += g1
        elif contador_loss == 2:
            gale = g2
            somas_gale += g2
        elif contador_loss == 3:
            gale = g3
            somas_gale += g3
        elif contador_loss == 4:
            gale = g4
            somas_gale += g4
        elif contador_loss == 5:
            gale = g5
            somas_gale += g5

        if num1 == prev2:
            banca += somas_gale - branco - branco
            somas_gale = g
            banca -= gale
        elif num1 == 0:
            banca += branco * 14
            somas_gale = g

        else:
            banca -= gale

        #Preencher log
            Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            Log.PreencheLog(f'Ganhos: {gain} Perdas: {loss} Coringa: {coringa}')
            Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            Log.PreencheLog(f'Entrar na Cor: ~~{prev_text.upper()}~~')
            Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            Log.PreencheLog(f'Cor da Rodada:{[roll1]} {cor_rodada(num1)}')
            Log.PreencheLog(
                f'Partida Nº{total_partidas}' f'Data e hora Atual: {datetime.now().strftime("%d/%m %H:%M")}')
            Log.PreencheLog(f'Tempo de trabalho: {"%.1f" % tempo_trabalho} min')
            Log.PreencheLog(f'Saldo atual: {"%.2f" % banca} {["%.2f" % gale]} {["%.2f" % somas_gale]}')
            Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # print dos dados para análise
            Log.PreencheLog(f'{num1, prev2, lista_previsoes}')
            Log.PreencheLog(f'{gain, loss}')
            Log.PreencheLog(f'{contador_gain, contador_loss, zerador_loss}')
            Log.PreencheLog(f'~')
            print('~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'Entrar na Cor: ~~{prev_text.upper()}~~')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'GALE:{[contador_loss]} Cor atual:{cor_rodada(num1)} {[roll1]}')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(f'Ganhos: {gain} Perdas: {loss} Coringa: {coringa}')
            print(f'Rodada Nº{total_partidas}', f'Data e hora Atual: {datetime.now().strftime("%d/%m %H:%M")}')
            print(f'Tempo de trabalho: {"%.1f" % tempo_trabalho} min.')
            print("Saldo atual: %.2f" % banca, )

        # print dos dados para análise
        '''print(f'{["%.2f"%gale]}, {["%.2f"%somas_gale]}, {["%.2f"%branco]}')
        print(num1, prev2, lista_previsoes)
        print(gain, loss)
        print(contador_gain, contador_loss, zerador_loss)
        print()'''



