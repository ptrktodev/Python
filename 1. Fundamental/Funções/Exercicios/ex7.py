'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def votar(ano):
    idade = 2023 - ano
    if idade < 16:
        return f"Você tem {idade} anos: Voto Negado!"
    elif idade <= 18:
        return f"Você tem {idade} anos: Voto Opcional!"
    else:
        return f"Você tem {idade} anos: Voto Obrigatório!"


ano_nasc = int(input('Ano de nacimento: '))

print(votar(ano_nasc))
