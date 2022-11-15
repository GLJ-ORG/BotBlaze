import requests
import json
import time

#lista_atual = []
#lista_atual = lista
lista = 0
lista1 = 0
lista2 = 0

while (lista == lista1):

    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista = [x['color'] for x in resultado]

#if atual != lista:

    print(lista, lista1, lista2)
    time.sleep(2)


n1, n2, n3, n4 *outra_lista, final = lista  #pegar 1 valor da lista

c = n1
preto = 0
vermelho = 0
branco = 0

if c == 0:  # inverter roll recente para calculo da maquina
    branco += 1
    c = 0
elif c == 1:
    vermelho += 1
    c = 2
elif c == 2:
    c = 1
    preto += 1

n = int(500)

gain = 0
loss = 0

acc = 0 #variavel acumuladora, guarda a soma
i = 0
res = 0
a = c
while(i < n ): #n vezes

    a = int(c)
    acc = acc + a
    numero = acc
    res = int(numero / 2)
    i = i + 1
    #time.sleep(5)
    print(c)

    if int(c) == a:
        gain = gain + 1
    else:
        loss = loss + 1

    if res % 2 == 0:

        print('Preto Par {}'.format(numero))
    else:

        print('Vermelho Impar {}'.format(numero))
    print('Gain {}'.format(gain), 'Loss {}'.format(loss))







































