from pprint import pprint

import numpy as np
import pandas as pd
import os

# example_data = {'PW_B1_before': 1500.0, 'PW_B1_after': 1500.0, 'PW_B2_before': 300.0, 'PW_B2_after': 300.0,
#                 'ER_before': 75.0, 'ER_after': 75.0, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
#                 'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
#                 'Pb_B2_after': 13875.0, 'tb_B2_before': 0.7, 'tb_B2_after': 0.7, 'PI_B1': 90000.0, 'PI_B2': 15000.0,
#                 'PI_A': 40000.0, 'QSI_A': 15.0, 'QSW_RUS_A_before': 0.0, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
#                 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 130000.0,
#                 'QDI_С': 3.0, 'QDI_B2': 2.0}

user_data = {'PW_B1_before': 1500.0, 'PW_B1_after': 1500.0, 'PW_B2_before': 300.0, 'PW_B2_after': 300.0,
            'ER_before': 75.0, 'ER_after': 75.0, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_B1_before': 82500.0,
            'Pb_B1_after': 82500.0, 'tb_B1_before': 0.0, 'tb_B1_after': 0.7, 'Pb_B2_before': 13875.0,
            'Pb_B2_after': 13875.0, 'tb_B2_before': 0.7, 'tb_B2_after': 0.7, 'PI_B1': 90000.0, 'PI_B2': 15000.0,
            'PI_A': 40000.0, 'QSI_A': 15.0, 'QSW_RUS_A_before': 0.0, 'QSW_RUS_A_after': 0.0, 'i_cost_before': 1.0,
            'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0, 'shift_QSI_A_after': 0.0, 'PI_С': 130000.0,
            'QDI_С': 3.0, 'QDI_B2': 2.0}

