'''13. Cree un programa similar al 12, pero en lugar de sumar debe escribir al Std. Out el cuadrado de los números recibidos.'''

import sys
import re

Bool = 2

while Bool == 2:

  Num = input()

  if  re.search('[1-9]', Num):

        print(pow(int(Num),2))

  elif Num == "":
        Bool += 2
    
  else:
        print("invalid value", Num, file = sys.stderr) 
  
