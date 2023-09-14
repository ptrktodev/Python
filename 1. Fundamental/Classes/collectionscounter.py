# mostrar os tops de vendas usando modulo

from collections import Counter

vend = {'ana': 34, "jul": 30, "beto": 90, 'ygao': 180}

d = Counter(vend)

print(d.most_common(2))
