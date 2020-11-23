''' 6. Cree un programa que reciba un numero como argumento de linea de comando, si el numero es negativo 
o cero debe escribir por el Standard Error el mensaje "Invalid input <numero>.". Si el numero es positivo, 
debe escribir por el Standard Output el mensaje "Good one <numero>.". '''

import sys

script, Num = sys.argv

if int(Num) <= 0:

    print("Invalid input", Num, file = sys.stderr)
else:
    print("Good one", Num)
