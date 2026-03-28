departamentos_municipios = {
    '16': {
        'nombre': 'Santa Bárbara',
        'municipios': 
        {
            '01': 'Santa Bárbara',
            '02': 'Arada',
            '03': 'Atima',
            '04': 'Azacualpa',
            '05': 'Ceguaca',
            '06': 'Colinas',
            '07': 'Concepcion del norte',
            '08': 'Concepción del Sur',
            '09': 'Chinda',
            '10': 'El Nispero',
            '11': 'Gualala',
            '12': 'Ilama',
            '13': 'Macuelizo',
            '14': 'Naranjito',
            '15': 'Nueva Celilac',
            '16': 'Petoa',
            '17': 'Protección',
            '18': 'Quimistan',
            '19': 'San Francisco de Ojuera',
            '20': 'San Luis',
            '21': 'San Marcos',
            '22': 'San Nicolas',
            '23': 'San Pedro Zacapa',
            '24': 'Santa Rita',
            '25': 'San Vicente Centenario',
            '26': 'Trinidad',
            '27': 'Las Vegas',
            '28': 'Nueva Frontera',
            
        } 
       },
}


while True:
    dni = input("Ingresa tu número de identidad: ")
    id_departamento=dni[0:2]
    id_municipio = dni[2:4]
    edad = 2024-int(dni[4:8])

    print(f"Departamento: {departamentos_municipios[id_departamento]['nombre']}")

    print(f"Municipio: {departamentos_municipios[id_departamento]['municipios'][id_municipio]}")

    print(f"Tienes {edad} años.")

    continuar = input("¿Deseas continuar? (s/n): ")
    if continuar.lower() != 's':
        break
