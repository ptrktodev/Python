produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']
preco_produtos = [100, 300, 150, 5500]

preco_dict = list(zip(preco_produtos, produtos))
preco_dict.sort(reverse=True)
print(preco_dict)
x = dict(preco_dict)
print(x)
