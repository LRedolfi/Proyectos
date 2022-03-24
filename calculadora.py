#La función validar cheque que el valor ingresado sea un número
def validar(mensaje):
    #Ejecutamos hasta que ingrese un número
    while True:
        try:
            #En esta linea se pide que ingrese un valor flotante
            dato=float(input("Ingrese "+mensaje))
            #Si el valor es un número, continua el programa
            return dato
        except ValueError:
            #Se imprime el mensaje si no es un número
            print("El dato debe ser un número")

#pedimos los datos de entrada
largo=validar("el largo del cuarto: ")
ancho=validar("el ancho del cuarto: ")
m2XCaja=validar("los metros cuadrados por caja: ")
precioXM2=validar("el precio por metros cuadrado: $")
#Calculos internos
#Precio por caja
precioXCaja=m2XCaja*precioXM2
#Metros cuadrados del cuarto
m2Cuarto=ancho*largo
#Cantidad de cajas
cajas=m2Cuarto/m2XCaja
#Precio total de los materiales
precioTotal=precioXCaja*cajas
#Impresión de resultados
print("Total de cajas que se necesitan: ",cajas)
print("Precio Total: $",precioTotal)