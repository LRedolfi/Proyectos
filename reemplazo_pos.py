"""2.-Reemplazar vocales por posiciones
Dado un string de longitud N. Donde N es mayor a 0.
Ejemplo.
'Hola mundo'
Desarrolla un programa en Python que permite reemplazar todas las vocales del String por sus correspondiente posición en la lista.
Donde las posiciones serán las siguientes.
a = 1
e = 2
i = 3
o = 4
u = 5
Salida.
'H4l1 m5nd4'"""
mensaje="Hola mundo" #Mensaje a evaluar
vocales=['a','e','i','o','u'] #Listado de vocales
nuevo_mensaje='' #String vacío sobre el que se va armando el mensaje final

for carácter in mensaje: #Iteración sobre cada carácter del mensaje
    if carácter.lower() in vocales: #Se evalúa si el carácter en minúscula esta en el listado de vocales
        if carácter=='a':
            carácter='1' #Si esta, se reemplaza ese carácter por su posición
        elif carácter=='e':
            carácter='2' #Si esta, se reemplaza ese carácter por su posición
        elif carácter=='i':
            carácter='3' #Si esta, se reemplaza ese carácter por su posición
        elif carácter=='o':
            carácter='4' #Si esta, se reemplaza ese carácter por su posición
        elif carácter=='u':
            carácter='5' #Si esta, se reemplaza ese carácter por su posición
    nuevo_mensaje=nuevo_mensaje+carácter #Se concatena para el armado del nuevo mensaje

print(nuevo_mensaje) #Impresion en consola del mensaje final