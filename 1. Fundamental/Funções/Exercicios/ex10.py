notas = [6.7, 5.7, 3.6, 7.8, 5.8, 9.1, 5.8]


def nota(listNotas, opc):
    qntd = len(listNotas)
    maior = max(listNotas)
    menor = min(listNotas)
    media = sum(listNotas) / qntd
    if opc == 1:
        return qntd
    elif opc == 2:
        return maior
    elif opc == 3:
        return menor
    elif opc == 4:
        return f"{media:.1f}"


print(nota(notas, 4))
