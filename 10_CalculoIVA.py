#Calcular el IVA de una cantidad ingresada por teclado (utilizar función para realizar el cálculo)
def calcularIVA(cantidad, tasa_iva ):
    iva = cantidad * tasa_iva /100
    return iva  #Operaciones y definiciones para el calculo de nuestro IVA
while True:
    try:
            cantidad = float(input("Ingresa una cantidad :"))   #Pedimos al usuario que ingrese dato, pero lo hacemos float para manejar operaciones y no textos
            break
    except ValueError:
        print("Esa no es una cantidad valida. Por favor intenta con un numero")

tasa_iva = 13   #En este caso ponemos la tasa fija nosotros de iva a calcular

monto_iva = calcularIVA(cantidad,tasa_iva) #Aplicamos la funcion 

precio_final = cantidad + monto_iva # sumamos nuestra cantidad e iva

print("Tu IVA sera de:", monto_iva)
print("Tu precio final total es de:",precio_final)

