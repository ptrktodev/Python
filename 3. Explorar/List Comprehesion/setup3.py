'''
Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.

Crie uma lista com as vendas de 2019.
'''

produto = ['iphone', 'galaxy', 'ipad'] # LIsta com produtos
vendas_2019 = [ 558147, 712350, 573823] # LIsta com vendas de 2019
vendas_2020 = [951642, 244295, 26964] # LIsta com vendas de 2020

vendas_produtos = list(zip(produto, vendas_2019, vendas_2020)) # zipando essas listas e colocando em list
# print -> [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964)]

lista_vendas_2019 = [ano_2019 for produto,ano_2019, ano_2020 in vendas_produtos] # List comprehension

print(lista_vendas_2019)
# print -> [558147, 712350, 573823