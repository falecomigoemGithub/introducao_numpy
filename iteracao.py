import numpy as np
import itertools

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(type(matriz))
for mt in matriz:
    # print(mt)
    pass

for linha in matriz:
    for valor in linha:
        pass
for l in itertools.product(matriz):
    pass
for valor in np.nditer(matriz):
    pass

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        # print(f"Elementos na posição -> ({i}, {j}): {matriz[i, j]}")
        pass

for linha in matriz:
    print("Retorno do shape ", linha.shape)
    print("Retorno do ndim ", linha.ndim)