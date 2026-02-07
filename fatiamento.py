import numpy as np

matriz = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

fatiamento = matriz[0 : , -1 : -3 : -1]
matriz[1 : 3, 1 : 3] = [[99, 100], [101, 102]]
print(matriz)