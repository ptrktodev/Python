from forex_python.converter import CurrencyRates

# Crie uma instância do CurrencyRates
c = CurrencyRates()

# Obtenha a taxa de câmbio do Euro para o Real
valor_euro_em_reais = c.get_rate('BRL', 'EUR')
valor_dolar_em_reais = c.get_rate('BRL', 'USD')


def dolar(num):
    d = num * valor_dolar_em_reais
    return f'{d:.2F} US$'


def euro(num):
    e = num * valor_euro_em_reais
    return f'{e:.2F} €'
