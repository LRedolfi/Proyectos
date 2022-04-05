"""14.- Diferencias entre 2 listas.
Define la función _array*diff*, que recibe como argumento dos listas de números enteros (lista *a* y *b*).
La función debe retornar un nuevo listado con todos aquellos elementos de la lista a que no se encuentren en la lista b y viceversa.
Ejemplos:
>>> array_diff([1], [1, 2, 3, 2])
[2, 3]
>>> array_diff([1, 2, 3, 2], [1])
[2, 3]
>>> array_diff([1, 4, 3, 5], [1, 2, 3, 2])
[4, 5, 2]"""
def ingresar(nro_lista): #Defino la función para ingresar valores a las listas, que recibe el número de lista
    lista=[]

    while True: #Mientras la condición sea verdadera
        try: 
            ingreso=int(input("Ingrese un número entero para agregar a la lista "+str(nro_lista)+", o una letra para finalizar: ")) #Evalúo que el ingreso sea un número entero
            lista.append(int(ingreso)) #Lo agrego a la lista
        except ValueError: #Si no se ingreso un número
            print("Procesando lista:") #Aviso que se esta procesando la lista
            break #Termino el while
    return lista#Retorno a donde se llamo la función

def lista_diferente(lista_1,lista_2): #Defino la función
    lista_nueva=[] #Defino una lista vacía
    for elemento in lista_1: #Recorro los elementos de la lista 1 de entrada
        if elemento not in lista_2 and elemento not in lista_nueva: #Si no esta en la lista 2 o en la nueva
            lista_nueva.append(elemento) #Lo agrego
    for elemento in lista_2: #Recorro los elementos de la lista 2 de entrada
        if elemento not in lista_1 and elemento not in lista_nueva: #Si no esta en la lista 1 o en la nueva
            lista_nueva.append(elemento) #Lo agrego
    return lista_nueva #Retorno la lista nueva


lista_1=ingresar(1) #Llamo a ingresar para formar la lista 1
lista_2=ingresar(2) #Llamo a ingresar para formar la lista 2
print(lista_diferente(lista_1,lista_2)) #Llamo a la función