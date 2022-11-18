import requests
import json
import time


previsao = int(0)
lista_previsoes = [0]
saida_recente = int(0)
lista_recents = [0]
lista_comparacao = int(0)
prev_text = str()
convert_prev = int(previsao)

preto = int(0)
vermelho = int(0)
branco = int(0)

# numeros recentes invertido para calculo de previsoes
num1 = int(0)
num2 = int(0)
num_recent = num1
num_anterior = num2

prev1 = int(0)
prev2 = int(0)
prev_recent = prev1
prev_anterior = prev2

gain = int(0)
loss = int(0)

contador_gains = int(0)
contador_losses = int(0)
zerador_losses = contador_losses
contador_branco = int(0)
entrada = int(0)
g1 = int(0)
g2 = int(0)

total_rodadas = int(0)
rodada = num1
condicao = int(0)
somas = 0
dividir_somas = 0
resultado_divisao = 0


# Laço de start
while rodada == 0:

    # Receber dados da api
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista = [x['color'] for x in resultado]

    # Gerar lista de previsoes e recentes
    lista_previsoes.insert(0, int(previsao))
    lista_recents.insert(0, int(rodada))

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
        prev_recent = 1
        preto += 1

    if prev2 == 0:
        prev_anterior = 0
        branco += 1
    if prev2 == 1:
        prev_anterior = 2
        vermelho += 1
    if prev2 == 2:
        prev_anterior = 1
        preto += 1

    # calculo para logica da previsao OK
    a = int(num_recent)
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

    # Definir string para previsoes
    if previsao == 1:
        prev_text = 'Preto'
    else:
        prev_text = 'Vermelho'

    # somar contadores de vitorias e derrotas
    if previsao == num_recent:
        gain += 1
        contador_gains += 1
        contador_losses = zerador_losses
    else:
        contador_losses += 1
        zerador_losses += 1
        continue

    if contador_losses == 3:
        contador_losses -= 3
        loss += 1



    #print(str(Previsao))
    print()
    print(prev_text)
    print('Gain {}'.format(gain), 'Loss {}'.format(loss))
    print(contador_gains, contador_losses, gain, loss, zerador_losses)
    print(num_recent,num_anterior, prev_recent, prev_anterior, previsao, convert_prev)

    #print(lista_recents)
    #print(lista_previsoes)
    time.sleep(28)
