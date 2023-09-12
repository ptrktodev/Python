
a = 5
b = 4
h = 4
c = 3
tupla = tuple((a, h , b, c))

x = tupla.count(4)
y = tupla.index(3)

print(tupla)
print(f"O valor aparece {x} vezes. ")
print(f"A posição do valor é {y}. ")


tupla_pares = tuple(x for x in tupla if x % 2 == 0)
print(tupla_pares)