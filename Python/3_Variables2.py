#Añadir al anterior ejercicio que, si está entre 11 y 20, muestre otro mensaje diferente y si está entre 21 y 30 otro mensaje

varnum = 30.9 #Aqui introducimos la variable numerica

if 0 <= varnum <= 10:
    print ("El numero esta entre 0 y 10")   #Condicionamos que si el numero estra entre 0 y 10 imprim el mensaje correcto

elif 10 <= varnum <= 20:
    print ("Tu numero esta entre 10 y 20")  #Aqui cambiamos el else por elseif para poner diversas condiciones y repetimos entre los numeros que nos piden
elif 20 <= varnum <= 30:
    print ("Tu numero esta entre 20 y 30")
else:
    print ("Tu numero no esta entre 0 y 30") #Si no esta en ninguna de las condiciones mostramos que no esta entre 0 y 30s
