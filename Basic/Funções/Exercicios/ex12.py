email = 'patrick@gmail.com'


def email_(x):
    try:
        # isolamento da linha que possivelmente pode haver erros
        posicao_arroba = x.index('@')
    except:
        raise ValueError("@ não digitado. ")
    else:
        posicao_ponto = x.index('.')
        serv = x[posicao_arroba + 1:posicao_ponto].lower()

        print(serv)


email_(email)
