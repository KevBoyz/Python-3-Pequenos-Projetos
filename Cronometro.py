import datetime
import time
from math import trunc

exit = False

print('-=-=-=Cronometro Pyton-=-=-=-=-')
while not exit:
    print('''Seleciono modo de uso:

Cronometro [1]
Data [2]
Fechar o programa [3]''')

    cod = int(input('->_ '))

    if cod != 1 and cod != 2 and cod != 3:
        print('Número inválido! Tente novamente')
        cod = int(input('->_ '))

    elif cod == 1:
        print('Para inicialzar o cronometro digite ´OK`')
        start = str(input('Digite sua confirmação: ')).strip().upper()
        if start == 'OK':
            timer_str = time.time()
            print('O cronometro está em execução...')
            end = input('Para parar o cronometro pressione qualquer tecla')
            timer_end = time.time()
            timer_calc = (timer_end - timer_str)
            current = trunc(timer_calc)
            segundos = current
            minutos = 0
            if current > 60:
                calc = (current / 60)
                minutos = calc
                segundos = (current % 60)
        print('Tempo decorrido: {}min  {}sec'.format(minutos, current))
        print('''
        ''')
    elif cod == 2:
        print('Data atual: {}'.format(datetime.date.today()))
        print('''
        ''')
    elif cod == 3:
        exit = True
print('processo finalizado')
time.sleep(3)
