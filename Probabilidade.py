from math import ceil

n_soma = 0
auto_ceil = True


print('''Calculadora de probabilidade 1.0''')

while True:
    print('''  
   </Menu de seleção\>
 Probabilidade Clássica [1]
 Probabiledade Frequntista [2]
 Instruções para ultilização [5]
 Opçoes e preferências [6]
 Fechar programa [8]
''')
    slc = int(input('>>> '))
    if slc == 1:
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
    elif slc == 2:
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
    elif slc == 3:
        print('''Este programa foi desenvolvido para facilitar o calculo de probabilidade, para sua ultilização
o usuario deve digitar na linha de comando sua escolha de calculo pelo numero entre conchetes.
Todos os resultados de porcentagem do programa são arredondados a menos esse recurso seja desabilitado
em opções. 
''')

    elif slc == 4:
        print('''Desabilitar arredondamento automatico [1]
Restaurar configurações padrão [2]''')
        cod = int(input('/> '))
        if cod == 1:
            auto_ceil = False
        elif cod == 2:
            auto_ceil = True
        print('Registrado!')

        if slc == 8:
            break
