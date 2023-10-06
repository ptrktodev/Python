pessoas = []
for x in range(0, 2):
    p = {}
    p['nome'] = str(input("Nome: "))
    p['idade'] = str(input("Idade: "))
    pessoas.append(p)

for dicts in pessoas:
    for key, value in dicts.items():
        print("-> ", key, value)
