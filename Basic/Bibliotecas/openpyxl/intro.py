import openpyxl

# pip install openpyxl

# Abrir um arquivo Excel
workbook = openpyxl.load_workbook('test.xlsx')

# Selecionar uma planilha
# Substitua 'Planilha1' pelo nome da sua planilha
sheet = workbook['Página1']
sheet['A7'].value = 'PAtrick'

# Salvar as alterações no arquivo
# workbook.save('nome_do_arquivo.xlsx') --------------------------------------------------------

for linha in sheet.iter_rows(min_row=6, max_row=15):
    print(linha[0].value)  # linha da coluna 0 = A / 1 = B.
    print(linha[1].value)


for column in sheet.iter_cols(min_col=1, max_col=2):
    print(column[10 - 1].value)  # da col 1 até col 2 na linha 10.
