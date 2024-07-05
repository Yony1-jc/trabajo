edad = int(input("Ingrese su edad: "))
ingresos_mensuales = int(input("Ingrese sus ingresos mensuales en soles: "))

if edad >= 18 and ingresos_mensuales >= 2000:
    print("Usted tiene que pagar impuestos.")
else:
    print("Usted no tiene que pagar impuestos.")