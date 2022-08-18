from openpyxl import Workbook
from openpyxl.workbook.defined_name import DefinedName
import openpyxl
from openpyxl import load_workbook
from openpyxl.formula import Tokenizer

wb = load_workbook('excel.xlsm')
new_range = DefinedName('newrange', attr_text='Sheet!$A$1:$A$5')
wb.defined_names.append(new_range)
print(new_range)