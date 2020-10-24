from random import randint
import time

exit = False
s = 0
acertos = 0
erros = 0

while not exit:
    print(''' =-=-= Math GAME by kEv =-=-=
  equipe : 
  Selecione o modo de jogo:
  Jogo da adivinhação [1]
  Tabuada MaxSpeed [2]
''')
    cod = int(input('Digite o numero desejado entre []: '))
    while cod != 1 and cod != 2:
        print('O número {} é invalido, tente novamente'.format(cod))
        cod = int(input('Digite o numero desejado entre []: '))
    if cod == 1:
        rand = randint(1, 5)
        win = False
        print('Tente adivinhar o número que eu pensei! de 0 a 5')
        while not win:
            n = int(input('Digite seu palpite: '))
            s += 1
            if n == rand:
                print('''Você ganhou! Eu pensei nesse número.
Tentativas usadas: {}

'''.format(s))
            win = True
        else:
            print('Você errou! Tente novamente')
    elif cod == 2:
        print('-=-=- Tabuada MaxSpeed -=-=-')
        info = str(input('Mostrar tutorial? s/n ')).strip().lower()
        if info == 's':
            print('''O jogo consiste em acertar a multiplicação de 5 números no menor tempo
            possivel acertando o maximo possivel
''')
        start = str(input('Para iniciar o jogo digite -> OK  ')).strip().upper()
        if start == 'OK':
            print('JOGO INICIADO')
            for c in range(0, 5):
                rand = randint(1, 10)
                rand2 = randint(1, 10)
                print('{} * {} = ?'.format(rand, rand2))
                calc = (rand * rand2)
                print(calc)
                resp = int(input('Qual é o resultado da conta? _-> '))
                if resp == calc:
                    acertos += 1
                else:
                    erros += 1
            print('Você acertou {} e errou {}'.format(acertos, erros))
            print('''
            
            
''')
