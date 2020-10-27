# 0.1 imports
from random import randint
from math import trunc
import time

# 0.2 variables
exit = False
s = 0
timer_cont = 0
acertos = 0
erros = 0
record = 0

# 0.3 colors
clr = {'red': '\033[31m',
       'green': '\033[32m',
       'orange': '\033[33m',
       'blue': '\033[34m',
       'purple': '\033[35m',
       'blue+': '\033[36m',
       'white': '\033[38m'}

# 1.1 select menu
while not exit:
    print('''{} =-=-= Math GAME by kEv =-=-=
  Selecione o modo de jogo:
  Jogo da adivinhação [1]
  Tabuada MaxSpeed [2]
'''.format(clr['blue+']))

    cod = int(input('{}Digite o numero desejado entre []: '.format(clr['green'])))

    # 1.2 detect invalid sintax
    while cod != 1 and cod != 2:
        print('{}O número {} é invalido, tente novamente'.format(clr['red'], cod))
        cod = int(input('{}Digite o numero desejado entre []: '.format(clr['white'])))

    # 2.1 program detect process
    if cod == 1:

        # 2.2 program run
        rand = randint(1, 5)
        win = False
        print('{} Tente adivinhar o número que eu pensei! de 0 a 5'.format(clr['purple']))
        while not win:
            n = int(input('{} Digite seu palpite: '.format(clr['white'])))
            s += 1

            # 2.3 win game detector
            if n == rand:
                print('{}Você ganhou! Eu pensei nesse número.'.format(clr['green']))
                print('Tentativas usadas: {}'.format(s))
                print('''
                ''')
                win = True
            else:
                print('{}Você errou! Tente novamente'.format(clr['red']))

    # 3.1 program detect process
    elif cod == 2:

        # 3.2 program run
        print('{}-=-=- Tabuada MaxSpeed -=-=-'.format(clr['blue+']))
        info = str(input('Mostrar tutorial? s/n ')).strip().lower()
        if info == 's':
            print('''{}O jogo consiste em acertar a multiplicação de 5 números no menor tempo
possivel acertando o maximo possivel
'''.format(clr['orange']))
        start = str(input('Para iniciar o jogo digite -> OK  '.format(clr['white']))).strip().upper()
        if start == 'OK':
            print('JOGO INICIADO')
            timer_str = time.time()
            for c in range(0, 5):
                rand = randint(1, 10)
                rand2 = randint(1, 10)
                print('{}{} * {} = ?'.format(clr['green'], rand, rand2))
                calc = (rand * rand2)
                print(calc)
                resp = int(input('{}Qual é o resultado da conta? _-> '.format(clr['blue+'])))

                # game win detector
                if resp == calc:
                    acertos += 1
                else:
                    erros += 1
            timer_end = time.time()
            time_calc = (timer_end - timer_str)
            current = trunc(time_calc)
            print('{}Você acertou {} e errou {}'.format(clr['purple'], acertos, erros))
            print('Tempo decorrido: {}s '.format(current))
            print('''
            ''')
