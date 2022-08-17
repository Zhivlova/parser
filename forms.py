import pandas as pd

"""Руководство пользователя"""
users_guide = {'color': ['orange', 'light blue', 'white'],
               'description': ['Для проведения численного моделирования необходимо менять управляющие воздействия '
                               'модели, обозначенные оранжевым цветом.',
                               'Светло-синим цветом обозначены ячейки, в которые требуется ввести входные данные '
                               '(начальное состояние рынка)',
                               'Расчетные значения']}
df_users_guide = pd.DataFrame(data=users_guide)
print(df_users_guide)
print('------------------------------------')

"""Внешние значения"""
external_values = {'Внешние значения': ['Доля ЕС в импорте', 'Доля ЕАЭС в импорте', 'Затраты на труд (руб./кг)',
                                        'Норма прибыли в отрасли', 'Прочие затраты SVA исключая труд',
                                        'Налоговая нагрузка в отрасли бумаги и бумажных изделий', 'Налог на прибыль'],
                   '%': ["{:.13%}".format(33.3172943617359 / 100), "{:.13%}".format(62.1876218742617 / 100), 0.544,
                         'Рентабельность (Росстат)!K6/100', 'SVA_0- N4', 'Налоговая нагрузка (ФНС)!B19/100',
                         "{:.2%}".format(0.2 / 100)]}

df_external_values = pd.DataFrame(data=external_values)
print(df_external_values)

"""Управляющие воздействия модели"""

control_actions_of_the_model = \
    {'Управляющие воздействия модели': ['Курс RUB/USD',
                                        'Цена импорта товара M USD (без тарифа), долл. США за кг',
                                        'Импортный нетарифный барьер на макулатуру',
                                        'Импортный тариф на макулатуру',
                                        'Собираемость макулатуры',
                                        'Нормировочная цена для собираемости макулатуры',
                                        'Прочие переменные издержки производства макулатурного картона (руб./кг)',
                                        'Выход продукции из макулатуры',
                                        'Доля собираемой макулатуры для производства картона',
                                        'Общее убывание волокна'
                                        ],
     'Обозначение': ['ER', 'P_MMI_USD', 'NMMI', 'TMMI', 'K', 'Λ', 'SVA', 'OUT', 'SH', ''],
     # 'Базовое равновесие': [72.14, 0.18, "{:.0%}".format(129/100), "{:.14%}".format(1.89061890628692/100), 14.686756,
     # "{:.2%}".format(85.55/100)]
     }
df = pd.DataFrame(data=control_actions_of_the_model)
print(df)

df["Базовое равновесие"] = pd.to_numeric(df["Базовое равновесие"])
df["Новое равновесие"] = pd.to_numeric(df["Новое равновесие"])

"""Налоги и благосостояние"""

taxes_and_welfare = {'Налоги и благосостояние': ['Импортный тариф', 'Производство макулатурных тарных картонов',
                                                 'Производство целлюлозных тарных картонов',
                                                 'Налог на потребителей тарных картонов (налог на прибыль)',
                                                 'Итого налоги', 'Изменение прибыли потребителей картона',
                                                 'Изменение прибыли производителей макулатурных картонов',
                                                 'Изменение прибыли производителей целлюлозных картонов',
                                                 'Изменение совокупной зарплаты сотрудников отрасли тарных картонов',
                                                 'Итого благосостояние'],
                     'Базовое рановесие (млн. руб)': ['(P_MMI_0*Q_MMI_0)*TMMI_0',
                                                      'P_SDP_0*Q_SDP_0*Tax+Lab*Q_SDP_0*47/130',
                                                      'Tax*P_FDP_0*Q_FDP_0+Lab*Q_FDP_0*47/130',
                                                      '(P_PDP_0*Q_PDP_0)*Рентабельность (ФНС) !B15/100*VAT',
                                                      'СУММ(N18:N21) pd.Series([], dtype="float64").sum()',
                                                      '(P_PDP_0*Q_PDP_0)*Рентабельность (ФНС) !B15/100*0,8',
                                                      'P_SDP_0*Q_SDP_0*profit*0,8', 'P_FDP_0*Q_FDP_0*profit*0,8',
                                                      'Q_SDP_0*Lab+Q_FDP_0*Lab',
                                                      'СУММ(N24:N27) pd.Series([], dtype="float64").sum()'],
                     'Новое равновесие (млн. руб)': ['(P_MMI_1*Q_MMI_1)*TMMI_1', 'P_SDP_1*Q_SDP_1*Tax+Lab*Q_SDP_1*47/130',
                                                     'Tax*P_FDP_1*Q_FDP_1+Lab*Q_FDP_1*47/130', 'N21+P21', 'N22+P22',
                                                     'N22+P22', 'N25+P25', 'N26+P26', 'N27+P27', 'N28+P28'],
                     }


df_taxes_and_welfare = pd.DataFrame(data=taxes_and_welfare)
print(df_taxes_and_welfare)