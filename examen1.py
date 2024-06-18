#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero1=(int(input("Ingresa el primer numero: ")))
numero2= (int(input("Ingresa el segundo numero: ")))

if numero2==0:
     print("Error")

else:
    division=numero1/numero2
    print(division)


#Escribir un programa que pida al usuario un número positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.

# num=(int(input("Ingrese numero positivo: ")))

# for i in range(1, num):
#  if i%2!=0:
#     print(i)

