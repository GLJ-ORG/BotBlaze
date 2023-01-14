from datetime import datetime
import requests
import json
import Log


#variaveis globais
rodada = 0
lista_cor = [0, 0, 0]
lista_color = []
lista_roll = []
lista_previsoes = [0, 0, 0]
lista_contador = [0, 0, 0]
lista_loss = [0, 0]
lista_somagales = [0, 0]
lista_diferenca_loss = [0, 0, 0]

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
prev3 = 0
cont1 = 0
cont2 = 0
cont3 = 0
loss1 = 0
loss2 = 0

contador_loss = 0
contador_gain = 0
zerador_loss = 0
gain = 0
loss = 0
coringa = 0

rev_previsao = int(0)
num1 = 0
num2 = 0
num3 = 0
roll1 = 0
roll2 = 0
previsao = 0
somas = 0
total_partidas = int(0)
resultado_divisao = int(0)

banca = int(500)
valor_banca = banca
entrada = 0
valor_entrada = float(0)
branco = float(0)
valor_branco = float(0)
gale = 0
somas_gale = float(0)
ultimo_loss = int(0)
diferenca_loss = int(0)
guardar1 = int(0)
guardar2 = int(0)
guardar3 = int(0)

g = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
#informações usuario

while True:
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

    roll1, roll2, *outras_lista2 = lista_roll
    rolo1, rolo2, *outras_lista3 = soma_roll_back

    soma_roll = sum(lista_roll)
    lista_cor.insert(0, int(num1))
    lista_cor.pop()

    nume1, nume2, nume3, *outros_nume = lista_cor

    if rolo1 != rolo2:
        num1, num2, num3,num, numm, *outras_lista = lista_color
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
        prev1, prev2, prev3, *outras_previsoes = lista_previsoes

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



        if num1 == 0:
            coringa +=1

        def cor_rodada(num1):
            if num1 == 1:
                return "Vermelho"
            elif num1 == 2:
                return "Preto"
            elif num1 == 0:
                return "CORINGA"

        lista_contador.insert(0, int(contador_loss))
        lista_contador.pop()
        cont1, cont2, *outras_contadores = lista_contador

        lista_loss.insert(0, int(loss))
        lista_loss.pop()
        loss1, loss2, *outros_loses = lista_loss



        #def tempo_trabalhado():
        tempo_trabalho = float(0)
        tempo_trabalho = total_partidas * 0.3 / 0.6
        #return Tempo_trabalhado

    #Simulador de banca
        # Definindo entrada
        valor_entrada = banca * 0.01
        if valor_entrada < 1.1:
            valor_entrada = 1.1
        else:
            valor_entrada = banca * 0.01

        branco = gale * 0.15
        if branco < 1.09:
            branco = float(1.1)
            valor_branco = float(1.1)
        else:
            branco = gale * 0.15
            valor_branco = branco

        # definindo valores dos gales
        g = valor_entrada + (valor_branco * 2)
        g1 = (g * 2) + valor_entrada + (valor_branco * 2)
        g2 = (g1 * 2) + valor_entrada + (valor_branco * 2)
        g3 = (g2 * 2) + valor_entrada + (valor_branco * 2)
        g4 = (g3 * 2) + valor_entrada + (valor_branco * 2)
        g5 = (g4 * 2) + valor_entrada + (valor_branco * 2)

        if contador_loss == 1:
            gale = 0
            somas_gale = 0
            valor_branco = 0
            gale = g
            somas_gale = g + valor_entrada
            branco = g * 0.15

        elif contador_loss == 2:
            gale = g1
            somas_gale += g1
            branco = g1 * 0.15

        elif contador_loss == 3:
            gale = g2
            somas_gale += g2
            branco = g2 * 0.15

        elif contador_loss == 4:
            gale = g3
            somas_gale += g3
            branco = g3 * 0.15

        elif contador_loss == 5:
            gale = g4
            somas_gale += g4
            branco = g4 * 0.15

        if num1 != prev2:
            valor_banca -= gale

        if cont1 < cont2 & num1 > 0:
            valor_banca += somas_gale
            banca += valor_entrada

        if loss1 > loss2:
            banca -= somas_gale
            ultimo_loss = total_partidas
            guardar2 = contador_gain - guardar1
            guardar1 = gain

            lista_diferenca_loss.insert(0, int(guardar2))
            lista_diferenca_loss.pop()

        if num1 == 0 & cont1 > 0:
            valor_banca += (branco * 14)
            gale = g
            somas_gale = g + valor_entrada

        guardar3 = gain - guardar1

        if cont1 == 3:
            guardar = gain

            #Preencher log
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'Entrar na Cor: ~~{prev_text.upper()}~~')
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'GALE:{[contador_loss]} Cor atual:{cor_rodada(num1)} {[roll1]}')
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'Ganhos: {gain} Perdas: {loss} Coringa: {coringa}')
        Log.PreencheLog(f'Rodada Nº{total_partidas}' f'Data e hora Atual: {datetime.now().strftime("%d/%m %H:%M")}')
        Log.PreencheLog(f'Tempo de trabalho: {"%.1f" % tempo_trabalho} min. Ultimo loss: Nº{ultimo_loss}')
        Log.PreencheLog(f'Saldo atual: {"%.2f"%banca} Aposta:{["%.2f"%valor_entrada]}')
        # print dos dados para análise
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'{["%.2f" % gale]} {["%.2f" % somas_gale]} {["%.2f" % valor_entrada]} {["%.2f" % valor_branco]}')
        Log.PreencheLog(f'Cor:{lista_cor}Prev:{lista_previsoes}Cont:{lista_contador}loss:{lista_loss}Gsoma:{lista_somagales}')
        Log.PreencheLog(f'{num1, prev2, lista_previsoes}')
        Log.PreencheLog(f'{gain, loss}')
        Log.PreencheLog(f'{contador_gain, contador_loss, zerador_loss}')
        Log.PreencheLog(f'~')

        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Entrar na Cor: ~~{prev_text.upper()}~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'GALE:{[contador_loss]} Cor atual:{cor_rodada(num1)} {[roll1]}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Ganhos: {gain} Perdas: {loss} Coringa: {coringa}')
        print(f'Rodada Nº{[total_partidas]}', f'Data e hora Atual: {datetime.now().strftime("%d/%m %H:%M")}')
        #print(f'Saldo atual: {"%.2f"%valor_banca, banca} Aposta:{["%.2f"%valor_entrada]}')
        print(f'Diferença atual: {[guardar3]} Ultimo G3: {guardar}')
        print(f'Ultima derrota na vitoria {[guardar1]}')
        print(f'Diferença losses:{lista_diferenca_loss}')
        print(f'Tempo de trabalho: {"%.1f" %tempo_trabalho} min. ')
        # print dos dados para análise
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        #print(f'{["%.2f"%gale]} {["%.2f"%somas_gale]} {["%.2f"%branco]} {["%.2f"%valor_branco]}')
       #print(f'Num atual:{num1} Prev Ante:{prev2} List Prev:{lista_previsoes}')
        #print(f'Cor:{[num1, num2, num3]}Prev:{[prev1, prev2, prev3]}')
        print(f'{["%.2f"%g]} {["%.2f"%g1]} {["%.2f"%g2]} {["%.2f"%g3]} {["%.2f"%g4]} {["%.2f"%g5]}')
        #print(f'loss:{lista_loss} Cont:{lista_contador}')
        #print(f'G:{gain} P:{loss}')
        #print(f'ContG:{contador_gain} ContP:{contador_loss} ZLss:{zerador_loss}')'''
        print()



