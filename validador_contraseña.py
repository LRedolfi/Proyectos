"""15.- Validador de contraseñas
Desarrolla un script el cual nos permita validar contraseñas para los usuarios de CódigoFacilito. El script debe cumplir con los siguientes requerimientos.
Las validaciones se deben hacerse sobre la función _is_valid*password*.
La función debe poseer como parámetro la variable password.
La función debe recibir como argumento (al momento de su llamado) una string en texto plano.
La función debe retornar un True en caso el parámetro cumpla con las validaciones de una contraseña segura.
La función debe retornar un False en caso el parámetro no cumpla con las validaciones de contraseña segura.
Una contraseña será segura siempre y cuando cumpla con los siguientes puntos.
Poseer una longitud mínima de 6 caracteres.
Contar con por lo menos una letra en Mayúsculas.
Contar con por lo menos una vocal en Mayúsculas.
Contar con por lo menos tres dígitos.
Los dígitos no deben ser consecutivos. Por ejemplo 123 o 456 no son combinaciones válidas. Por el contrario 168 y 414 si lo so
Poseer por lo menos con un carácter espacial (?*%&@)
Las contraseñas no pueden comenzar con la palabra Password.
Ejemplo.
>>> is_valid_password('password')
False
>>> is_valid_password('Password152?')
True
>>> is_valid_password('pywombat')
False
>>> is_valid_password('ExamplePyWombat123?')
False
>>> is_valid_password('ExamplePyWombat135?')
True"""

def es_consecutivo(lista): #Defino la función para saber si los números son consecutivos
    n = len(lista) #Obtengo el largo de la lista
    if n > 0: #Si hay números en la lista
        suma = n * min(lista) + n * (n - 1) / 2 #Realizo la suma aritmética de los números
    else: 
        suma=0 #Sino la suma es 0
    return sum(lista) == suma #Si el resultado de la suma aritmética el igual a la suma de todos los números, son consecutivos y retornara verdadero

def validar_contraseña(): #Defino la función para validar contraseñas
    válida=False #Variable auxiliar para saber si la contraseña es valida
    while válida ==False: #Ciclo mientras la contraseña sea falsa
        lista=[] #Lista vacía para los números de la clave
        cuenta_números=0 #Variable para contar los números
        especiales=False        #\
        largo=False             # |
        mayúscula=False         # |
        no_consecutivos=False   # |>Validaciones para cada característica de la contraseña
        no_password=False       # |
        números=False           #/
        contraseña=input("Ingrese la contraseña: ") #La contraseña se ingresa por teclado
        if len(contraseña)<6: #Si la contraseña es muy corta
            print("La contraseña debe tener mínimo 6 caracteres") #Lo aviso
        else:
            largo=True #Si no, valido el largo
        if "password" in contraseña[:8].lower(): #Si la contraseña empieza con password
            print("La contraseña no puede comenzar con la palabra password") #Lo aviso
        else:
            no_password=True #Si no, valido el inicio
        for letra in contraseña: #Para cada carácter de la contraseña
            if letra.isupper()==True: #Si la contraseña contiene una mayúscula
                mayúscula=True #Valido la mayúscula
        if mayúscula==False:
            print("La contraseña debe contener una mayúscula") #Si no, aviso
        for letra in contraseña: #Para cada carácter de la contraseña
            if letra in "0123456789": #Si es un número
                lista.append(int(letra)) #Lo agrego a la lista
                cuenta_números+=1 #Incremento la cuenta
        if cuenta_números<3: #Si la contraseña tiene menos de 3 números
            print("La contraseña debe tener mínimo 3 números") #Lo aviso
        else:
            números=True #Si no, valido la cantidad de números
        if cuenta_números>=3: #Si la contraseña tiene 3 números o mas 
            if es_consecutivo(lista)==True: #Y los números son consecutivos
                print("La contraseña no puede tener números consecutivos") #Lo aviso
            else:
                no_consecutivos=True #Si no, valido los números no consecutivos
        if contraseña.isalnum()==True: #Si la contraseña solo tiene letras y números
            print("La contraseña debe tener al menos un carácter especial (?*%&@)") #Lo aviso
        else:
            especiales=True #Si no, valido los caracteres especiales
        válida=especiales and largo and mayúscula and no_consecutivos and no_password and números #La contraseña solo sera válida si se cumplen todas las condiciones
        if válida==False: #Si no es válida
            print("Intente nuevamente") #Pido que ingrese una nueva
        else:
            print("La contraseña es correcta!") #Si no informo que es correcta
    return contraseña #Retorno la contraseña

clave=validar_contraseña() #Llamado a la función