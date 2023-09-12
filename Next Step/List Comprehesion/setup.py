preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

def calcular_imp(preco, imposto):
    return preco * imposto
    
impostos = [calcular_imp(preco, 0.3) for preco in preco_produtos]
print(impostos)

'''
valor_atualizado = []
for x in range(1, len(preco_produtos) + 1):
    valor_atualizado.append(preco_produtos[x - 1] - descontos[x - 1] )
    
print(valor_atualizado)'''

        