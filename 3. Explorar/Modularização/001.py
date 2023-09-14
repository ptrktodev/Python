import uteis001
print(' --- VAMOS CONVERTER O REAL PARA? --- ')
num = int(input('Digite um valor R$ '))

print('--' * 10)
opc = int(input('Conversão: 1 para Euro e 2 para Dolar: '))
print('--' * 10)

if opc == 1:
    print(uteis001.euro(num))
elif opc == 2:
    print(uteis001.dolar(num))
