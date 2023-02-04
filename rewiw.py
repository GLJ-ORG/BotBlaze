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
lista_diferenca_loss = [0, 0, 0, 0, 0]
lista_diferenca_branco = [0, 0, 0, 0, 0]

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
guardar = int(0)
guardar1 = int(0)
guardar2 = int(0)
guardar3 = int(0)
branco_guardar = int(0)
branco_guardar1 = int(0)

saldo_banca = float(0)
aplicar = float(0)
aplicar1 = float(0)
aplicar2 = float(0)
aplicar3 = float(0)
v_branco = float(0)
v_branco1 = float(0)
v_branco2 = float(0)
v_branco3 = float(0)
montante = float(550)
g1 = int(0)

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
        if somas == 10:
            somas = 0
        elif somas > 10:
            somas = 1
        resultado_divisao = (round(dividir_somas / 2))
        total_partidas += 1

    #previsão da partida
        if resultado_divisao % 2 == 0:
            previsao = 2
            prev_text = 'Preto'
        else:
            previsao = 1
            prev_text = 'Vermelho'

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
            contador_loss = 0

        def cor_rodada(num1):
            if num1 == 1:
                return "Vermelho 🔴"
            elif num1 == 2:
                return "Preto ⚫"
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

        if loss1 > loss2:
            ultimo_loss = total_partidas
            guardar2 = contador_gain - guardar1
            guardar1 = gain

            lista_diferenca_loss.insert(0, int(guardar2))
            lista_diferenca_loss.pop()

        guardar3 = gain - guardar1

        if cont1 == 2:
            guardar = gain

        if num1 == 0:
            branco_guardar = total_partidas - branco_guardar1
            branco_guardar1 = total_partidas
            lista_diferenca_branco.insert(0, int(branco_guardar))
            lista_diferenca_branco.pop()
        branco_guardar3 = total_partidas - branco_guardar1

        def gale_conservador():
            global aplicar
            global aplicar1
            global aplicar2
            global aplicar3
            global v_branco
            global v_branco1
            global v_branco2
            global v_branco3
            global montante
            aplicar = 1
            aplicar1 = 2
            aplicar2 = 4
            aplicar3 = 8
            v_branco = 0.5
            v_branco1 = 1
            v_branco2 = 1.5
            v_branco3 = 2
            return aplicar, aplicar1, aplicar2, aplicar3, v_branco, v_branco1, v_branco2, v_branco3

        def saldo():
            global saldo_banca
            global prev2
            global num1
            global cont1
            global cont2
            global v_branco
            global v_branco1
            global v_branco2
            global v_branco3
            global aplicar
            global aplicar1
            global aplicar2
            global aplicar3

            if num1 == prev2:
                if cont1 == 0:
                    if cont2 == 0:
                        saldo_banca += (aplicar * 2) + (v_branco * 2)
                    elif cont2 == 1:
                        saldo_banca += (aplicar * 2) + (v_branco * 2)
                    elif cont2 == 2:
                        saldo_banca += (aplicar * 2) + (v_branco * 2)
                    elif cont2 == 3:
                        saldo_banca += (aplicar * 2) + (v_branco * 2)
            else:
                'calculo invalido'


            if num1 != prev2:
                if cont1 == 0:
                    if cont2 == 0:
                        saldo_banca -= (aplicar) + (v_branco * 2)
                    elif cont2 == 1:
                        saldo_banca -= (aplicar) + (v_branco * 2)
                    elif cont2 == 2:
                        saldo_banca -= (aplicar) + (v_branco * 2)
                    elif cont2 == 3:
                        saldo_banca -= (aplicar) + (v_branco * 2)

            if num1 == 0:
                saldo_banca += v_branco * 14

            return saldo_banca

        if cont1 == 1:
            g1 += 1
        if cont1 == 0 and cont2 == 3:
            if prev2 != num1:
                g1 -= 1

        msgn5 = f'Continue com cautela, estipule uma meta de vitória e derrota\n Nunca saia da sua gestão de risco!'
        msgn4 = f'PARABÉNS CORINGA!⚪\n Sempre proteger o branco com 15% do valor da sua entrada na rodada\n Good Luck 🍀'
        msgn2 = '~~~~~~~~~~~~~~~~~~~~~~~'
        msgn3 = f'Vamos para o Gale:{cont1}\n🔥💰🤑🚀'
        msgn1 = f'{msgn2}\n🛸GANHOS: {gain} PERDAS: {loss} BRANCO: {coringa}🛸'
        msgn = f'ENTRAR NA COR: {prev_text.upper()}'
        if prev2 == num1:
            msgn = f'VITÓRIA NO GALE:{cont2}\n {msgn5}\n✅✅✅\n{msgn2}'
        elif cont2 == 3 and num1 != 0:
            msgn = f'DERROTA, não desanime siga a gestão e aguarde o próximo sinal!\n❌❌❌\n{msgn2}'
        elif num1 == 0:
            msgn = f'{msgn4}\n{msgn2}'
        else:
            msgn = f'{msgn}\n{msgn3}\n{msgn2}'

        token = '6192919039:AAGMJx8Fktd3UUrVIh5YgE15AgTWjmXJB-E'
        chat_id = '-1001875785629'

        URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+msgn1
        url = "https://api.telegram.org/bot"+token+ "/sendMessage?chat_id="+chat_id+"&text="+msgn


        resposta = requests.get(URL)
        resposta = requests.get(url)





            #Preencher log
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Entrar na Cor: ~~{prev_text.upper()}~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'GALE:{[contador_loss]} Cor atual:{cor_rodada(num1)} {[roll1]}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'GANHOS: {gain} PERDAS: {loss} CORINGA: {coringa}')
        print(f'Rodada Nº:{[total_partidas]} Data e hora: {datetime.now().strftime("%d/%m %H:%M")}')
        print(f'Diferença entre LOSS: {[guardar3]} Ultimo G3:{guardar}')
        print(f'Ultimo LOSS {[guardar1]} Soma: {somas, resultado_divisao}')
        print(f'Diferença losses:{lista_diferenca_loss}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'Ultimo branco:{branco_guardar1} DIFERENÇA BRANCO ATUAL:{branco_guardar3}')
        print(f'Lista diferenca branco:{lista_diferenca_branco}')
        print(f'TEMPO ATIVO: {"%.1f" %tempo_trabalho} min. Vitórias G1:{g1}')
        print(round(saldo(), 2))
        print('--------------------------------------------')
        print(aplicar, aplicar1, aplicar2, aplicar3, v_branco, v_branco1, v_branco2, v_branco3)
        print(prev2, num1, cont1, cont2)

        Log.PreencheLog(f'Entrar na Cor: ~~{prev_text.upper()}~~')
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'GALE:{[contador_loss]} Cor atual:{cor_rodada(num1)} {[roll1]}')
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'GANHOS: {gain} PERDAS: {loss} CORINGA: {coringa}')
        Log.PreencheLog(f'Rodada Nº:{[total_partidas]} Data e hora: {datetime.now().strftime("%d/%m %H:%M")}')
        Log.PreencheLog(f'Diferença entre LOSS: {[guardar3]} Ultimo G3:{guardar}')
        Log.PreencheLog(f'Ultimo LOSS {[guardar1]} Soma: {somas, resultado_divisao}')
        Log.PreencheLog(f'Diferença losses:{lista_diferenca_loss}')
        Log.PreencheLog('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Log.PreencheLog(f'Ultimo branco:{branco_guardar1} DIFERENÇA BRANCO ATUAL:{branco_guardar3}')
        Log.PreencheLog(f'Lista diferenca branco:{lista_diferenca_branco}')
        Log.PreencheLog('--------------------------------------------')
        Log.PreencheLog(f'TEMPO ATIVO: {"%.1f" % tempo_trabalho} min. Vitórias G1:{g1}')
        Log.PreencheLog(f'{round(saldo(), 2)}')
        Log.PreencheLog(f'{gale_conservador()}')
        Log.PreencheLog(f'{prev2, num1, cont1, cont2}')