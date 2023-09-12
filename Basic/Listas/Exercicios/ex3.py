'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em 
uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela.
'''

numeros = []  # Cria uma lista vazia para armazenar os números
x = True
y = 0


while x == True:
            
    if y < 5:
        numero = int(input("Digite um número: "))
        if numero in numeros:
            print("numero ja adicionado.")
            x = True
        else:
            numeros.append(numero)
            y += 1
    else: 
        print("Fim do programa!")
        x = False

print('Ordem estabelecida por você: ', numeros)                
numeros.sort()            
print('Ordem numérica estabelecida: ', numeros)