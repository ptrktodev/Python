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


contador(2, 10, 2)
help(contador)
