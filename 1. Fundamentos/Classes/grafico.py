import matplotlib.pyplot as plt # https://matplotlib.org/

# matplotlib -> Biblioteca
# pyplot -> sub-módulo

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

lenn = max(vendas_meses) - min(vendas_meses)

plt.bar(meses, vendas_meses, color='red') # tipo de grafico: bar() = barra 
plt.title('Análise de Vendas Mensais.', fontweight='bold', fontsize='16')
# plt.xlabel('Meses')
plt.ylabel("Vendas", fontweight='bold', color='green') # sub-titulo para eixo y
plt.xlabel("2022", fontweight='bold', color='green') # sub-titulo para eixo x
plt.axis([-1 , len(meses) , min(vendas_meses) - 300, max(vendas_meses) + 300])
plt.show()

# Tipo de gráfico: https://matplotlib.org/stable/plot_types/basic/step.html
# formatações: