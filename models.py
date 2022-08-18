import pandas as pd

"""Управляющие воздействия модели"""

class ModelControlActions:

    def __init__(self, ER, P_MMI_USD, NMMI, TMMI, SVA, SH):
        # Курс RUB/USD
        self.ER = ER
        # Цена импорта товара M USD (без тарифа), долл. США за кг
        self.P_MMI_USD = P_MMI_USD
        # Импортный нетарифный барьер на товар M
        self.NMMI = NMMI
        # Импортный тариф на товар M
        self.TMMI = TMMI
        # Прочие переменные издержки производства макулатурного картона (руб./кг)
        self.SVA = SVA
        # Доля собираемой макулатуры для производства картона
        self.SH = SH

    """Курс RUB/USD"""

    # Базовое равновесие
    ER_0 = 72.14
    # Новое равновесие Курс RUB/USD
    def course(self, ER_0):
        ER_1 = ER_0 * 1.2
        return ER_1

    """Цена импорта товара M USD (без тарифа), долл. США за кг"""

    # Базовое равновесие
    P_MMI_USD_0 = 0.18

    """Импортный нетарифный барьер на товар M"""

    # Базовое равновесие
    NMMI_0 = "{:.0%}".format(129 / 100)
    # Новое равновесие
    def import_non_tariff_barrier(self):
        NMMI_1 = "{:.0%}".format(0 / 100)
        return NMMI_1

    """Импортный тариф на товар M"""

    # Базовое равновесие
    TMMI_0 = "{:.14%}".format(1.89061890628692 / 100)
    # Новое равновесие
    def import_tariff(self):
        TMMI_1 = "{:.0%}".format(0 / 100)
        return TMMI_1

    """Собираемость макулатуры"""

    # Базовое равновесие
    def basic_waste_paper_collection(self, Q_MDI_0, Q_PDC_0):
        K_0 = Q_MDI_0 / Q_PDC_0
        return K_0
    # Новое равновесие
    def new_waste_paper_collection(self, -P_MDI_1, Λ_1):
        K_1 = (1 - EXP(-P_MDI_1 / Λ_1))
        return K_1

    """Нормировочная цена для собираемости макулатуры"""

    # Базовое равновесие
    def basic_rationing_price(self, -P_MDI_0, K_0):
        Λ_0 = -P_MDI_0 / LN(1 - K_0)
        return Λ_0
    # Новое равновесие
    def new_rationing_price(self, Λ_0):
        Λ_1 = Λ_0
        return Λ_1

    """Прочие переменные издержки производства макулатурного картона (руб./кг)"""

    # Базовое равновесие
    SVA_0 = 14.686756
    # Новое равновесие
    def SVA_1(self,SVA_0):
        SVA_1 = SVA_0
        return SVA_1

    """Выход продукции из макулатуры"""

    # Базовое равновесие
    def basic_output_of_waste(self, Q_SDP_0, Q_MIC_0, SH_0):
        OUT_0 = Q_SDP_0 / (Q_MIC_0 * SH_0)
        return OUT_0
    # Новое равновесие
    def new_output_of_waste(self, OUT_0):
        OUT_1 = OUT_0
        return OUT_1

    """Доля собираемой макулатуры для производства картона"""

    # Базовое равновесие
    SH_0 = "{:.2%}".format(85.55 / 100)
    # Новое равновесие
    def new_share_of_waste(self, SH_0):
        SH_1 = SH_0
        return SH_1

    """Общее убывание волокна"""

    # Базовое равновесие
    def basic_total_fiber_decrease(self, K_0, OUT_0, SH_0):
        return K_0*OUT_0*SH_0
    # Новое равновесие
    def new_total_fiber_decrease(self, K_1, OUT_1, SH_1):
        return K_1*OUT_1*SH_1



if __name__ == "__main__":
    calculation = ModelControlActions(72.14, 0.18, "{:.0%}".format(129/100), "{:.14%}".format(1.89061890628692/100),
                                      14.686756, "{:.2%}".format(85.55/100))
    print(calculation.basic_total_fiber_decrease())





