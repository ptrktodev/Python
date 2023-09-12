workers = []

numbers_workers = int(input('Números de trablhadores: '))

for x in range(numbers_workers):
    worker = {}
    worker['nome'] = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    worker['idade'] = 2023 - ano_nascimento
    r_worke = str(input('Você trabalha atualmente, S ou N: ')).upper()
    if 'S' in r_worke:
        worker['trabalho'] = 'Trabalhador'
        worker['salario'] = int(input('Digite o seu salário: '))
    else:
        worker['trabalho'] = 'Não é Trabalhador'
    worker['aposentadoria'] = 60 - (2023 - ano_nascimento)
    workers.append(worker)

for d in workers:
    print(d)
