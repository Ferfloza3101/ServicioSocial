import random # Importamos la librería de random para la generación de números aleatorios
def juego_adivinar_numero(): # Dejaremos definidas las variables que utilizaremos
    numero_secreto = random.randint(1, 100) # Utilizamos randint para la generación del número
    intentos = 0
    adivinado = False
    print("Listo para jugar adivina el número")
    print("Estoy pensando en un número entre 1 y 100.")
    while not adivinado: # Definimos el bucle que solo se acabará hasta coincidir con el número
        while True:
            try:
                intento = int(input("Introduce tu intento: "))
                if 1 <= intento <= 100 :
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 100.")
            except ValueError:
                print("Eso no es un número válido. Por favor, ingrese un número del 1 al 100.")
        intentos += 1 # Aumentamos 1 cada intento fallido
        if intento < numero_secreto: # Ponemos condiciones para las pistas, si es mayor o si es menor al número generado
            print("El número es mayor que", intento)
        elif intento > numero_secreto:
            print("El número es menor que", intento)
        else:
            adivinado = True # Cambiamos a Verdadero en el momento que el número coincida
            print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
juego_adivinar_numero()