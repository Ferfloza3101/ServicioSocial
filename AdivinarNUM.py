#Juego de adivinar el número, generaremos un número entre 1 y 100.

import random   #Importamos la libreria de random para la generacion de numeros aleatorios

def juego_adivinar_numero():                    #Dejaremos definidas las variables que utilizaremos
    numero_secreto = random.randint(1, 100)     #Utilizamos randit para la generacion del numero
    intentos = 0
    adivinado = False

    print("Listo para jugar adivina el numero")
    print("Estoy pensando en un número entre 1 y 100.")

    while not adivinado:                                #Definimos el bucle que solo se acabara hasta coincidir con el numero
        intento = int(input("Introduce tu intento: "))
        intentos += 1                                      #Aumentamos 1 cada intento fallido

        if intento < numero_secreto:                    #Ponemos condiciones para las pistas, si es mayor o si es menor al numero generado
            print("El número es mayor que", intento)    
        elif intento > numero_secreto:
            print("El número es menor que", intento)
        else:
            adivinado = True                            #Cambiamos a Verdadero en el momento que el numero coincida 
            print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
            
juego_adivinar_numero()
