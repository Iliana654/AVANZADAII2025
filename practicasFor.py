#Suma de números pares

# Inicializa la variable suma
suma = 0

# Utiliza un bucle for para iterar sobre los números del 1 al 100
for numero in range(1, 101):
    # Verifica si el número es par
    if numero % 2 == 0:
        # Si es par, añádelo a la suma
        suma += numero

# Imprime el resultado final
print("La suma de los números pares del 1 al 100 es:", suma)

# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingresa un número entero positivo: "))

# Verificar que n sea positivo
if n <= 0:
    print("El número debe ser positivo.")
else:
    # Inicializar un contador
    contador = 1
    
    # Utilizar un bucle while para imprimir los números desde 1 hasta n
    while contador <= n:
        print(contador)
        contador += 1

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar una variable para almacenar el intento del usuario
intento = 0

# Utilizar un bucle while para solicitar al usuario que adivine el número
while True:
    # Solicitar al usuario que ingrese un número
    intento = int(input("Adivina el número (entre 1 y 100): "))
    
    # Verificar si el intento es correcto
    if intento == numero_secreto:
        print("¡Felicitaciones! ¡Has adivinado el número.")
        break  # Salir del bucle while
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    else:
        print("El número secreto es menor. Intenta nuevamente.")

agenda = {}

while True:
    print("\nBienvenido a la agenda de contactos")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")

    elif opcion == '2':
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
        else:
            print(f"El contacto '{nombre}' no está en la agenda.")

    elif opcion == '3':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"El contacto '{nombre}' no está en la agenda.")

    elif opcion == '4':
        if agenda:
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("La agenda está vacía.")

    elif opcion == '5':
        print("Gracias por usar la agenda. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-5).")
