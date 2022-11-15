import os
from openpyxl import Workbook, load_workbook


mydir = '/Users/natalazivlova/Desktop/parser/food_products_import/food_products_import/'
myfile = 'Импорт_все_продтовары (2).xlsm'
file = os.path.join(mydir, myfile)

wb = load_workbook(file, data_only=True)

sheet = wb.worksheets[0]

pricing_characteristics_dict = {"name": [], "designation": [], 'measure': [], "before": [], "after": [], 'increment': []}
for row in range(3, 13):
    name = sheet[row][0].value
    pricing_characteristics_dict['name'].append(name)
    designation = sheet[row][1].value
    pricing_characteristics_dict['designation'].append(designation)
    measure = sheet[row][2].value
    pricing_characteristics_dict['measure'].append(measure)
    before = sheet[row][3].value
    pricing_characteristics_dict['before'].append(before)
    after = sheet[row][4].value
    pricing_characteristics_dict['after'].append(after)
    increment = sheet[row][5].value
    pricing_characteristics_dict['increment'].append(increment)
print(pricing_characteristics_dict)

quantitative_characteristics = {"name": [], "designation": [], 'measure': [], "before": [], "after": [], 'increment': []}
for row in range(15, 21):
    name = sheet[row][0].value
    quantitative_characteristics['name'].append(name)
    designation = sheet[row][1].value
    quantitative_characteristics['designation'].append(designation)
    measure = sheet[row][2].value
    quantitative_characteristics['measure'].append(measure)
    before = sheet[row][3].value
    quantitative_characteristics['before'].append(before)
    after = sheet[row][4].value
    quantitative_characteristics['after'].append(after)
    increment = sheet[row][5].value
    quantitative_characteristics['increment'].append(increment)
print(quantitative_characteristics)

effects = {"name": [], "val": [], 'measure': [], "increment_pr": []}
for row in range(24, 47):
    name = sheet[row][0].value
    effects['name'].append(name)
    val = sheet[row][1].value
    effects['val'].append(val)
    measure = sheet[row][2].value
    effects['measure'].append(measure)
    increment_pr = sheet[row][3].value
    effects['increment_pr'].append(increment_pr)
print(effects)

equations_dict = {"name": [], "val": [], 'val2': []}
for row in range(12, 19):
    name = sheet[row][7].value
    equations_dict['name'].append(name)
    val = sheet[row][8].value
    equations_dict['val'].append(val)
    val2 = sheet[row][9].value
    equations_dict['val2'].append(val2)
print(equations_dict)