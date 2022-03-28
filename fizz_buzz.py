"""7.- Fizz Buzz
Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “fizz”, los múltiplos de 5 por “buzz” y los
múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”."""
for numero in range(100): #Defino la iteración sobre el rango de 100
    if numero%15==0: #Si es múltiplo de 15
        print("fizzbuzz")
    elif numero%5==0: #Si es múltiplo de 5
        print("buzz")
    elif numero%3==0: #Si es múltiplo de 3
        print("fizz")
    else:
        print(numero)