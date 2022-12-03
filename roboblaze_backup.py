import requests
import json
import time



previsao = int(0)
lista_previsoes = [0]
saida_recente = int(0)
lista_recents = [0]
lista_comparacao = int(0)
lista_somas_gains = [0]
lista_somas_losses = [0]

prev_text = str()
rodada_text = str()

preto = int(0)
vermelho = int(0)
branco = int(0)
coringa = str()
somas_coringas = int(0)

# numeros recentes invertido para calculo de previsoes
num1 = int(0)
num2 = int(0)
num_recent = num1
num_anterior = num2

prev1 = int(0)
prev2 = int(0)
prev_recent = int(0)
prev_anterior = int(prev2)

gain = int(0)
loss = int(0)

contador_gains = int(0)
contador_losses = int(0)
zerador_losses = contador_losses
contador_branco = int(0)
entrada = int(0)
g1 = int(0)
g2 = int(0)

total_rodadas = int(0 - 1)
rodada = num1
condicao = int(0)
somas = int(0)
dividir_somas = int(0)
resultado_divisao = int(0)

banca_total = int(0)
tipo_conta = int(0)
valor_banca = int(0)
entrada = int(0)
multiplicador = int(0)
valor_branco = int(0)

g = int(0)
g1 = int(0)
g2 = int(0)
g3 = int(0)
g4 = int(0)
g5 = int(0)

somas_gain = int(0)
somas_loss = int(0)
somas_branco = int(0)
stop_loss = int(0)
stop_gain = int(0)


tipo_conta = int(0) #int(input('Deseja operar em conta REAL(1) ou Treinamento(2)? (1 ou 2)'))
valor_banca = int(1000) #int(input('Qual o valor da sua banca?'))
entrada = int(50) #int(input('Qual valor da sua primeira entrada?'))
stop_loss = 0 #int(input('Quantos loss você aceita tomar?'))
stop_gain = 0 #int(input('Qual sua meta de vitória em porcentagem(%)?'))
quantidade_gales = 0 #int(input('Quantos gales você quer?'))
multiplicador = int(2) #int(input('Qual será seu fator multiplicador de gale?'))

 #simulador banca
g1 = int(0)
g2 = int(0)
g3 = int(0)
g4 = int(0)
g5 = int(0)

# definindo valor do branco
valor_branco = int(entrada * 0.1)
if valor_branco < 2:
    valor_branco = 2
somas_branco = int(valor_branco * 14)

# Definições de gales
g = valor_branco + entrada
g1 = g * multiplicador
g2 = g1 * multiplicador
g3 = g2 * multiplicador
g4 = g3 * multiplicador
g5 = g4 * multiplicador

# Laço de start
while rodada == 0:

    # Receber dados da api OK
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista = [x['color'] for x in resultado]

    # calculo para logica da previsao OK
    a = int(num1)
    somas += a
    dividir_somas = somas
    resultado_divisao = int(dividir_somas / 2)
    total_rodadas = total_rodadas + 1


    # condição de previsão OK
    if resultado_divisao % 2 == 0:
        # Preto padrão API numero Par OK
        previsao = 1
    else:
        # Vermelho padrão API numero Impar OK
        previsao = 2

    # Gerar lista de previsoes e recentes OK
    lista_previsoes.insert(0, int(previsao))
    lista_recents.insert(0, int(num_recent))

    # Pegar numeros separadamente da lista
    num1, num2, *outras_lista = lista
    prev1, prev2, *outras_previsoes = lista_previsoes
    rece1, rece2, *outras_recentes = lista_recents

    # inverter valores, somar cores e catalogar OK
    if num1 == 0:
        num_recent = 0
        branco += 1
    if num1 == 1:
        num_recent = 2
        vermelho += 1
    if num1 == 2:
        num_recent = 1
        preto += 1

    if num2 == 0:
        num_anterior = 0
        branco += 1
    if num2 == 1:
        num_anterior = 2
        vermelho += 1
    if num2 == 2:
        num_anterior = 1
        preto += 1

    if prev1 == 0:
        prev_recent = 0
        branco += 1
    if prev1 == 1:
        prev_recent = 2
        vermelho += 1
    if prev1 == 2:
        prev1_recent = 1
        preto += 1

    if prev2 == 1:
        prev_recent = 2
        vermelho += 1
    if prev2 == 2:
        prev_recent = 1
        preto += 1

    # Definir string para previsoes OK
    if previsao == 1:
        prev_text = 'Preto'
    if previsao == 2:
        prev_text = 'Vermelho'


    # Definir string de rodadas ok
    if num1 == 0:
        coringa = 'Coringa'
    if num1 == 2:
        coringa = 'Preto'
    if num1 == 1:
        coringa = 'Vermelho'

    # somar contadores de vitorias e derrotas
    if num_recent == prev2 & prev2 > 0:
        gain += 1
        contador_gains += 1
        contador_losses -= contador_losses
        zerador_losses -= zerador_losses
    elif prev2 > 0:
            contador_losses += 1
            zerador_losses += 1

    if num_recent == 0:
        somas_coringas += 1
        contador_losses -= contador_losses
        zerador_losses -= zerador_losses
        banca_total += valor_branco * 14

    if contador_losses == 4:
        loss += 1
        contador_losses -= 4
        zerador_losses -= 4


