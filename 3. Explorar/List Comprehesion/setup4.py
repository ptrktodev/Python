meta = 1800
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['tv', 'vinho', 'microondas', 'iphone']

produtos_metas = [prod for i, prod in enumerate(produtos) if vendas_produtos[i] > meta]

print(produtos_metas)

 # -----
 
par = [x for x in range(22) if x % 2 == 0]
# print(par)

sentence = "This is a sample sentence for list comprehension"
long_words = [word for word in sentence.split() if len(word) > 5]
# print(long_words)