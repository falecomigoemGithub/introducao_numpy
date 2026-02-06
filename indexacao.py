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


minha_matriz = np.arange(1, 10).reshape(3, 3)
# print(minha_matriz)

fatia = minha_matriz > 5

# print(minha_matriz[fatia])

indices_linhas = np.array([1, 2, 2, 2])
indices_colunas = np.array([2, 0, 1, 2])

elementos_alvo_indexacao = minha_matriz[indices_linhas, indices_colunas]
print(f"Resultado com indexação avançada: {elementos_alvo_indexacao}")