# Simulador de banca

    #condicionais para atualização por rodada do saldo em banca


    # Gerar lista de somas de gains/ loss e gains/loss
    lista_somas_gains.insert(0, int(contador_gains))
    lista_somas_losses.insert(0, int(contador_losses))

    sg_recent, sg_anterior, *outros_gains = lista_somas_gains
    sl_recent, sl_anterior, *outros_losses = lista_somas_losses

    if num_recent == prev2 & prev2 > 0:
        banca_total += entrada - valor_branco
        somas_loss -= somas_loss
        somas_gain -= somas_gain
    else:
        somas_loss -= entrada + valor_branco
        somas_gain = entrada + valor_branco


    if contador_losses == 1:
        somas_loss -= g
        banca_total -= g
        somas_gain += g + g

    if contador_losses == 2:
        somas_loss -= g1
        banca_total -= g1
        somas_gain += g1

    if contador_losses == 3:
        somas_loss -= g2
        banca_total -= g2
        somas_gain += g2

    if contador_losses == 4:
        somas_loss -= g3
        banca_total -= g3
        somas_gain += g3

    if contador_losses == 5:
        somas_loss -= g4
        banca_total -= g4
        somas_gain += g4

    if contador_losses == 5:
        somas_loss -= g5
        banca_total -= g5
        somas_gain += g5

        #if contador_losses == 6:
     #   somas_loss += g1 + valor_branco
     #   banca_total -= entrada + g1 + valor_branco
     #   somas_gain -= entrada + g1 + valor_branco
    valor_banca = int(valor_banca + (gain * entrada ) + (somas_coringas * somas_branco) + (somas_loss))
    banca_total = valor_banca


    #print(str(Previsao))
    print()
    print('Apostar na cor: {}'.format(prev_text))
    print('Partida Nº: {}'.format(total_rodadas))
    #print()
    print('Cor da rodada: {}'.format(coringa))
    print('Gain {}'.format(gain), 'Loss {}'.format(loss), 'Branco {}'.format(somas_coringas))
    lucro_bruto = 0
    lucro_liquido = 0
    lucro_bruto = (gain * entrada)+(somas_coringas * valor_branco * 14)
    lucro_liquido = lucro_bruto - (loss * entrada) + (somas_coringas * valor_branco) - valor_branco
    print('Lucro bruto: {}'.format(lucro_bruto), 'Lucro liquido: {}'.format(lucro_liquido))
    hora_atual = float(0)
    hora_atual = total_rodadas * 0.3 / 0.6
    print('Tempo de trabalho: {} mim'.format(hora_atual, 2))
    print('Saldo atual:{}'.format(banca_total))
    print(contador_gains, contador_losses, gain, loss, zerador_losses)
    print(num_recent, num_anterior, prev1, prev2, rodada, previsao)
    print(somas_gain, somas_loss, valor_branco, somas_branco)
    print(sg_recent, sg_anterior, sl_recent, sl_anterior)
    #print(g, g1, g2, g3, g4, g5)
    print(resultado_divisao)
    #print(lista_recents)

    time.sleep(29.63)
