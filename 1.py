import openpyxl

wb = openpyxl.load_workbook('excel.xlsm')

# ['Руководство пользователя', 'Модель', 'Вид для портала', 'Эластичность спроса', 'Рентабельность (Росстат)',
# 'Структура затрат (ЦСР)', 'Эластичности замещения (GTAP)', 'Налоговая нагрузка (ФНС)', 'Рентабельность (ФНС) ']
sheet = wb.active
print(sheet)
print(sheet['A1'].value)
sheet2 = wb['Эластичность спроса']
# print(sheet2['A2'].value)
#
# for row in sheet['A1':'D12']:
#     string = ''
#     for cell in row:
#         string = string + str(cell.value) + ' '
#     print(string)
