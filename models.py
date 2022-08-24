
"""Управляющие воздействия модели"""

class ModelControlActions:

    # def __init__(self, ER, P_MMI_USD, NMMI, TMMI, SVA, SH):
    #     # Курс RUB/USD
    #     self.ER = ER
    #     # Цена импорта товара M USD (без тарифа), долл. США за кг
    #     self.P_MMI_USD = P_MMI_USD
    #     # Импортный нетарифный барьер на товар M
    #     self.NMMI = NMMI
    #     # Импортный тариф на товар M
    #     self.TMMI = TMMI
    #     # Прочие переменные издержки производства макулатурного картона (руб./кг)
    #     self.SVA = SVA
    #     # Доля собираемой макулатуры для производства картона
    #     self.SH = SH

    """Курс RUB/USD"""

    # Базовое равновесие
    ER_0 = 72.14
    # Новое равновесие Курс RUB/USD
    def ER_1(self, ER_0):
        ER_1 = ER_0 * 1.2
        return ER_1


    # """Цена импорта товара M USD (без тарифа), долл. США за кг"""
    #
    # # Базовое равновесие
    # P_MMI_USD_0 = 0.18
    # # Новое равновесие
    #
    """Импортный нетарифный барьер на товар M"""

    # Базовое равновесие
    NMMI_0 = 0
    # Новое равновесие
    NMMI_1 = 0




    """Импортный тариф на товар M"""

    # Базовое равновесие
    TMMI_0 = "{:.14%}".format(1.89061890628692 / 100)
    # Новое равновесие
    def import_tariff(self):
        TMMI_1 = "{:.0%}".format(0 / 100)
        return TMMI_1

table = ModelControlActions()

    # """Собираемость макулатуры"""
    #
    # # Базовое равновесие
    # def basic_waste_paper_collection(self, Q_MDI_0, Q_PDC_0):
    #     K_0 = Q_MDI_0 / Q_PDC_0
    #     return K_0
    # # Новое равновесие
    # def new_waste_paper_collection(self, -P_MDI_1, Λ_1):
    #     K_1 = (1 - EXP(-P_MDI_1 / Λ_1))
    #     return K_1

    # """Нормировочная цена для собираемости макулатуры"""
    #
    # # Базовое равновесие
    # def basic_rationing_price(self, -P_MDI_0, K_0):
    #     Λ_0 = -P_MDI_0 / LN(1 - K_0)
    #     return Λ_0
    # # Новое равновесие
    # def new_rationing_price(self, Λ_0):
    #     Λ_1 = Λ_0
    #     return Λ_1
    #
    # """Прочие переменные издержки производства макулатурного картона (руб./кг)"""
    #
    # # Базовое равновесие
    # SVA_0 = 14.686756
    # # Новое равновесие
    # def SVA_1(self,SVA_0):
    #     SVA_1 = SVA_0
    #     return SVA_1
    #
    # """Выход продукции из макулатуры"""
    #
    # # Базовое равновесие
    # def basic_output_of_waste(self, Q_SDP_0, Q_MIC_0, SH_0):
    #     OUT_0 = Q_SDP_0 / (Q_MIC_0 * SH_0)
    #     return OUT_0
    # # Новое равновесие
    # def new_output_of_waste(self, OUT_0):
    #     OUT_1 = OUT_0
    #     return OUT_1
    #
    # """Доля собираемой макулатуры для производства картона"""
    #
    # # Базовое равновесие
    # SH_0 = "{:.2%}".format(85.55 / 100)
    # # Новое равновесие
    # def new_share_of_waste(self, SH_0):
    #     SH_1 = SH_0
    #     return SH_1
    #
    # """Общее убывание волокна"""
    #
    # # Базовое равновесие
    # def basic_total_fiber_decrease(self, K_0, OUT_0, SH_0):
    #     return K_0*OUT_0*SH_0
    # # Новое равновесие
    # def new_total_fiber_decrease(self, K_1, OUT_1, SH_1):
    #     return K_1*OUT_1*SH_1



# if __name__ == "__main__":
#     calculation = ModelControlActions(72.14, 0.18, "{:.0%}".format(129/100), "{:.14%}".format(1.89061890628692/100),
#                                       14.686756, "{:.2%}".format(85.55/100))
#     print(calculation.basic_total_fiber_decrease())




