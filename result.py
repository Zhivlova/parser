from scipy.optimize import fsolve
from sympy import exp
import math
from math import fsum
from elasticity import average_value

# получаем данные от пользователя
# from_front = [72.14, 0.18, 1.29, 0, 0.01890618906286916, 0, 14.686756, 0.8555, 42, 15.139, 3822, 2999, 1006, 4186, 38,
#               2125, 42]


class InputDataBase:
    def __init__(self, ER_0, P_MMI_USD_0, NMMI_0, NMMI_1, TMMI_0, TMMI_1, SVA_0, SH_0, Q_MMI_0, P_MDI_0, Q_MDI_0, Q_SDP_0,
                 Q_FDC_0, Q_PDC_0, P_FDP_0, Q_FDP_0, P_FXP_0):
        self.ER_0 = ER_0
        self.P_MMI_USD_0 = P_MMI_USD_0
        self.NMMI_0 = NMMI_0
        self.NMMI_1 = NMMI_1
        self.TMMI_0 = TMMI_0
        self.TMMI_1 = TMMI_1
        self.SVA_0 = SVA_0
        self.SH_0 = SH_0
        self.Q_MMI_0 = Q_MMI_0
        self.P_MDI_0 = P_MDI_0
        self.Q_MDI_0 = Q_MDI_0
        self.Q_SDP_0 = Q_SDP_0
        self.Q_FDC_0 = Q_FDC_0
        self.Q_PDC_0 = Q_PDC_0
        self.P_FDP_0 = P_FDP_0
        self.Q_FDP_0 = Q_FDP_0
        self.P_FXP_0 = P_FXP_0


input = InputDataBase(72.14, 0.18, 1.29, 0, 0.01890618906286916, 0, 14.686756, 0.8555, 42, 15.139, 3822, 2999, 1006,
                      4186, 38, 2125, 42)



