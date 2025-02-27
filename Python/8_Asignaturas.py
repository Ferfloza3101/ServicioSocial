#Escribir un programa que almacene 10 asignaturas de un curso en una lista y que muestre las asignaturas de la lista de la posición 3 a la 6 y posteriormente mostrar la lista original.

asignaturas = []    #Creamos una lista vacia donde almacenaremos
for i in range(10):
    asignatura = input(f"Ingresa la asignatura {i +1}:")
    asignaturas.append(asignatura)
#Con este bucle pedimos que ingrese una por una y solo maximo 10 y con appened las sumamos a nuestra lista vacia

asignaturas_3a6 = asignaturas[2:6]
print ("Estas son las asignaturas de la 3 a la 6",asignaturas_3a6)

#Con esto hacemos que solo muestre desde los lugares que queremos

print ("Lista completa de asignaturas:" , asignaturas)
