n = int(input("Ingrese un número entero: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()