class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.PW_B1_before = float(dict_from_frontend.get('PW_B1_before'))
        self.PW_B1_after = float(dict_from_frontend.get('PW_B1_after'))
        self.PW_B2_before = float(dict_from_frontend.get('PW_B2_before'))
        self.PW_B2_after = float(dict_from_frontend.get('PW_B2_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.TD_before = float(dict_from_frontend.get('TD_before'))
        self.TD_after = float(dict_from_frontend.get('TD_after'))
        self.Pb_B1_before = float(dict_from_frontend.get('Pb_B1_before'))
        self.Pb_B1_after = float(dict_from_frontend.get('Pb_B1_after'))
        self.tb_B1_before = float(dict_from_frontend.get('tb_B1_before'))
        self.tb_B1_after = float(dict_from_frontend.get('tb_B1_after'))
        self.Pb_B2_before = float(dict_from_frontend.get('Pb_B2_before'))
        self.Pb_B2_after = float(dict_from_frontend.get('Pb_B2_after'))
        self.tb_B2_before = float(dict_from_frontend.get('tb_B2_before'))
        self.tb_B2_after = float(dict_from_frontend.get('tb_B2_after'))
        self.PI_B1 = float(dict_from_frontend.get('PI_B1'))
        self.PI_B2 = float(dict_from_frontend.get('PI_B2'))
        self.PI_A = float(dict_from_frontend.get('PI_A'))
        self.QSI_A = float(dict_from_frontend.get('QSI_A'))
        self.QSW_RUS_A_before = float(dict_from_frontend.get('QSW_RUS_A_before'))
        self.QSW_RUS_A_after = float(dict_from_frontend.get('QSW_RUS_A_after'))
        self.i_cost_before = float(dict_from_frontend.get('i_cost_before'))
        self.i_cost_after = float(dict_from_frontend.get('i_cost_after'))
        self.shift_QSI_A_before = float(dict_from_frontend.get('shift_QSI_A_before'))
        self.shift_QSI_A_after = float(dict_from_frontend.get('shift_QSI_A_after'))
        self.PI_С = float(dict_from_frontend.get('PI_С'))
        self.QDI_С = float(dict_from_frontend.get('QDI_С'))
        self.QDI_B2 = float(dict_from_frontend.get('QDI_B2'))

def oil_export(input_data):
    # Получаем модель
    mydir = '/Users/natalazivlova/Desktop/parser/new_calc/'
    myfile = 'Экспорт_масло_легенда.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:Q', index_col=0)

    # Список товаров
    list_of_products = df[:4][['Список товаров', 'Вклад в ИПЦ']]
    #print(list_of_products.to_markdown())

    # Эластичности по собственной цене
    elasticity_at_its_own_price = df.iloc[6:12, 0:1]
    elasticity_at_its_own_price = elasticity_at_its_own_price.rename(columns={
        'Список товаров': 'Эластичности по собственной цене'})
    # print(elasticity_at_its_own_price.to_markdown())

    # Коэффициенты выхода продукции
    output_coefficients = df.iloc[14:16, 0:1]
    output_coefficients = output_coefficients.rename(columns={
        'Список товаров': 'Коэффициенты выхода продукции'})
    # print(output_coefficients.to_markdown())

    # Цены на мировом рынке товаров группы B
    prices_on_world_market_of_group_b_products = df.iloc[1:7, 3:9]
    prices_on_world_market_of_group_b_products.index = np.arange(0, len(prices_on_world_market_of_group_b_products))
    prices_on_world_market_of_group_b_products = prices_on_world_market_of_group_b_products.rename(columns={
        'Unnamed: 4': 'Цены на мировом рынке товаров группы B',
        'Unnamed: 5': 'currency',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    prices_on_world_market_of_group_b_products.at[0, 'before'] = input_data.PW_B1_before
    prices_on_world_market_of_group_b_products.at[0, 'after'] = input_data.PW_B1_after
    prices_on_world_market_of_group_b_products.at[1, 'before'] = input_data.PW_B2_before
    prices_on_world_market_of_group_b_products.at[1, 'after'] = input_data.PW_B2_after
    prices_on_world_market_of_group_b_products.at[4, 'before'] = input_data.ER_before
    prices_on_world_market_of_group_b_products.at[4, 'after'] = input_data.ER_after
    prices_on_world_market_of_group_b_products.at[5, 'before'] = input_data.TD_before
    prices_on_world_market_of_group_b_products.at[5, 'after'] = input_data.TD_after
    # print(prices_on_world_market_of_group_b_products.to_markdown())

    # Расчет суммы вывозной таможенной пошлины
    calculation_of_amount_of_export_customs_duty = df.iloc[9:17, 3:9]
    calculation_of_amount_of_export_customs_duty.index = np.arange(0, len(calculation_of_amount_of_export_customs_duty))
    calculation_of_amount_of_export_customs_duty = calculation_of_amount_of_export_customs_duty.rename(columns={
        'Unnamed: 4': 'Расчет суммы вывозной таможенной пошлины',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    calculation_of_amount_of_export_customs_duty.at[0, 'before'] = input_data.Pb_B1_before
    calculation_of_amount_of_export_customs_duty.at[0, 'after'] = input_data.Pb_B1_after
    calculation_of_amount_of_export_customs_duty.at[1, 'before'] = input_data.tb_B1_before
    calculation_of_amount_of_export_customs_duty.at[1, 'after'] = input_data.tb_B1_after
    calculation_of_amount_of_export_customs_duty.at[4, 'before'] = input_data.Pb_B2_before
    calculation_of_amount_of_export_customs_duty.at[4, 'after'] = input_data.Pb_B2_after
    calculation_of_amount_of_export_customs_duty.at[5, 'before'] = input_data.tb_B2_before
    calculation_of_amount_of_export_customs_duty.at[5, 'after'] = input_data.tb_B2_after
    # print(calculation_of_amount_of_export_customs_duty.to_markdown())

    # Внутренний рынок товаров группы B
    domestic_market_of_group_b_products = df.iloc[19:21, 3:8]
    domestic_market_of_group_b_products.index = np.arange(0, len(domestic_market_of_group_b_products))
    domestic_market_of_group_b_products = domestic_market_of_group_b_products.rename(columns={
        'Unnamed: 4': 'Внутренний рынок товаров группы B',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    domestic_market_of_group_b_products.at[0, 'before'] = input_data.PI_B1
    domestic_market_of_group_b_products.at[1, 'before'] = input_data.PI_B2
    # print(domestic_market_of_group_b_products.to_markdown())

    # Внутренний рынок товара А
    internal_market_of_product_a = df.iloc[23:26, 3:8]
    internal_market_of_product_a.index = np.arange(0, len(internal_market_of_product_a))
    internal_market_of_product_a = internal_market_of_product_a.rename(columns={
        'Unnamed: 4': 'Внутренний рынок товара А',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    internal_market_of_product_a.at[2, 'before'] = input_data.PI_A
    # print(internal_market_of_product_a.to_markdown())

    # Внутреннее производство и баланс товара А
    internal_production_and_balance_of_goods_a = df.iloc[28:33, 3:9]
    internal_production_and_balance_of_goods_a.index = np.arange(0, len(internal_production_and_balance_of_goods_a))
    internal_production_and_balance_of_goods_a = internal_production_and_balance_of_goods_a.rename(columns={
        'Unnamed: 4': 'Внутреннее производство и баланс товара А',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    internal_production_and_balance_of_goods_a.at[0, 'before'] = input_data.QSI_A
    internal_production_and_balance_of_goods_a.at[1, 'before'] = input_data.QSW_RUS_A_before
    internal_production_and_balance_of_goods_a.at[1, 'after'] = input_data.QSW_RUS_A_after
    internal_production_and_balance_of_goods_a.at[2, 'before'] = input_data.i_cost_before
    internal_production_and_balance_of_goods_a.at[2, 'after'] = input_data.i_cost_after
    internal_production_and_balance_of_goods_a.at[3, 'before'] = input_data.shift_QSI_A_before
    internal_production_and_balance_of_goods_a.at[3, 'after'] = input_data.shift_QSI_A_after
    # print(internal_production_and_balance_of_goods_a.to_markdown())

    # Внутреннее производство товара С
    internal_production_of_goods_c = df.iloc[35:39, 3:8]
    internal_production_of_goods_c.index = np.arange(0, len(internal_production_of_goods_c))
    internal_production_of_goods_c = internal_production_of_goods_c.rename(columns={
        'Unnamed: 4': 'Внутреннее производство товара С',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    internal_production_of_goods_c.at[0, 'before'] = input_data.PI_С
    internal_production_of_goods_c.at[2, 'before'] = input_data.QDI_С
    # print(internal_production_of_goods_c.to_markdown())

    # Производство и баланс товаров группы B
    production_and_balance_of_group_b_goods = df.iloc[41:47, 3:8]
    production_and_balance_of_group_b_goods.index = np.arange(0, len(production_and_balance_of_group_b_goods))
    production_and_balance_of_group_b_goods = production_and_balance_of_group_b_goods.rename(columns={
        'Unnamed: 4': 'Производство и баланс товаров группы B',
        'Unnamed: 5': 'measure',
        'Unnamed: 6': 'designation',
        'до': 'before',
        'после': 'after',
        'Unnamed: 9': 'status'
    })
    production_and_balance_of_group_b_goods.at[4, 'before'] = input_data.QDI_B2
    # print(production_and_balance_of_group_b_goods.to_markdown())

    # Цены
    prices = df.iloc[2:7, 10:16]
    prices.index = np.arange(0, len(prices))
    prices = prices.rename(columns={
        'Результаты': 'Цены',
        'Unnamed: 12': 'measure',
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
        'Unnamed: 12': 'measure',
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
        'Unnamed: 12': 'measure',
        'до.1': 'До',
        'после.1': 'После',
        'Прирост': 'Прирост +/-',
        'Unnamed: 16': 'Прирост %'
    })
    # print(cost_effects.to_markdown())

    result_to_front = {
        'input_table': [
            {
                'id': '1',
                'title': 'Мировая цена товара B1',
                'measure': prices_on_world_market_of_group_b_products.iloc[0].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[0].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[0].before,
                'after': prices_on_world_market_of_group_b_products.iloc[0].after,
                'status': prices_on_world_market_of_group_b_products.iloc[0].status
            },
            {
                'id': '2',
                'title': 'Мировая цена товара B2',
                'measure': prices_on_world_market_of_group_b_products.iloc[1].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[1].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[1].before,
                'after': prices_on_world_market_of_group_b_products.iloc[1].after,
                'status': prices_on_world_market_of_group_b_products.iloc[1].status
            },
            {
                'id': '3',
                'title': 'Стоимость услуг трейдеров товара B1',
                'measure': prices_on_world_market_of_group_b_products.iloc[2].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[2].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[2].before,
                'after': prices_on_world_market_of_group_b_products.iloc[2].after
            },
            {
                'id': '4',
                'title': 'Стоимость услуг трейдеров товара B2',
                'measure': prices_on_world_market_of_group_b_products.iloc[3].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[3].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[3].before,
                'after': prices_on_world_market_of_group_b_products.iloc[3].after
            },
            {
                'id': '5',
                'title': 'Обменный курс',
                'measure': prices_on_world_market_of_group_b_products.iloc[4].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[4].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[4].before,
                'after': prices_on_world_market_of_group_b_products.iloc[4].after,
                'status': prices_on_world_market_of_group_b_products.iloc[4].status
            },
            {
                'id': '6',
                'title': 'Дисконт к эквивалентной цене',
                'measure': prices_on_world_market_of_group_b_products.iloc[5].currency,
                'params': prices_on_world_market_of_group_b_products.iloc[5].designation,
                'before': prices_on_world_market_of_group_b_products.iloc[5].before,
                'after': prices_on_world_market_of_group_b_products.iloc[5].after,
                'status': prices_on_world_market_of_group_b_products.iloc[5].status
            },
            {
                'id': '7',
                'title': 'Базовая цена товара B1',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[0].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[0].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[0].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[0].after,
                'status': calculation_of_amount_of_export_customs_duty.iloc[0].status
            },
            {
                'id': '8',
                'title': 'Ставка вывозной пошлины товара B1',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[1].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[1].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[1].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[1].after,
                'status': calculation_of_amount_of_export_customs_duty.iloc[1].status
            },
            {
                'id': '9',
                'title': 'Вывозная таможенная пошлина на товар B1',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[2].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[2].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[2].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[2].after
            },
            {
                'id': '10',
                'title': 'Адвалорная ставка пошлины на товар B1',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[3].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[3].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[3].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[3].after
            },
            {
                'id': '11',
                'title': 'Базовая цена товара B2',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[4].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[4].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[4].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[4].after,
                'status': calculation_of_amount_of_export_customs_duty.iloc[4].status
            },
            {
                'id': '12',
                'title': 'Ставка вывозной пошлины товара B2',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[5].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[5].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[5].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[5].after,
                'status': calculation_of_amount_of_export_customs_duty.iloc[5].status
            },
            {
                'id': '13',
                'title': 'Вывозная таможенная пошлина на товар B2',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[6].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[6].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[6].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[6].after
            },
            {
                'id': '14',
                'title': 'Адвалорная ставка пошлины на товар B2',
                'measure': calculation_of_amount_of_export_customs_duty.iloc[7].measure,
                'params': calculation_of_amount_of_export_customs_duty.iloc[7].designation,
                'before': calculation_of_amount_of_export_customs_duty.iloc[7].before,
                'after': calculation_of_amount_of_export_customs_duty.iloc[7].after
            },
            {
                'id': '15',
                'title': 'Внутренняя цена товара B1',
                'measure': domestic_market_of_group_b_products.iloc[0].measure,
                'params': domestic_market_of_group_b_products.iloc[0].designation,
                'before': domestic_market_of_group_b_products.iloc[0].before,
                'after': domestic_market_of_group_b_products.iloc[0].after
            },
            {
                'id': '16',
                'title': 'Внутренняя цена товара B2',
                'measure': domestic_market_of_group_b_products.iloc[1].measure,
                'params': domestic_market_of_group_b_products.iloc[1].designation,
                'before': domestic_market_of_group_b_products.iloc[1].before,
                'after': domestic_market_of_group_b_products.iloc[1].after
            },
            {
                'id': '17',
                'title': 'Стоимость продуктов переработки 1 единицы товара А',
                'measure': internal_market_of_product_a.iloc[0].measure,
                'params': internal_market_of_product_a.iloc[0].designation,
                'before': internal_market_of_product_a.iloc[0].before,
                'after': internal_market_of_product_a.iloc[0].after
            },
            {
                'id': '18',
                'title': 'Стоимость переработки 1 единицы товара А',
                'measure': internal_market_of_product_a.iloc[1].measure,
                'params': internal_market_of_product_a.iloc[1].designation,
                'before': internal_market_of_product_a.iloc[1].before,
                'after': internal_market_of_product_a.iloc[1].after
            },
            {
                'id': '19',
                'title': 'Внутренняя цена товара А',
                'measure': internal_market_of_product_a.iloc[2].measure,
                'params': internal_market_of_product_a.iloc[2].designation,
                'before': internal_market_of_product_a.iloc[2].before,
                'after': internal_market_of_product_a.iloc[2].after
            },
            {
                'id': '20',
                'title': 'Объем внутреннего производства товара А',
                'measure': internal_production_and_balance_of_goods_a.iloc[0].measure,
                'params': internal_production_and_balance_of_goods_a.iloc[0].designation,
                'before': internal_production_and_balance_of_goods_a.iloc[0].before,
                'after': internal_production_and_balance_of_goods_a.iloc[0].after
            },
            {
                'id': '21',
                'title': 'Экспорт товара А (экзогенно)',
                'measure': internal_production_and_balance_of_goods_a.iloc[1].measure,
                'params': internal_production_and_balance_of_goods_a.iloc[1].designation,
                'before': internal_production_and_balance_of_goods_a.iloc[1].before,
                'after': internal_production_and_balance_of_goods_a.iloc[1].after
            },
            {
                'id': '22',
                'title': 'Индекс превышения затрат на производство над ценами',
                'measure': internal_production_and_balance_of_goods_a.iloc[2].measure,
                'params': internal_production_and_balance_of_goods_a.iloc[2].designation,
                'before': internal_production_and_balance_of_goods_a.iloc[2].before,
                'after': internal_production_and_balance_of_goods_a.iloc[2].after,
                'status': internal_production_and_balance_of_goods_a.iloc[2].status
            },
            {
                'id': '23',
                'title': 'Экзогенный сдвиг во внутреннем предложении товара А',
                'measure': internal_production_and_balance_of_goods_a.iloc[3].measure,
                'params': internal_production_and_balance_of_goods_a.iloc[3].designation,
                'before': internal_production_and_balance_of_goods_a.iloc[3].before,
                'after': internal_production_and_balance_of_goods_a.iloc[3].after,
                'status': internal_production_and_balance_of_goods_a.iloc[3].status
            },
            {
                'id': '24',
                'title': 'Калибруемый вспомогательный параметр',
                'measure': internal_production_and_balance_of_goods_a.iloc[4].measure,
                'params': internal_production_and_balance_of_goods_a.iloc[4].designation,
                'before': internal_production_and_balance_of_goods_a.iloc[4].before,
                'after': internal_production_and_balance_of_goods_a.iloc[4].after
            },
            {
                'id': '25',
                'title': 'Внутренняя цена товара С',
                'measure': internal_production_of_goods_c.iloc[0].measure,
                'params': internal_production_of_goods_c.iloc[0].designation,
                'before': internal_production_of_goods_c.iloc[0].before,
                'after': internal_production_of_goods_c.iloc[0].after
            },
            {
                'id': '26',
                'title': 'Затраты на производство и обращение товара С (без учета стоимости В)',
                'measure': internal_production_of_goods_c.iloc[1].measure,
                'params': internal_production_of_goods_c.iloc[1].designation,
                'before': internal_production_of_goods_c.iloc[1].before,
                'after': internal_production_of_goods_c.iloc[1].after
            },
            {
                'id': '27',
                'title': 'Внутренний спрос на товар С',
                'measure': internal_production_of_goods_c.iloc[2].measure,
                'params': internal_production_of_goods_c.iloc[2].designation,
                'before': internal_production_of_goods_c.iloc[2].before,
                'after': internal_production_of_goods_c.iloc[2].after
            },
            {
                'id': '28',
                'title': 'Калибруемый вспомогательный параметр',
                'measure': internal_production_of_goods_c.iloc[3].measure,
                'params': internal_production_of_goods_c.iloc[3].designation,
                'before': internal_production_of_goods_c.iloc[3].before,
                'after': internal_production_of_goods_c.iloc[3].after
            },
            {
                'id': '29',
                'title': 'Объем внутреннего производства товара B1',
                'measure': production_and_balance_of_group_b_goods.iloc[0].measure,
                'params': production_and_balance_of_group_b_goods.iloc[0].designation,
                'before': production_and_balance_of_group_b_goods.iloc[0].before,
                'after': production_and_balance_of_group_b_goods.iloc[0].after
            },
            {
                'id': '30',
                'title': 'Внутренний спрос на товар B1',
                'measure': production_and_balance_of_group_b_goods.iloc[1].measure,
                'params': production_and_balance_of_group_b_goods.iloc[1].designation,
                'before': production_and_balance_of_group_b_goods.iloc[1].before,
                'after': production_and_balance_of_group_b_goods.iloc[1].after
            },
            {
                'id': '31',
                'title': 'Экспорт товара B1',
                'measure': production_and_balance_of_group_b_goods.iloc[2].measure,
                'params': production_and_balance_of_group_b_goods.iloc[2].designation,
                'before': production_and_balance_of_group_b_goods.iloc[2].before,
                'after': production_and_balance_of_group_b_goods.iloc[2].after
            },
            {
                'id': '32',
                'title': 'Объем внутреннего производства товара B2',
                'measure': production_and_balance_of_group_b_goods.iloc[3].measure,
                'params': production_and_balance_of_group_b_goods.iloc[3].designation,
                'before': production_and_balance_of_group_b_goods.iloc[3].before,
                'after': production_and_balance_of_group_b_goods.iloc[3].after
            },
            {
                'id': '33',
                'title': 'Внутренний спрос на товар B2',
                'measure': production_and_balance_of_group_b_goods.iloc[4].measure,
                'params': production_and_balance_of_group_b_goods.iloc[4].designation,
                'before': production_and_balance_of_group_b_goods.iloc[4].before,
                'after': production_and_balance_of_group_b_goods.iloc[4].after
            },
            {
                'id': '34',
                'title': 'Экспорт товара B2',
                'measure': production_and_balance_of_group_b_goods.iloc[5].measure,
                'params': production_and_balance_of_group_b_goods.iloc[5].designation,
                'before': production_and_balance_of_group_b_goods.iloc[5].before,
                'after': production_and_balance_of_group_b_goods.iloc[5].after
            },

        ]
    }
    return result_to_front



input_data = InputDataBase(user_data)
x = oil_export(input_data)
pprint(x)


