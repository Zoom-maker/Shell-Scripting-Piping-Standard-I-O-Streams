''' 12. Cree un programa que reciba números desde el Std. Input hasta recibir una linea en blanco, vacía, 
para luego escribir al Std. Output la sumatoria de los valores.'''

import sys
import re

Acumulator = 0
Bool = 2

while Bool == 2:

  Num = input()

  if  re.search('[1-9]', Num):

        Acumulator += int(Num)

  elif Num == "":
        Bool += 2
    
  else:
        print("invalid value", Num, file = sys.stderr) 
  

print("La suma es: ", Acumulator)
