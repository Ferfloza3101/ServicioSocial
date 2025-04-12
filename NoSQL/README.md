# Aplicación con Vulnerabilidad NoSQL

## Instrucciones

Las instrucciones para la aplicación creada con una vulnerabilidad NoSQL son las siguientes:

1. Descargar todos los archivos tal cual estan por la jerarquia de orden que se otorgo.
2. Posteriormente hay que tener instalado node.js y los "node_modules" que importan las librerias para la conexion con mogodb, y express para el servidor estos se instalan desde el cmd de la computadora, aplicando los siguientes comandos: "npm init-y" "npm install mongodb" "npm install express" "npm install cors"

3. Continuaremos lanzando el servidor desde la terminal de visual studio con el archivo server.js, esto lo hacemos abriendo la terminal desde el apartado view y despues terminal, y lo lanzaremos desde la terminal con el comando "node server.js" y nos dira si fue lanzado correctamente y el puerto en el que se lanzo

4. Una vez lanzado el servidor, abriremos la pagina html donde tendremos el formulario el cual no funcionara ningun usuario que no se encuentre en la base de datos, y para probar la existencia de vulnerabilidad, utilizaremos la extension de Thunder Client en visual studio, que hara de funcion como una API

5. Ya instalada la extension, daremos click en ella, le daremos a "new request" y nos pedira que cambiemos el metodo, el cual lo elegiremos como "post" y despues pondremos la direccion a donde se mandan los datos, en este caso (http://localhost:3000/login)

6. Para continuar desde la seccion body de thunder client, y mandando un Json otorgaremos un repeat del siguiente comando: { "user": { "$ne": 1 }, "password": { "$ne": 1 } } lo que hara que iguale usuario y contraseña a 1, y dicho repeat terminara entregandonos en consola un usuario y una contraseña valida de la base de datos de mongodb de la coleccion o carpeta que hayamos puesto en nuestro codigo

7. Por ultimo solo quedaria probar que el usuario y la contraseña que nos otorgo si puede acceder en la pagina que creamos.