"""17.- Lista ordenada?
Define una función llamada ordenamiento.
La función debe recibir como argumento un listado de números enteros con longitud N.
La función debe retornar True, o False, si el listado se encuentra ordenado de forma ascendente.
Ejemplo.
>>> ordenamiento([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
True
>>> ordenamiento([1, 2, 3, 4, 5, 6, 2, 1 ])
False
>>> ordenamiento([9, 20, 32, 45, 60, 89, 90])
True"""
def ingresar(): #Defino la función para ingresar valores a la lista
    lista=[]

    condición=True #Variable auxiliar de condición
    while condición: #Mientras la condición sea verdadera
        try: 
            ingreso=int(input("Ingrese un número entero para agregar a la lista, o una letra para finalizar: ")) #Evalúo que el ingreso sea un número entero
            lista.append(int(ingreso)) #Lo agrego a la lista
        except ValueError: #Si no se ingreso un número
            print("Procesando lista:") #Aviso que se esta procesando la lista
            condición=False #Cambio la condición para terminar el while
    return lista#Retorno a donde se llamo la función

def ordenamiento(lista): #Defino la función
    ordenada=True #Variable auxiliar
    largo=len(lista) #Largo de la lista
    for posición in range(1,largo): #Recorro la lista
        if lista[posición]<=lista[posición-1]: #Si el elemento actual es menor que el anterior
            ordenada=False #La lista no esta ordenada
    return ordenada #Retorno el valor del orden


lista=ingresar() #Ingreso la lista
orden=ordenamiento(lista) #Chequeo si esta ordenada
if orden==True:                  #\   
    print("Lista ordenada")      # |>Informo el estado de la lista
else:                            # |
    print("Lista desordenada")   #/