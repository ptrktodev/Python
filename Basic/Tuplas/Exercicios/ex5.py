palavras_tupla = ("Python", "programação")

# Definindo uma lista para armazenar as vogais encontradas
vogais_encontradas = []

# Definindo uma lista com as vogais possíveis
vogais = "aeiouAEIOUãàá"

for palavra in palavras_tupla:
    for letter in palavra:
        if letter in vogais:
            vogais_encontradas.append(letter)
            
qntd_vogais_encontradas = len(vogais_encontradas)
print(vogais_encontradas)
print(f"{qntd_vogais_encontradas} vogais encontrada.")