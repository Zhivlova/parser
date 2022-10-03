import numpy as np
import pandas as pd
import os
import openpyxl
from pandas import DataFrame

mydir = '/Users/natalazivlova/Desktop/parser/new_calc/'
myfile = 'Экспорт_масло.xlsm'
file = os.path.join(mydir, myfile)

df = pd.read_excel(file, usecols='A:Q', index_col=0)

# Список товаров
list_of_products = df[:4][['Список товаров', 'Вклад в ИПЦ']]
# print(list_of_products)

# Эластичности по собственной цене
elasticity_at_its_own_price = df.iloc[6:12, 0:1]
# print(elasticity_at_its_own_price)

# Коэффициенты выхода продукции
output_coefficients = df.iloc[14:16, 0:1]
# print(output_coefficients)

# Цены на мировом рынке товаров группы B
prices_on_world_market_of_group_b_products = df.iloc[1:7, 3:9]
prices_on_world_market_of_group_b_products.index = np.arange(0, len(prices_on_world_market_of_group_b_products))
# print(prices_on_world_market_of_group_b_products)

# Расчет суммы вывозной таможенной пошлины
calculation_of_amount_of_export_customs_duty = df.iloc[9:17, 3:9]
calculation_of_amount_of_export_customs_duty.index = np.arange(0, len(calculation_of_amount_of_export_customs_duty))
# print(calculation_of_amount_of_export_customs_duty)

# Внутренний рынок товаров группы B
domestic_market_of_group_b_products = df.iloc[19:21, 3:9]
domestic_market_of_group_b_products.index = np.arange(0, len(domestic_market_of_group_b_products))
# print(domestic_market_of_group_b_products)

# Внутренний рынок товара А
internal_market_of_product_a = df.iloc[23:26, 3:9]
internal_market_of_product_a.index = np.arange(0, len(internal_market_of_product_a))
# print(internal_market_of_product_a)

# Внутреннее производство и баланс товара А
internal_production_and_balance_of_goods_a = df.iloc[28:33, 3:9]
internal_production_and_balance_of_goods_a.index = np.arange(0, len(internal_production_and_balance_of_goods_a))
# print(internal_production_and_balance_of_goods_a)

# Внутреннее производство товара С
internal_production_of_goods_c = df.iloc[34:39, 3:9]
internal_production_of_goods_c.index = np.arange(0, len(internal_production_of_goods_c))
# print(internal_production_of_goods_c)

# Производство и баланс товаров группы B
production_and_balance_of_group_b_goods = df.iloc[41:47, 3:9]
production_and_balance_of_group_b_goods.index = np.arange(0, len(production_and_balance_of_group_b_goods))
print(production_and_balance_of_group_b_goods)





# print(elasticity_at_its_own_price.columns.tolist())
# list_of_products = df['Список товаров'][:4]

# print(list_of_products)
# print(list_of_products.iloc[0:3])
# print(list_of_products[['Список товаров', 'Вклад в ИПЦ']])
# print(list_of_products.index)
# print(list_of_products.columns.tolist())
