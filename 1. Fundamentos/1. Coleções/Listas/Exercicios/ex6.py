

dados = []

for x in range(0, 3):
    pessoa = []  # Cria uma nova lista "pessoa" em cada iteração do loop
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Peso: ")))
    dados.append(pessoa)

print(f"Foram cadastradas um total de {len(dados)} dados.")

for y in dados:
    if y[1] < 75:
        print(f"{y[0]} é magro(a).")
    elif y[1] < 100:
        print(f"{y[0]} é quase gordo(a).")
    else:
        print(f"{y[0]} é gordo(a).")
