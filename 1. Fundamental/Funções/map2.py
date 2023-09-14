'''
### Lambda em map()
- Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto
'''

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}
imposto = 30


valores_impostos = list(map(lambda value: value * 1.30, preco_tecnologia.values()))

prodts = list(preco_tecnologia.keys())

produtos_impostos = dict(zip(prodts, valores_impostos))

print(produtos_impostos)