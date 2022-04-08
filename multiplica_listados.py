"""16.- Multiplicación de dos listados
Dado 2 listas de números enteros.
Ejemplo.
lista_uno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_dos = [2, 5, 7, 8, 1, 3, 5, 6, 8, 10]
Desarrolla una función que permita multiplicar cada uno de los elementos de ambos listados.
La función tendrá por nombre multiplicación.
La función debe recibir, de forma obligatoria, 2 lista de números enteros.
La función debe validar que ambas listas poseen exactamente la misma cantidad de elementos.
Si las listas no cumplen con el punto anterior la función retornará un listado vacío.
La función retornara una nueva lista con el resultado de multiplicar cada uno de los elementos de ambos listados. El primer elemento de la primera lista con el
primer elemento de la segunda lista, el segundo elemento de la primera lista con el segundo elemento de la segunda lista y así sucesivamente.
Ejemplo.
>>> multiplicación(lista_uno, lista_dos)
[2, 10, 21, 32, 5, 18, 35, 48, 72, 100]"""
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

def multiplicación(lista_1,lista_2): #Defino la función para multiplicar las dos listas
    largo_lista_1=len(lista_1) #Obtengo el largo de las listas
    largo_lista_2=len(lista_2)
    lista_multiplicada=[] #Lista para almacenar la multiplicación
    multiplicación=0
    if largo_lista_1 != largo_lista_2: #Si las listas no tienen el mismo largo
        print("Las listas deben tener el mismo largo") #Lo aviso
    else: 
        for posición in range(0,largo_lista_1): #Si no, las recorro
            multiplicación=lista_1[posición]*lista_2[posición] #Y multiplico sus elementos
            lista_multiplicada.append(multiplicación) #Agrego el resultado a la lista de multiplicaciones
    return lista_multiplicada #Regreso la lista multiplicada

lista_1=ingresar(1) #Llamo a ingresar para formar la lista 1
lista_2=ingresar(2) #Llamo a ingresar para formar la lista 2

print(multiplicación(lista_1,lista_2)) #Llamo a la función