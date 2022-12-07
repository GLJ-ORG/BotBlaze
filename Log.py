import logging
import os
import datetime
from datetime import date

MesAno = date.today()
MesAno = MesAno.strftime('%m%Y')

Diretorio = f'C:\LogBot\{MesAno}'
try:
    os.makedirs(Diretorio)
finally:
    Dia = date.today()
    Dia = Dia.strftime('%d')
    Diretorio = f'{Diretorio}/{Dia}.log'
    logging.basicConfig(level=logging.DEBUG, filename=Diretorio, encoding='utf-8')
    logging.info('Testando Log')
