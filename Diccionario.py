#Genera en un diccionario como agenda y solicitar el nombre de la persona, si la persona existe en el diccionario mostrar el número telefónico, de lo contrario informar que no cuenta con número telefónico

agenda = {
            "Fernando": "12345",
            "Omar": "54321",
            "Eric": "12121",
            "Juan" : "22222",
            "Angie" : "98765",
            "Vane" : "77777",
            "Marilyn": "14077"
}       #Creamos nuestra agenda de nombres con numeros de telefono 

nombre = input ("Ingresa el nombre de quien buscas:")
if nombre in agenda:    #Si el nombre esta en la agenda
    print("El numero de telefono de", nombre, "es:",agenda[nombre])
else:
    print("No tenemos el numero de esa persona")
