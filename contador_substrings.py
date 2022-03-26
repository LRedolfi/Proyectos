"""5.- Contador de substrings.
Desarrolla una función que permita conocer la cantidad de veces que existe un substring en un string.
La función debe cumplir con los siguientes requerimientos.
La función debe tener por nombre _contador*substrings*.
La función debe recibir como argumento el string a evaluar y el substring del cual se quiere conocer la cantidad de coincidencias.
La función debe retornar, mediante un número entero, la cantidad de veces que existe el substring en el string original.
Ejemplos.
>>> contador_substrings('Hola mundo', 'o')
2
>>> contador_substrings('Nuevo ejercicio en PyWombat', 'ue')
1
>>> contador_substrings('Contador de caracteres', 'de')
1
>>> contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py')
3"""

def contador_substrings(string,substring): #Definición de la función.
    contador=0 #Contador de coincidencias
    long_string=len(string) #Longitud del string
    long_substring=len(substring) #Longitud del substring
    for posición in range(0,long_string): #Iteración sobre las posiciones del string en todo su rango
        if string[posición:posición+long_substring]==substring: #Comparo en la posición actual mas el largo del substring
            contador+=1 #Incremento el contador
    return contador #Retorno el contador

print(contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py')) #Imprimo el valor de contador que me regresa la función
