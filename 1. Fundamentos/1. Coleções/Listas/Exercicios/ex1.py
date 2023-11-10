# insira valores em uma lista

val = list()
    
for x  in range(0, 5):
    val.append(int(input("Digite o número: ")))
    
print(val)
print(f"O maior valor é {max(val)} e está na posição {val.index(max(val))}.")
print(f"O menor valor é {min(val)} e está na posição {val.index(min(val))}.")
val.sort()


print(f"A lista em ordem numérica: {val}")
val.sort(reverse=True)
print(f"A lista em ordem reversa numérica: {val}") 