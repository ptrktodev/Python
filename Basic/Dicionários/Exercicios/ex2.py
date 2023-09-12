'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

room = []

numero_estudantes = int(input('Digite o número de estudantes: '))

for c in range(numero_estudantes):
    aluno = {}
    aluno['nome'] = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    soma = (n1 + n2 + (n3 * 2)) / 3
    if soma < 7:
        aluno['situacao'] = 'Reprovado(a)'
        aluno['notafinal'] = soma
    else:
        aluno['situacao'] = 'Aprovado(a)'
        aluno['notafinal'] = soma
    room.append(aluno)

for dicts in room:
    print(
        f"{dicts['nome']} tem uma nota de {dicts['notafinal']:.2f} e está {dicts['situacao']}.")

# NOTAS ALUNOS - Media

media_alunos = []
for dicts in room:
    media_alunos.append(dicts['notafinal'])

somaMedia = sum(media_alunos)
media_total_denotas = somaMedia / len(media_alunos)
print(f"A meia da nota dos alunos é: {media_total_denotas:.2f}")
