from rewiw import num1



valor_entrada = 5
valor_branco = 2
valor_entrada = gestao_banca(100, 3)

def gales(valor_entrada, branco, contador):
  g = valor_entrada + branco
  g1 = (g * 2) + branco
  g2 = (g1 * 2) + branco
  g3 = (g2 * 2) + branco
  g4 = (g3 * 2) + branco
  g5 = (g4 * 2) + branco

  if contador == 0:
    return g
  elif contador == 1:
    return g1
  elif contador == 2:
    return g2
  elif contador == 3:
    return g3
  elif contador == 4:
    return g4
  elif contador == 5:
    return g5
  else:
    return "Contador inválido"


def branco(entrada):
  valor_branco = entrada * 0.15
  if valor_branco < 1.1:
    valor_branco = 1.1
  return valor_branco

def estrategia(num1):
  soma = num1
  for i in range(num1):
    soma += i
  return soma / 2

def gestao_banca(stop_loss, quantidade_gales):
  if quantidade_gales == 1:
    valor_entrada = stop_loss / 3
  elif quantidade_gales == 2:
    valor_entrada = stop_loss / 7
  elif quantidade_gales == 3:
    valor_entrada = stop_loss / 15
  elif quantidade_gales == 4:
    valor_entrada = stop_loss / 31
  elif quantidade_gales == 5:
    valor_entrada = stop_loss / 63
  else:
    valor_entrada = 0
  return valor_entrada

def contadores_vd(num1, prev2, quantidade_loss, gain, loss, contador_loss, zerador_loss):
  if num1 == prev2 & prev2 > 0 or num1 == 0:
    gain += 1
    contador_loss = 0
    zerador_loss = 0
  else:
    contador_loss += 1
    zerador_loss += 1
    if contador_loss == quantidade_loss + 1:
      loss += 1
      contador_loss = 0
      zerador_loss = 0
  return gain, loss, contador_loss, zerador_loss

def cor_rodada(rewiw.

    num1):
  if num1 == 1:
    return "vermelho"
  elif num1 == 2:
    return "preto"
  elif num1 == 0:
    return "coringa"
#def cor


#def simulador_banca


#def conta_real


#def inversao_numero


#def pegar_numeros


#def previsao_darodada

      #      return text_cor

