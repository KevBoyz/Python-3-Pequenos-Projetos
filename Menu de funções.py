from time import sleep
maior = 0
exit = False
print('\033[36m__MENU 1.0__')
n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
while not exit:
    print('''\033[39m   -=-=-=-=-=-=-=-=-
    SOMAR [1]
    MULTIPLICAR [2]
    MAIOR [3]
    NOVOS NÚMEROS [4]
    SAIR DO PROGRAMA [5]
    -=-=-=-=-=-=-=-=-''')
    cod = int(input('\033[38m_-> '))
    if cod == 1:
        print('\033[35m {} + {} = {}'.format(n1, n2, n2+n1))
    elif cod == 2:
        print('\033[35m{} x {} = {}'.format(n1, n2, n1*n2))
    elif cod == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
    elif cod == 4:
        n1 = int(input('Digite um número '))
        n2 = int(input('Digite outro número '))
    elif cod == 5:
        exit = True
print('\033[31mProcesso Finalizado')
sleep(3)