"""Поведенческие параметры"""
class Behavioral_parameters:
    σ_MIC = 2.5
    σ_PDP = 2.25
    Ω_FDP = 2.95  # комментарий разработчиков GTAP
    ε_MMI = 10
    ε_FDP = 0.3
    ε_PDP = 'Эластичность спроса!C11'
    ε_PXM = 1
    ε_FXP = -10

    def rho_r_σ_MIC(self, σ_MIC):
        r_σ_MIC = (σ_MIC-1)/σ_MIC
        return r_σ_MIC

    def rho_r_σ_PDP(self, σ_PDP):
        r_σ_PDP = (σ_PDP-1)/σ_PDP
        return r_σ_PDP

    def rho_r_Ω_FDP(self, Ω_FDP):
        r_Ω_FDP = (Ω_FDP+1)/Ω_FDP
        return r_Ω_FDP

    def SS_DS_Z_MMI(self, Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI):
        Z_MMI = Q_MMI_0/((P_MMI_0/(ER_0*(1+TMMI_0)*(1+NMMI_0)))^ε_MMI)
        return Z_MMI

    def SS_DS_Z_FDP(self, Q_FDP_0, P_FDP_0, ε_FDP):
        Z_FDP = Q_FDP_0/(P_FDP_0)^ε_FDP
        return Z_FDP

    def SS_DS_Z_PDP(self, Q_PDP_0, P_PDP_0, ε_PDP):
        Z_PDP = Q_PDP_0/(P_PDP_0)^ε_PDP
        return Z_PDP

    def SS_DS_Z_PXM(self, Q_PXM_0, ER_0, ε_PXM):
        Z_PXM = Q_PXM_0/(1/ER_0)^ε_PXM
        return Z_PXM

    def SS_DS_Z_FXP(self, Q_FXP_0, P_FXP_0, ER_0, ε_FXP):
        Z_FXP = Q_FXP_0/(P_FXP_0/ER_0)^ε_FXP
        return Z_FXP


