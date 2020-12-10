from time import time
from time import sleep
from datetime import date
from math import ceil

clr = {1: '\033[31m',    # Red Green Orange Blue Purple Blue+ White
       2: '\033[32m',    # Primeiro versionamento Github
       3: '\033[33m',
       4: '\033[34m',
       5: '\033[35m',
       6: '\033[36m',
       7: '\033[38m'}

timer_str = time()
print(f'{clr[2]}\+_Engineer Calculator 2.8_+/=  {date.today()}')
while True:
    print(f'''{clr[3]}
    Select your calc tool
    Brick calculator [1]
    Greatness Converter [2]
    Volume calculator  [3]
    Painting Wall [4]
    Exit [5]''')
    select = int(input('-> '))

    if select > 5 or select <= 0:
        print(f'{clr[1]}Invalid number')

    elif select == 1:
        info = str(input(f'{clr[7]}Show info? y/n ')).strip().lower()
        if info == 'y':
            print(f'{clr[2]}Calculate how many bricks will be needed to build a wall')

        brick_largura = float(input(f'{clr[3]}What is the length of the brick in cm '))
        brick_altura = float(input('How tall is the brick in cm '))
        brick_m2 = 10000/(brick_largura * brick_altura)
        print(f'{clr[5]}OK! Enter the wall data:')
        wall_largura = float(input(f'{clr[3]}What is the length of the wall in meters? '))
        wall_altura = float(input('How high is the wall in meters? '))
        wall_m2 = wall_largura * wall_altura
        print('''{}REGISTERED DATA!

Will be spent {:.2f} bricks per square meter
For the construction of the wall, there will be approximately {:.2f} bricks
'''.format(clr[5], brick_m2, wall_m2*brick_m2))

    elif select == 2:
        info = str(input(f'{clr[7]}Show info? y/n '))
        if info == 'y':
            print(f'{clr[2]}simple greatness Converter ')
        med = int(input(f'{clr[3]}Amount in meters to be converted ->'))
        print(f'''{clr[5]}Km   {med/1000}
hm   {med/100}
dam  {med/10}
m    {med}
dm   {med*10}
cm   {med*100}
mm   {med*1000}''')

    elif select == 3:
        info = str(input('Show info? y/n '))
        if info == 'y':
            print('Ferramenta de calculo de volume para piscinas')
        pool_comprimento = float(input('Comprimento em m ->' ))
        pool_largura = float(input('Largura em m -> '))
        pool_profundidade = float(input('Profundidade em m ->'))
        pool_m3 = pool_comprimento*pool_largura*pool_profundidade
        print(f'''Tendo uma area total de {pool_m3} metros cubicos
a piscina nessesitará de {pool_m3*1000} litros de agua ou {(pool_m3*1000)/1000}KL''')

    elif select == 4:
        info = str(input('Show info? s/n')).strip().lower()
        if info == 's':
            print('Calcula quantidade de tinta gasta para pintar uma  ou  mais paredes')
            print('Medidas cobradas no programa devem ser colocadas em metro')
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
                    sub_altura = float(input('Altura: '))
                    subm2_calc = sub_altura*sub_largura
                    subm2_calc += sub_m2
        if sub == 'n':
            sub_m2 = 0
        m2_sub = wall_m2 - sub_m2
        print(f'''Ok!
A área total da parede é de {m2_sub}m2''')
        litro_m2 = float(input('Litro de tinta por m2: '))
        print(f'Uma parede com {m2_sub}m2, sendo pintada com um galão que consome {litro_m2} litros por m2')
        print(f'consumirá aproximadamente {m2_sub/litro_m2} litros de tinta')

    elif select == 5:
        timer_end = time()
        break
timer_calc = (timer_end - timer_str)
cron = ('Você ultilizou o programa por {:.2f} minutos'.format(timer_calc/60))
print(cron.replace('.', ':'))
sleep(5)
