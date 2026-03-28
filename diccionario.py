# Crear Diccionario:
usuarios = {
    "1": {"nombre": "Iliana Liceth Zuniga", "edad": 18},
    "2": {"nombre": "Jorge Arturo Vallecillo Espinoza", "edad": 18},
    "3": {"nombre": "Lucas Rodrigo Bautista Juarez", "edad": 18},
    "4": {"nombre": "Jose David Mejia Mendoza", "edad": 31},
    "5": {"nombre": "Kennet Andersson Martinez Varela", "edad": 21},
    "6": {"nombre": "Tomy Jose Montufar Zuniga", "edad": 19},
    "7": {"nombre": "Angel Antonio Perez Rodriguez", "edad": 18},
    "8": {"nombre": "Jose Eduardo Sabillon Hurtado", "edad": 19},
    "9": {"nombre": "Diany Lizbeth Enamorado Fernandez", "edad": 19},
    "10": {"nombre": "Anderson Jair Garcia Menjivar", "edad": 19},
    "11": {"nombre": "Derick Dair Muñoz Iraheta", "edad": 20},
    "12": {"nombre": "Norman Bú", "edad": 25},
    "13": {"nombre": "Arnold Stanly Ford", "edad": 18},
    "14": {"nombre": "Walter Eduardo Rápalo Smith", "edad": 20},
    "15": {"nombre": "Edson Jhair Ríos Coto", "edad": 26}
}

# Mostrar el diccionario
print("Diccionario de compañeros:")
for id, info in usuarios.items():
    print(f"ID: {id}, Nombre: {info['nombre']}, Edad: {info['edad']}")


# Buscar usuario:
id_a_buscar = "12"
if id_a_buscar in usuarios:
    print(f"\nInformación del compañero con ID {id_a_buscar}:")
    print(f"Nombre: {usuarios[id_a_buscar]['nombre']}, Edad: {usuarios[id_a_buscar]['edad']}")
else:
    print(f"No se encontró un compañero con el ID {id_a_buscar}")

# Para eliminar un usuario, hacemos uso del del
id_a_eliminar = "15"
if id_a_eliminar in usuarios:
    del usuarios[id_a_eliminar]
    print(f"Se ha eliminado el usuario con ID {id_a_eliminar}.")
else:
    print(f"No se ha encontrado un usuario con el ID {id_a_eliminar}")