#
# """Поведенческие параметры"""
# class Behavioral_parameters:
#     σ_MIC = 2.5
#     σ_PDP = 2.25
#     Ω_FDP = 2.95  # комментарий разработчиков GTAP
#     ε_MMI = 10
#     ε_FDP = 0.3
#     ε_PDP = 'Эластичность спроса!C11'
#     ε_PXM = 1
#     ε_FXP = -10
#
#     def rho_r_σ_MIC(self, σ_MIC):
#         r_σ_MIC = (σ_MIC-1)/σ_MIC
#         return r_σ_MIC
#
#     def rho_r_σ_PDP(self, σ_PDP):
#         r_σ_PDP = (σ_PDP-1)/σ_PDP
#         return r_σ_PDP
#
#     def rho_r_Ω_FDP(self, Ω_FDP):
#         r_Ω_FDP = (Ω_FDP+1)/Ω_FDP
#         return r_Ω_FDP
#
#     def SS_DS_Z_MMI(self, Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI):
#         Z_MMI = Q_MMI_0/((P_MMI_0/(ER_0*(1+TMMI_0)*(1+NMMI_0)))^ε_MMI)
#         return Z_MMI
#
#     def SS_DS_Z_FDP(self, Q_FDP_0, P_FDP_0, ε_FDP):
#         Z_FDP = Q_FDP_0/(P_FDP_0)^ε_FDP
#         return Z_FDP
#
#     def SS_DS_Z_PDP(self, Q_PDP_0, P_PDP_0, ε_PDP):
#         Z_PDP = Q_PDP_0/(P_PDP_0)^ε_PDP
#         return Z_PDP
#
#     def SS_DS_Z_PXM(self, Q_PXM_0, ER_0, ε_PXM):
#         Z_PXM = Q_PXM_0/(1/ER_0)^ε_PXM
#         return Z_PXM
#
#     def SS_DS_Z_FXP(self, Q_FXP_0, P_FXP_0, ER_0, ε_FXP):
#         Z_FXP = Q_FXP_0/(P_FXP_0/ER_0)^ε_FXP
#         return Z_FXP
#
#
# """Налоги и благосостояние"""
# class Taxes_welfare:
#
#     """Импортный тариф"""
#
#     # Базовое рановесие
#     def base_import_tariff(self, P_MMI_0, Q_MMI_0, TMMI_0):
#         base_import_tariff = (P_MMI_0*Q_MMI_0)*TMMI_0
#         return base_import_tariff
#     # Новое равновесие
#     def new_import_tariff(self, P_MMI_1, Q_MMI_1, TMMI_1):
#         new_import_tariff = (P_MMI_1*Q_MMI_1)*TMMI_1
#         return new_import_tariff
#     # Изменение млн. руб
#     def change_import_tariff(self, new_import_tariff, base_import_tariff):
#         change_import_tariff = new_import_tariff - base_import_tariff
#         return  change_import_tariff
#     # Изменение % к начальному
#     def change_pr_import_tariff(self, new_import_tariff, base_import_tariff):
#         return  new_import_tariff / base_import_tariff - 1
#
#     """Производство макулатурных тарных картонов"""
#
#     # Базовое рановесие
#     def base_production_wastepaper(self, P_SDP_0, Q_SDP_0, Tax, Lab, Q_SDP_0):
#         base_production_wastepaper = P_SDP_0*Q_SDP_0*Tax+Lab*Q_SDP_0*47/130
#         return base_production_wastepaper
#     # Новое равновесие
#     def new_production_wastepaper(self, P_SDP_1, Q_SDP_1, Tax, Lab, Q_SDP_1):
#         new_production_wastepaper = P_SDP_1*Q_SDP_1*Tax+Lab*Q_SDP_1*47/130
#         return new_production_wastepaper
#     # Изменение млн. руб
#     def change_production_wastepaper(self, base_production_wastepaper, new_production_wastepaper):
#         return new_production_wastepaper - base_production_wastepaper
#     # Изменение % к начальному
#     def change_pr_production_wastepaper(self,  new_production_wastepaper, base_production_wastepaper):
#         return new_production_wastepaper / base_production_wastepaper - 1
#
#     """Производство целлюлозных тарных картонов"""
#
#     # Базовое рановесие
#     def base_production_cellulose(self, Tax, P_FDP_0, Q_FDP_0, Lab, Q_FDP_0):
#         base_production_cellulose = Tax*P_FDP_0*Q_FDP_0+Lab*Q_FDP_0*47/130
#         return base_production_cellulose
#     # Новое равновесие
#     def new_production_cellulose(self, Tax, P_FDP_1, Q_FDP_1, Lab, Q_FDP_1):
#         new_production_cellulose = Tax*P_FDP_1*Q_FDP_1+Lab*Q_FDP_1*47/130
#         return new_production_cellulose
#     # Изменение млн. руб
#     def change_production_cellulose(self, new_production_cellulose, base_production_cellulose):
#         return new_production_cellulose - base_production_cellulose
#     # Изменение % к начальному
#     def change_pr_production_cellulose(self,  new_production_cellulose, base_production_cellulose):
#         return new_production_cellulose / base_production_cellulose - 1
#
#     """Налог на потребителей тарных картонов (налог на прибыль)"""
#
#     # Базовое рановесие
#     def base_tax_consumers(self,P_PDP_0, Q_PDP_0, 'Рентабельность (ФНС) !B15', VAT):
#         base_tax_consumers = (P_PDP_0*Q_PDP_0)*'Рентабельность (ФНС) !B15'/100*VAT
#         return base_tax_consumers
#     # Новое равновесие
#     def new_tax_consumers(self, base_tax_consumers, change_tax_consumers):
#         new_tax_consumers = base_tax_consumers + change_tax_consumers
#         return new_tax_consumers
#     # Изменение млн. руб
#     def change_tax_consumers(self, P_PDP_0, P_PDP_1,Q_PDP_1, Q_PDP_0):
#         change_tax_consumers =  ((P_PDP_0-P_PDP_1)*(Q_PDP_1+Q_PDP_0)/2)*0,2
#         return change_tax_consumers
#     # Изменение % к начальному
#     def change_pr_tax_consumers(self, change_tax_consumers, base_tax_consumers):
#         return change_tax_consumers / base_tax_consumers
#
#     """Итого налоги"""
#
#     # Базовое рановесие
#     def base_total_taxes(self, base_import_tariff, base_production_wastepaper, base_production_cellulose, base_tax_consumers):
#         base_total_taxes = base_import_tariff + base_production_wastepaper + base_production_cellulose + base_tax_consumers
#         return base_total_taxes
#     # Новое равновесие
#     def new_total_taxes(self, base_total_taxes, change_tax_consumers):
#         return base_total_taxes + change_tax_consumers
#     # Изменение млн. руб
#     def change_total_taxes(self, change_import_tariff,change_production_wastepaper, change_production_cellulose, change_tax_consumers):
#         change_total_taxes = change_import_tariff + change_production_wastepaper + change_production_cellulose + change_tax_consumers
#         return change_total_taxes
#     # Изменение % к начальному
#     def change_pr_total_taxes(self, change_total_taxes, base_total_taxes):
#         return change_total_taxes / base_total_taxes
#
#     """Изменение прибыли потребителей картона"""
#
#     # Базовое рановесие
#     def base_change_profit_consumers(self, P_PDP_0, Q_PDP_0, 'Рентабельность (ФНС) !B15'):
#         base_change_profit_consumers = (P_PDP_0 * Q_PDP_0) * 'Рентабельность (ФНС) !B15' / 100 * 0, 8
#         return base_change_profit_consumers
#     # Новое равновесие
#     def new_change_profit_consumers(self, base_change_profit_consumers, ch_change_profit_consumers):
#         new_change_profit_consumers = base_change_profit_consumers + ch_change_profit_consumers
#         return new_change_profit_consumers
#     # Изменение млн. руб
#     def ch_change_profit_consumers(self, P_PDP_0, P_PDP_1, Q_PDP_1, Q_PDP_0):
#         ch_change_profit_consumers = ((P_PDP_0-P_PDP_1)*(Q_PDP_1+Q_PDP_0)/2)*0,8
#         return ch_change_profit_consumers
#     # Изменение % к начальному
#     def ch_pr_change_profit_consumers(self, ch_change_profit_consumers, base_change_profit_consumers):
#         ch_pr_change_profit_consumers = ch_change_profit_consumers / base_change_profit_consumers
#         return ch_pr_change_profit_consumers
#
#     """Изменение прибыли производителей макулатурных картонов"""
#
#     # Базовое рановесие
#     def base_change_profit_manufacturers(self, P_SDP_0, Q_SDP_0, profit):
#         base_change_profit_manufacturers = P_SDP_0*Q_SDP_0*profit*0,8
#         return base_change_profit_manufacturers
#     # Новое равновесие
#     def new_change_profit_manufacturers(self, base_change_profit_manufacturers, ch_change_profit_manufacturers):
#         new_change_profit_manufacturers = base_change_profit_manufacturers + ch_change_profit_manufacturers
#         return new_change_profit_manufacturers
#     # Изменение млн. руб
#     def ch_change_profit_manufacturers(self,P_SDP_1, Q_SDP_1, P_SDP_0, Q_SDP_0, profit)
#         ch_change_profit_manufacturers = (P_SDP_1*Q_SDP_1-P_SDP_0*Q_SDP_0)*profit*0,8
#         return ch_change_profit_manufacturers
#     # Изменение % к начальному
#     def ch_pr_change_profit_manufacturers(self, ch_change_profit_manufacturers, base_change_profit_manufacturers):
#         ch_pr_change_profit_manufacturers = ch_change_profit_manufacturers / base_change_profit_manufacturers
#         return ch_pr_change_profit_manufacturers
#
#     """Изменение прибыли производителей целлюлозных картонов"""
#
#     # Базовое рановесие
#     def base_change_profit_cellulose_manufacturers(self,P_FDP_0, Q_FDP_0, profit):
#         base_change_profit_cellulose_manufacturers = P_FDP_0*Q_FDP_0*profit*0,8
#         return base_change_profit_cellulose_manufacturers
#     # Новое равновесие
#     def new_change_profit_cellulose_manufacturers(self, base_change_profit_cellulose_manufacturers, ch_change_profit_cellulose_manufacturers):
#         new_change_profit_cellulose_manufacturers = base_change_profit_cellulose_manufacturers + ch_change_profit_cellulose_manufacturers
#         return new_change_profit_cellulose_manufacturers
#     # Изменение млн. руб
#     def ch_change_profit_cellulose_manufacturers(self, P_FDP_1, Q_FDP_1, P_FDP_0, Q_FDP_0, profit):
#         ch_change_profit_cellulose_manufacturers = (P_FDP_1*Q_FDP_1-P_FDP_0*Q_FDP_0)*profit*0,8
#         return ch_change_profit_cellulose_manufacturers
#     # Изменение % к начальному
#     def ch_pr_change_profit_cellulose_manufacturers(self, ch_change_profit_cellulose_manufacturers, base_change_profit_cellulose_manufacturers):
#         ch_pr_change_profit_cellulose_manufacturers = ch_change_profit_cellulose_manufacturers / base_change_profit_cellulose_manufacturers
#         return ch_pr_change_profit_cellulose_manufacturers
#
#     """Изменение совокупной зарплаты сотрудников отрасли тарных картонов"""
#
#     # Базовое рановесие
#     def base_change_salary_employees(self, Q_SDP_0, Lab, Q_FDP_0):
#         base_change_salary_employees = Q_SDP_0*Lab+Q_FDP_0*Lab
#         return base_change_salary_employees
#     # Новое равновесие
#     def new_change_salary_employees(self, base_change_salary_employees, ch_change_salary_employees):
#         new_change_salary_employees = base_change_salary_employees + ch_change_salary_employees
#         return new_change_salary_employees
#     # Изменение млн. руб
#     def ch_change_salary_employees(self, Q_SDP_1, Q_SDP_0, Lab, Q_FDP_1, Q_FDP_0):
#         ch_change_salary_employees = (Q_SDP_1-Q_SDP_0)*Lab+(Q_FDP_1-Q_FDP_0)*Lab
#         return ch_change_salary_employees
#     # Изменение % к начальному
#     def ch_pr_change_salary_employees(self, ch_change_salary_employees, base_change_salary_employees):
#         ch_pr_change_salary_employees = ch_change_salary_employees / base_change_salary_employees
#         return ch_pr_change_salary_employees
#
#     """Итого благосостояние"""
#
#     # Базовое рановесие
#     def base_total_wealth(self, base_change_profit_consumers, base_change_profit_manufacturers,
#                           base_change_profit_cellulose_manufacturers, base_change_salary_employees):
#         base_total_wealth = base_change_profit_consumers + base_change_profit_manufacturers + \
#                             base_change_profit_cellulose_manufacturers + base_change_salary_employees
#         return base_total_wealth
#     # Новое равновесие
#     def new_total_wealth(self, base_total_wealth, change_total_wealth):
#         new_total_wealth = base_total_wealth + change_total_wealth
#         return new_total_wealth
#     # Изменение млн. руб
#     def change_total_wealth(self, ch_change_profit_consumers, ch_change_profit_manufacturers,
#                             ch_change_profit_cellulose_manufacturers, ch_change_salary_employees):
#         change_total_wealth = ch_change_profit_consumers + ch_change_profit_manufacturers + \
#                               ch_change_profit_cellulose_manufacturers + ch_change_salary_employees
#         return change_total_wealth
#     # Изменение % к начальному
#     def change_pr_total_wealth(self, change_total_wealth, base_total_wealth):
#         change_pr_total_wealth = change_total_wealth / base_total_wealth
#         return change_pr_total_wealth