"""Налоги и благосостояние"""
class Taxes_welfare:

    """Импортный тариф"""

    # Базовое рановесие
    def base_import_tariff(self, P_MMI_0, Q_MMI_0, TMMI_0):
        base_import_tariff = (P_MMI_0*Q_MMI_0)*TMMI_0
        return base_import_tariff
    # Новое равновесие
    def new_import_tariff(self, P_MMI_1, Q_MMI_1, TMMI_1):
        new_import_tariff = (P_MMI_1*Q_MMI_1)*TMMI_1
        return new_import_tariff
    # Изменение млн. руб
    def change_import_tariff(self, new_import_tariff, base_import_tariff):
        change_import_tariff = new_import_tariff - base_import_tariff
        return  change_import_tariff
    # Изменение % к начальному
    def change_pr_import_tariff(self, new_import_tariff, base_import_tariff):
        return  new_import_tariff / base_import_tariff - 1

    """Производство макулатурных тарных картонов"""

    # Базовое рановесие
    def base_production_wastepaper(self, P_SDP_0, Q_SDP_0, Tax, Lab, Q_SDP_0):
        base_production_wastepaper = P_SDP_0*Q_SDP_0*Tax+Lab*Q_SDP_0*47/130
        return base_production_wastepaper
    # Новое равновесие
    def new_production_wastepaper(self, P_SDP_1, Q_SDP_1, Tax, Lab, Q_SDP_1):
        new_production_wastepaper = P_SDP_1*Q_SDP_1*Tax+Lab*Q_SDP_1*47/130
        return new_production_wastepaper
    # Изменение млн. руб
    def change_production_wastepaper(self, base_production_wastepaper, new_production_wastepaper):
        return new_production_wastepaper - base_production_wastepaper
    # Изменение % к начальному
    def change_pr_production_wastepaper(self,  new_production_wastepaper, base_production_wastepaper):
        return new_production_wastepaper / base_production_wastepaper - 1

    """Производство целлюлозных тарных картонов"""

    # Базовое рановесие
    def base_production_cellulose(self, Tax, P_FDP_0, Q_FDP_0, Lab, Q_FDP_0):
        base_production_cellulose = Tax*P_FDP_0*Q_FDP_0+Lab*Q_FDP_0*47/130
        return base_production_cellulose
    # Новое равновесие
    def new_production_cellulose(self, Tax, P_FDP_1, Q_FDP_1, Lab, Q_FDP_1):
        new_production_cellulose = Tax*P_FDP_1*Q_FDP_1+Lab*Q_FDP_1*47/130
        return new_production_cellulose
    # Изменение млн. руб
    def change_production_cellulose(self, new_production_cellulose, base_production_cellulose):
        return new_production_cellulose - base_production_cellulose
    # Изменение % к начальному
    def change_pr_production_cellulose(self,  new_production_cellulose, base_production_cellulose):
        return new_production_cellulose / base_production_cellulose - 1

    """Налог на потребителей тарных картонов (налог на прибыль)"""

    # Базовое рановесие
    def base_tax_consumers(self,P_PDP_0, Q_PDP_0, 'Рентабельность (ФНС) !B15', VAT):
        base_tax_consumers = (P_PDP_0*Q_PDP_0)*'Рентабельность (ФНС) !B15'/100*VAT
        return base_tax_consumers
    # Новое равновесие
    def new_tax_consumers(self, base_tax_consumers, change_tax_consumers):
        new_tax_consumers = base_tax_consumers + change_tax_consumers
        return new_tax_consumers
    # Изменение млн. руб
    def change_tax_consumers(self, P_PDP_0, P_PDP_1,Q_PDP_1, Q_PDP_0):
        change_tax_consumers =  ((P_PDP_0-P_PDP_1)*(Q_PDP_1+Q_PDP_0)/2)*0,2
        return change_tax_consumers
    # Изменение % к начальному
    def change_pr_tax_consumers(self, change_tax_consumers, base_tax_consumers):
        return change_tax_consumers / base_tax_consumers

    """Итого налоги"""

    # Базовое рановесие
    def base_total_taxes(self, base_import_tariff, base_production_wastepaper, base_production_cellulose, base_tax_consumers):
        base_total_taxes = base_import_tariff + base_production_wastepaper + base_production_cellulose + base_tax_consumers
        return base_total_taxes
    # Новое равновесие
    def new_total_taxes(self, base_total_taxes, change_tax_consumers):
        return base_total_taxes + change_tax_consumers
    # Изменение млн. руб
    def change_total_taxes(self, change_import_tariff,change_production_wastepaper, change_production_cellulose, change_tax_consumers):
        change_total_taxes = change_import_tariff + change_production_wastepaper + change_production_cellulose + change_tax_consumers
        return change_total_taxes
    # Изменение % к начальному
    def change_pr_total_taxes(self, change_total_taxes, base_total_taxes):
        return change_total_taxes / base_total_taxes

    """Изменение прибыли потребителей картона"""

    # Базовое рановесие
    def base_change_profit_consumers(self, P_PDP_0, Q_PDP_0, 'Рентабельность (ФНС) !B15'):
        base_change_profit_consumers = (P_PDP_0 * Q_PDP_0) * 'Рентабельность (ФНС) !B15' / 100 * 0, 8
        return base_change_profit_consumers
    # Новое равновесие
    def new_change_profit_consumers(self, base_change_profit_consumers, ch_change_profit_consumers):
        new_change_profit_consumers = base_change_profit_consumers + ch_change_profit_consumers
        return new_change_profit_consumers
    # Изменение млн. руб
    def ch_change_profit_consumers(self, P_PDP_0, P_PDP_1, Q_PDP_1, Q_PDP_0):
        ch_change_profit_consumers = ((P_PDP_0-P_PDP_1)*(Q_PDP_1+Q_PDP_0)/2)*0,8
        return ch_change_profit_consumers
    # Изменение % к начальному
    def ch_pr_change_profit_consumers(self, ch_change_profit_consumers, base_change_profit_consumers):
        ch_pr_change_profit_consumers = ch_change_profit_consumers / base_change_profit_consumers
        return ch_pr_change_profit_consumers

    """Изменение прибыли производителей макулатурных картонов"""

    # Базовое рановесие
    def base_change_profit_manufacturers(self, P_SDP_0, Q_SDP_0, profit):
        base_change_profit_manufacturers = P_SDP_0*Q_SDP_0*profit*0,8
        return base_change_profit_manufacturers
    # Новое равновесие
    def new_change_profit_manufacturers(self, base_change_profit_manufacturers, ch_change_profit_manufacturers):
        new_change_profit_manufacturers = base_change_profit_manufacturers + ch_change_profit_manufacturers
        return new_change_profit_manufacturers
    # Изменение млн. руб
    def ch_change_profit_manufacturers(self,P_SDP_1, Q_SDP_1, P_SDP_0, Q_SDP_0, profit)
        ch_change_profit_manufacturers = (P_SDP_1*Q_SDP_1-P_SDP_0*Q_SDP_0)*profit*0,8
        return ch_change_profit_manufacturers
    # Изменение % к начальному
    def ch_pr_change_profit_manufacturers(self, ch_change_profit_manufacturers, base_change_profit_manufacturers):
        ch_pr_change_profit_manufacturers = ch_change_profit_manufacturers / base_change_profit_manufacturers
        return ch_pr_change_profit_manufacturers

    """Изменение прибыли производителей целлюлозных картонов"""

    # Базовое рановесие
    def base_change_profit_cellulose_manufacturers(self,P_FDP_0, Q_FDP_0, profit):
        base_change_profit_cellulose_manufacturers = P_FDP_0*Q_FDP_0*profit*0,8
        return base_change_profit_cellulose_manufacturers
    # Новое равновесие
    def new_change_profit_cellulose_manufacturers(self, base_change_profit_cellulose_manufacturers, ch_change_profit_cellulose_manufacturers):
        new_change_profit_cellulose_manufacturers = base_change_profit_cellulose_manufacturers + ch_change_profit_cellulose_manufacturers
        return new_change_profit_cellulose_manufacturers
    # Изменение млн. руб
    def ch_change_profit_cellulose_manufacturers(self, P_FDP_1, Q_FDP_1, P_FDP_0, Q_FDP_0, profit):
        ch_change_profit_cellulose_manufacturers = (P_FDP_1*Q_FDP_1-P_FDP_0*Q_FDP_0)*profit*0,8
        return ch_change_profit_cellulose_manufacturers
    # Изменение % к начальному
    def ch_pr_change_profit_cellulose_manufacturers(self, ch_change_profit_cellulose_manufacturers, base_change_profit_cellulose_manufacturers):
        ch_pr_change_profit_cellulose_manufacturers = ch_change_profit_cellulose_manufacturers / base_change_profit_cellulose_manufacturers
        return ch_pr_change_profit_cellulose_manufacturers

    """Изменение совокупной зарплаты сотрудников отрасли тарных картонов"""

    # Базовое рановесие
    def base_change_salary_employees(self, Q_SDP_0, Lab, Q_FDP_0):
        base_change_salary_employees = Q_SDP_0*Lab+Q_FDP_0*Lab
        return base_change_salary_employees
    # Новое равновесие
    def new_change_salary_employees(self, base_change_salary_employees, ch_change_salary_employees):
        new_change_salary_employees = base_change_salary_employees + ch_change_salary_employees
        return new_change_salary_employees
    # Изменение млн. руб
    def ch_change_salary_employees(self, Q_SDP_1, Q_SDP_0, Lab, Q_FDP_1, Q_FDP_0):
        ch_change_salary_employees = (Q_SDP_1-Q_SDP_0)*Lab+(Q_FDP_1-Q_FDP_0)*Lab
        return ch_change_salary_employees
    # Изменение % к начальному
    def ch_pr_change_salary_employees(self, ch_change_salary_employees, base_change_salary_employees):
        ch_pr_change_salary_employees = ch_change_salary_employees / base_change_salary_employees
        return ch_pr_change_salary_employees

    """Итого благосостояние"""

    # Базовое рановесие
    def base_total_wealth(self, base_change_profit_consumers, base_change_profit_manufacturers,
                          base_change_profit_cellulose_manufacturers, base_change_salary_employees):
        base_total_wealth = base_change_profit_consumers + base_change_profit_manufacturers + \
                            base_change_profit_cellulose_manufacturers + base_change_salary_employees
        return base_total_wealth
    # Новое равновесие
    def new_total_wealth(self, base_total_wealth, change_total_wealth):
        new_total_wealth = base_total_wealth + change_total_wealth
        return new_total_wealth
    # Изменение млн. руб
    def change_total_wealth(self, ch_change_profit_consumers, ch_change_profit_manufacturers,
                            ch_change_profit_cellulose_manufacturers, ch_change_salary_employees):
        change_total_wealth = ch_change_profit_consumers + ch_change_profit_manufacturers + \
                              ch_change_profit_cellulose_manufacturers + ch_change_salary_employees
        return change_total_wealth
    # Изменение % к начальному
    def change_pr_total_wealth(self, change_total_wealth, base_total_wealth):
        change_pr_total_wealth = change_total_wealth / base_total_wealth
        return change_pr_total_wealth
