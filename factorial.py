"""19.- Factorial
Definir una función la cual nos permita conocer el factorial de un número.
La función debe tener por nombre factorial.
La función debe poseer el parámetro valor.
La función debe retornar el factorial del parámetro.
La función no debe hacer uso de ningún tipo ciclo.
Ejemplos.
>>> factorial(3)
6
>>> factorial(5)
120
>>> factorial(15)
1307674368000"""
def factorial(valor): #Defino la función
    if valor==1: #El factorial de 1 es 1
        return valor
    else:
        return valor*factorial(valor-1) #Retorno el numero multiplicado por su anterior

número=int(input("Ingrese el número a factorizar: ")) #Ingreso el número a factorizar
factor=str(factorial(número)) #Llamo a la función
print("El factorial es: "+factor) #Imprimo el resultado