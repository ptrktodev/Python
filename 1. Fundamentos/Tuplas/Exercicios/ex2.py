brasileirao23 = ('Botafogo', 'Flamengo', 'Palmeiras', 'Gremio', 
                 'Fluminense', 'Bragantino', 'Atl PR', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Fortaleza',
                 'Internacional', 'Atl MG', 'Corinthians', 'Santos', 'Goiás', 'Bahia', 'Coritiba', 'America MG',
                 'Vasco')

try:
    a = True
    while a == True:
        choice = int(input("Escolha uma das opções abaixo:\n"
                    "[1] - Os 5 primeiros times.\n"
                    "[2] - Os últimos 4 colocados.\n"
                    "[3] - Times em ordem alfabética.\n"
                    "[4] - Em que posição está o time...\n"
                    "Digite o número da opção desejada: "))

        
        if choice == 1 :
            for pos, time in enumerate(brasileirao23[0:6]):
                print(f"{pos}. {time}")
            r = input('Deseja continuar? N ou S: ').capitalize()
            if r == 'N':
                a = False
        elif choice == 2 :
            for pos, time in enumerate(brasileirao23[-4:], start=17):
                print(f"{pos}. {time}")
            r = input('Deseja continuar? N ou S: ').capitalize()
            if r == 'N':
                a = False
        elif choice == 3 :
                ordem = sorted(brasileirao23)
                for pos, timeOrd in enumerate(ordem):
                    print(pos + 1, timeOrd)
                r = input('Deseja continuar? N ou S: ').capitalize()
                if r == 'N':
                    a = False
        elif choice == 4:
            nome_search = input('Nome do time: ').lower().capitalize()
            enc = False
            posi = ''
            for pos, time in enumerate(brasileirao23):
                if time == nome_search:
                    enc = True
                    posi = pos
            if enc:
                inteiro = int(posi)
                print(f"-> Encontrado na {inteiro}ª posição.")
            else: 
                print("Não encontrado.")
            r = input('Deseja continuar? N ou S: ').capitalize()
            if r == 'N':
                a = False
              
except ValueError:
    print('Digite um número inteiro válido')