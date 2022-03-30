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
    frase_convertida=""
    largo_frase=len(frase)
    pos_ult_espacio=0
    primer_espacio=0
    for posición in range(0,largo_frase):
        if frase[posición]==" ":
            palabra=frase[pos_ult_espacio+primer_espacio:posición]
            primer_espacio=1
            pos_ult_espacio=posición
            nueva_palabra="" #Defino un string vacío
            primer_carácter=palabra[0].lower() #Defino el primer carácter
            if primer_carácter in "aeiou": #Si es una vocal
                nueva_palabra=palabra+"way" #Agrego way al final
            else:
                nueva_palabra=palabra[1:]+primer_carácter+"ay" #Si no tomo la palabra sin el primer carácter, lo sumo al final y agrego ay
            frase_convertida=frase_convertida+nueva_palabra+" "
        elif posición==largo_frase-1:
            palabra=frase[pos_ult_espacio+1:]
            nueva_palabra_final="" #Defino un string vacío
            primer_carácter=palabra[0].lower() #Defino el primer carácter
            if primer_carácter in "aeiou": #Si es una vocal
                nueva_palabra_final=palabra+"way" #Agrego way al final
            else:
                nueva_palabra_final=palabra[1:]+primer_carácter+"ay" #Si no tomo la palabra sin el primer carácter, lo sumo al final y agrego ay
            frase_convertida=frase_convertida+nueva_palabra_final
    return frase_convertida #Retorno la nueva palabra

print(pig_latín("eat fone car air"))