"""Переменные"""

class Variable:
    # def __init__(self, MDI, FDP, FXP):
    #     # Потребление отечественной макулатуры
    #     self.MDI = MDI
    #     # Отечественное производство товара F
    #     self.FDP = FDP
    #     # Экспорт товара F
    #     self.FXP = FXP

#     """Импорт товара M"""
#
#     # Базовое равновесие Цена (P), руб за кг
#     def good_import(self,P_MMI_USD_0, ER_0,TMMI_0):
#         P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
#         return P_MMI_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_MMI_0 = 42
#
#     # Новое равновесие Цена (P), руб за кг
#     P_MMI_1 = 7.80922017051985
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_MMI_1 = 166.487602924277
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_good_import(self, P_MMI_1, P_MMI_0):
#         return P_MMI_1/P_MMI_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_good_import(self, Q_MMI_1, Q_MMI_0)
#         return Q_MMI_1/Q_MMI_0-1
#
    """Потребление отечественного товара M"""

    # Базовое равновесие
    P_MDI_0 = 15.139
    # Базовое равновесие Количество (Q) тыс. тонн
    def q_consumption_home_goods(self):
        Q_MDI_0 = 3876-54
        return Q_MDI_0
#
#     # Новое равновесие
#     P_MDI_1 = 15.6016971682569
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_MDI_1 = 3760.9600057833
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_consumption_home_goods(self, P_MDI_1, P_MDI_0):
#         return P_MDI_1/P_MDI_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_good_import_consumption_home_goods(self, Q_MDI_1, Q_MDI_0):
#         return Q_MDI_1/Q_MDI_0-1
#
#     """Потребление отраслью S товара M"""
#
#     # Базовое равновесие
#     def good_consumption(self, P_MDI_0,Q_MDI_0, P_MMI_0, Q_MMI_0,Q_MIC_0):
#         P_MIC_0 = (P_MDI_0*Q_MDI_0+P_MMI_0*Q_MMI_0)/Q_MIC_0
#         return P_MIC_0
#     # Базовое равновесие Количество (Q) тыс. тонн
#     def q_good_consumption(self, Q_MDI_0, Q_MMI_0):
#         Q_MIC_0 = Q_MDI_0+Q_MMI_0
#         return Q_MIC_0
#
#     # Новое равновесие
#     P_MIC_1 = 15.2713679199154
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_MIC_1 = 3927.44760870758
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_good_consumption(self, P_MIC_1, P_MIC_0):
#         return P_MIC_1/P_MIC_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_good_consumption(self, Q_MIC_1, Q_MIC_0)
#         return Q_MIC_1/Q_MIC_0-1
#
    # """Отечественное производство S"""
    #
    # # Базовое равновесие
    # def home_production(self, P_MIC_0, OUT_0, SVA_0):
    #     P_SDP_0 = P_MIC_0/OUT_0+SVA_0
    #     return P_SDP_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_SDP_0 = 2999
