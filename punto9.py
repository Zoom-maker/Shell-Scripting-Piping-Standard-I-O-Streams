''' 9. Cree un programa similar al 6, pero que reciba su entrada desde el Standard Input, no desde los argumentos 
de linea de comando. '''

import sys

Num = input("Ingrese un numero:")

if int(Num) <= 0:
    print("Invalid Input", Num, file = sys.stderr)
else:
    print("Good one", Num)