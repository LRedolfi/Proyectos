"""13.- Eliminar elementos duplicados de una lista.
Dada una lista de números enteros.
Ejemplo:
[1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
Desarrolla una función que elimine todos los elementos duplicados dentro de la colección.
La función debe cumplir con los siguientes requerimientos.
La función debe tener por nombre simple_list.
La función debe recibir como argumento una lista de números enteros.
La función debe retornar una lista con elementos únicos dentro de ella.
Si dentro de la lista existen 2 o más elementos duplicados, la lista debe retornar únicamente un elemento único.
Ejemplo.
lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
>>> simple_list(lista_a)
[1, 2, 3, 10, 20, 4, 5]
lista_b = [110, 20, 45, 50]
>>> simple_list(lista_b)
[110, 20, 45, 50]
lista_c = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
>>> simple_list(lista_c)
[1, 2, 3, 4]"""
def ingresar(): #Defino la función para ingresar valores a la lista
    condición=True #Variable auxiliar de condición
    while condición: #Mientras la condición sea verdadera
        try: 
            ingreso=int(input("Ingrese un número entero para agregar a la lista, o una letra para finalizar: ")) #Evalúo que el ingreso sea un número entero
            lista.append(int(ingreso)) #Lo agrego a la lista
        except ValueError: #Si no se ingreso un número
            print("Procesando lista:") #Aviso que se esta procesando la lista
            condición=False #Cambio la condición para terminar el while
    return #Retorno a donde se llamo la función

def lista_simple(lista): #Defino la función
    lista_nueva=[] #Defino una lista vacía
    for elemento in lista: #Recorro los elementos de la lista de entrada
        if elemento not in lista_nueva: #Si no esta en la lista nueva
            lista_nueva.append(elemento) #Lo agrego
    return lista_nueva #Retorno la lista nueva

lista=[]
ingreso=""

ingresar()
print(lista_simple(lista))