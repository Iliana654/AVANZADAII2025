#Agregar una opción en el menú para buscar un municipio por su nombre:
elif selec == '4':
    limpiar()
    nombre_municipio = input("Ingrese el nombre del municipio a buscar: ").title()
    encontrado = False
    for dept in departamentos_municipios.values():
        for municipio in dept['municipios'].values():
            if nombre_municipio in municipio:
                print(f"Municipio {nombre_municipio} encontrado en el departamento {dept['nombre']}")
                encontrado = True
                break
        if encontrado:
            break
    if not encontrado:
        print("Municipio no encontrado.")
    input("Presione Enter para continuar...")

#Agregar una opción en el menú para contar el número total de municipios en un departamento:
elif selec == '5':
    limpiar()
    id = input("Ingrese el número de departamento para contar sus municipios (ejemplo 16):


#Buscar subcadena en municipios
elif selec == '4':
    limpiar()
    subcadena = input("Ingrese la subcadena a buscar en los municipios: ").lower()
    encontrado = False
    for dept_id, dept in departamentos_municipios.items():
        for mun_id, municipio in dept['municipios'].items():
            if subcadena in municipio.lower():
                print(f"Municipio encontrado: {municipio} en el departamento {dept['nombre']}")
                encontrado = True
    if not encontrado:
        print("Subcadena no encontrada en ningún municipio.")
    input("Presione Enter para continuar...")


#Contar municipios por departamento
elif selec == '5':
    limpiar()
    print("Conteo de municipios por departamento:")
    for dept_id, dept in departamentos_municipios.items():
        num_municipios = len(dept['municipios'])
        print(f"Departamento: {dept['nombre']} tiene {num_municipios} municipios.")
    input("Presione Enter para continuar...")

#Ordenar municipios alfabéticamente:

elif selec == '6':
    limpiar()
    id = input("Ingrese el número de departamento para ordenar sus municipios (ejemplo 16): ")
    if not id.isdigit() or len(id) != 2:
        print("Código no válido, por favor intente de nuevo. (2 dígitos y solo enteros)")
        input("Presione Enter para continuar...")
    else:
        if id not in departamentos_municipios:
            print("Departamento no encontrado.")
            input("Presione Enter para continuar...")
        else:
            municipios = list(departamentos_municipios[id]['municipios'].values())
            municipios.sort()
            print(f"Municipios del departamento {departamentos_municipios[id]['nombre']} ordenados alfabéticamente:")
            for municipio in municipios:
                print(municipio)
            input("Presione Enter para continuar...")

# Mostrar información fija usando tuplas:

elif selec == '7':
    limpiar()
    datos_fijos = ("PI: 3.14159", "e: 2.71828", "Gravedad: 9.8 m/s^2")
    print("Información fija:")
    for dato in datos_fijos:
        print(dato)
    input("Presione Enter para continuar...")

#Modificación del menú principal para incluir nuevas opciones:
while True:
    limpiar()
    print("Bienvenido al programa")
    print("1. Inspeccionar departamentos y municipios.")
    print("2. Ingresar su cédula.")
    print("3. Salir.")
    print("4. Buscar subcadena en municipios.")
    print("5. Contar municipios por departamento.")
    print("6. Ordenar municipios alfabéticamente.")
    print("7. Mostrar información fija.")
    print("8. Guardar datos.")
    print("9. Cargar datos.")
    selec = input("Elija una opción: ")

    # Opciones ya existentes...

    if selec == '4':
        limpiar()
        subcadena = input("Ingrese la subcadena a buscar en los municipios: ").lower()
        encontrado = False
        for dept_id, dept in departamentos_municipios.items():
            for mun_id, municipio in dept['municipios'].items():
                if subcadena in municipio.lower():
                    print(f"Municipio encontrado: {municipio} en el departamento {dept['nombre']}")
                    encontrado = True
        if not encontrado:
            print("Subcadena no encontrada en ningún municipio.")
        input("Presione Enter para continuar...")

    elif selec == '5':
        limpiar()
        print("Conteo de municipios por departamento:")
        for dept_id, dept in departamentos_municipios.items():
            num_municipios = len(dept['municipios'])
            print(f"Departamento: {dept['nombre']} tiene {num_municipios} municipios.")
        input("Presione Enter para continuar...")

    elif selec == '6':
        limpiar()
        id = input("Ingrese el número de departamento para ordenar sus municipios (ejemplo 16): ")
        if not id.isdigit() or len(id) != 2:
            print("Código no válido, por favor intente de nuevo. (2 dígitos y solo enteros)")
            input("Presione Enter para continuar...")
        else:
            if id not in departamentos_municipios:
                print("Departamento no encontrado.")
                input("Presione Enter para continuar...")
            else:
                municipios = list(departamentos_municipios[id]['municipios'].values())
                municipios.sort()
                print(f"Municipios del departamento {departamentos_municipios[id]['nombre']} ordenados alfabéticamente:")
                for municipio in municipios:
                    print(municipio)
                input("Presione Enter para continuar...")

    elif selec == '7':
        limpiar()
        datos_fijos = ("PI: 3.14159", "e: 2.71828", "Gravedad: 9.8 m/s^2")
        print("Información fija:")
        for dato in datos_fijos:
            print(dato)
        input("Presione Enter para continuar...")

    elif selec == '8':
        guardar_datos()
        input("Presione Enter para continuar...")

    elif selec == '9':
        cargar_datos()
        input("Presione Enter para continuar...")

    # Opción para salir
    elif selec == '3':
        limpiar()
        print("Programa finalizado.")
        exit()
    else:
        print("Opción no válida, intente de nuevo.")
        input("Presione Enter para continuar...")
