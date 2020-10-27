import time
from math import trunc

print('''-=-=-=Cronometro Pyton-=-=-=-=-''')
while not exit:
  print('''Seleciono modo de uso:
  Cronometro [1]
  Data [2]
  Medidor de velocidade [3]''')
  
  cod = int(input('->_ '))
  
  if cod != 1 and cod != 2 and cod != 3:
    print('Número inválido! Tente novamente')
    cod = int(input('->_ '))
  
  elif cod == 1:
    print('Para inicialzar o cronometro digite ´OK`')
    start = str(input('Digite sua confirmação: ')).strip().upper()
    if start == 'OK':
      timer_str = time.time()
      end = int(input('Para parar o cronometro digite 0 _-> '))
      timer_end = time.time()
      timer_calc = (timer_end - timer_str)
      current = trunc(timer_calc)
      if current > 60:
        calc = (current/60)
        minutos = calc
        segundos = (current//60)
