import requests
import json
import time


previsao = int(0)
lista_previsoes = [0]
# lista_previsoes.append(0)
saida_recente = int(0)
lista_recents = [0]
lista_comparacao = int(0)
prev_text = str()

preto = int(0)
vermelho = int(0)
branco = int(0)

# numeros recentes invertido para calculo de previsoes
num1 = int(0)
num2 = int(0)
num3 = int(0)

prev1 = int(0)
prev2 = int(0)
prev3 = int(0)

gain = int(0)
contador_gains = int(0)
loss = int(0)
contador_losses = int(0)

contador_branco = int(0)
entrada = int(0)
g1 = int(0)
g2 = int(0)

total_rodadas = int(0)
rodada = int(num1)
condicao = int(0)
somas = int(0)
divsao_somas = int(0)
resultado_divisao = int(0)


# Laço de start
while rodada == 0:
    a = num1
    somas = somas + num1
    divsao_somas = somas / 2
    total_rodadas = total_rodadas + 1

    # condição de previsão
    # Preto padrão API numero Par
    if int(divsao_somas % 2) == 0:
        previsao = 2
    # Vermelho padrão API numero Impar
    else:
        previsao = 1

    if previsao == 2:
        prev_text = 'Preto'
    else:
        prev_text = 'Vermelho'

    # Gerar lista de previsoes e recentes
    lista_previsoes.insert(0, int(previsao))
    lista_recents.insert(0, int(rodada))

    # Receber dados da api
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista = [x['color'] for x in resultado]

    # Pegar numeros separadamente da lista
    num1, num2, *outras_lista = lista
    prev1, prev2, *outras_previsoes = lista_previsoes
    rece1, rece2, *outras_recentes = lista_recents

    # somar contadores de vitorias e derrotas
    if num1 == prev2 & prev2 > 0:
        contador_gains += 1
        gain += 1

    if prev2 > 0 & num1 != prev2:
        contador_losses += 1

    if num1 == prev2:
        contador_losses +1

    if contador_losses == 3:
        contador_losses -= 3
        loss += 1

    # inverter valores somar cores catalogar
    if num1 == 0:
        branco += 1
        num1 = 0
    elif num1 == 1:
        vermelho += 1
        num1 = 2
    elif num1 == 2:
        num1 = 1
        preto += 1

    if num2 == 0:
        branco += 1
        num2 = 0
    elif num2 == 1:
        vermelho += 1
        num2 = 2
    elif num2 == 2:
        num2 = 1
        preto += 1

    if num3 == 0:
        branco += 1
        num3 = 0
    elif num3 == 1:
        vermelho += 1
        num3 = 2
    elif num3 == 2:
        num3 = 1
        preto += 1

    if prev1 == 0:
            branco += 1
            prev1 = 0
    elif prev1 == 1:
            vermelho += 1
            prev1 = 2
    elif prev1 == 2:
            prev1 = 1
            preto += 1

    if prev2 == 0:
            branco += 1
            prev2 = 0
    elif prev2 == 1:
            vermelho += 1
            prev2 = 2
    elif prev2 == 2:
            prev2 = 1
            preto += 1

    if prev3 == 0:
            branco += 1
            prev3 = 0
    elif prev3 == 1:
            vermelho += 1
            prev3 = 2
    elif prev3 == 2:
            prev3 = 1
            preto += 1
    #print(str(Previsao))
    print()
    print(prev_text)
    print('Gain {}'.format(gain), 'Loss {}'.format(loss))
    print(contador_gains, contador_losses, gain, loss)
    print(num1,num2, prev1, prev2, rece1, rece2)

    # print(lista_recents)
    # print(lista_previsoes)

    time.sleep(28)
