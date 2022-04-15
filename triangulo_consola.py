"""20.- Triangulo en consola
Escribe un programa en Python que imprima en consola un triangulo de asterisco (*) de N filas.
El programa debe pedir al usuario la cantidad de filas que desea imprimir.
Ingresa la cantidad de filas: 10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
Ingresa la cantidad de filas: 3
  *
 ***
*****"""
def triangulo(filas): #Defino la función
    for fila in range(0,filas): #Recorro la cantidad de filas
        impresion_espacio=filas-fila #Variable para saber cuantos espacios debo imprimir
        while impresion_espacio>1: #Ciclo para la impresion de espacios
            print(" ",end="")
            impresion_espacio-=1
        impresion_asterisco=fila+1 #Variable para saber cuantos asteriscos antes del centro debo imprimir
        while impresion_asterisco>0: #Ciclo para la impresion de los asteriscos
            print("*",end="")
            impresion_asterisco-=1
        impresion_asteriscos=fila #Variable para saber cuantos asteriscos despues del centro debo imprimir
        while impresion_asteriscos>0: #Ciclo para la impresion de los asteriscos
            print("*",end="")
            impresion_asteriscos-=1
        print("") #Impresion de una nueva linea

filas=int(input("Ingrese la cantidad de filas: "))
triangulo(filas)