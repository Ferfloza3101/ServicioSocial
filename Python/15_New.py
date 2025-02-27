import os

# Crear un diccionario vacío para la agenda
agenda = {}

# Crear un diccionario vacío para los números de teléfono
telefonos = {}

class Persona:
    def __init__(self, nombre='', apellido_paterno='', apellido_materno='', genero='', edad=0):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.edad = edad

    # Setters y Getters
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_apellido_paterno(self, apellido_paterno):
        if isinstance(apellido_paterno, str):
            self.apellido_paterno = apellido_paterno

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        if isinstance(apellido_materno, str):
            self.apellido_materno = apellido_materno

    def get_apellido_materno(self):
        return self.apellido_materno

    def set_genero(self, genero):
        if isinstance(genero, str) and genero.lower() in ['masculino', 'femenino']:
            self.genero = genero
        else:
            raise ValueError("El género debe ser 'masculino' o 'femenino'.")

    def get_genero(self):
        return self.genero

    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self.edad = edad

    def get_edad(self):
        return self.edad

    # Métodos para mostrar y actualizar información
    def mostrar_informacion(self):
        return (f"Nombre: {self.nombre}\n"
                f"Apellido Paterno: {self.apellido_paterno}\n"
                f"Apellido Materno: {self.apellido_materno}\n"
                f"Género: {self.genero}\n"
                f"Edad: {self.edad}")

    def actualizar_nombre(self, nombre):
        self.set_nombre(nombre)
        return True

    def actualizar_apellido_paterno(self, apellido_paterno):
        self.set_apellido_paterno(apellido_paterno)
        return True

    def actualizar_apellido_materno(self, apellido_materno):
        self.set_apellido_materno(apellido_materno)
        return True

    def actualizar_edad(self, edad):
        self.set_edad(edad)
        return True

    def actualizar_genero(self, genero):
        self.set_genero(genero)
        return True

def convertir_claves_minusculas(agenda):
    return {k.lower(): v for k, v in agenda.items()}

def insertar_contacto(nombre, persona, telefono):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda.")
    else:
        agenda[nombre] = persona
        telefonos[nombre] = telefono
        print(f"{nombre} ha sido agregado a la agenda.")

