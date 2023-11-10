# Pontuação do aluno
pontuacao = 75

# Estrutura
if pontuacao >= 90:
    nota = 'A'
elif pontuacao >= 80:
    nota = 'B'
elif pontuacao >= 70:
    nota = 'C'
elif pontuacao >= 60:
    nota = 'D'
else:
    nota = 'F'

# resultado
print(f'A pontuação {pontuacao} corresponde à nota {nota}.')