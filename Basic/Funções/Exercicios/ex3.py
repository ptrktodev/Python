def contador(i, f, p):
    # DOCSTRING
    ''' 
    Criamos um contador: 
    i = inicio
    f = fim
    p = passo
    '''
    y = i
    while y <= f:
        print(y)
        y += p


contador(2, 20, 2)
# help(contador)


def reversecontador(numero, passo):
    num = numero
    while num != 0:
        print(num)
        num -= passo


# reversecontador(30, 5)
