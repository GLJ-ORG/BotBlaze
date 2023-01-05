import requests
import json
import time


banca = 100
# Receber dados da api OK
def atualizador_color():

  while True:
    dados = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado = json.loads(dados.content)
    lista_color = [x['color'] for x in resultado]
    num1, num2, *outras_lista = lista_color
    return num1, num2, lista_color

def atualizador_roll():

  while True:
    dados2 = requests.get('https://blaze.com/api/roulette_games/recent')
    resultado2 = json.loads(dados2.content)
    lista_roll = [y['roll'] for y in resultado2]
    roll1, roll2, *outras_lista2 = lista_roll
    return roll1, roll2, lista_roll


#Simulador de banca
def simuladorde_banca():
 while True:
    banca = int(100)
    entrada = banca * 0.01
    valor_entrada = float(0)
    branco = valor_entrada * 0.15
    valor_branco = float(0)
    gale = 0
    somas_gale = float(0)
    quantidade_entradas = 4
    contador_loss = 1
    num1 = atualizador_roll()[0]
    prev2 = 1
#Definindo entrada
    if entrada < float(1.1):
        valor_entrada = float(1.1)
    else:
        valor_entrada = entrada
#definindo valor do branco
    if branco < 1.1:
          valor_branco = 1.1
    else:
        valor_branco = branco
#definindo valores dos gales
    g = (valor_entrada + branco) + branco
    g1 = (g * 2) + branco
    g2 = (g1 * 2) + branco
    g3 = (g2 * 2) + branco
    g4 = (g3 * 2) + branco
    g5 = (g4 * 2) + branco
    if contador_loss == 0:
        gale = g
        somas_gale = g
    elif contador_loss == 1:
        gale = g
        somas_gale = g
    elif contador_loss == 2:
        gale = g1
        somas_gale += g1
    elif contador_loss == 3:
        gale = g2
        somas_gale += g2
    elif contador_loss == 4:
        gale = g3
        somas_gale += g3
    elif contador_loss == 5:
        gale = g4
        somas_gale += g4
        return gale, somas_gale
    else:
        return 'Soma invalida'

    if num1 == 0 & contador_loss >= 1:
        banca += (branco * 14)
        somas_gale = 0
    elif num1 == prev2:
        banca += (gale + valor_entrada)
    elif contador_loss >= 1 & prev2 != num1:
        banca -= gale

        #print(banca, valor_entrada, valor_branco, gale, somas_gale, entrada, branco)
    return(banca)

#def contadores_vd(num1, prev2, quantidade_loss, gain, loss, contador_loss, zerador_loss):
 # if num1 == prev2 & prev2 > 0 or num1 == 0:
  #  gain += 1
   # contador_loss = 0
    #zerador_loss = 0
  #else:
   # contador_loss += 1
    #zerador_loss += 1
  #if contador_loss == quantidade_loss + 1:
   # loss += 1
    #contador_loss = 0
    #zerador_loss = 0
  #return gain, loss, contador_loss, zerador_loss

#def gales(valor_entrada, branco, contador):
 # g = valor_entrada + branco
  #g1 = (g * 2) + branco
  #g2 = (g1 * 2) + branco
  #g3 = (g2 * 2) + branco
  #g4 = (g3 * 2) + branco
  #g5 = (g4 * 2) + branco

  #if contador == 0:
   # return g
  #elif contador == 1:
   # return g1
  #elif contador == 2:
   # return g2
  #elif contador == 3:
   # return g3
  #elif contador == 4:
   # return g4
  #elif contador == 5:
   # return g5
  #else:
   # return "Contador inválido"

  #print(gales())
  #print(g, g1, g2, g3, g4, g5)


#def branco(entrada):
 # valor_branco = entrada * 0.15
  #if valor_branco < 1.1:
   # valor_branco = 1.1
  #return valor_branco

#def estrategia(num1):
 # soma = num1
  #for i in range(num1):
   # soma += i
  #return soma / 2

#def gestao_banca(stop_loss, quantidade_gales):
  #if quantidade_gales == 1:
   # valor_entrada = stop_loss / 3
  #elif quantidade_gales == 2:
   # valor_entrada = stop_loss / 7
  #elif quantidade_gales == 3:
   # valor_entrada = stop_loss / 15
  #elif quantidade_gales == 4:
   # valor_entrada = stop_loss / 31
  #elif quantidade_gales == 5:
   # valor_entrada = stop_loss / 63
  #else:
   # valor_entrada = 0
  #return valor_entrada



#def cor_rodada(num1):
 # if num1 == 1:
  #  return "vermelho"
  #elif num1 == 2:
   # return "preto"
  #elif num1 == 0:
   # return "coringa"
#valor_entrada = banca * 0.01
#if valor_entrada < 1.1:
 # valor_entrada = 1.1

#branco = valor_entrada * 0.15
#if branco < 1.1:
 # branco = 1.1

#g = valor_entrada + branco + branco
#g1 = (g * 2) + branco
#g2 = (g1 * 2) + branco
#g3 = (g2 * 2) + branco
#g4 = (g3 * 2) + branco
#g5 = (g4 * 2) + branco

#if contador == 0:
 # return g
#elif contador == 1:
 # return g1
#elif contador == 2:
 # return g2
#elif contador == 3:
 # return g3
#elif contador == 4:
 # return g4
#elif contador == 5:
 # return g5
#else:
''' return "Contador inválido"
def simulador_banca(valor_banca, num1, prev2, g, branco):
  if num1 == prev2:
    valor_banca += gales(g, branco) * 2
  elif num1 == 0:
    valor_banca += branco * 14
  else:
    valor_banca -= gales(g, branco)
  return valor_banca


#def cor


#def conta_real


#def inversao_numero


#def pegar_numeros


#def previsao_darodada

      #      return text_cor '''

