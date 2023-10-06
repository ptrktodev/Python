produtos = 1.1
servicos = 1.15
royalties = 1.25


def calcular_imposto(imposto):
    return lambda preco: preco * imposto

calcular_preco_produto = calcular_imposto(produtos)
calcular_preco_servicos = calcular_imposto(servicos)
calcular_preco_royalties = calcular_imposto(royalties)

print(int(calcular_preco_royalties(100)))