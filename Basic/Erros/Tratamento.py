x = True

num1 = 0

while x:
    try:
        if num1 == 0:
            num1 = int(input('Valor inteiro: '))

        num2 = float(input('Valor real: '))
        x = False
        print(f'O valor inteiro é {num1} e o real é {num2}. ')

    except ValueError:
        print('Digite o valor pedido corretamente!!!')
        x = True
    except KeyboardInterrupt:
        print('Usuário preferiu não digitar')
