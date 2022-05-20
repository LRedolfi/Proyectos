"""1.-Reemplaza vocales por @.
Dado un string de longitud N. Donde N es mayor a 0.
Ejemplo.
'Hola mundo'
Desarrolla un programa en Python que permite reemplazar todas las vocales del string por arrobas (@).
'H@l@ m@nd@'"""
mensaje="Hola mundo" #Mensaje a evaluar
vocales=['a','e','i','o','u'] #Listado de vocales
nuevo_mensaje='' #String vacío sobre el que se va armando el mensaje final

for carácter in mensaje: #Iteración sobre cada carácter del mensaje
    if carácter.lower() in vocales: #Se evalúa si el carácter en minúscula esta en el listado de vocales
        carácter='@' #Si esta, se reemplaza ese carácter por @
    nuevo_mensaje=nuevo_mensaje+carácter #Se concatena para el armado del nuevo mensaje

print(nuevo_mensaje) #Impresión en consola del mensaje final