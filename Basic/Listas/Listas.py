lanche = ['pizza','sanduiche' ,'pudim', 'refrigerante']
lanche[2] = 'Bolo' # substitui item na lista 
lanche.append("cachorro-quente") # add novo item a lista
lanche.insert(2, "Hamburguer") # add novo item a lista no espaço desejado
del lanche[-1] # exclui item da lista pelo indice
lanche.remove('pizza') # exclui item da lista pelo valor
print(lanche, len(lanche))


