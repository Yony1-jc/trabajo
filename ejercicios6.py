edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    precio = 0
    print("El cliente puede entrar gratis!")
elif 4 <= edad <= 18:
    precio = 10
    print("El precio de la entrada es de 10 soles.")
else:
    precio = 20
    print("El precio de la entrada es de 20 soles.")
print("El precio total es de", precio, "soles.")