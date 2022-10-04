import numpy as np
import pandas as pd
import os

from sqlalchemy.dialects.mssql.information_schema import columns

mydir = '/Users/natalazivlova/Desktop/parser/new_calc/'
myfile = 'Экспорт_масло.xlsm'
file = os.path.join(mydir, myfile)


df = pd.read_excel(file, usecols='A:Q', index_col=0)

# Список товаров
list_of_products = df[:4][['Список товаров', 'Вклад в ИПЦ']]
# print(list_of_products.to_markdown())

# Эластичности по собственной цене
elasticity_at_its_own_price = df.iloc[6:12, 0:1]
elasticity_at_its_own_price = elasticity_at_its_own_price.rename(columns={'Список товаров': 'Эластичности по собственной цене'})
# print(elasticity_at_its_own_price.to_markdown())

# Коэффициенты выхода продукции
output_coefficients = df.iloc[14:16, 0:1]
output_coefficients = output_coefficients.rename(columns={'Список товаров': 'Коэффициенты выхода продукции'})
# print(output_coefficients.to_markdown())

# Цены на мировом рынке товаров группы B
prices_on_world_market_of_group_b_products = df.iloc[1:7, 3:9]
prices_on_world_market_of_group_b_products.index = np.arange(0, len(prices_on_world_market_of_group_b_products))
prices_on_world_market_of_group_b_products =prices_on_world_market_of_group_b_products.rename(columns={
    'Unnamed: 4': 'Цены на мировом рынке товаров группы B',
    'Unnamed: 5': 'Валюта',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(prices_on_world_market_of_group_b_products.to_markdown())

# Расчет суммы вывозной таможенной пошлины
calculation_of_amount_of_export_customs_duty = df.iloc[9:17, 3:9]
calculation_of_amount_of_export_customs_duty.index = np.arange(0, len(calculation_of_amount_of_export_customs_duty))
calculation_of_amount_of_export_customs_duty = calculation_of_amount_of_export_customs_duty.rename(columns={
    'Unnamed: 4': 'Расчет суммы вывозной таможенной пошлины',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(calculation_of_amount_of_export_customs_duty.to_markdown())

# Внутренний рынок товаров группы B
domestic_market_of_group_b_products = df.iloc[19:21, 3:8]
domestic_market_of_group_b_products.index = np.arange(0, len(domestic_market_of_group_b_products))
domestic_market_of_group_b_products = domestic_market_of_group_b_products.rename(columns={
    'Unnamed: 4': 'Внутренний рынок товаров группы B',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(domestic_market_of_group_b_products.to_markdown())

# Внутренний рынок товара А
internal_market_of_product_a = df.iloc[23:26, 3:8]
internal_market_of_product_a.index = np.arange(0, len(internal_market_of_product_a))
internal_market_of_product_a = internal_market_of_product_a.rename(columns={
    'Unnamed: 4': 'Внутренний рынок товара А',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(internal_market_of_product_a.to_markdown())

# Внутреннее производство и баланс товара А
internal_production_and_balance_of_goods_a = df.iloc[28:33, 3:9]
internal_production_and_balance_of_goods_a.index = np.arange(0, len(internal_production_and_balance_of_goods_a))
internal_production_and_balance_of_goods_a = internal_production_and_balance_of_goods_a.rename(columns={
    'Unnamed: 4': 'Внутреннее производство и баланс товара А',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(internal_production_and_balance_of_goods_a.to_markdown())

# Внутреннее производство товара С
internal_production_of_goods_c = df.iloc[35:39, 3:8]
internal_production_of_goods_c.index = np.arange(0, len(internal_production_of_goods_c))
internal_production_of_goods_c = internal_production_of_goods_c.rename(columns={
    'Unnamed: 4': 'Внутреннее производство товара С',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(internal_production_of_goods_c.to_markdown())

# Производство и баланс товаров группы B
production_and_balance_of_group_b_goods = df.iloc[41:47, 3:8]
production_and_balance_of_group_b_goods.index = np.arange(0, len(production_and_balance_of_group_b_goods))
production_and_balance_of_group_b_goods = production_and_balance_of_group_b_goods.rename(columns={
    'Unnamed: 4': 'Производство и баланс товаров группы B',
    'Unnamed: 5': 'Единица измерения',
    'Unnamed: 6': 'Обозначение',
    'Unnamed: 9': 'Статус'
})
# print(production_and_balance_of_group_b_goods.to_markdown())

# Цены
prices = df.iloc[2:7, 10:16]
prices.index = np.arange(0, len(prices))
prices = prices.rename(columns={
    'Результаты': 'Цены',
    'Unnamed: 12': 'Единица измерения',
    'до.1': 'До',
    'после.1': 'После',
    'Прирост': 'Прирост +/-',
    'Unnamed: 16': 'Прирост %'
})
# print(prices.to_markdown())

# Производство и потребление
production_and_consumption = df.iloc[9:17, 10:16]
production_and_consumption.index = np.arange(0, len(production_and_consumption))
production_and_consumption = production_and_consumption.rename(columns={
    'Результаты': 'Производство и потребление',
    'Unnamed: 12': 'Единица измерения',
    'до.1': 'До',
    'после.1': 'После',
    'Прирост': 'Прирост +/-',
    'Unnamed: 16': 'Прирост %'
})
# print(production_and_consumption.to_markdown())

# Стоимостные эффекты
cost_effects = df.iloc[20:57, 10:16]
cost_effects.index = np.arange(0, len(cost_effects))
cost_effects = cost_effects.rename(columns={
    'Результаты': 'Стоимостные эффекты',
    'Unnamed: 12': 'Единица измерения',
    'до.1': 'До',
    'после.1': 'После',
    'Прирост': 'Прирост +/-',
    'Unnamed: 16': 'Прирост %'
})
print(cost_effects.to_markdown())
