"""11.- Adivina el número
Define una función llamada _adivina*numero*. La función debe cumplir con los siguiente requerimientos.
La función no poseerá parámetro alguno.
La función elegirá un número aleatorio entre el 1 y el 100.
La función preguntará al usuario que número se ha elegido.
Cada vez que el usuario ingrese un número la función imprimirá alguno de los siguientes mensajes (Dependiendo cual sea el caso). Esto para darle una pista
al usuario en su siguiente turno.
Más alto.
Más bajo.
Correcto.
Si el usuario responde incorrectamente en 5 ocasiones seguidas la función finalizará con el mensaje: Lo sentimos, el número que estaba pensando es
<Número>.
Si el usuario responde correctamente la función finalizará en ese momento.
Ejemplo 1.
En que número estoy pensando: 10
Más alto.
En que número estoy pensando: 55
Más bajo.
En que número estoy pensando: 30
Más alto.
Lo sentimos, el número que estaba pensando es 41.
Ejemplo 2.
En que número estoy pensando: 40
Más alto.
En que número estoy pensando: 60
Más alto.
En que número estoy pensando: 61
Correcto"""
from random import randint #Importo la función que devuelve un entero aleatorio

def adivina_numero(): #Defino la función
    numero_secreto=randint(0,100) #Creo el número aleatorio entre 0 y 100
    ganador=False #Defino el booleano para saber si el usuario gano o no

    for intento in range(0,5): #Le doy 5 intentos al usuario
        numero_arriesgado=int(input("Cual es el número secreto? ")) #El número ingresado por el usuario lo convierto y guardo
        if numero_arriesgado==numero_secreto: #Si acertó el número
            ganador=True #Cambio el estado de ganador
            print("Felicidades! Acertó el número") #Imprimo el mensaje de felicitación
            break #Termino el ciclo for
        elif numero_arriesgado>numero_secreto: #Si el número ingresado es mayor
            print("El número es mas bajo") #Le aviso
        else: # Si no, evidentemente es menor
            print("El número es mas alto") #Le aviso

    if ganador==False: #Si el ciclo termino sin que gane
        print("Lo sentimos, se quedo sin intentos. El número secreto es: "+str(numero_secreto)) #Se lo comunico y le digo cual era el número

    print("Gracias por jugar") #Mensaje de agradecimiento

adivina_numero() #Llamado a la función