#
#     # Новое равновесие Цена (P), руб за кг
#     P_SDP_1 = 31.5196429313786
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_SDP_1 = 3048,24414557817
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_home_production(self, P_SDP_1, P_SDP_0):
#         return P_SDP_1/P_SDP_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_home_production(self, Q_SDP_1, Q_SDP_0)
#         return Q_SDP_1/Q_SDP_0-1
#
#     """Отечественное потребление F"""
#
#     # Базовое равновесие
#     def home_consumption_f(self, P_FDP_0, Q_FDP_0, P_FXP_0, Q_FXP_0, Q_FDC_0):
#         P_FDC_0 = (P_FDP_0*Q_FDP_0-P_FXP_0*Q_FXP_0)/Q_FDC_0
#         return P_FDC_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_FDC_0 = 1006
#
#     # Новое равновесие Цена (P), руб за кг
#     P_FDC_1 = 35.8411597582987
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_FDC_1 = 892.04380089303
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_home_consumption_f(self, P_FDC_1, P_FDC_0):
#         return P_FDC_1/P_FDC_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_home_consumption_f(self, Q_FDC_1, Q_FDC_0)
#         return Q_FDC_1/Q_FDC_0-1
#
#     """Отечественное потребление P"""
#
#     # Базовое равновесие Цена (P), руб за кг
#     def home_consumption_p(self, P_SDP_0, Q_SDP_0, P_FDC_0, Q_FDC_0, Q_PDP_0):
#         P_PDP_0 = (P_SDP_0*Q_SDP_0+P_FDC_0*Q_FDC_0)/Q_PDP_0
#         return P_PDP_0
#     # Базовое равновесие Количество (Q) тыс. тонн
#     def q_home_consumption_p(self, Q_SDP_0, Q_FDC_0):
#         Q_PDP_0 = Q_SDP_0+Q_FDC_0
#         return Q_PDP_0
#
#     # Новое равновесие Цена (P), руб за кг
#     P_PDP_1 = 32.4979933332257
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_PDP_1 = 3940.2879464712
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_home_consumption_p(self, P_PDP_1,P_PDP_0):
#         return P_PDP_1/P_PDP_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_home_consumption_p(self, Q_PDP_1, Q_PDP_0)
#         return Q_PDP_1/Q_PDP_0-1
#
#
#     """Нетто импорт P"""
#
#     # Базовое равновесие Цена (P), руб за кг
#     def netto_import(self, P_MDI_0):
#         P_PXM_0 = P_MDI_0
#         return P_PXM_0
#     # Базовое равновесие Количество (Q) тыс. тонн
#     def q_netto_import(self, Q_PDC_0, Q_PDP_0):
#         Q_PXM_0 = Q_PDC_0-Q_PDP_0
#         return Q_PXM_0
#
#     # Новое равновесие Цена (P), руб за кг
#     P_PXM_1 = 15.6016971682569
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_PXM_1 = 150.833333333333
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_netto_import(self, P_PXM_1, P_PXM_0):
#         return P_PXM_1/P_PXM_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_netto_import(self, Q_PXM_1, Q_PXM_0)
#         return Q_PXM_1/Q_PXM_0-1
#
#     """Общее образование P"""
#
#     # Базовое равновесие Цена (P), руб за кг
#     def general_education(self, P_MDI_0):
#         P_PDC_0 = P_MDI_0
#         return P_PDC_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_PDC_0 = 4186
#
#     # Новое равновесие Цена (P), руб за кг
#     P_PDC_1 = 15.6016971682569
#     # Новое равновесие Количество (Q) тыс. тонн
#     Q_PDC_1 = 4091.12127980453
#
#     # Изменение (%) Цена (P)
#     def perc_change_price_general_education(self, P_PDC_1, P_PDC_0):
#         return P_PDC_1/P_PDC_0-1
#     # Изменение (%) Количество (Q)
#     def perc_change_quantity_general_education(self, Q_PDC_1, Q_PDC_0)
#         return Q_PDC_1/Q_PDC_0-1
#
    """Отечественное производство товара F"""

    # Базовое равновесие Цена (P), руб за кг
    P_FDP_0 = 38
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_FDP_0 = 2125

    # # Новое равновесие Цена (P), руб за кг
    # P_FDP_1 = 44.03846291456
    # # Новое равновесие Количество (Q) тыс. тонн
    # Q_FDP_1 = 2221,1275608247
    #
    # # Изменение (%) Цена (P)
    # def perc_change_price_home_production(self, P_FDP_1, P_FDP_0):
    #     return P_FDP_1/P_FDP_0-1
    # # Изменение (%) Количество (Q)
    # def perc_change_quantity_home_production(self, Q_FDP_1, Q_FDP_0)
    #     return Q_FDP_1/Q_FDP_0-1
