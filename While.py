i=0

while i<10:
    print(i)
    i += 1

print("Ciclo controlado por banderin")
while True:
    entrada = input("INGRESA s PARA SALIR")
    if entrada.upper == 'S':
        break
    print("Escribiste", entrada)

print("Ciclo controlado por banderin 2")
bandera= "x"
while bandera != 'S':
    bandera = input("Ingresa S para salir")


print("Ciclo controlado por banderin 3")

bandera=True 
while bandera!= False:
    bandera= input("Ingresa False para salir: ")
    print(bandera.upper())
    salir=bandera.upper()
    if salir == "S":
        bandera= False
    print("Saliste del ciclo")
