'''11. Cree un programa que escriba al Std. Out los números del 1 hasta N'''


import sys

Script, (Num) = sys.argv

if (int(Num) <= 0) or isinstance (Num, str):

    print("invalid value", Num, file = sys.stderr) 

else:

    for x in range(1, int(Num) + 1):
        print(x)

print()
