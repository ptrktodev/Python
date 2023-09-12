vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000

x = []
for item in vendedores_dic:
    if vendedores_dic[item] > meta :
        x.append(vendedores_dic[item] * 0.1)
print(x)

bonus = [vendedores_dic[item] * 0.1 for item in vendedores_dic if vendedores_dic[item] > meta] # LIsta somente quem ganhou bonus
print(bonus)

bonus_esembonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic ]
# print(bonus_esembonus)