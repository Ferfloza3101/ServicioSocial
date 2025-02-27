# Servicio Social

Estos son algunos de los ejercicios practicados durante mi Servicio Social especificamente de PYTHON.

## Ejercicios de Python

1. **Mostrar el precio del IVA (21%) de un producto con un valor de 100 y su precio final.**
   - [Enlace al ejercicio 1](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/1_IVA.py)

2. **Crea una variable numérica y si la variable está entre 0 y 10, mostrar un mensaje indicándolo.**
   - [Enlace al ejercicio 2](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python2/_Variable.py)

3. **Añadir al anterior ejercicio que, si está entre 11 y 20, muestre otro mensaje diferente y si está entre 21 y 30 otro mensaje.**
   - [Enlace al ejercicio 3](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/3_Variables2.py)

4. **Mostrar con un while los números del 1 al 100.**
   - [Enlace al ejercicio 4](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/4_While.py)

5. **Mostrar con un for los números del 1 al 100.**
   - [Enlace al ejercicio 5](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/5_For.py)

6. **Mostrar cada carácter de la cadena “Hola mundo”.**
   - [Enlace al ejercicio 6](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/6_HolaMundo.py)

7. **Ingresar por teclado 10 valores separados por comas y guardar cada elemento en una lista (mostrar la lista al finalizar).**
   - [Enlace al ejercicio 7](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/7_Lista.py)

8. **Escribir un programa que almacene 10 asignaturas de un curso en una lista y que muestre las asignaturas de la lista de la posición 3 a la 6 y posteriormente mostrar la lista original.**
   - [Enlace al ejercicio 8](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/8_Asignaturas.py)

9. **Generar un diccionario como agenda y solicitar el nombre de la persona. Si la persona existe en el diccionario, mostrar el número telefónico, de lo contrario, informar que no cuenta con número telefónico.**
   - [Enlace al ejercicio 9](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/9_Diccionario.py)

10. **Calcular el IVA de una cantidad ingresada por teclado (utilizar función para realizar el cálculo).**
    - [Enlace al ejercicio 10](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/10_CalculoIVA.py)

11. **Con la función de IVA calcular los siguientes casos:**
    - **Si el monto se encuentra entre 1500 y 2500, el IVA será del 2%.**
    - **Si el monto es mayor a 2500, el IVA será del 5%.**
    - **Si es menor de 1500, el IVA será del 1%.**
    - [Enlace al ejercicio 11](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/11_FuncionIva.py)

12. **Juego de adivinar el número:**
    - **Generaremos un número entre 1 y 100. Nuestro objetivo es adivinar el número.**
    - **Si fallamos, nos dirán si es mayor o menor que el número buscado.**
    - **También se debe poner el número de intentos requeridos.**
    - [Enlace al ejercicio 12](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/12_AdivinarNUM.py)

13. **Agregar un menú para que el usuario determine si desea agregar o modificar un registro.**
    - **En el caso de seleccionar la opción Insertar, validar lo siguiente:**
      - **Si el nombre existe en el diccionario, preguntar si desea modificar la información; en caso de responder de manera afirmativa, modificar el registro.**
      - **Al terminar el proceso, indicar el registro que fue actualizado o creado.**
    - **En el caso de seleccionar la opción Modificar, validar lo siguiente:**
      - **Si el nombre no existe en el diccionario, preguntar si desea insertar un nuevo registro; en caso de responder de manera afirmativa, insertar el registro.**
      - **Al terminar el proceso, indicar el registro que fue actualizado o creado.**
    - **Añadir al menú la opción de Visualizar Agenda.**
      - **Al seleccionar la opción, mostrar la información como se muestra a continuación:**
        ```
        Nombre: FRANCISCO       Teléfono:  55555555555
        ```
    - [Enlace al ejercicio 13](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/13_DiccionarioMejorado.py)

14. **Iniciar el programa cargando la información del archivo de texto.**
    - **Agregar un menú para que el usuario determine si desea buscar, agregar, eliminar o modificar un registro.**
      - **En el caso de seleccionar la opción Insertar, validar lo siguiente:**
        - **Si el nombre existe en el diccionario, preguntar si desea modificar la información; en caso de responder de manera afirmativa, modificar el registro.**
        - **Al terminar el proceso, indicar el registro que fue actualizado o creado.**
      - **En el caso de seleccionar la opción Modificar, validar lo siguiente:**
        - **Si el nombre no existe en el diccionario, preguntar si desea insertar un nuevo registro; en caso de responder de manera afirmativa, insertar el registro.**
        - **Al terminar el proceso, indicar el registro que fue actualizado o creado.**
      - **En el caso de seleccionar la opción Buscar, validar lo siguiente:**
        - **Si el nombre no existe en el diccionario, preguntar si desea insertar un nuevo registro; en caso de responder de manera afirmativa, insertar el registro.**
        - **Al terminar el proceso, indicar el registro que fue insertado o el resultado del elemento que encontramos en la agenda.**
    - **La información del contacto debe mostrarse igual que en el ejercicio 13.**
    - **Al cerrar el programa, proceder a guardar en el archivo de texto.**
    - [Enlace al ejercicio 14](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/14_txt.py)
   
15. **Tomando como base el ejercicio 14 vamos a solicitar más información de contacto, para ello vamos a crear una clase llamada Persona.**

    Sus atributos son: nombre, apellido paterno, apellido materno, genero, y edad.

    Generar:
    - **Un constructor, donde los datos pueden estar vacíos.**
    - **Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.**
    - **Método `mostrar_informacion()`: Muestra los datos de la persona.**
    - **Método `actualizar_nombre()`: Se actualiza la información y se devuelve un valor lógico indicando si fue actualizado**
    - **Método `actualizar_apellido_paterno()`: Se actualiza la información y se devuelve un valor lógico indicando si fue actualizado.**
    - **Método `actualizar_apellido_materno()`: Se actualiza la información y se devuelve un valor lógico indicando si fue actualizado.**
    - **Método `actualizar_edad()`: Se actualiza la información y se devuelve un valor lógico indicando si fue actualizado.**
    - **Método `actualizar_genero()`: Se actualiza la información y se devuelve un valor lógico indicando si fue actualizado.**
    - **Utilizaremos la clase para recabar esa información y mantendremos la funcionalidad del ejercicio 14.**
    - [Enlace al ejercicio 15](https://github.com/Ferfloza3101/ServicioSocial/blob/main/Python/15_New.py)


 
