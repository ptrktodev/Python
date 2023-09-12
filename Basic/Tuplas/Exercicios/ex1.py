count = ('zero', 'um', 'dois', 'tres')
f = True

while f == True:
    num = input("Digite um número até 3: ")
    if num.isalpha():
        print("Você digitou um carater alfabético.")
        f = True
    elif num.isdigit():
        x = int(num)
        if x >= 4:
            print("Digito Numérico não corresponde!")
            f = True
        else: 
            print(f"Você digitou o número {count[x]}.")
            f = False
    