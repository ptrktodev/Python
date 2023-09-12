
# Normal
def soma(x):
    return x + 5

print(soma(10))

# Lambda

y = 5
multi_dois = lambda parametro_y: parametro_y * 2 # minha_funcao = lambda parametro: expressão
print(multi_dois(y))

# ------------------------------------------      
# exemplo mais util

valor_produto = 1000

def impost(value): # com def
    return (value * 0.3) + value

print(impost(valor_produto)) # 1300

impost2 = lambda value: (value * 0.3) + value # com Lambda

print(impost2(valor_produto)) # 1300