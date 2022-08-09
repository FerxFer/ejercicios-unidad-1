"""
cree un programa que incorpore el modulo sys,
al cual desde la terminal se le puedan pasar tres parametros.
el programa debe tomar los parametros e indicar en la terminal
si son multiplos de dos.
"""
import sys
print("Ingrese tres parametros")
print(sys.argv)
#print(sys.argv[0])
print("El programa tomara los datos y si el numer es par retornara un cero. ")
print("Valor 1: ", int(sys.argv[1])%2)
print("Valor 2: ", int(sys.argv[2])%2)
print("Valor 3: ", int(sys.argv[3])%2)

