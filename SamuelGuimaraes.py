#autor: Samuel Guimaraes
#Data: 01/11/2024
# Código: Baskara a, b, c

# importando biblioteca matemática
import math
#

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
if delta == 0:
    raiz1 = (-b+math.sqrt(delta))/(2*a)
    print(" Essa equação tem a as mesmas raízes: ", raiz1)
else:
    if delta < 0:
        print("A equação não tem raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b-math.sqrt(delta))/(2*a)
        print("A primeira raiz da equação é: ", raiz1)
        print("A segunda raiz da equação é: ", raiz2)