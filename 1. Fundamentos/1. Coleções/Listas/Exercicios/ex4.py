numeros = []  # Cria uma lista vazia para armazenar os números
x = True
y = 0


while x == True:
            
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        r = input("Quer continuar, S ou N: ").upper()
        if r == "S":
            x = True
        else:
            x = False


print(numeros)
print(f"Você digitou {len(numeros)} números.")
numeros.sort(reverse=True)
print(f"Sua lista de valores em ordem descrescente: {numeros}")
if 5 in numeros:
    print(f"O valor 8 está na lista e aparece {numeros.count(8)}.")
    
