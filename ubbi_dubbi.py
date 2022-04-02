"""12.- Ubbi Dubbi
Ubbi Dubbi es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.
Su regla es simple.
Se deben anteponer ub a todas las vocales en una palabra. Ejemplo: mi milk se convierte en mubilk, python se convierte en pythubon y example se convierte
en ubexubamplube (En palabras largas puede ser difícil de pronunciar).
Con esto en mente, desarrolla una función que nos permita realizar la traducción del ingles al Ubbi Dubbi. La función debe cumplir con los siguiente requerimientos.
La función debe tener por nombre _*ubbi\dubbi*.
La función debe recibir como valor de entrada el string que se desea convertir (Se asume que se encuentra en ingles).
La función debe retornar la traducción de cada palabra al Ubbi Dubbi.
Ejemplos.
>>> ubbi_dubbi('program')
prubogrubam
>>> ubbi_dubbi('demo')
dubemubo
>>> ubbi_dubbi('car')
cubar"""

def ubbi_dubbi(frase): #Defino la función
    frase_convertida="" #Defino una cadena vacía para armar la frase final
    largo_frase=len(frase) #Obtengo el largo de la frase
    pos_ult_espacio=0 #Posición del ultimo espacio encontrado
    aux_paso_primer_espacio=0 #Variable auxiliar de paso por primer espacio
    for posición in range(0,largo_frase): #Recorro la frase posición por posición
        if frase[posición]==" ": #Al encontrar un espacio
            palabra=frase[pos_ult_espacio+aux_paso_primer_espacio:posición] #Tomo la palabra como substring desde la posición del ultimo espacio encontrado hasta la posición actual
            aux_paso_primer_espacio=1 #Como pase por el primer espacio, cambio el valor de la auxiliar
            pos_ult_espacio=posición #Actualizo la posición del ultimo espacio encontrado
            nueva_palabra="" #Defino un string vacío
            for carácter in palabra: #Recorro cada carácter de la palabra
                if carácter in "aeiou": #Si es una vocal
                    carácter="ub"+carácter #Lo modifico agregando ub antes
                nueva_palabra=nueva_palabra+carácter #Concateno para ir armando la nueva palabra
            frase_convertida=frase_convertida+nueva_palabra+" " #Concateno los resultados
        elif posición==largo_frase-1: #Si llego a la ultima posición de la frase
            palabra=frase[pos_ult_espacio+aux_paso_primer_espacio:] #Tomo la palabra como substring desde la posición del ultimo espacio encontrado hasta la posición final
            nueva_palabra_final="" #Defino un string vacío
            for carácter in palabra: #Recorro cada carácter de la palabra
                if carácter in "aeiou": #Si es una vocal
                    carácter="ub"+carácter #Lo modifico agregando ub antes
                nueva_palabra_final=nueva_palabra_final+carácter #Concateno para ir armando la nueva palabra
            frase_convertida=frase_convertida+nueva_palabra_final #Concateno los resultados
    return frase_convertida #Retorno la nueva frase


entrada=input("Ingrese la/s palabra/s: ")
print(ubbi_dubbi(entrada))