meta = 10000

vendedores = {
    'Beto': 12000,
    'Julia': 15010,
    'Rodri': 18000,
    'Tina': 4500,
    'ALb': 16000,
    'KIna': 9010,
    'JUlio': 8000,
    'Tina': 8500,
    'Neto': 8000,
    'Zouza': 52010,
    'Carlos': 3000,
    'Karla': 18500
}

# porcentagem = (parte / total) * 100


def batedores_metas(list, meta=0):
    batedores = []
    for key, value in list.items():
        if value > meta:
            batedores.append(key)
    percentual = (len(batedores) / len(list)) * 100
    return batedores, percentual


def n_batedores_metas(list, meta=0):
    n_batedores = []
    for key, value in list.items():
        if value < meta:
            n_batedores.append(key)
    percentual = (len(n_batedores) / len(list)) * 100
    return n_batedores, percentual


percentual_metas_batidas = batedores_metas(vendedores, meta)[1]
percentual_metas_n_batidas = n_batedores_metas(vendedores, meta)[1]

print(f"{percentual_metas_batidas:.0f}% bateram a meta.")
print(f"{percentual_metas_n_batidas:.0f}% não bateram a meta.")

print('Nomes que bateram a meta: ')
for c in batedores_metas(vendedores, meta)[0]:
    print(c)

print('Nomes que não bateram a meta: ')
for c in n_batedores_metas(vendedores, meta)[0]:
    print(c)
