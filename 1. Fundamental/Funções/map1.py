nomes = [' lucas  ', 'KlaudiU']

def padronizar_texto(texto):
    texto = texto.lower()
    texto = texto.strip()
    texto = texto.capitalize()
    return texto 

# COM FOR:s
for c in nomes:
    print(padronizar_texto(c)) 

# COM MAP:
lista_nomes = list(map(padronizar_texto, nomes))
print(lista_nomes)