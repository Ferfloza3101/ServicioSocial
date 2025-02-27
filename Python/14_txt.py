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

# Función para eliminar un contacto de la agenda
def eliminar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        del agenda[nombre]
        print(f"{nombre} ha sido eliminado de la agenda.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

# Función para guardar la agenda en un archivo de texto
def guardar_agenda(archivo):
    with open(archivo, 'w') as f:
        for nombre, telefono in agenda.items():
            f.write(f"{nombre}:{telefono}\n")
    print(f"Agenda guardada en {archivo}.")

# Función para cargar la agenda desde un archivo de texto
def cargar_agenda(archivo):
    global agenda
    agenda = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                nombre, telefono = linea.strip().split(':')
                agenda[nombre] = telefono
        print(f"Agenda cargada desde {archivo}.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se creará uno nuevo al guardar la agenda.")

# Función para buscar un contacto en la agenda
def buscar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print(f"{nombre} no se encuentra en la agenda.")
        opcion = input("¿Desea insertar un nuevo registro? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"Se ha creado un nuevo registro para {nombre}.")

# Función para mostrar el menú
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Buscar un registro")
    print("2. Agregar o Modificar un registro")
    print("3. Eliminar un registro")
    print("4. Visualizar Agenda")
    print("5. Salir")

# Función para agregar o modificar un registro
def agregar_modificar_registro():
    nombre = input("Ingrese el nombre: ").strip().lower()
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda con el número {agenda[nombre]}.")
        opcion = input("¿Desea modificar la información? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el nuevo teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"El registro de {nombre} ha sido actualizado.")
        else:
            print("No se ha realizado ninguna modificación.")
    else:
        telefono = input("Ingrese el teléfono: ").strip()
        agenda[nombre] = telefono
        print(f"Se ha creado un nuevo registro para {nombre}.")

import os

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

#Cambiamos o modificamos contactos que ya existen
def modificar_contacto(nombre, telefono):
    nombre = nombre.lower()
    if nombre in agenda:
        agenda[nombre] = telefono
        print(f"El número de teléfono de {nombre} ha sido actualizado a {telefono}.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

#Eliminamos contacto de la agenda
def eliminar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        del agenda[nombre]
        print(f"{nombre} ha sido eliminado de la agenda.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

# Función para guardar la agenda en un archivo de texto
def guardar_agenda(archivo):
    with open(archivo, 'w') as f:
        for nombre, telefono in agenda.items():
            f.write(f"{nombre}:{telefono}\n")
    print(f"Agenda guardada en {archivo}.")

# Función para cargar la agenda desde un archivo de texto
def cargar_agenda(archivo):
    if os.path.exists(archivo):
        global agenda
        agenda = {}
        with open(archivo, 'r') as f:
            for linea in f:
                nombre, telefono = linea.strip().split(':')
                agenda[nombre] = telefono
        print(f"Agenda cargada desde {archivo}.")
    else:
        print(f"El archivo {archivo} no existe. Se utilizará la agenda predeterminada.")

#Con esta funcion hacemos la busqueda de los contactos 
def buscar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print(f"{nombre} no se encuentra en la agenda.")
        opcion = input("¿Desea insertar un nuevo registro? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"Se ha creado un nuevo registro para {nombre}.")

#Desplegamos el menu al usuario
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Buscar un registro")
    print("2. Agregar o Modificar un registro")
    print("3. Eliminar un registro")
    print("4. Visualizar Agenda")
    print("5. Salir")

#Agregamos o modificamos los datos de nuestra agenda
def agregar_modificar_registro():
    nombre = input("Ingrese el nombre: ").strip().lower()
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda con el número {agenda[nombre]}.")
        opcion = input("¿Desea modificar la información? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el nuevo teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"El registro de {nombre} ha sido actualizado.")
        else:
            print("No se ha realizado ninguna modificación.")
    else:
        telefono = input("Ingrese el teléfono: ").strip()
        agenda[nombre] = telefono
        print(f"Se ha creado un nuevo registro para {nombre}.")

# Función para ver la agenda
def visualizar_agenda():
    print("\nAgenda:")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre:<15} Teléfono: {telefono}")
    print("")

# Función principal
def main():
    archivo = "agenda.txt"
    cargar_agenda(archivo)
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()
        if opcion == '1':
            nombre = input("Ingrese el nombre a buscar: ").strip().lower()
            buscar_contacto(nombre)
        elif opcion == '2':
            agregar_modificar_registro()
        elif opcion == '3':
            nombre = input("Ingrese el nombre a eliminar: ").strip().lower()
            eliminar_contacto(nombre)
        elif opcion == '4':
            visualizar_agenda()
        elif opcion == '5':
            guardar_agenda(archivo)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
