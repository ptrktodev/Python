def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))

resposta = par(num)

if resposta == True:
    print("É par.")
else:
    print('Não é par.')
