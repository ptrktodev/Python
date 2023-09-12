import random

# Criação de uma tupla com 5 números inteiros aleatórios entre 1 e 100
tupla_aleatoria = tuple(random.randint(20, 100) for value in range(5))

print(tupla_aleatoria)
print(f"Maior valor: {max(tupla_aleatoria)}")
print(f"Menor valor: {min(tupla_aleatoria)}")
