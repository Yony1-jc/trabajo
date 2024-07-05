divisas = {'Soles':'S', 'Dolar':'$', 'Quetzal':'Q', 'Yen':'¥'}
divisa_usuario = input("Ingrese una divisa: ")
if divisa_usuario in divisas:
    print("El símbolo de la divisa", divisa_usuario, "es", divisas[divisa_usuario])
else:
    print("La divisa", divisa_usuario, "no está en el diccionario")