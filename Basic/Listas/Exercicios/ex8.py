dados = []

for x in range(0, 2):
    pessoa = []
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Nota 1: ")))
    pessoa.append(float(input("Nota 2: ")))
    pessoa.append(float(input("Nota 3: ")))
    
    dados.append(pessoa)

print(dados)

for ind, y in enumerate(dados):
    media = (y[1] + y[2] + (y[3] * 2)) / 3
    print(f"A média de {y[0]} é {media:.1f}.")
    if media > 7:
        print(f"{y[0]} Aprovado!")
    else: print(f"{y[0]} Reprovado!")
    