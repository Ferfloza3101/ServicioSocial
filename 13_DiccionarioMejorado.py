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

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Agregar o Modificar un registro")
    print("2. Visualizar Agenda")
    print("3. Salir")

def agregar_modificar_registro(agenda):
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
        opcion = input(f"{nombre} no existe en la agenda. ¿Desea crear un nuevo registro? (s/n): ").strip().lower()
        if opcion == 's':
            telefono = input("Ingrese el teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"Se ha creado un nuevo registro para {nombre}.")

def visualizar_agenda(agenda):
    print("\nAgenda:")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre:<15} Teléfono: {telefono}")
    print("")

def main():                  #Lo utilizaremos como nuestr bucle principal donde llamaremos a todas las funciones que desarrollamos
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()
        if opcion == '1':
            agregar_modificar_registro(agenda)
        elif opcion == '2':
            visualizar_agenda(agenda)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()                          #Ejecutamos el main 
