import numpy as np

temperaturas = np.random.randint(19, 29, size=30)

print(temperaturas)

semanas = np.split(temperaturas, 5)
print(semanas)