mi_tupla=(1, "dos",{3,33,"cuatro"}, (5,0,6))

print(mi_tupla)
print(mi_tupla[0])
print(mi_tupla[3][1])
print(mi_tupla[1][2])

lista_1 = list(mi_tupla)
print(lista_1)


#Unpaking de tuplas
a, b, c, d= mi_tupla
print(a)
print(b)
print(c)
print(d)

#tupla de PI, e, gravedad
tuplaconst=(3.1416, 2.71, 9.8)
pi, ex, gr= tuplaconst
print("pi:" ,pi, "ex:", ex,"gravedad:", gr)