def modificar_contacto(nombre, persona, telefono):
    nombre = nombre.lower()
    if nombre in agenda:
        agenda[nombre] = persona
        telefonos[nombre] = telefono
        print(f"La información de {nombre} ha sido actualizada.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

def eliminar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        del agenda[nombre]
        del telefonos[nombre]
        print(f"{nombre} ha sido eliminado de la agenda.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

def guardar_agenda(archivo):
    with open(archivo, 'w') as f:
        for nombre, persona in agenda.items():
            telefono = telefonos.get(nombre, "")
            f.write(f"{nombre},{persona.apellido_paterno},{persona.apellido_materno},{persona.genero},{persona.edad},{telefono}\n")
    print(f"Agenda guardada en {archivo}.")

def cargar_agenda(archivo):
    global agenda, telefonos
    agenda = {}
    telefonos = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) == 6:
                    nombre, apellido_paterno, apellido_materno, genero, edad, telefono = datos
                    persona = Persona(nombre, apellido_paterno, apellido_materno, genero, int(edad))
                    agenda[nombre.lower()] = persona
                    telefonos[nombre.lower()] = telefono
        agenda = convertir_claves_minusculas(agenda)
        print(f"Agenda cargada desde {archivo}.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se creará uno nuevo al guardar la agenda.")

def buscar_contacto(nombre):
    nombre = nombre.lower()
    if nombre in agenda:
        print(f"Información de {nombre}:\n{agenda[nombre].mostrar_informacion()}\nTeléfono: {telefonos[nombre]}")
    else:
        print(f"{nombre} no se encuentra en la agenda.")
        opcion = input("¿Desea insertar un nuevo registro? (s/n): ").strip().lower()
        if opcion == 's':
            persona, telefono = crear_persona(nombre)
            agenda[nombre] = persona
            telefonos[nombre] = telefono
            print(f"Se ha creado un nuevo registro para {nombre}.")

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Buscar un registro")
    print("2. Agregar o Modificar un registro")
    print("3. Eliminar un registro")
    print("4. Mostrar Información")
    print("5. Visualizar Agenda")
    print("6. Salir")

def agregar_modificar_registro():
    nombre = input("Ingrese el nombre: ").strip().lower()
    if nombre in agenda:
        print(f"{nombre} ya existe en la agenda con los siguientes datos:\n{agenda[nombre].mostrar_informacion()}\nTeléfono: {telefonos[nombre]}")
        opcion = input("¿Desea modificar la información? (s/n): ").strip().lower()
        if opcion == 's':
            print("Seleccione el dato a modificar:")
            print("1. Nombre")
            print("2. Apellido Paterno")
            print("3. Apellido Materno")
            print("4. Género")
            print("5. Edad")
            print("6. Teléfono")
            dato = input("Ingrese el número del dato a modificar: ").strip()
            if dato == '1':
                nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
                persona = agenda.pop(nombre)
                persona.actualizar_nombre(nuevo_nombre)
                agenda[nuevo_nombre.lower()] = persona
                telefonos[nuevo_nombre.lower()] = telefonos.pop(nombre)
            elif dato == '2':
                apellido_paterno = input("Ingrese el nuevo apellido paterno: ").strip()
                agenda[nombre].actualizar_apellido_paterno(apellido_paterno)
            elif dato == '3':
                apellido_materno = input("Ingrese el nuevo apellido materno: ").strip()
                agenda[nombre].actualizar_apellido_materno(apellido_materno)
            elif dato == '4':
                genero = input("Ingrese el nuevo género: ").strip().lower()
                try:
                    agenda[nombre].actualizar_genero(genero)
                except ValueError as e:
                    print(e)
                    return
            elif dato == '5':
                edad = int(input("Ingrese la nueva edad: ").strip())
                agenda[nombre].actualizar_edad(edad)
            elif dato == '6':
                telefono = input("Ingrese el nuevo teléfono: ").strip()
                telefonos[nombre] = telefono
            print(f"El registro de {nombre} ha sido actualizado.")
        else:
            print("No se ha realizado ninguna modificación.")
    else:
        persona, telefono = crear_persona(nombre)
        agenda[nombre.lower()] = persona
        telefonos[nombre.lower()] = telefono
        print(f"Se ha creado un nuevo registro para {nombre}.")

def crear_persona(nombre):
    apellido_paterno = input("Ingrese el apellido paterno: ").strip()
    apellido_materno = input("Ingrese el apellido materno: ").strip()
    genero = input("Ingrese el género: ").strip().lower()
    while genero not in ['masculino', 'femenino']:
        print("El género debe ser 'masculino' o 'femenino'.")
        genero = input("Ingrese el género: ").strip().lower()
    edad = int(input("Ingrese la edad: ").strip())
    telefono = input("Ingrese el número de teléfono: ").strip()
    return Persona(nombre, apellido_paterno, apellido_materno, genero, edad), telefono

def visualizar_agenda():
    print("\nAgenda:")
    for nombre, persona in agenda.items():
        print(f"Nombre: {nombre}\nInformación:\n{persona.mostrar_informacion()}\nTeléfono: {telefonos.get(nombre, 'No disponible')}")
    print("")

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
            nombre = input("Ingrese el nombre a mostrar información: ").strip().lower()
            if nombre in agenda:
                print(f"Información de {nombre}:\n{agenda[nombre].mostrar_informacion()}\nTeléfono: {telefonos[nombre]}")
            else:
                print(f"{nombre} no se encuentra en la agenda.")
        elif opcion == '5':
            visualizar_agenda()
        elif opcion == '6':
            guardar_agenda(archivo)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
