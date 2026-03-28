#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero1=(int(input("Ingresa el primer numero: ")))
numero2= (int(input("Ingresa el segundo numero: ")))

if numero2==0:
     print("Error")

else:
    division=numero1/numero2
    print(division)


