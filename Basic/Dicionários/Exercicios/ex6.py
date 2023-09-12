pessoas = []

qntd_pessoa = int(input('Numero de pessoas: '))

for x in range(qntd_pessoa):
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo: ')).upper()
    pessoas.append(pessoa)


# Tamannho da lista contendo os dicionários.
print(f"O tamanho da lista é: {len(pessoas)}.")
print('----')

# Verificar a média de idade das pessoas
soma = []
for dictio in pessoas:
    soma.append(dictio['idade'])

media = sum(soma) / len(soma)
print(f'A média de idade é: {media:.0f}.')
print('----')

# Lista com as mulheres.

mulheres = []

for dic in pessoas:
    if dic['sexo'] == 'FEMININO' or dic['sexo'] == 'FEMININA':
        mulheres.append(dic)

print(f"As mulheres dessa lista são:")
for c in mulheres:
    print(c['nome'])
print('----')

# lista de pessoas com idade acima da média (30 anos)

acima_da_media = []

for dic in pessoas:
    if dic['idade'] > 30:
        acima_da_media.append(dic)

print('Acima da média estão: ')
for pss in acima_da_media:
    print(pss['nome'])
