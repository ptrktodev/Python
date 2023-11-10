jogadores = []

numero_jogadores = int(input('Número de jogadores: '))


for c in range(numero_jogadores):
    qntd_gols = []
    jogador = {}
    jogador['nome'] = str(input('Nome: '))
    jogador['camisa'] = int(input('Numero da camisa: '))
    jogador['posicao'] = str(input('Posição em campo: '))
    n_partidas = int(input('Número de partidas: '))
    jogador['partidas'] = n_partidas
    for x in range(1, n_partidas + 1):
        qntd_gols.append(int(input(f'Gols na {x} partida: ')))
        jogador['gols'] = qntd_gols
    jogador['totalGols'] = sum(jogador['gols'])
    jogadores.append(jogador)

for g in jogadores:
    print(g)
