#Escribir un programa que pida al usuario un número positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.

num=(int(input("Ingrese numero positivo: ")))

for i in range(1, num):
 if i%2!=0:
    print(i)