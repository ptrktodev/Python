def msg(text):
    print('---' * 10)
    print(text)
    print('---' * 10)


msg('PATRICK RODRIGUEZ')


def sum(x, y):
    print(x + y)


sum(3, 5)


def contador(* num):
    print(len(num))


def soma(* num):
    lista_num = list(num)
    soma = 0
    for c in lista_num:
        soma += c
    return soma


print(f"soma: {soma(2, 4, 6)}")

contador(2, 3, 54, 6, 22)
contador(2, 3, 54)
contador(2, 3, 54, 6, 22, 4, 4, 4)
