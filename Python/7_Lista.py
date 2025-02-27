#Ingresar por teclado 10 valores separados por comas y guardar cada elemento en una lista (mostrar la lista al finalizar)


while True:
    valores_entrada = input("Introduce tus 10 valores siempre separados por comas") #Pedimos los valores en terminal
    lista = valores_entrada.split (",")     #Con esto asignamos la "," como nuestro separador

    if len(lista)==10:
        break
    else:
        print("Por favor asegurate de ingresar EXACTAMENTE 10 valores separados por comas")


print("Tu lista es:",lista)
