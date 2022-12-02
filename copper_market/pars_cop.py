import os
from openpyxl import Workbook, load_workbook


mydir = '/Users/natalazivlova/Desktop/parser/copper_market/'
myfile = 'PE_медь.xlsm'
file = os.path.join(mydir, myfile)

wb = load_workbook(file, data_only=True)

sheet = wb.worksheets[0]

model_control_actions = {"name": [], "designation": [], "before": [], "after": []}
for row in range(3, 23):
    name = sheet[row][0].value
    model_control_actions['name'].append(name)
    designation = sheet[row][1].value
    model_control_actions['designation'].append(designation)
    before = sheet[row][2].value
    model_control_actions['before'].append(before)
    after = sheet[row][3].value
    model_control_actions['after'].append(after)
print(model_control_actions)

parameters = {"name": [], "before": [], "after": []}
for row in range(2, 15):
    name = sheet[row][7].value
    parameters['name'].append(name)
    before = sheet[row][8].value
    parameters['before'].append(before)
    after = sheet[row][9].value
    parameters['after'].append(after)
print(parameters)

variables = {"name": [], "designation": [], "base_pr": [], "base_q": [], "quality": [], "new_pr": [], "new_q": [],
             "price_change": [], "q_change": []}
for row in range(25, 37):
    name = sheet[row][0].value
    variables['name'].append(name)
    designation = sheet[row][1].value
    variables['designation'].append(designation)
    base_pr = sheet[row][2].value
    variables['base_pr'].append(base_pr)
    base_q = sheet[row][3].value
    variables['base_q'].append(base_q)
    quality = sheet[row][4].value
    variables['quality'].append(quality)
    new_pr = sheet[row][5].value
    variables['new_pr'].append(new_pr)
    new_q = sheet[row][6].value
    variables['new_q'].append(new_q)
    price_change = sheet[row][7].value
    variables['price_change'].append(price_change)
    q_change = sheet[row][8].value
    variables['q_change'].append(q_change)
print(variables)

equations = {"name": [], "formule": []}
for row in range(38, 62):
    name = sheet[row][0].value
    equations['name'].append(name)
    formule = sheet[row][1].value
    equations['formule'].append(formule)
print(equations)
