"""4.- Contenido de un string
Dado el siguiente string.
Title: 'Nuevo ejercicio'
Desarrolla un programa en Python que permita generar un nuevo string con todos los caracteres después de los dos puntos (:). El programa deberá imprimir en
consola el nuevo string.
Ejemplo.
$ python main.py
'Nuevo ejercicio'"""
mensaje="Title: 'Nuevo ejercicio'" #Mensaje a evaluar
carácter_paso=False #Booleano para avisar que se paso por el carácter ":"
nuevo_mensaje="" #String vacío sobre el que se va armando el mensaje final

for carácter in mensaje: #Iteración sobre cada carácter del mensaje
    if carácter==":": #Cuando llego al carácter ":" cambio el valor del booleano a True
        carácter_paso=True
    if carácter_paso==True and carácter!=":": #Una vez que pase por el carácter ":" concateno para el armado del nuevo mensaje
        nuevo_mensaje=nuevo_mensaje+carácter

print(nuevo_mensaje) #Impresion en consola del mensaje final