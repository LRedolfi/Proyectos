"""3.-Cantidad de números en un string.
Dado un String de longitud N. Donde N es mayor a 0.
Ejemplo.
Hola mundo desde Python en su versión 3.10
Desarrolla un programa en Python que permita conocer la cantidad de números que posee el string. El programa deberá imprimir en consola, la cantidad de números
que posee el string.
Ejemplo.
El String posee 3 números enteros.
En caso el string posea un solo número entero el mensaje será el siguiente:
'El string solo posee un número entero.'
En caso el string no posea algún número entero el mensaje será el siguiente:
'Lo sentimos, el string no posee un número entero.'"""

mensaje="Hola mundo desde Python en su versión 3.10"

contador=0

for carácter in mensaje:
    if carácter in "0123456789":
        contador+=1

if contador==1:
    print("El string solo posee un número entero.")
elif contador>1:
    print("El String posee "+str(contador)+" números enteros.")
else:
    print("Lo sentimos, el string no posee un número entero.")