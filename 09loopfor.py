#ciclo for

#for i in range(10):
    #print(i)

#for a in range(2, 22, 2): #(inicio, fin, incremento)
    #print(a)

#Ciclo for con listas

#lista=["uno","dos","tres", "cuatro"]
#for item in lista:
    #print(item)

    #invertir el orden de una lista
    #for item in reversed(lista):
        #print(item)
#for para imprimir una tupla


#mi_tupla=("uno","dos","tres","cuatro")
# for item in mi_tupla:
#     print(item)


#for con diccionarios:

# diccionario ={
#     "CURSOS": "Vive la vida loca",
#     "CLASES":"Ciclos de la vida",
#     "PROFESORA": "ILIANA"
# }

# print(diccionario)
# for llave in reversed(diccionario):
#     print(llave, ":", diccionario[llave])


# tabla=int(input("Ingrese un número: "))

# for i in range(1, 11):
#     print(f"{tabla} * {i}= {tabla*i}")


#Factorial ejercicio:

factorial=int(input("Ingresa el valor:"))
resultado=1
for i in range(1, factorial+1):
    resultado *= i
print(f"{factorial}: es {resultado}")

