matriz1 = ((1, 2, 3), (4, 5, 6))
matriz2 = ((7, 8), (9, 10), (11, 12))
def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    cols_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    cols_matriz2 = len(matriz2[0])
    if cols_matriz1!= filas_matriz2:
        raise ValueError("Las matrices no son multiplicables")
    matriz_resultado = [[0 for _ in range(cols_matriz2)] for _ in range(filas_matriz1)]
    for i in range(filas_matriz1):
        for j in range(cols_matriz2):
            for k in range(cols_matriz1):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_resultado
matriz_producto = multiplicar_matrices(matriz1, matriz2)
print("Matriz producto:")
for fila in matriz_producto:
    print(fila)