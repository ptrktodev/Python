'''
PARAMETRO OPCIONAL
'''


def somar(a, b, c=0):
    s = a + b + c
    print(f"Soma: {s}")


somar(4, 6)


'''
return em def
'''


def multiplicar(a, b, c=1):
    soma = a * b * c
    return soma


resp = multiplicar(6, 2)
print(f"{multiplicar(3, 6)} e {resp}")
