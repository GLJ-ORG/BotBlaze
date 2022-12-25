import logging
import os
import datetime
from datetime import date

def PreencheLog(Msg):
    MesAno = date.today()
    MesAno = MesAno.strftime('%m%Y')

    Diretorio = f'C:\LogBot\Rewiw{MesAno}'
    try:
        os.makedirs(Diretorio)
    except:
        exit
    finally:
        Dia = date.today()
        Dia = Dia.strftime('%d')
        Diretorio = f'{Diretorio}/{Dia}.log'

        DataHora = datetime.datetime.now()
        DataHora = DataHora.strftime('%d/%m/%Y %H:%M:%S')

        logging.basicConfig(format=f'{DataHora} - %(message)s', level=logging.INFO, filename=Diretorio, encoding='utf-8')
        logging.info(Msg)
        os.system('cls')