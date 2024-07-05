entrada_usuario = input("Ingrese los pares de palabras y traducciones (separados por comas y dos puntos): ")
traducciones = {}
for par in entrada_usuario.split(","):
    palabra, traduccion = par.split(":")
    traducciones[palabra.strip()] = traduccion.strip()
frase_espanol = input("Ingrese una frase en español: ")
frase_ingles = []
for palabra in frase_espanol.split():
    if palabra in traducciones:
        frase_ingles.append(traducciones[palabra])
    else:
        frase_ingles.append(palabra)
print("Frase traducida:", " ".join(frase_ingles))