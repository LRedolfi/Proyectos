def validar(mensaje):
    while True:
        try:
            data=float(input("Coloca "+mensaje+": "))
            return data
        except ValueError:
            print("El dato debe ser un numero")

def validarTexto(mensaje):
    while True:
        try:
            dato=str(input("Coloca "+mensaje+": "))
            return dato
        except ValueError:
            print("El dato debe ser un texto")

producto=validarTexto("Qué comprarás ")
precio=validar("el precio de lo que compraras ")
ahorroActual=0

while precio>ahorroActual:
    mesada=validar("tu mesada")
    ahorroActual=ahorroActual+mesada
    restante=precio-ahorroActual
    tiempoTotal=precio/mesada
    tiempoActual=ahorroActual/mesada
    tiempoRestante=tiempoTotal-tiempoActual
    print("Actualmente tienes ahorrado: $",ahorroActual)
    print("El dinero que te falta es: $",restante)
    print("Los meses que te faltan son ",tiempoRestante)

print("Felicidades! Llegaste al objetivo", producto)
