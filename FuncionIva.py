#Con la función de IVA calcular los siguiente:

#Con la función de IVA calcular los siguiente:
def calcular_iva(cantidad):
    if cantidad > 2500:
        iva = cantidad * 0.05
    elif 1500 <= cantidad <= 2500:
        iva = cantidad * 0.02
    else:
        iva = cantidad * 0.01
    return iva

# Pedimos que se ingrese la cantidad por el teclado usando float para dato numerico
cantidad = float(input("Introduce la cantidad: "))

# Calculamos el IVA
iva = calcular_iva(cantidad)

#Pintamos el rsultado
print("El IVA de la cantidad ingresada es:", iva)
