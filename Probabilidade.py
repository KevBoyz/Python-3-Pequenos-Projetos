from math import ceil

s = 0
n_soma = 0
auto_ceil = True
n = 0
calc_s = 1

while True:
    print('''Calculadora de probabilidade 1.0
    
Menu de seleção [1]
Instruções para ultilização [2]
Oções [3]
Créditos [4]
''')
    st_slc = int(input('_>'))
    if st_slc == 1:
        break
    elif st_slc == 2:
        print('''Este programa foi desenvolvido para facilitar o calculo de probabilidade, para sua ultilização
o usuario deve digitar na linha de comando sua escolha de calculo pelo numero entre conchetes.
Todos os resultados de porcentagem do programa são arredondados a menos esse recurso seja desabilitado
em opções. 
        ''')
    elif st_slc == 3:
        print('''Desabilitar arredondamento automatico [1]
Restaurar configurações padrão [2]
Sair [0]''')
        cod = int(input('/> '))
        if cod == 1:
            auto_ceil = False
            print('Registrado!')
            print('')
        elif cod == 2:
            auto_ceil = True
            print('Registrado!')
        print('')
    elif cod == 0:
        print('')
    elif st_slc == 4:
        print('Programa escrito po KevBoys -> ')

while True:
    print('''  
   </Menu de seleção\>
 Probabilidade Clássica [1]
 Probabiledade Frequntista [2]
 Probilidade de Quebra de senhas [3]
 Contagem de Possibilidades [4]
 
''')
    slc = int(input('>>> '))
    if slc == 1:
        while True:
            n_soma += 1
            n_fav = int(input('Numero de casos favoraveis: '))
            n_pos = int(input('Numero de casos possiveis: '))
            print('')
            if n_pos < n_fav:
                while n_pos < n_fav:
                    print('O casos favoraveis não podem ser maior que os possiveis, tente novamente')
                    n_fav = int(input('Numero de casos favoraveis: '))
                    n_pos = int(input('Numero de casos possiveis: '))
                    print('')

            if auto_ceil:
                print(f'Resultados:  [Decimal] = {n_fav/n_pos:.5f} [Porcentagem] = {ceil((n_fav/n_pos)*100)}%')
            elif not auto_ceil:
                print(f'Resultados:  [Decimal] = {n_fav / n_pos} [Porcentagem] = {(n_fav / n_pos) * 100}%')
            retry = str(input('Fazer nova operação s/n ')).strip().lower()
            if retry == 'n':
                break

    elif slc == 2:
        while True:
            n_soma += 1
            n_ocr = int(input('Numero de ocorrencias: '))
            n_exe = int(input('Numero de ações executadas: '))
            if n_exe > n_ocr:
                while n_ocr > n_exe:
                    print('O numero de ocorrencias não pode ser maior que o numero de ações executadas, tente novamente')
                    n_ocr = int(input('Numero de ocorrencias'))
                    n_exe = int(input('Numero de ações executadas'))
                    print('')

            if auto_ceil:
                print(f'Resultados:  [Decimal] = {n_ocr / n_exe:.5f} [Porcentagem] = {ceil((n_ocr / n_exe) * 100)}%')
            elif not auto_ceil:
                print(f'Resultados:  [Decimal] = {n_ocr / n_exe} [Porcentagem] = {(n_ocr / n_exe) * 100}%')
            retry = str(input('Fazer nova operação s/n ')).strip().lower()
            if retry == 'n':
                break
    elif slc == 3:
        num = str(input('A senha possui numeros? s/n ')).strip().lower()
        if num == 's':
            n += 10
        letter = str(input('A senha possui letras? s/n ')).strip().lower()
        if letter == 's':
            n += 26
        simbols = str(input('A senha possui simblos? s/n ')).strip().lower()
        if simbols == 's':
            n += 20
        carcteres = int(input('Quantos caracteres a senha possui? '))
        print(n)
        print('OK!')
        for c in range(0, carcteres):
            calc_s *= n
        print(f'Maximo de tentativas para quebra de senha {calc_s}')
        print(f'Probabilidade de ocorrer quebra por tentativa {1/calc_s:.4f}')
        print(f'Em porcentagem -> {(1/calc_s)*100:.4f}%')


    elif slc == 4:
        calc = 1
        n_soma += 1
        n_ind = int(input('Número de individuos: '))
        n_op = int(input('Número de opções: '))
        for c in range(1, n_op):
            if c == 1:
                calc *= n_ind * (n_ind - c)
            else:
                calc *= (n_ind - c)
            print(f'Resultado -> {calc}')
            print('')

