import pandas as pd

# Загружаем ваш файл в переменную `file` / вместо 'example' укажите название свого файла из текущей директории
file = 'excel.xlsm'

# Загружаем spreadsheet в объект pandas
xl = pd.ExcelFile(file)

# Печатаем название листов в данном файле
# print(xl.sheet_names)

# Загрузить лист в DataFrame по его имени: df1
# df1 = xl.parse('Руководство пользователя')
# # excel_data_df = pd.read_excel('excel.xlsm', sheet_name='Модель',  usecols=['Управляющие воздействия модели',  'Базовое равновесие', 'Новое равновесие'])
#
# excel_data_df = pd.read_excel('excel.xlsm', sheet_name='Модель')
# print(excel_data_df)
# print(excel_data_df.columns)
# print(excel_data_df.dtypes)
# print(excel_data_df.index)
# print(excel_data_df['Эластичность спроса'])
# show_these = ['1', '2']
# print(excel_data_df.iloc[show_these])

# columns = ['Управляющие воздействия модели', 'Базовое равновесие']
# rows = ['1', '2', '3']
# excel_data_df.iloc[rows][columns]





