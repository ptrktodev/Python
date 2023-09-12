dados = []
pessoa1 = ["Patrick", 20, "Guarulhos"]
pessoa2 = ["Júlio", 19, "Rio de Janeiro"]
pessoa3 = ["Bia", 25, "Salvador"]

dados.append(pessoa1)
dados.append(pessoa2)
dados.append(pessoa3)

for ind, x in enumerate(dados):
    print(
        f"O nome é {dados[ind][0]}, a idade é {dados[ind][1]} e mora em {dados[ind][2]}.")
