nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H/M): ")
nombre_mayus = nombre.upper()
if sexo.upper() == "M" and nombre_mayus < "M":
    grupo = "A"
elif sexo.upper() == "H" and nombre_mayus > "N":
    grupo = "A"
else:
    grupo = "B"
print(f"Tu grupo es: {grupo}")