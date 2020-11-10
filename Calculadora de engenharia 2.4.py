from time import time
from time import sleep
from datetime import date


clr = {'red': '\033[31m',
       'green': '\033[32m',
       'orange': '\033[33m',
       'blue': '\033[34m',
       'purple': '\033[35m',
       'blue+': '\033[36m',
       'white': '\033[38m'}

timer_str = time()
print('=\+_Engineer Calculator 2.4_+/=  {}'.format(date.today()))
while True:
    print('''
    Select your calc tool
    Brick calculator [1]
    Greatness Converter [2]
    Volume calculator  [3]
    Painting Wall [4]
    Exit [5]''')
    select = int(input('-> '))

    if select > 5 or select <= 0:
        print('Invalid number')

    elif select == 1:
        info = str(input('Show info? y/n ')).strip().lower()
        if info == 'y':
            print('Calculate how many bricks will be needed to build a wall')

        c = float(input('What is the length of the brick in cm '))
        a = float(input('How tall is the brick in cm '))
        brick_calc = 10000/(a * c)
        print('OK! Enter the wall data:')
        c1 = float(input('What is the length of the wall in meters? '))
        a1 = float(input('How high is the wall in meters? '))
        wall_calc = c1 * a1
        print('''REGISTERED DATA!

Will be spent {:.2f} bricks per square meter
For the construction of the wall, there will be approximately {:.2f} bricks
'''.format(brick_calc, wall_calc*brick_calc))

    elif select == 2:
        info = str(input('Show info? y/n '))
        if info == 'y':
            print('simple greatness Converter ')
        med = float(input('Amount in meters to be converted ->'))
        print('''Km   {:.2f}
hm   {:.2f}
dam  {:.2f}
m    {:.0f}
dm   {:.0f}
cm   {:.0f}
mm   {:.0f}'''.format(med/1000, med/100, med/10, med, med*10, med*100, med*1000, med*1000))

    elif select == 3:
        info = str(input('Show info? y/n '))
        if info == 'y':
            print('Ferramenta de calculo de volume para piscinas')
        c = float(input('Comprimento em m ->' ))
        l = float(input('Largura em m -> '))
        p = float(input('Profundidade em m ->'))
        calc = c*l*p
        print('''Tendo uma area total de {:.2f} metros cubicos
a piscina nessesitará de {:.2f} litros de agua ou {:.2f}KL'''.format(calc, calc*1000, (calc*1000)/1000))

    elif select == 4:
        info = str(input('Show info? s/n')).strip().lower()
        if info == 's':
            print('Calcula quantidade de tinta gasta para pintar uma  ou  mais paredes')
            print('')
        wall_largura = float(input('Largura da parede: '))
        wall_altura = float(input('Altura da parede: '))
        wall_m2 = wall_largura*wall_altura
        sub = str(input('Sua parede possui portas ou janelas? s/n')).strip().lower()
        if sub == 's':
            print('Adicione as medidas dos tais')
            sub_largura = float(input('Largura: '))
            sub_altura = float(input('Largura: '))
            sub_m2 = sub_largura*sub_altura
            add = str(input('Existe mais alguma porta ou janela? s/n')).strip().lower()
            if add == 's':
                add_num = int(input('Quantas? '))
                for cont in range(0, add_num+1):
                    sub_largura = float(input('Largura: '))
                    sub_altura = float(input('Largura: '))
                    subm2_calc = sub_altura*sub_largura
                    subm2_calc += sub_m2
        if sub == 'n':
            sub_m2 = 0
        m2_sub = wall_m2 - sub_m2
        print('''Ok!
A área total da parede é de {:.2f}m2'''.format(m2_sub))
        litro_m2 = int(input('Litro de tinta por m2: '))
        print(f'Uma parede com {m2_sub}m2, sendo pintada com um galão que consome {litro_m2} litros por m2')
        print('consumirá aproximadamente {} litros de tinta'.format(m2_sub/litro_m2))

    elif select == 5:
        timer_end = time()
        break
timer_calc = (timer_end - timer_str)
cron = ('Você ultilizou o programa por {:.2f} minutos'.format(timer_calc/60))
print(cron.replace('.', ':'))

sleep(5)
