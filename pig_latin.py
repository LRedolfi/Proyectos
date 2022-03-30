"""10.- Pig Latin*
Pig Latin es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.
Sus reglas son simples.
Si la palabra comienza con una vocal (a, e, i, o, u) se deberá agregar way al final de la palabra. Ejemplos: "air" se convierte en "airway". "eat" se convierte en
"eatway"
Si la palabra comienza con otro carácter, se toma la primera letra y se añade al final, agregando "ay". Ejemplos: "Python" se convierte en "ythonpay". "Demo"
se convierte en "emoday"
Con todo esto en mente, desarrolla una función la cual nos permita hacer la traducción entre el Ingles y el Pig Latin.
La función debe cumplir con los siguiente requerimientos.
La función debe tener por nombre _*pig\latin*.
La función debe recibir como valor de entrada el string que se desea convertir (Se asume que se encuentra en inglés).
La función debe retornar la traducción de cada palabra al Pig Latin.
Ejemplo.
>>> pig_latin('Python')
ythonpay
>>> pig_latin('School')
choolSay"""
def pig_latín(frase): #Defino la función
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
            primer_carácter=palabra[0].lower() #Defino el primer carácter
            if primer_carácter in "aeiou": #Si es una vocal
                nueva_palabra=palabra+"way" #Agrego way al final
            else:
                nueva_palabra=palabra[1:]+primer_carácter+"ay" #Si no tomo la palabra sin el primer carácter, lo sumo al final y agrego ay
            frase_convertida=frase_convertida+nueva_palabra+" " #Concateno los resultados
        elif posición==largo_frase-1: #Si llego a la ultima posición de la frase
            palabra=frase[pos_ult_espacio+aux_paso_primer_espacio:] #Tomo la palabra como substring desde la posición del ultimo espacio encontrado hasta la posición final
            nueva_palabra_final="" #Defino un string vacío
            primer_carácter=palabra[0].lower() #Defino el primer carácter
            if primer_carácter in "aeiou": #Si es una vocal
                nueva_palabra_final=palabra+"way" #Agrego way al final
            else:
                nueva_palabra_final=palabra[1:]+primer_carácter+"ay" #Si no tomo la palabra sin el primer carácter, lo sumo al final y agrego ay
            frase_convertida=frase_convertida+nueva_palabra_final #Concateno los resultados
    return frase_convertida #Retorno la nueva palabra


entrada=input("Ingrese la/s palabra/s: ")
print(pig_latín(entrada))