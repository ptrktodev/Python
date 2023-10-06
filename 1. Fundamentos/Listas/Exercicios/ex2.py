'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma 
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente.
'''

numeros = []  # Cria uma lista vazia para armazenar os números
x = True
y = 0

try: 
    while x == True:
        
        if y < 3:
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
            
    print(numeros)
    
except ValueError:
    print("Caráter inválido!")
