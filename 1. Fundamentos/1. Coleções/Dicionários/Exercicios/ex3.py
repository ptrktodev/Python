import random

resultados = []

numero_jogadores = int(input('Digite o número de jogadores: '))

for x in range(numero_jogadores):
    print('Diga seu nome e jogue o dado..: ')
    jogador = {}
    jogador['nome'] = str(input('Nome: '))
    jogador['numero'] = random.randint(1, 6)
    print('Dado na mesa. A máquina armazenou seu número.')
    resultados.append(jogador)

maior_numero = []
for dict in resultados:
    print(f"{dict['nome']}, seu número do dado é: {dict['numero']}.")
    maior_numero.append(dict['numero'])

print(
    f'O maior número é {max(maior_numero):.2f}. Se caso houve empate, iniciem novamnete somente ambos.')
