import numpy as np

temperaturas = np.random.randint(19, 29, size=30)

print(temperaturas)

semanas = np.array_split(temperaturas, 4)
print(semanas)