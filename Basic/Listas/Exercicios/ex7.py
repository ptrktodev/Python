dados = []

par = []
impar = []

for x in range(0, 4):
    numero = int(input("Numero: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
        
dados.append(par)
dados.append(impar)
print(dados)