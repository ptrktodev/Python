def calculos(x, y):
    soma = x + y
    dif = x - y
    mult = x * y
    div = x / y
    return (soma, dif, mult, div)  # retorna mais de uma resposta em tupla


print(type(calculos(6, 5)))
print(calculos(6, 5))
