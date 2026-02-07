import numpy as np

letras = np.array(["a", "b", "c", "d", "e", "f"])

a = letras[2 :: -1]
print(a)

b = letras[-2 : -4 : -1]
print(b)