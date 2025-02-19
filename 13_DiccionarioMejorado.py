# Crear un diccionario como agenda con algunos nombres y números telefónicos
agenda = {
    "Fernando": "12345",
    "Omar": "54321",
    "Eric": "12121",
    "Juan": "22222",
    "Angie": "98765",
    "Vane": "77777",
    "Marilyn": "14077"
}

# Convertir claves del diccionario a minúsculas
agenda = {k.lower(): v for k, v in agenda.items()}

# Función para insertar un nuevo contacto en la agenda
def insertar_contacto(nombre, telefono):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda con el número {agenda[nombre]}.")
    else:
        agenda[nombre] = telefono
        print(f"{nombre} ha sido agregado a la agenda con el número {telefono}.")

# Función para modificar el número de teléfono de un contacto existente
def modificar_contacto(nombre, telefono):
    nombre = nombre.lower()
    if nombre in agenda:
        agenda[nombre] = telefono
        print(f"El número de teléfono de {nombre} ha sido actualizado a {telefono}.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

# Solicitar el nombre de la persona y mostrar el número telefónico si existe en la agenda
nombre = input("Ingresa el nombre de quien buscas: ").lower()
if nombre in agenda:
    print("El número de teléfono de", nombre, "es:", agenda[nombre])
else:
    print("No tenemos el número de esa persona.")

# Insertar un nuevo contacto
nombre_nuevo = input("Ingresa el nombre del nuevo contacto: ").lower()
telefono_nuevo = input("Ingresa el número de teléfono del nuevo contacto: ")
insertar_contacto(nombre_nuevo, telefono_nuevo)

# Modificar el número de teléfono de un contacto existente
nombre_modificar = input("Ingresa el nombre del contacto a modificar: ").lower()
telefono_modificar = input("Ingresa el nuevo número de teléfono: ")
modificar_contacto(nombre_modificar, telefono_modificar)

# Mostrar la agenda actualizada
print("Agenda actualizada:", agenda)
