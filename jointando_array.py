import numpy as np

array_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array_2 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])

produto = np.concatenate((array_1, array_2), axis=1)

arr_nomes = np.array(["Alice", "Bob", "Charlie"])
notas_fisica = np.array([8, 9, 7])
notas_quimica = np.array([5, 8, 6])

alunos = np.column_stack((arr_nomes, notas_fisica, notas_quimica))
print(alunos)
