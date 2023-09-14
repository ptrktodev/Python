from forex_python.converter import CurrencyRates

# pip install forex-python <-

# Crie uma instância do CurrencyRates
c = CurrencyRates()

# Obtenha a taxa de câmbio entre Dólar e Euro e  Armazene a taxa de câmbio em uma variável
usd_to_eur_rate = c.get_rate('USD', 'EUR')
eur_to_eur_rate = c.get_rate('EUR', 'EUR')

# Converta 100 dólares para euros
valor = 100
euros_amount = c.convert('USD', 'EUR', valor)

# listar todas as taxas de câmbio disponíveis para uma moeda específica.
moeda = c.get_rates('BRL')
for dic in moeda.items():
    print(F"{dic[0]} -> {dic[1]}")
