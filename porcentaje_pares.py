"""8.- Porcentaje números pares
Dado un listado de números enteros con Longitud N. Donde N es mayor a 0.
Ejemplo.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Define una función que permita conocer si más del 50% de los números son pares.
La función debe cumplir con los siguientes puntos.
Debe tener por nombre pares.
La función debe recibir, de forma obligatoria, un listado de números enteros.
La función retorna verdadero, o falso, dependiendo si más de la mitad de los números pares.
Ejemplo.
>>> pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
True
>>> pares([2, 2, 2, 2, 3, 4, 2])
True
>>> pares([2, 1, 1, 1, 1, 3, 10])
False"""
def pares(números): #Defino la función
    contador=0 #Defino un contador
    largo=len(números) #Obtengo el largo del listado
    
    for numero in números: #Itero sobre cada numero
        if numero%2==0: #Evalúo si es par
            contador+=1 #Si es par incremento el contador
    #Luego de completar la evaluación sobre todos los números
    if contador>=largo/2: #Si hubo mas pares que la mitad de los componentes
        return True #Retorno verdadero
    else:
        return False #Si no retorno falso

print(pares([2, 1, 1, 1, 1, 3, 10]))