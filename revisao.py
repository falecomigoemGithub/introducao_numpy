import numpy as np

nomes = np.array(["Alice", "Bob", "Charlie", "Diana", "Emma"])

grupos = np.split(nomes, 3)
print(grupos)