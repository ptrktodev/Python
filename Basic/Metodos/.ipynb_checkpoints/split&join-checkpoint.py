# Divide uma string em uma lista de substrings com base em um caractere delimitador.

frase = "Python é uma linguagem de programação"

nova_frase = frase.split()

print(nova_frase) # Saída: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

# Concatena elementos de uma lista em uma única string, usando um separador específico.

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
frase = " ".join(palavras)
print(frase)  # Saída: "Python é uma linguagem de programação"
