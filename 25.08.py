import math
import json

def calc(user_values):

    result = dict()

    ER_0 = user_values[0]
    result['ER_0'] = ER_0
    print(f' от пользователя получено значение ER_0  {ER_0}')

    ER_1 = ER_0 * 1.2
    result['ER_1'] = ER_1

    P_MMI_USD_0 = user_values[1]
    print(f' от пользователя получено значение P_MMI_USD_0  {P_MMI_USD_0}')
    result['P_MMI_USD_0'] = P_MMI_USD_0

    NMMI_0 = user_values[2]
    print(f' от пользователя получено значение NMMI_0  {NMMI_0}')
    result['NMMI_0'] = NMMI_0
    NMMI_1 = 0
    result['NMMI_1'] = NMMI_1

    TMMI_0 = user_values[3]
    print(f' от пользователя получено значение TMMI_0  {TMMI_0}')
    result['TMMI_0'] = TMMI_0
    TMMI_1 = 0
    result['TMMI_1'] = TMMI_1

    SVA_0 = user_values[4]
    print(f' от пользователя получено значение SVA_0  {SVA_0}')
    result['SVA_0'] = SVA_0

    SVA_1 = SVA_0
    result['SVA_1'] = SVA_1

    SH_0 = user_values[5]
    print(f' от пользователя получено значение SH_0  {SH_0}')
    result['SH_0'] = SH_0

    SH_1 = SH_0
    result['SH_1'] = SH_1

    P_MDI_0 = user_values[6]
    print(f' от пользователя получено значение P_MDI_0  {P_MDI_0}')
    result['P_MDI_0'] = P_MDI_0

    P_FDP_0 = user_values[7]
    print(f' от пользователя получено значение P_FDP_0  {P_FDP_0}')
    result['P_FDP_0'] = P_FDP_0

    P_FXP_0 = user_values[8]
    print(f' от пользователя получено значение P_FXP_0  {P_FXP_0}')
    result['P_FXP_0'] = P_FXP_0

    Q_MMI_0 = user_values[9]
    print(f' от пользователя получено значение Q_MMI_0  {Q_MMI_0}')
    result['Q_MMI_0'] = Q_MMI_0

    Q_MDI_0 = user_values[10]
    print(f' от пользователя получено значение Q_MDI_0  {Q_MDI_0}')
    result['Q_MDI_0'] = Q_MDI_0

    Q_SDP_0 = user_values[11]
    print(f' от пользователя получено значение Q_SDP_0  {Q_SDP_0}')
    result['Q_SDP_0'] = Q_SDP_0

    Q_FDC_0 = user_values[12]
    print(f' от пользователя получено значение Q_FDC_0  {Q_FDC_0}')
    result['Q_FDC_0'] = Q_FDC_0

    Q_PDC_0 = user_values[13]
    print(f' от пользователя получено значение Q_PDC_0  {Q_PDC_0}')
    result['Q_PDC_0'] = Q_PDC_0

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

    def K_1(P_MDI_1, Λ_1):
        K_1 = (1 - math.exp(-P_MDI_1 / Λ_1))
        return K_1

    P_MDI_1 = 15.6016971682569
    result['P_MDI_1'] = P_MDI_1

    K_1 = K_1(P_MDI_1, Λ_1)
    result['K_1'] = K_1

    def new_total_fiber_decrease(K_1, OUT_1, SH_1):
        return K_1 * OUT_1 * SH_1

    new_total_fiber_decrease = new_total_fiber_decrease(K_1, OUT_1, SH_1)
    result['new_total_fiber_decrease'] = new_total_fiber_decrease

    P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
    result['P_MMI_0'] = P_MMI_0

    P_MIC_0 = (P_MDI_0*Q_MDI_0+P_MMI_0*Q_MMI_0)/Q_MIC_0
    result['P_MIC_0'] = P_MIC_0

    P_SDP_0 = P_MIC_0/OUT_0+SVA_0
    result['P_SDP_0'] = P_SDP_0

    Q_PDP_0 = Q_SDP_0+Q_FDC_0
    result['Q_PDP_0'] = Q_PDP_0

    P_PXM_0 = P_MDI_0
    result['P_PXM_0'] = P_PXM_0

    P_PDC_0 = P_MDI_0
    result['P_PDC_0'] = P_PDC_0

    Q_FDP_0 = user_values[14]
    print(f' от пользователя получено значение Q_FDP_0  {Q_FDP_0}')
    result['Q_FDP_0'] = Q_FDP_0

    Q_FXP_0 = Q_FDP_0-Q_FDC_0
    result['Q_FXP_0'] = Q_FXP_0

    Q_PXM_0 = Q_PDC_0-Q_PDP_0
    result['Q_PXM_0'] = Q_PXM_0

    P_FDC_0 = (P_FDP_0*Q_FDP_0-P_FXP_0*Q_FXP_0)/Q_FDC_0
    result['P_FDC_0'] = P_FDC_0

    P_PDP_0 = (P_SDP_0*Q_SDP_0+P_FDC_0*Q_FDC_0)/Q_PDP_0
    result['P_PDP_0'] = P_PDP_0

    P_MMI_1 = 7.809220170519853
    result['P_MMI_1'] = P_MMI_1

    P_MDI_1 = 15.601697168256912
    result['P_MDI_1'] = P_MDI_1

    P_MIC_1 = 15.271367919915447
    result['P_MIC_1'] = P_MIC_1

    P_SDP_1 = 31.519642931378577
    result['P_SDP_1'] = P_SDP_1

    P_FDC_1 = 35.84115975829865
    result['P_FDC_1'] = P_FDC_1

    P_PDP_1 = 32.49799333322565
    result['P_PDP_1'] = P_PDP_1

    P_PXM_1 = 15.601697168256912
    result['P_PXM_1'] = P_PXM_1

    P_PDC_1 = 15.601697168256912
    result['P_PDC_1'] = P_PDC_1

    P_FDP_1 = 44.03846291455995
    result['P_FDP_1'] = P_FDP_1

    P_FXP_1 = 49.540263241232324
    result['P_FXP_1'] = P_FXP_1

    Q_MMI_1 = 166.4876029242774
    result['Q_MMI_1'] = Q_MMI_1

    Q_MDI_1 = 3760.960005783304
    result['Q_MDI_1'] = Q_MDI_1

    Q_MIC_1 = 3927.447608707581
    result['Q_MIC_1'] = Q_MIC_1

    Q_SDP_1 = 3048.2441455781654
    result['Q_SDP_1'] = Q_SDP_1

    Q_FDC_1 = 892.0438008930299
    result['Q_FDC_1'] = Q_FDC_1

    Q_PDP_1 = 3940.287946471196
    result['Q_PDP_1'] = Q_PDP_1

    Q_PXM_1 = 150.8333333333333
    result['Q_PXM_1'] = Q_PXM_1

    Q_PDC_1 = 4091.1212798045276
    result['Q_PDC_1'] = Q_PDC_1

    Q_FDP_1 = 2221.1275608246965
    result['Q_FDP_1'] = Q_FDP_1

    Q_FXP_1 = 1329.0837599316676
    result['Q_FXP_1'] = Q_FXP_1

    """Импорт товара M"""
    # Изменение (%) Цена (P)
    def perc_change_price_good_import(P_MMI_1, P_MMI_0):
        return P_MMI_1/P_MMI_0-1
    perc_change_price_good_import = perc_change_price_good_import(P_MMI_1, P_MMI_0)
    result['perc_change_price_good_import'] = perc_change_price_good_import

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import(Q_MMI_1, Q_MMI_0):
        return Q_MMI_1/Q_MMI_0-1
    perc_change_quantity_good_import = perc_change_quantity_good_import(Q_MMI_1, Q_MMI_0)
    result['perc_change_quantity_good_import'] = perc_change_quantity_good_import

    """Потребление отечественного товара M"""
    # Изменение (%) Цена (P)
    def perc_change_price_consumption_home_goods(P_MDI_1, P_MDI_0):
        return P_MDI_1/P_MDI_0-1
    perc_change_price_consumption_home_goods = perc_change_price_consumption_home_goods(P_MDI_1, P_MDI_0)
    result['perc_change_price_consumption_home_goods'] = perc_change_price_consumption_home_goods

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import_consumption_home_goods(Q_MDI_1, Q_MDI_0):
        return Q_MDI_1/Q_MDI_0-1
    perc_change_quantity_good_import_consumption_home_goods = perc_change_quantity_good_import_consumption_home_goods(Q_MDI_1, Q_MDI_0)
    result['perc_change_quantity_good_import_consumption_home_goods'] = perc_change_quantity_good_import_consumption_home_goods

    """Потребление отраслью S товара M"""
    # Изменение (%) Цена (P)
    def perc_change_price_good_consumption(P_MIC_1, P_MIC_0):
        return P_MIC_1/P_MIC_0-1
    perc_change_price_good_consumption = perc_change_price_good_consumption(P_MIC_1, P_MIC_0)
    result['perc_change_price_good_consumption'] = perc_change_price_good_consumption

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_consumption(Q_MIC_1, Q_MIC_0):
        return Q_MIC_1/Q_MIC_0-1
    perc_change_quantity_good_consumption = perc_change_quantity_good_consumption(Q_MIC_1, Q_MIC_0)
    result['perc_change_quantity_good_consumption'] = perc_change_quantity_good_consumption

    """Отечественное производство S"""
    # Изменение (%) Цена (P)
    def perc_change_price_home_production(P_SDP_1, P_SDP_0):
        return P_SDP_1/P_SDP_0-1
    perc_change_price_home_production = perc_change_price_home_production(P_SDP_1, P_SDP_0)
    result['perc_change_price_home_production'] = perc_change_price_home_production

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production(Q_SDP_1, Q_SDP_0):
        return Q_SDP_1/Q_SDP_0-1
    perc_change_quantity_home_production = perc_change_quantity_home_production(Q_SDP_1, Q_SDP_0)
    result['perc_change_quantity_home_production'] = perc_change_quantity_home_production

    """Отечественное потребление F"""

    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_f(P_FDC_1, P_FDC_0):
        return P_FDC_1/P_FDC_0-1
    perc_change_price_home_consumption_f = perc_change_price_home_consumption_f(P_FDC_1, P_FDC_0)
    result['perc_change_price_home_consumption_f'] = perc_change_price_home_consumption_f

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_f(Q_FDC_1, Q_FDC_0):
        return Q_FDC_1/Q_FDC_0-1
    perc_change_quantity_home_consumption_f = perc_change_quantity_home_consumption_f(Q_FDC_1, Q_FDC_0)
    result['perc_change_quantity_home_consumption_f'] = perc_change_quantity_home_consumption_f

    """Отечественное потребление P"""
    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_p(P_PDP_1,P_PDP_0):
        return P_PDP_1/P_PDP_0-1

    perc_change_price_home_consumption_p = perc_change_price_home_consumption_p(P_PDP_1,P_PDP_0)
    result['perc_change_price_home_consumption_p'] = perc_change_price_home_consumption_p

    #     # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_p(Q_PDP_1, Q_PDP_0):
        return Q_PDP_1/Q_PDP_0-1
    perc_change_quantity_home_consumption_p = perc_change_quantity_home_consumption_p(Q_PDP_1, Q_PDP_0)
    result['perc_change_quantity_home_consumption_p'] = perc_change_quantity_home_consumption_p

    """Нетто импорт P"""
    # Изменение (%) Цена (P)
    def perc_change_price_netto_import(P_PXM_1, P_PXM_0):
        return P_PXM_1/P_PXM_0-1
    perc_change_price_netto_import = perc_change_price_netto_import(P_PXM_1, P_PXM_0)
    result['perc_change_price_netto_import'] = perc_change_price_netto_import

    # Изменение (%) Количество (Q)
    def perc_change_quantity_netto_import(Q_PXM_1, Q_PXM_0):
        return Q_PXM_1/Q_PXM_0-1
    perc_change_quantity_netto_import = perc_change_quantity_netto_import(Q_PXM_1, Q_PXM_0)
    result['perc_change_quantity_netto_import'] = perc_change_quantity_netto_import

    """Общее образование P"""
    # Изменение (%) Цена (P)
    def perc_change_price_general_education(P_PDC_1, P_PDC_0):
        return P_PDC_1/P_PDC_0-1
    perc_change_price_general_education = perc_change_price_general_education(P_PDC_1, P_PDC_0)
    result['perc_change_price_general_education'] = perc_change_price_general_education

    # Изменение (%) Количество (Q)
    def perc_change_quantity_general_education(Q_PDC_1, Q_PDC_0):
        return Q_PDC_1/Q_PDC_0-1

    perc_change_quantity_general_education = perc_change_quantity_general_education(Q_PDC_1, Q_PDC_0)
    result['perc_change_quantity_general_education'] = perc_change_quantity_general_education

    """Отечественное производство товара F"""
    # Изменение (%) Цена (P)
    def perc_change_price_home_production_f(P_FDP_1, P_FDP_0):
        return P_FDP_1/P_FDP_0-1
    perc_change_price_home_production_f = perc_change_price_home_production_f(P_FDP_1, P_FDP_0)
    result['perc_change_price_home_production_f'] = perc_change_price_home_production_f

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production_f(Q_FDP_1, Q_FDP_0):
        return Q_FDP_1/Q_FDP_0-1
    perc_change_quantity_home_production_f = perc_change_quantity_home_production_f(Q_FDP_1, Q_FDP_0)
    result['perc_change_quantity_home_production_f'] = perc_change_quantity_home_production_f

    """Экспорт товара F"""

    # Изменение (%) Цена (P)
    def perc_change_price_export_goodsself (P_FXP_1, P_FXP_0):
        return P_FXP_1/P_FXP_0-1
    perc_change_price_export_goodsself = perc_change_price_export_goodsself(P_FXP_1, P_FXP_0)
    result['perc_change_price_export_goodsself'] = perc_change_price_export_goodsself

    # Изменение (%) Количество (Q)
    def perc_change_quantity_export_goods(Q_FXP_1, Q_FXP_0):
        return Q_FXP_1/Q_FXP_0-1
    perc_change_quantity_export_goods = perc_change_quantity_export_goods(Q_FXP_1, Q_FXP_0)
    result['perc_change_quantity_export_goods'] = perc_change_quantity_export_goods

    """Поведенческие параметры"""

    σ_MIC = 2.5
    print(f'σ_MIC = {σ_MIC}')

    def r_σ_MIC(σ_MIC):
        return (σ_MIC-1)/σ_MIC
    r_σ_MIC = r_σ_MIC(σ_MIC)
    print(f'r_σ_MIC = {r_σ_MIC}')

    σ_PDP = 2.25
    print(f'σ_PDP = {σ_PDP}')

    def r_σ_PDP(σ_PDP):
        return (σ_PDP-1)/σ_PDP
    r_σ_PDP = r_σ_PDP(σ_PDP)
    print(f'r_σ_PDP = {r_σ_PDP}')

    Ω_FDP = 2.95
    print(f'Ω_FDP = {Ω_FDP}')

    def r_Ω_FDP(Ω_FDP):
        return (Ω_FDP + 1) / Ω_FDP
    r_Ω_FDP = r_Ω_FDP(Ω_FDP)
    print(f'r_Ω_FDP = {r_Ω_FDP}')

    ε_MMI = 10
    ε_FDP = 0.3
    ε_PDP = -0.8822222222222221
    ε_PXM = 1
    ε_FXP = -10


    def Z_MMI(Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI):
        return Q_MMI_0/((P_MMI_0/(ER_0*(1+TMMI_0)*(1+NMMI_0)))**ε_MMI)
    Z_MMI = Z_MMI(Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI)
    print(f'Z_MMI = {Z_MMI}')

    def Z_FDP(Q_FDP_0, P_FDP_0, ε_FDP):
        return Q_FDP_0/(P_FDP_0)**ε_FDP
    Z_FDP = Z_FDP(Q_FDP_0, P_FDP_0, ε_FDP)
    print(f'Z_FDP = {Z_FDP}')

    def Z_PDP(Q_PDP_0, P_PDP_0, ε_PDP):
        return Q_PDP_0/(P_PDP_0)**ε_PDP
    Z_PDP = Z_PDP(Q_PDP_0, P_PDP_0, ε_PDP)
    print(f'Z_PDP = {Z_PDP}')

    def Z_PXM(Q_PXM_0, ER_0, ε_PXM):
        return Q_PXM_0/(1/ER_0)**ε_PXM
    Z_PXM = Z_PXM(Q_PXM_0, ER_0, ε_PXM)
    print(f'Z_PXM = {Z_PXM}')

    def Z_FXP(Q_FXP_0, P_FXP_0, ER_0, ε_FXP):
        return  Q_FXP_0/(P_FXP_0/ER_0)**ε_FXP
    Z_FXP = Z_FXP(Q_FXP_0, P_FXP_0, ER_0, ε_FXP)
    print(f'Z_FXP = {Z_FXP}')

    """Внешние значения"""

    EU = 0.3331729436173592
    EAEU = 0.6218762187426168
    Lab = 0.544
    profit = 0.098
    NoL = 14.142756
    Tax = 0.03374120043652237
    VAT = 0.2

    """Относительное качество"""

    def K_MMI(Q_MMI_0, Q_MDI_0, r_σ_MIC, P_MMI_0, P_MDI_0):
        return (Q_MMI_0/Q_MDI_0)**(1-r_σ_MIC)*(P_MMI_0/P_MDI_0)
    K_MMI = K_MMI(Q_MMI_0, Q_MDI_0, r_σ_MIC, P_MMI_0, P_MDI_0)
    print(f'K_MMI = {K_MMI}')

    K_MDI = 1

    def E20(Q_MIC_0, K_MMI, Q_MMI_0, r_σ_MIC, K_MDI, Q_MDI_0):
        return Q_MIC_0/(K_MMI*Q_MMI_0**r_σ_MIC+K_MDI*Q_MDI_0**r_σ_MIC)**(1/r_σ_MIC)
    E20 = E20(Q_MIC_0, K_MMI, Q_MMI_0, r_σ_MIC, K_MDI, Q_MDI_0)
    print(f'E20 = {E20}')

    K_SDP = 1

    def K_FDC(Q_FDC_0, Q_SDP_0, r_σ_PDP, P_FDC_0, P_SDP_0):
        return (Q_FDC_0/Q_SDP_0)**(1-r_σ_PDP)*(P_FDC_0/P_SDP_0)
    K_FDC = K_FDC(Q_FDC_0, Q_SDP_0, r_σ_PDP, P_FDC_0, P_SDP_0)
    print(f'K_FDC = {K_FDC}')

    def E23(Q_PDP_0, K_SDP, Q_SDP_0, r_σ_PDP, K_FDC, Q_FDC_0):
        return Q_PDP_0/(K_SDP*Q_SDP_0**r_σ_PDP+K_FDC*Q_FDC_0**r_σ_PDP)**(1/r_σ_PDP)
    E23 = E23(Q_PDP_0, K_SDP, Q_SDP_0, r_σ_PDP, K_FDC, Q_FDC_0)
    print(f'E23 = {E23}')

    def K_FXP(Q_FXP_0, Q_FDC_0, r_Ω_FDP, P_FXP_0, K_FDC, P_FDC_0):
        return ((Q_FXP_0/Q_FDC_0)**(1-r_Ω_FDP))*(P_FXP_0*K_FDC/P_FDC_0)
    K_FXP = K_FXP(Q_FXP_0, Q_FDC_0, r_Ω_FDP, P_FXP_0, K_FDC, P_FDC_0)
    print(f'K_FXP = {K_FXP}')

    """Уравнения"""

    def MMI_SUPPLY(Q_MMI_1, Z_MMI, P_MMI_1, NMMI_1, TMMI_1, ER_1, ε_MMI):
        return Q_MMI_1-Z_MMI*(P_MMI_1/((1+NMMI_1)*(1+TMMI_1)*ER_1))**ε_MMI
    MMI_SUPPLY = MMI_SUPPLY(Q_MMI_1, Z_MMI, P_MMI_1, NMMI_1, TMMI_1, ER_1, ε_MMI)
    print(f'MMI_SUPPLY = {MMI_SUPPLY}')

    def MIC_BUD_CES(P_MIC_1, Q_MIC_1, P_MDI_1, Q_MDI_1, P_MMI_1, Q_MMI_1):
        return P_MIC_1*Q_MIC_1-P_MDI_1*Q_MDI_1-P_MMI_1*Q_MMI_1
    MIC_BUD_CES = MIC_BUD_CES(P_MIC_1, Q_MIC_1, P_MDI_1, Q_MDI_1, P_MMI_1, Q_MMI_1)
    print(f'MIC_BUD_CES = {MIC_BUD_CES}')





    # result_to_front = {
    #     'Базовое равновесие': [
    #         ER_0,
    #         P_MMI_USD_0,
    #         NMMI_0,
    #         TMMI_0,
    #         K_0,
    #         SVA_0,
    #         SH_0,
    #         basic_total_fiber_decrease
    #     ],
    #     ' Новое равновесие':[
    #         ER_1,
    #         NMMI_1,
    #         TMMI_0,
    #         K_1,
    #         SVA_1,
    #         SH_1,
    #         new_total_fiber_decrease
    #     ]
    # }
    # return result_to_front

user_values = [72.14, 0.18, 1.29, 0.01890618906286916, 14.686756, 0.8555, 15.139, 38, 42, 42, 3822, 2999, 1006,
               4186, 2125]
print(calc(user_values))
