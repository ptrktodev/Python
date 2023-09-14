'''
### Lambda em map()
- Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto
'''

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000,
                    'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}
imposto = 1.3  # 30%


def caluclar_imposto(imposto):
    return lambda valor: valor * imposto


# 1
'''def calcular(imp, value):
    return value * imp'''

# 2
'''def calcular(value):
    return value * imposto'''


def_imposto = caluclar_imposto(imposto)

# valores dos produtos como impostos
valores_impostos = list(map(def_imposto, preco_tecnologia.values()))


# 1
'''valores_impostos = list(
    map(lambda x: calcular(imposto, x), preco_tecnologia.values()))'''

# 2
'''valores_impostos = [calcular(i) for i in preco_tecnologia.values()]
print(valores_impostos)'''

produtos = list(preco_tecnologia.keys())  # lista somente com os nomes produtos

# zipando eles para um dicionário
produtos_impostos = dict(zip(produtos, valores_impostos))

print(produtos_impostos)