def calc(user_values):

    result = dict()

    ER_0 = input.ER_0
    result['ER_0'] = ER_0

    ER_1 = ER_0 * 1.2
    result['ER_1'] = ER_1

    P_MMI_USD_0 = input.P_MMI_USD_0
    result['P_MMI_USD_0'] = P_MMI_USD_0

    NMMI_0 = input.NMMI_0
    result['NMMI_0'] = NMMI_0

    NMMI_1 = 0
    result['NMMI_1'] = NMMI_1

    TMMI_0 = input.TMMI_0
    result['TMMI_0'] = TMMI_0

    TMMI_1 = 0
    result['TMMI_1'] = TMMI_1

    SVA_0 = input.SVA_0
    result['SVA_0'] = SVA_0

    SVA_1 = SVA_0
    result['SVA_1'] = SVA_1

    SH_0 = input.SH_0
    result['SH_0'] = SH_0

    SH_1 = SH_0
    result['SH_1'] = SH_1

    P_MDI_0 = input.P_MDI_0
    result['P_MDI_0'] = P_MDI_0

    P_FDP_0 = input.P_FDP_0
    result['P_FDP_0'] = P_FDP_0

    P_FXP_0 = input.P_FXP_0
    result['P_FXP_0'] = P_FXP_0

    Q_MMI_0 = input.Q_MMI_0
    result['Q_MMI_0'] = Q_MMI_0

    Q_MDI_0 = input.Q_MDI_0
    result['Q_MDI_0'] = Q_MDI_0

    Q_SDP_0 = input.Q_SDP_0
    result['Q_SDP_0'] = Q_SDP_0

    Q_FDC_0 = input.Q_FDC_0
    result['Q_FDC_0'] = Q_FDC_0

    Q_PDC_0 = input.Q_PDC_0
    result['Q_PDC_0'] = Q_PDC_0

    Q_FDP_0 = input.Q_FDP_0
    result['Q_FDP_0'] = Q_FDP_0

    K_0 = Q_MDI_0 / Q_PDC_0
    result['K_0'] = K_0

    Λ_0 = -P_MDI_0 / math.log(1 - K_0)
    result['Λ_0'] = Λ_0

    Λ_1 = Λ_0
    result['Λ_1'] = Λ_1

    Q_MIC_0 = Q_MDI_0 + Q_MMI_0
    result['Q_MIC_0'] = Q_MIC_0

    OUT_0 = Q_SDP_0 / (Q_MIC_0 * SH_0)
    result['OUT_0'] = OUT_0

    OUT_1 = OUT_0
    result['OUT_1'] = OUT_1

    def basic_total_fiber_decrease(K_0, OUT_0, SH_0):
        return K_0 * OUT_0 * SH_0
    basic_total_fiber_decrease = basic_total_fiber_decrease(K_0, OUT_0, SH_0)
    result['basic_total_fiber_decrease'] = basic_total_fiber_decrease

    P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
    result['P_MMI_0'] = P_MMI_0

    P_MIC_0 = (P_MDI_0 * Q_MDI_0 + P_MMI_0 * Q_MMI_0) / Q_MIC_0
    result['P_MIC_0'] = P_MIC_0

    P_SDP_0 = P_MIC_0 / OUT_0 + SVA_0
    result['P_SDP_0'] = P_SDP_0

    Q_PDP_0 = Q_SDP_0 + Q_FDC_0
    result['Q_PDP_0'] = Q_PDP_0

    P_PXM_0 = P_MDI_0
    result['P_PXM_0'] = P_PXM_0

    P_PDC_0 = P_MDI_0
    result['P_PDC_0'] = P_PDC_0

    Q_FXP_0 = Q_FDP_0 - Q_FDC_0
    result['Q_FXP_0'] = Q_FXP_0

    Q_PXM_0 = Q_PDC_0 - Q_PDP_0
    result['Q_PXM_0'] = Q_PXM_0

    P_FDC_0 = (P_FDP_0 * Q_FDP_0 - P_FXP_0 * Q_FXP_0) / Q_FDC_0
    result['P_FDC_0'] = P_FDC_0

    P_PDP_0 = (P_SDP_0 * Q_SDP_0 + P_FDC_0 * Q_FDC_0) / Q_PDP_0
    result['P_PDP_0'] = P_PDP_0

    σ_MIC = 2.5
    result['σ_MIC'] = σ_MIC

    r_σ_MIC = (σ_MIC-1)/σ_MIC
    result['r_σ_MIC'] = r_σ_MIC

    σ_PDP = 2.25
    result['σ_PDP'] = σ_PDP

    r_σ_PDP = (σ_PDP-1)/σ_PDP
    result['r_σ_PDP'] = r_σ_PDP

    Ω_FDP = 2.95
    result['Ω_FDP'] = Ω_FDP

    r_Ω_FDP = (Ω_FDP+1)/Ω_FDP
    result['r_Ω_FDP'] = r_Ω_FDP

    ε_MMI = 10
    result['ε_MMI'] = ε_MMI

    ε_FDP = 0.3
    result['ε_FDP'] = ε_FDP

    ε_PDP = average_value
    result['ε_PDP'] = ε_PDP

    ε_PXM = 1
    result['ε_PXM'] = ε_PXM

    ε_FXP = -10
    result['ε_FXP'] = ε_FXP

    Z_MMI = Q_MMI_0/((P_MMI_0/(ER_0*(1+TMMI_0)*(1+NMMI_0)))**ε_MMI)
    result['Z_MMI'] = Z_MMI

    Z_FDP = Q_FDP_0/(P_FDP_0)**ε_FDP
    result['Z_FDP'] = Z_FDP

    Z_PDP = Q_PDP_0/(P_PDP_0)**ε_PDP
    result['Z_PDP'] = Z_PDP

    Z_PXM = Q_PXM_0/(1/ER_0)**ε_PXM
    result['Z_PXM'] = Z_PXM

    Z_FXP = Q_FXP_0/(P_FXP_0/ER_0)**ε_FXP
    result['Z_FXP'] = Z_FXP

    K_MMI = (Q_MMI_0/Q_MDI_0)**(1-r_σ_MIC)*(P_MMI_0/P_MDI_0)
    result['K_MMI'] = K_MMI

    K_MDI = 1
    result['K_MDI'] = K_MDI

    E20 = Q_MIC_0/(K_MMI*Q_MMI_0**r_σ_MIC+K_MDI*Q_MDI_0**r_σ_MIC)**(1/r_σ_MIC)
    result['E20'] = E20

    K_SDP = 1
    result['K_SDP'] = K_SDP

    K_FDC = (Q_FDC_0/Q_SDP_0)**(1-r_σ_PDP)*(P_FDC_0/P_SDP_0)
    result['K_FDC'] = K_FDC

    E23 = Q_PDP_0/(K_SDP*Q_SDP_0**r_σ_PDP+K_FDC*Q_FDC_0**r_σ_PDP)**(1/r_σ_PDP)
    result['E23'] = E23

    K_FXP = ((Q_FXP_0/Q_FDC_0)**(1-r_Ω_FDP))*(P_FXP_0*K_FDC/P_FDC_0)
    result['K_FXP'] = K_FXP

    def func(z):
        Q_MMI_1 = z[0]
        P_MMI_1 = z[1]
        P_MIC_1 = z[2]
        Q_MIC_1 = z[3]
        P_MDI_1 = z[4]
        Q_MDI_1 = z[5]
        P_SDP_1 = z[6]
        Q_SDP_1 = z[7]
        Q_FDP_1 = z[8]
        P_FDP_1 = z[9]
        P_FDC_1 = z[10]
        Q_FDC_1 = z[11]
        P_FXP_1 = z[12]
        Q_FXP_1 = z[13]
        P_PDP_1 = z[14]
        Q_PDP_1 = z[15]
        Q_PXM_1 = z[16]
        Q_PDC_1 = z[17]
        P_PDC_1 = z[18]
        P_PXM_1 = z[19]

        MMI_SUPPLY = Q_MMI_1 - Z_MMI * (P_MMI_1 / ((1 + NMMI_1) * (1 + TMMI_1) * ER_1)) ** ε_MMI
        MIC_BUD_CES = P_MIC_1 * Q_MIC_1 - P_MDI_1 * Q_MDI_1 - P_MMI_1 * Q_MMI_1
        MIC_CES = Q_MMI_1 / Q_MDI_1 - ((P_MMI_1 / (P_MDI_1)) * (K_MDI / K_MMI)) ** (1 / (r_σ_MIC - 1))
        MIC_BAL_CES = Q_MIC_1 - Q_MDI_1 - Q_MMI_1
        SDP_P = P_SDP_1 - P_MIC_1 / OUT_1 - SVA_1
        SDP_Q = Q_SDP_1 - Q_MIC_1 * OUT_1 * SH_1
        FDP_SUPPLY = Q_FDP_1 - Z_FDP * (P_FDP_1) ** ε_FDP
        FDP_BUD_CET = P_FDP_1 * Q_FDP_1 - P_FDC_1 * Q_FDC_1 - P_FXP_1 * Q_FXP_1
        FDP_CET = Q_FXP_1 / Q_FDC_1 - ((P_FXP_1 / (P_FDC_1)) * (K_FDC / K_FXP)) ** (1 / (r_Ω_FDP - 1))
        FDP_BAL_CET = Q_FDP_1 - Q_FDC_1 - Q_FXP_1
        FXP_DEMAND = Q_FXP_1 - Z_FXP * (P_FXP_1 / ER_1) ** ε_FXP
        PDP_BUD_CES = P_PDP_1 * Q_PDP_1 - P_SDP_1 * Q_SDP_1 - P_FDC_1 * Q_FDC_1
        PDP_CES = Q_SDP_1 / Q_FDC_1 - ((P_SDP_1 / (P_FDC_1)) * (K_FDC / K_SDP)) ** (1 / (r_σ_PDP - 1))
        PDP_BAL_CES = Q_PDP_1 - Q_SDP_1 - Q_FDC_1
        PDP_DEMAND = Q_PDP_1 - Z_PDP * (P_PDP_1) ** ε_PDP
        PXM_SUPPLY = Q_PXM_1 - Z_PXM * (1 / ER_1) ** ε_PXM
        PDC_BAL = Q_PDC_1 - Q_PXM_1 - Q_PDP_1
        PDC_P = P_PDC_1 - P_MDI_1
        MDI_BAL = Q_MDI_1 - Q_PDC_1 * (1 - exp(-P_MDI_1 / Λ_1))
        PXM_P = P_PXM_1 - P_MDI_1

        return MMI_SUPPLY, MIC_BUD_CES, MIC_CES, MIC_BAL_CES, SDP_P, SDP_Q, FDP_SUPPLY, FDP_BUD_CET, FDP_CET, FDP_BAL_CET, \
               FXP_DEMAND, PDP_BUD_CES, PDP_CES, PDP_BAL_CES, PDP_DEMAND, PXM_SUPPLY, PDC_BAL, PDC_P, MDI_BAL, PXM_P

    z0 = [Q_MMI_0, P_MMI_0, P_MIC_0, Q_MIC_0, P_MDI_0, Q_MDI_0, P_SDP_0, Q_SDP_0, Q_FDP_0, P_FDP_0,
          P_FDC_0, Q_FDC_0, P_FXP_0, Q_FXP_0, P_PDP_0, Q_PDP_0, Q_PXM_0, Q_PDC_0, P_PDC_0, P_PXM_0]

    eq_result = fsum(func(z0))

    if eq_result < 0.000001:
        solution = 'Решение найдено'
        print(f'{eq_result} {solution}')
    else:
        solution = 'Решение не найдено'
        print(f'{eq_result} {solution}')

    solved_value = fsolve(func, z0)

    Q_MMI_1 = solved_value[0]
    result['Q_MMI_1'] = Q_MMI_1

    P_MMI_1 = solved_value[1]
    result['P_MMI_1'] = P_MMI_1

    P_MIC_1 = solved_value[2]
    result['P_MIC_1'] = P_MIC_1

    Q_MIC_1 = solved_value[3]
    result['Q_MIC_1'] = Q_MIC_1

    P_MDI_1 = solved_value[4]
    result['P_MDI_1'] = P_MDI_1

    Q_MDI_1 = solved_value[5]
    result['Q_MDI_1'] = Q_MDI_1

    P_SDP_1 = solved_value[6]
    result['P_SDP_1'] = P_SDP_1

    Q_SDP_1 = solved_value[7]
    result['Q_SDP_1'] = Q_SDP_1

    Q_FDP_1 = solved_value[8]
    result['Q_FDP_1'] = Q_FDP_1

    P_FDP_1 = solved_value[9]
    result['P_FDP_1'] = P_FDP_1

    P_FDC_1 = solved_value[10]
    result['P_FDC_1'] = P_FDC_1

    Q_FDC_1 = solved_value[11]
    result['Q_FDC_1'] = Q_FDC_1

    P_FXP_1 = solved_value[12]
    result['P_FXP_1'] = P_FXP_1

    Q_FXP_1 = solved_value[13]
    result['Q_FXP_1'] = Q_FXP_1

    P_PDP_1 = solved_value[14]
    result['P_PDP_1'] = P_PDP_1

    Q_PDP_1 = solved_value[15]
    result['Q_PDP_1'] = Q_PDP_1

    Q_PXM_1 = solved_value[16]
    result['Q_PXM_1'] = Q_PXM_1

    Q_PDC_1 = solved_value[17]
    result['Q_PDC_1'] = Q_PDC_1

    P_PDC_1 = solved_value[18]
    result['P_PDC_1'] = P_PDC_1

    P_PXM_1 = solved_value[19]
    result['P_PXM_1'] = P_PXM_1

    K_1 = (1 - exp(-P_MDI_1 / Λ_1))
    result['K_1'] = K_1

    new_total_fiber_decrease = K_1 * OUT_1 * SH_1
    result['new_total_fiber_decrease'] = new_total_fiber_decrease

    """Импорт товара M"""
    # Изменение (%) Цена (P)
    perc_change_price_good_import = P_MMI_1 / P_MMI_0 - 1
    result['perc_change_price_good_import'] = perc_change_price_good_import
    # Изменение (%) Количество (Q)
    perc_change_quantity_good_import = Q_MMI_1 / Q_MMI_0 - 1
    result['perc_change_quantity_good_import'] = perc_change_quantity_good_import

    """Потребление отечественного товара M"""
    # Изменение (%) Цена (P)
    perc_change_price_consumption_home_goods = P_MDI_1/P_MDI_0-1
    result['perc_change_price_consumption_home_goods'] = perc_change_price_consumption_home_goods
    # Изменение (%) Количество (Q)
    perc_change_quantity_good_import_consumption_home_goods = Q_MDI_1/Q_MDI_0-1
    result['perc_change_quantity_good_import_consumption_home_goods'] = perc_change_quantity_good_import_consumption_home_goods

    """Потребление отраслью S товара M"""
    # Изменение (%) Цена (P)
    perc_change_price_good_consumption = P_MIC_1/P_MIC_0-1
    result['perc_change_price_good_consumption'] = perc_change_price_good_consumption
    # Изменение (%) Количество (Q)
    perc_change_quantity_good_consumption = Q_MIC_1/Q_MIC_0-1
    result['perc_change_quantity_good_consumption'] = perc_change_quantity_good_consumption

    """Отечественное производство S"""
    # Изменение (%) Цена (P)
    perc_change_price_home_production = P_SDP_1/P_SDP_0-1
    result['perc_change_price_home_production'] = perc_change_price_home_production
    # Изменение (%) Количество (Q)
    perc_change_quantity_home_production = Q_SDP_1/Q_SDP_0-1
    result['perc_change_quantity_home_production'] = perc_change_quantity_home_production

    """Отечественное потребление F"""
    # Изменение (%) Цена (P)
    perc_change_price_home_consumption_f = P_FDC_1/P_FDC_0-1
    result['perc_change_price_home_consumption_f'] = perc_change_price_home_consumption_f
    # Изменение (%) Количество (Q)
    perc_change_quantity_home_consumption_f = Q_FDC_1/Q_FDC_0-1
    result['perc_change_quantity_home_consumption_f'] = perc_change_quantity_home_consumption_f

    """Отечественное потребление P"""
    # Изменение (%) Цена (P)
    perc_change_price_home_consumption_p = P_PDP_1/P_PDP_0-1
    result['perc_change_price_home_consumption_p'] = perc_change_price_home_consumption_p
    # Изменение (%) Количество (Q)
    perc_change_quantity_home_consumption_p = Q_PDP_1/Q_PDP_0-1
    result['perc_change_quantity_home_consumption_p'] = perc_change_quantity_home_consumption_p

    """Нетто импорт P"""
    # Изменение (%) Цена (P)
    perc_change_price_netto_import = P_PXM_1/P_PXM_0-1
    result['perc_change_price_netto_import'] = perc_change_price_netto_import
    # Изменение (%) Количество (Q)
    perc_change_quantity_netto_import = Q_PXM_1/Q_PXM_0-1
    result['perc_change_quantity_netto_import'] = perc_change_quantity_netto_import

    """Общее образование P"""
    # Изменение (%) Цена (P)
    perc_change_price_general_education = P_PDC_1/P_PDC_0-1
    result['perc_change_price_general_education'] = perc_change_price_general_education
    # Изменение (%) Количество (Q)
    perc_change_quantity_general_education = Q_PDC_1/Q_PDC_0-1
    result['perc_change_quantity_general_education'] = perc_change_quantity_general_education

    """Отечественное производство товара F"""
    # Изменение (%) Цена (P)
    perc_change_price_home_production_f = P_FDP_1/P_FDP_0-1
    result['perc_change_price_home_production_f'] = perc_change_price_home_production_f
    # Изменение (%) Количество (Q)
    perc_change_quantity_home_production_f = Q_FDP_1/Q_FDP_0-1
    result['perc_change_quantity_home_production_f'] = perc_change_quantity_home_production_f

    """Экспорт товара F"""
    # Изменение (%) Цена (P)
    perc_change_price_export_goodsself = P_FXP_1/P_FXP_0-1
    result['perc_change_price_export_goodsself'] = perc_change_price_export_goodsself
    # Изменение (%) Количество (Q)
    perc_change_quantity_export_goods = Q_FXP_1/Q_FXP_0-1
    result['perc_change_quantity_export_goods'] = perc_change_quantity_export_goods

    """Внешние значения"""

    EU = 0.3331729436173592
    EAEU = 0.6218762187426168
    Lab = 0.544
    profit = 9.8 / 100
    NoL = SVA_0 - Lab
    Tax = 3.37412004365224 / 100
    VAT = 0.2

    """Налоги и благосостояние"""

    """Импортный тариф"""
    # Базовое рановесие
    base_import_tariff = (P_MMI_0 * Q_MMI_0) * TMMI_0
    # Новое равновесие
    new_import_tariff = (P_MMI_1 * Q_MMI_1) * TMMI_1
    # Изменение млн. руб
    change_import_tariff = new_import_tariff - base_import_tariff
    # Изменение % к начальному
    change_pr_import_tariff = new_import_tariff / base_import_tariff - 1

    """Производство макулатурных тарных картонов"""
    # Базовое рановесие
    base_production_wastepaper = P_SDP_0*Q_SDP_0*Tax+Lab*Q_SDP_0*47/130
    # Новое равновесие
    new_production_wastepaper = P_SDP_1 * Q_SDP_1 * Tax + Lab * Q_SDP_1 * 47 / 130
    # Изменение млн. руб
    change_production_wastepaper = new_production_wastepaper - base_production_wastepaper
    # Изменение % к начальному
    change_pr_production_wastepaper = new_production_wastepaper / base_production_wastepaper - 1

    """Производство целлюлозных тарных картонов"""
    # Базовое рановесие
    base_production_cellulose = Tax * P_FDP_0 * Q_FDP_0 + Lab * Q_FDP_0 * 47 / 130
    # Новое равновесие
    new_production_cellulose = Tax * P_FDP_1 * Q_FDP_1 + Lab * Q_FDP_1 * 47 / 130
    # Изменение млн. руб
    change_production_cellulose = new_production_cellulose - base_production_cellulose
    # Изменение % к начальному
    change_pr_production_cellulose = new_production_cellulose / base_production_cellulose - 1

    """Налог на потребителей тарных картонов (налог на прибыль)"""
    # Базовое рановесие
    base_tax_consumers = (P_PDP_0 * Q_PDP_0) * 12.2 / 100 * VAT
    # Изменение млн. руб
    change_tax_consumers = ((P_PDP_0-P_PDP_1)*(Q_PDP_1+Q_PDP_0)/2)*0.2
    # Новое равновесие
    new_tax_consumers = base_tax_consumers + change_tax_consumers
    # Изменение % к начальному
    change_pr_tax_consumers = change_tax_consumers / base_tax_consumers

    """Итого налоги"""
    # Базовое рановесие
    base_total_taxes = base_import_tariff + base_production_wastepaper + base_production_cellulose + base_tax_consumers
    # Изменение млн. руб
    change_total_taxes = change_import_tariff + change_production_wastepaper + change_production_cellulose + change_tax_consumers
    # Новое равновесие
    new_total_taxes = base_total_taxes + change_total_taxes
    # Изменение % к начальному
    change_pr_total_taxes = change_total_taxes / base_total_taxes

    """Изменение прибыли потребителей картона"""
    # Базовое рановесие
    base_change_profit_consumers = (P_PDP_0 * Q_PDP_0) * 12.2 / 100 * 0.8
    # Изменение млн. руб
    ch_change_profit_consumers = ((P_PDP_0 - P_PDP_1) * (Q_PDP_1 + Q_PDP_0) / 2) * 0.8
    # Новое равновесие
    new_change_profit_consumers = base_change_profit_consumers + ch_change_profit_consumers
    # Изменение % к начальному
    ch_pr_change_profit_consumers = ch_change_profit_consumers / base_change_profit_consumers

    """Изменение прибыли производителей макулатурных картонов"""
    # Базовое рановесие
    base_change_profit_manufacturers = P_SDP_0 * Q_SDP_0 * profit * 0.8
    # Изменение млн. руб
    ch_change_profit_manufacturers = (P_SDP_1 * Q_SDP_1 - P_SDP_0 * Q_SDP_0) * profit * 0.8
    # Новое равновесие
    new_change_profit_manufacturers = base_change_profit_manufacturers + ch_change_profit_manufacturers
    # Изменение % к начальному
    ch_pr_change_profit_manufacturers = ch_change_profit_manufacturers / base_change_profit_manufacturers

    """Изменение прибыли производителей целлюлозных картонов"""
    # Базовое рановесие
    base_change_profit_cellulose_manufacturers = P_FDP_0 * Q_FDP_0 * profit * 0.8
    # Изменение млн. руб
    ch_change_profit_cellulose_manufacturers = (P_FDP_1 * Q_FDP_1 - P_FDP_0 * Q_FDP_0) * profit * 0.8
    # Новое равновесие
    new_change_profit_cellulose_manufacturers = base_change_profit_cellulose_manufacturers + ch_change_profit_cellulose_manufacturers
    # Изменение % к начальному
    ch_pr_change_profit_cellulose_manufacturers = ch_change_profit_cellulose_manufacturers / base_change_profit_cellulose_manufacturers

    """Изменение совокупной зарплаты сотрудников отрасли тарных картонов"""
    # Базовое рановесие
    base_change_salary_employees = Q_SDP_0 * Lab + Q_FDP_0 * Lab
    # Изменение млн. руб
    ch_change_salary_employees = (Q_SDP_1 - Q_SDP_0) * Lab + (Q_FDP_1 - Q_FDP_0) * Lab
    # Новое равновесие
    new_change_salary_employees = base_change_salary_employees + ch_change_salary_employees
    # Изменение % к начальному
    ch_pr_change_salary_employees = ch_change_salary_employees / base_change_salary_employees

    """Итого благосостояние"""
    # Базовое рановесие
    base_total_wealth = base_change_profit_consumers + base_change_profit_manufacturers + base_change_profit_cellulose_manufacturers + base_change_salary_employees
    # Изменение млн. руб
    change_total_wealth = ch_change_profit_consumers + ch_change_profit_manufacturers + ch_change_profit_cellulose_manufacturers + ch_change_salary_employees
    # Новое равновесие
    new_total_wealth = base_total_wealth + change_total_wealth
    # Изменение % к начальному
    change_pr_total_wealth = change_total_wealth / base_total_wealth

    result_to_front = {
        'Управляющие воздействия модели': [
            {'id': '1', 'title': 'Курс RUB/USD', 'params': 'ER', 'basebalance': ER_0, 'newbalance': ER_1},
            {'id': '2', 'title': 'Цена импорта макулатуры USD (без тарифа), долл. США за кг', 'params': 'P_MMI_USD_0',
             'basebalance': P_MMI_USD_0, 'newbalance': None},
            {'id': '3', 'title': 'Импортный нетарифный барьер на макулатуру', 'params': 'NMMI', 'basebalance': NMMI_0,
             'newbalance': NMMI_1},
            {'id': '4', 'title': 'Импортный тариф на макулатуру', 'params': 'TMMI', 'basebalance': TMMI_0,
             'newbalance': TMMI_1},
            {'id': '5', 'title': 'Собираемость макулатуры', 'params': 'K', 'basebalance': K_0, 'newbalance': K_1},
            {'id': '6', 'title': 'Прочие переменные издержки производства макулатурного картона (руб./кг)', 'params': 'SVA',
             'basebalance': SVA_0, 'newbalance': SVA_1},
            {'id': '7', 'title': 'Доля собираемой макулатуры для производства картона', 'params': 'SH', 'basebalance': SH_0,
             'newbalance': SH_1},
            {'id': '8', 'title': 'Общее убывание волокна', 'params': ' ', 'basebalance': basic_total_fiber_decrease,
             'newbalance': new_total_fiber_decrease}
        ],
        'Поиск решения': solution,
        'Наименование переменной': [
            {'id': '1',
             'title': 'Импорт макулатуры',
             'params': 'MMI',
             'basebalance_pr': P_MMI_0,
             'basebalance_quan': Q_MMI_0,
             'newbalance_pr': P_MMI_1,
             'newbalance_quan': Q_MMI_1,
             'perc_change_price_good_import': perc_change_price_good_import,
             'perc_change_quantity_good_import': perc_change_quantity_good_import},

            {'id': '2',
             'title': 'Потребление отечественной макулатуры',
             'params': 'MDI',
             'basebalance_pr': P_MDI_0,
             'basebalance_quan': Q_MDI_0,
             'newbalance_pr': P_MDI_1,
             'newbalance_quan': Q_MDI_1,
             'perc_change_price_consumption_home_goods': perc_change_price_consumption_home_goods,
             'perc_change_quantity_good_import_consumption_home_goods': perc_change_quantity_good_import_consumption_home_goods},

            {'id': '3',
             'title': 'Потребление макулатуры',
             'params': 'MIC',
             'basebalance_pr': P_MIC_0,
             'basebalance_quan': Q_MIC_0,
             'newbalance_pr': P_MIC_1,
             'newbalance_quan': Q_MIC_1,
             'perc_change_price_good_consumption': perc_change_price_good_consumption,
             'perc_change_quantity_good_consumption': perc_change_quantity_good_consumption},

            {'id': '4',
             'title': 'Отечественное производство макулатурных тарных картонов',
             'params': 'SDP',
             'basebalance_pr': P_SDP_0,
             'basebalance_quan': Q_SDP_0,
             'newbalance_pr': P_SDP_1,
             'newbalance_quan': Q_SDP_1,
             'perc_change_price_home_production': perc_change_price_home_production,
             'perc_change_quantity_home_production': perc_change_quantity_home_production},

            {'id': '5',
             'title': 'Отечественное потребление целлюлозных тарных картонов',
             'params': 'FDC',
             'basebalance_pr': P_FDC_0,
             'basebalance_quan': Q_FDC_0,
             'newbalance_pr': P_FDC_1,
             'newbalance_quan': Q_FDC_1,
             'perc_change_price_home_consumption_f': perc_change_price_home_consumption_f,
             'perc_change_quantity_home_consumption_f': perc_change_quantity_home_consumption_f},

            {'id': '6',
             'title': 'Отечественное потребление тарных картонов',
             'params': 'PDP',
             'basebalance_pr': P_PDP_0,
             'basebalance_quan': Q_PDP_0,
             'newbalance_pr': P_PDP_1,
             'newbalance_quan': Q_PDP_1,
             'perc_change_price_home_consumption_p': perc_change_price_home_consumption_p,
             'perc_change_quantity_home_consumption_p': perc_change_quantity_home_consumption_p},

            {'id': '7',
             'title': 'Нетто импорт тарных картнов в составе упакованных товаров',
             'params': 'PXM',
             'basebalance_pr': P_PXM_0,
             'basebalance_quan': Q_PXM_0,
             'newbalance_pr': P_PXM_1,
             'newbalance_quan': Q_PXM_1,
             'perc_change_price_netto_import': perc_change_price_netto_import,
             'perc_change_quantity_netto_import': perc_change_quantity_netto_import},

            {'id': '8',
             'title': 'Общее образование макулатуры',
             'params': 'PDC',
             'basebalance_pr': P_PDC_0,
             'basebalance_quan': Q_PDC_0,
             'newbalance_pr': P_PDC_1,
             'newbalance_quan': Q_PDC_1,
             'perc_change_price_general_education': perc_change_price_general_education,
             'perc_change_quantity_general_education': perc_change_quantity_general_education},

            {'id': '9',
             'title': 'Отечественное производство целлюлозных тарных картонов',
             'params': 'FDP',
             'basebalance_pr': P_FDP_0,
             'basebalance_quan': Q_FDP_0,
             'newbalance_pr': P_FDP_1,
             'newbalance_quan': Q_FDP_1,
             'perc_change_price_home_production_f': perc_change_price_home_production_f,
             'perc_change_quantity_home_production_f': perc_change_quantity_home_production_f},

            {'id': '10',
             'title': 'Экспорт целлюлозных тарных картонов',
             'params': 'FXP',
             'basebalance_pr': P_FXP_0,
             'basebalance_quan': Q_FXP_0,
             'newbalance_pr': P_FXP_1,
             'newbalance_quan': Q_FXP_1,
             'perc_change_price_export_goodsself': perc_change_price_export_goodsself,
             'perc_change_quantity_export_goods': perc_change_quantity_export_goods}

        ]}
    return result_to_front


print(calc(input))