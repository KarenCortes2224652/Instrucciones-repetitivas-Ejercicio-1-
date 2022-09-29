# Ejercico 1: Instrucciones repetitivas.

#Input
from re import I


N = int(input("Ingrese el valor de N:"))

#Processing
i = 0
sum = 0
while i<=N:
    sum = sum + i
    i = i + 1

#Output
print("La suma es:" + str (sum))



