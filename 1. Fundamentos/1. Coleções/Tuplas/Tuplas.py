''' Tuplas são variáveis compostas. (IMUTÁVEIS) '''

tuple = (('one', 'two')) # declaração de tupla
lanche = ('pizza', 'xis', 'sorvete', 'cachorro-quente')

# print(len(lanche)) # 4

'''for ind in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[ind]}.")    

for pos, c in enumerate(lanche): # posição e dado
    print(f"{lanche[pos]} está na posição {pos}.")   '''
    
print(sorted(lanche)) # em Ordem Alfabética

a = (3, 4, 2, 5)
b = (1, 0, 1,)
c = a + b
print(c) # (3, 4, 2, 5, 1, 0, 1)
print(len(c)) # 7
print(c.count(1)) # quantas há: 2
print(c.index(5)) # position: 3
# del(c) 