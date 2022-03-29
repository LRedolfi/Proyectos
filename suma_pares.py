"""9.- Suma de números pares
Desarrolla una función en Python que permita sumar números pares-
La función debe tener por nombre _suma*pares*.
La función debe recibir como argumento un litado de números enteros.
La función debe retornar la suma de todos los números pares positivos del listado.
Ejemplo.
>>> suma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
42
>>> suma_pares([2, 2, 2, 2, 3, 4, 2])
14
>>> suma_pares([2, 1, 1, 1, 1, 3, 10])
12"""
def suma_pares(números): #Defino la función
    suma=0 #Defino variable para la suma
    
    for numero in números: #Itero sobre cada numero
        if numero%2==0: #Evalúo si es par
            suma=suma+numero #Si es par lo agrego a la suma
    return suma #Retorno la suma


print(suma_pares([2, 1, 1, 1, 1, 3, 10]))