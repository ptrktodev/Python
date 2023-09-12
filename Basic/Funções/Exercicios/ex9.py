def leiaInt(g):
    n = str(g)
    if n.isdigit():
        x = int(n)
        return f'Caráter Numérico. {x}'
    else:
        return 'Caráter Alfabético.'


print(leiaInt(55))
print(leiaInt('km'))