#
    """Экспорт товара F"""

    # Базовое равновесие Цена (P), руб за кг
    P_FXP_0 = 42
    # Базовое равновесие Количество (Q) тыс. тонн
    def export_goods(self, Q_FDP_0, Q_FDC_0):
        Q_FXP_0 = Q_FDP_0-Q_FDC_0
        return Q_FXP_0

    # # Новое равновесие Цена (P), руб за кг
    # P_FXP_1 = 49.5402632412323
    # # Новое равновесие Количество (Q) тыс. тонн
    # Q_FXP_1 = 1329.08375993167
    #
    # # Изменение (%) Цена (P)
    # def perc_change_price_export_goodsself (self, P_FXP_1, P_FXP_0):
    #     return P_FXP_1/P_FXP_0-1
    # # Изменение (%) Количество (Q)
    # def perc_change_quantity_export_goods(self, Q_FXP_1, Q_FXP_0)
    #     return Q_FXP_1/Q_FXP_0-1
#
#
# """Уравнения"""
#
# class Equations:
#     MMI_SUPPLY = Q_MMI_1-Z_MMI*(P_MMI_1/((1+NMMI_1)*(1+TMMI_1)*ER_1))^ε_MMI
#     MIC_BUD_CES = P_MIC_1*Q_MIC_1-P_MDI_1*Q_MDI_1-P_MMI_1*Q_MMI_1
#     MIC_CES = Q_MMI_1/Q_MDI_1-((P_MMI_1/(P_MDI_1))*(K_MDI/K_MMI))^(1/(r_σ_MIC-1))
#     MIC_BAL_CES = =Q_MIC_1-Q_MDI_1-Q_MMI_1
#     SDP_P = P_SDP_1 - P_MIC_1 / OUT_1 - SVA_1
#     SDP_Q = Q_SDP_1 - Q_MIC_1 * OUT_1 * SH_1
#     FDP_SUPPLY  = Q_FDP_1 - Z_FDP * (P_FDP_1) ^ ε_FDP
#     FDP_BUD_CET = P_FDP_1 * Q_FDP_1 - P_FDC_1 * Q_FDC_1 - P_FXP_1 * Q_FXP_1
#     FDP_CET = Q_FXP_1 / Q_FDC_1 - ((P_FXP_1 / (P_FDC_1)) * (K_FDC / K_FXP)) ^ (1 / (r_Ω_FDP - 1))
#     FDP_BAL_CET = Q_FDP_1 - Q_FDC_1 - Q_FXP_1
#     FXP_DEMAND = Q_FXP_1 - Z_FXP * (P_FXP_1 / ER_1) ^ ε_FXP
#     PDP_BUD_CES  = P_PDP_1 * Q_PDP_1 - P_SDP_1 * Q_SDP_1 - P_FDC_1 * Q_FDC_1
#     PDP_CES = Q_SDP_1 / Q_FDC_1 - ((P_SDP_1 / (P_FDC_1)) * (K_FDC / K_SDP)) ^ (1 / (r_σ_PDP - 1))
#     PDP_BAL_CES = Q_PDP_1 - Q_SDP_1 - Q_FDC_1
#     PDP_DEMAND = Q_PDP_1 - Z_PDP * (P_PDP_1) ^ ε_PDP
#     PXM_SUPPLY = Q_PXM_1 - Z_PXM * (1 / ER_1) ^ ε_PXM
#     PDC_BAL = Q_PDC_1 - Q_PXM_1 - Q_PDP_1
#     PDC_P = P_PDC_1 - P_MDI_1
#     MDI_BAL = Q_MDI_1 - Q_PDC_1 * (1 - EXP(-P_MDI_1 / Λ_1))
#     PXM_P = P_PXM_1 - P_MDI_1
#
# """Внешние значения"""
#
# class External_values:
#     # Доля ЕС в импорте
#     def EU_share_of_imports(self):
#         EU =  "{:.13%}".format(33.3172943617359/100)
#         return EU
#     # Доля ЕАЭС в импорте
#     def share_of_EAEU_in_imports(self):
#         EAEU = "{:.13%}".format(62.1876218742617/100)
#         return EAEU
#     # Затраты на труд (руб./кг)
#     Lab = 0.544
#     # Норма прибыли в отрасли
#     def rate_of_profit(self):
#         profit = 'Рентабельность (Росстат)!K6/100'
#         return profit
#     # Прочие затраты SVA исключая труд
#     def other_SVA_costs_ex_labor(self, SVA_0, N4):
#         NoL = SVA_0- N4
#         return NoL
#     # Налоговая нагрузка в отрасли бумаги и бумажных изделий
#     def tax_burden(self):
#         Tax = 'Налоговая нагрузка (ФНС)!B19/100'
#         return Tax
#     # Налог на прибыль
#     def income_tax(self):
#         VAT = "{:.0%}".format(20/100)
#         return VAT


