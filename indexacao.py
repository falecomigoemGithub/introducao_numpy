import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matriz[2, 2])
# print(matriz[0])
# print(matriz[:, 1])
# print(matriz[0])
# subarray = matriz[0:2, 1:3]
# print(subarray)

mascara = matriz > 5
# print(mascara)

print(matriz[mascara])

mask = matriz[3, ]
print(mask)
linhas = np.array([1, 2, 2, 2])
colunas = np.array([2, 0, 1, 2])

valores_vermelhos = mat[linhas, colunas]
print(valores_vermelhos)