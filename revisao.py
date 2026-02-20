import numpy as np

nomes = np.array(["Alice", "Bob", "Charlie", "Diana", "Emma"])

grupos = np.array_split(nomes, 3)

for i, sub_grupo in enumerate(grupos):
    print(f"Grupo {i + 1}: {sub_grupo}")
