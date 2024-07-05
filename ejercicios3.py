num1 = float(input("Ingrese el dividendo: "))
num2 = float(input("Ingrese el divisor: "))

if num2 == 0:
    print("Error: no se puede dividir entre cero")
else:
    resultado = num1 / num2
    print("La división es:", resultado)