preco_produtos = [100,300, 150, 5500]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']
dados_lista = list(zip(preco_produtos, produtos))

dados_lista.sort(reverse=True)

produtos = {preco for preco, produto in dados_lista}

print(produtos)