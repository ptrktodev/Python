import random


aleat = []


def gerar(qntd):
    for c in range(qntd):
        aleat.append(random.randint(0, 100))
    print(f"NUmeros aleatorios gerados: {aleat}")


gerar(20)

sorteados = []


def sortear(numeros):
    sorteios = 5
    for c in range(sorteios):
        sorteados.append(random.choice(numeros))
    print(f"5 números sorteados: {sorteados}")


sortear(aleat)

pares = []


def encontrar_pares(lista):
    for x in lista:
        y = 0
        if x % 2 == 0:
            y += x
            pares.append(y)
    print(f"pares encontrados: {pares}.")
    soma = 0
    for n in pares:
        soma += n
    print(f"Soma dos pares: {soma}")


encontrar_pares(sorteados)
