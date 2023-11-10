x = [3, 54, 3, 26, 43]

try:
    print(x[5] / 0)
    # print(x / 0) // 2° erro
except IndexError as erro:
    print('Index não encontrado!')
except TypeError as erro:
    print('não é possivel dividir')
finally:
    print("Terminou!")
