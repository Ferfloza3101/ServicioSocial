#Ingresar por teclado 10 valores separados por comas y guardar cada elemento en una lista (mostrar la lista al finalizar)

valores_entrada = input("Introduce tus 10 valores siempre separados por comas") #Pedimos los valores en terminal

lista = valores_entrada.split (",")     #Con esto asignamos la "," como nuestro separador

#Mostramos los valores de la lista
print ("Tu lista es:",lista)
