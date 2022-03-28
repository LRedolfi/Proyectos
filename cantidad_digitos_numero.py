"""6.- Cantidad de dígitos número entero.
Definir una función la cual nos permita conocer cuántos dígitos posee un número.
La función debe tener por nombre cantidad_dígitos.
La función debe poseer el parámetro numero.
La función debe retornar la cantidad de dígitos del parámetro.
No es posible utilizar la función str.
Ejemplos
>>> cantidad_dígitos(10)
2
>>> cantidad_dígitos(2019)
4
>>> cantidad_dígitos(1234567890)
10"""
def cantidad_dígitos(numero): #Definición de la función
    contador=0 #Definición del contador
    while numero>0: #Mientras el numero sea mayor a 0
        contador+=1 #Incremento el contador
        numero=numero//10 #Divido por 10 buscando el entero mas próximo hacia abajo
    return contador #Retorno el contador

print(cantidad_dígitos(1023456789))