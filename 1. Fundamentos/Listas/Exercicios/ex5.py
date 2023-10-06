lista = []

par = []
impar = []

print("Digite 6 números.")
for x in range(0, 6):
    number = int(input("Digite um número: "))
    lista.append(number)
    
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)
        
print("Números pares: ", par)
print("Números impares: ", impar)
        