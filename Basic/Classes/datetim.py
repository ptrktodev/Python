from datetime import datetime

# BÁSICO E INTORDUTÓRIO

agora = datetime.now()

year = agora.year
month = agora.month
day = agora.day

hour = agora.hour
minute = agora.minute
seconds = agora.second

print(f"Estamos no ano de {year}, mês {month}, no dia {day}.")

# AVANÇADO

'''
Monday->Segunda-feira
Tuesday->Terça-feira
Wednesday->Quarta-feira
Thursday->Quinta-feira
Friday->Sexta-feira
Saturday->Sábado
Sunday->Domingo
'''

# https://strftime.org/ <- SheetCheat

day_week = agora.strftime("%a")  # retorna abreviação do dia da semana
day_week_A = agora.strftime("%A")  # retorna nome complet. do dia da semana

month_complete = agora.strftime("%B")
year_int = agora.strftime("%Y")
hour_int = agora.strftime("%-H")
locality = agora.strftime('%p')
dayyear_int = agora.strftime('%-j')
print(dayyear_int)


print('hello')
