import requests
import json
import time

#lista_atual = []
#lista_atual = lista
lista = 0
lista1 = 0
lista2 = 0

g1 = 0
g2 = 0


preto = 0
vermelho = 0
branco = 0
previsao = 0

entrada = 0
gain = 0
loss = 0
contador_gain = 0
contador_loss = 0



n = int(2)

while(n1 > 0): #n vezes
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista = [x['color'] for x in resultado]
    print(lista)
    time.sleep(30)

c = n1
c1 = n2
c2 = n3
n1, n2, n3, n4, *outra_lista, final = lista  #pegar 1 valor da lista

if c == 0:  # inverter roll recente para calculo da maquina
    branco += 1
    c = 0
elif c == 1:
    vermelho += 1
    c = 2
elif c == 2:
    c = 1
    preto += 1

if c1 == 0:  # inverter roll recente para calculo da maquina
    branco += 1
    c1 = 0
elif c1 == 1:
    vermelho += 1
    c1 = 2
elif c1 == 2:
    c1 = 1
    preto += 1

if c2 == 0:  # inverter roll recente para calculo da maquina
    branco += 1
    c2 = 0
elif c2 == 1:
    vermelho += 1
    c2 = 2
elif c2 == 2:
    c2 = 1
    preto += 1

    acc = 0  # variavel acumuladora, guarda a soma
    i = 0
    res = 0
    a = c

    a = int(c)
    acc = acc + a
    numero = acc
    res = int(numero / 2)
    i = i + 1
    #time.sleep(5)


    if previsao != c:
        contador_loss += 1
    else:
        contador_gain += 1

    if contador_loss == 3:
        loss += 1
        contador_loss -= 3

    if n1 != previsao:
        gain = gain + 1

    if res % 2 == 0:
        previsao = 1
        print('Preto Par')
    else:
        previsao = 2
        print('Vermelho Impar')
    print('Gain {}'.format(gain), 'Loss {}'.format(loss))
    print(lista)
    print(c, c1, c2)







































