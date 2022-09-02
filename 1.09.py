import math


def calc(user_values):
    result = dict()

    """Управляющие воздействия модели"""

    ER_0 = user_values[0]
    result['ER_0'] = ER_0

    ER_1 = ER_0 * 1.2
    result['ER_1'] = ER_1

    P_MMI_USD_0 = user_values[1]
    result['P_MMI_USD_0'] = P_MMI_USD_0

    NMMI_0 = user_values[2]
    result['NMMI_0'] = NMMI_0

    NMMI_1 = 0
    result['NMMI_1'] = NMMI_1

    TMMI_0 = user_values[3]
    result['TMMI_0'] = TMMI_0

    TMMI_1 = 0
    result['TMMI_1'] = TMMI_1

    SVA_0 = user_values[4]
    result['SVA_0'] = SVA_0

    SVA_1 = SVA_0
    result['SVA_1'] = SVA_1

    SH_0 = user_values[5]
    result['SH_0'] = SH_0

    SH_1 = SH_0
    result['SH_1'] = SH_1

    """Наименование переменной"""

    P_MDI_0 = user_values[6]
    result['P_MDI_0'] = P_MDI_0

    P_FDP_0 = user_values[7]
    result['P_FDP_0'] = P_FDP_0

    P_FXP_0 = user_values[8]
    result['P_FXP_0'] = P_FXP_0

    Q_MMI_0 = user_values[9]
    result['Q_MMI_0'] = Q_MMI_0

    Q_MDI_0 = user_values[10]
    result['Q_MDI_0'] = Q_MDI_0

    Q_SDP_0 = user_values[11]
    result['Q_SDP_0'] = Q_SDP_0

    Q_FDC_0 = user_values[12]
    result['Q_FDC_0'] = Q_FDC_0

    Q_PDC_0 = user_values[13]
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

    def Q_MIC_0(Q_MDI_0, Q_MMI_0):
        return Q_MDI_0 + Q_MMI_0
    Q_MIC_0 = Q_MIC_0(Q_MDI_0, Q_MMI_0)
    result['Q_MIC_0'] = Q_MIC_0

    def basic_total_fiber_decrease(K_0, OUT_0, SH_0):
        return K_0 * OUT_0 * SH_0
    basic_total_fiber_decrease = basic_total_fiber_decrease(K_0, OUT_0, SH_0)
    result['basic_total_fiber_decrease'] = basic_total_fiber_decrease

    P_MDI_1 = 15.6016971682569
    result['P_MDI_1'] = P_MDI_1

    def K_1(P_MDI_1, Λ_1):
        return (1 - math.exp(-P_MDI_1 / Λ_1))
    K_1 = K_1(-P_MDI_1, Λ_1)
    result['K_1'] = K_1

    def new_total_fiber_decrease(K_1, OUT_1, SH_1):
        return K_1 * OUT_1 * SH_1
    new_total_fiber_decrease = new_total_fiber_decrease(K_1, OUT_1, SH_1)
    result['new_total_fiber_decrease'] = new_total_fiber_decrease

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

    Q_FDP_0 = user_values[14]
    result['Q_FDP_0'] = Q_FDP_0

    Q_FXP_0 = Q_FDP_0 - Q_FDC_0
    result['Q_FXP_0'] = Q_FXP_0

    Q_PXM_0 = Q_PDC_0 - Q_PDP_0
    result['Q_PXM_0'] = Q_PXM_0

    P_FDC_0 = (P_FDP_0 * Q_FDP_0 - P_FXP_0 * Q_FXP_0) / Q_FDC_0
    result['P_FDC_0'] = P_FDC_0

    P_PDP_0 = (P_SDP_0 * Q_SDP_0 + P_FDC_0 * Q_FDC_0) / Q_PDP_0
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
        return P_MMI_1 / P_MMI_0 - 1
    perc_change_price_good_import = perc_change_price_good_import(P_MMI_1, P_MMI_0)
    result['perc_change_price_good_import'] = perc_change_price_good_import

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import(Q_MMI_1, Q_MMI_0):
        return Q_MMI_1 / Q_MMI_0 - 1
    perc_change_quantity_good_import = perc_change_quantity_good_import(Q_MMI_1, Q_MMI_0)
    result['perc_change_quantity_good_import'] = perc_change_quantity_good_import

    """Потребление отечественного товара M"""

    # Изменение (%) Цена (P)
    def perc_change_price_consumption_home_goods(P_MDI_1, P_MDI_0):
        return P_MDI_1 / P_MDI_0 - 1
    perc_change_price_consumption_home_goods = perc_change_price_consumption_home_goods(P_MDI_1, P_MDI_0)
    result['perc_change_price_consumption_home_goods'] = perc_change_price_consumption_home_goods

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import_consumption_home_goods(Q_MDI_1, Q_MDI_0):
        return Q_MDI_1 / Q_MDI_0 - 1
    perc_change_quantity_good_import_consumption_home_goods = perc_change_quantity_good_import_consumption_home_goods(
        Q_MDI_1, Q_MDI_0)
    result['perc_change_quantity_good_import_consumption_home_goods'] = perc_change_quantity_good_import_consumption_home_goods

    """Потребление отраслью S товара M"""

    # Изменение (%) Цена (P)
    def perc_change_price_good_consumption(P_MIC_1, P_MIC_0):
        return P_MIC_1 / P_MIC_0 - 1
    perc_change_price_good_consumption = perc_change_price_good_consumption(P_MIC_1, P_MIC_0)
    result['perc_change_price_good_consumption'] = perc_change_price_good_consumption

    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_consumption(Q_MIC_1, Q_MIC_0):
        return Q_MIC_1 / Q_MIC_0 - 1
    perc_change_quantity_good_consumption = perc_change_quantity_good_consumption(Q_MIC_1, Q_MIC_0)
    result['perc_change_quantity_good_consumption'] = perc_change_quantity_good_consumption

    """Отечественное производство S"""

    # Изменение (%) Цена (P)
    def perc_change_price_home_production(P_SDP_1, P_SDP_0):
        return P_SDP_1 / P_SDP_0 - 1
    perc_change_price_home_production = perc_change_price_home_production(P_SDP_1, P_SDP_0)
    result['perc_change_price_home_production'] = perc_change_price_home_production

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production(Q_SDP_1, Q_SDP_0):
        return Q_SDP_1 / Q_SDP_0 - 1
    perc_change_quantity_home_production = perc_change_quantity_home_production(Q_SDP_1, Q_SDP_0)
    result['perc_change_quantity_home_production'] = perc_change_quantity_home_production

    """Отечественное потребление F"""

    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_f(P_FDC_1, P_FDC_0):
        return P_FDC_1 / P_FDC_0 - 1
    perc_change_price_home_consumption_f = perc_change_price_home_consumption_f(P_FDC_1, P_FDC_0)
    result['perc_change_price_home_consumption_f'] = perc_change_price_home_consumption_f

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_f(Q_FDC_1, Q_FDC_0):
        return Q_FDC_1 / Q_FDC_0 - 1
    perc_change_quantity_home_consumption_f = perc_change_quantity_home_consumption_f(Q_FDC_1, Q_FDC_0)
    result['perc_change_quantity_home_consumption_f'] = perc_change_quantity_home_consumption_f

    """Отечественное потребление P"""

    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_p(P_PDP_1, P_PDP_0):
        return P_PDP_1 / P_PDP_0 - 1
    perc_change_price_home_consumption_p = perc_change_price_home_consumption_p(P_PDP_1, P_PDP_0)
    result['perc_change_price_home_consumption_p'] = perc_change_price_home_consumption_p

    #     # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_p(Q_PDP_1, Q_PDP_0):
        return Q_PDP_1 / Q_PDP_0 - 1
    perc_change_quantity_home_consumption_p = perc_change_quantity_home_consumption_p(Q_PDP_1, Q_PDP_0)
    result['perc_change_quantity_home_consumption_p'] = perc_change_quantity_home_consumption_p

    """Нетто импорт P"""

    # Изменение (%) Цена (P)
    def perc_change_price_netto_import(P_PXM_1, P_PXM_0):
        return P_PXM_1 / P_PXM_0 - 1
    perc_change_price_netto_import = perc_change_price_netto_import(P_PXM_1, P_PXM_0)
    result['perc_change_price_netto_import'] = perc_change_price_netto_import

    # Изменение (%) Количество (Q)
    def perc_change_quantity_netto_import(Q_PXM_1, Q_PXM_0):
        return Q_PXM_1 / Q_PXM_0 - 1
    perc_change_quantity_netto_import = perc_change_quantity_netto_import(Q_PXM_1, Q_PXM_0)
    result['perc_change_quantity_netto_import'] = perc_change_quantity_netto_import

    """Общее образование P"""

    # Изменение (%) Цена (P)
    def perc_change_price_general_education(P_PDC_1, P_PDC_0):
        return P_PDC_1 / P_PDC_0 - 1
    perc_change_price_general_education = perc_change_price_general_education(P_PDC_1, P_PDC_0)
    result['perc_change_price_general_education'] = perc_change_price_general_education

    # Изменение (%) Количество (Q)
    def perc_change_quantity_general_education(Q_PDC_1, Q_PDC_0):
        return Q_PDC_1 / Q_PDC_0 - 1
    perc_change_quantity_general_education = perc_change_quantity_general_education(Q_PDC_1, Q_PDC_0)
    result['perc_change_quantity_general_education'] = perc_change_quantity_general_education

    """Отечественное производство товара F"""

    # Изменение (%) Цена (P)
    def perc_change_price_home_production_f(P_FDP_1, P_FDP_0):
        return P_FDP_1 / P_FDP_0 - 1
    perc_change_price_home_production_f = perc_change_price_home_production_f(P_FDP_1, P_FDP_0)
    result['perc_change_price_home_production_f'] = perc_change_price_home_production_f

    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production_f(Q_FDP_1, Q_FDP_0):
        return Q_FDP_1 / Q_FDP_0 - 1
    perc_change_quantity_home_production_f = perc_change_quantity_home_production_f(Q_FDP_1, Q_FDP_0)
    result['perc_change_quantity_home_production_f'] = perc_change_quantity_home_production_f

    """Экспорт товара F"""

    # Изменение (%) Цена (P)
    def perc_change_price_export_goodsself(P_FXP_1, P_FXP_0):
        return P_FXP_1 / P_FXP_0 - 1
    perc_change_price_export_goodsself = perc_change_price_export_goodsself(P_FXP_1, P_FXP_0)
    result['perc_change_price_export_goodsself'] = perc_change_price_export_goodsself

    # Изменение (%) Количество (Q)
    def perc_change_quantity_export_goods(Q_FXP_1, Q_FXP_0):
        return Q_FXP_1 / Q_FXP_0 - 1
    perc_change_quantity_export_goods = perc_change_quantity_export_goods(Q_FXP_1, Q_FXP_0)
    result['perc_change_quantity_export_goods'] = perc_change_quantity_export_goods

    """Поведенческие параметры"""

    σ_MIC = 2.5

    def r_σ_MIC(σ_MIC):
        return (σ_MIC - 1) / σ_MIC

    r_σ_MIC = r_σ_MIC(σ_MIC)
    result['r_σ_MIC'] = r_σ_MIC

    σ_PDP = 2.25

    def r_σ_PDP(σ_PDP):
        return (σ_PDP - 1) / σ_PDP

    r_σ_PDP = r_σ_PDP(σ_PDP)
    result['r_σ_PDP'] = r_σ_PDP

    Ω_FDP = 2.95

    def r_Ω_FDP(Ω_FDP):
        return (Ω_FDP + 1) / Ω_FDP

    r_Ω_FDP = r_Ω_FDP(Ω_FDP)
    result['r_Ω_FDP'] = r_Ω_FDP

    ε_MMI = 10
    ε_FDP = 0.3
    ε_PDP = -0.8822222222222221
    ε_PXM = 1
    ε_FXP = -10

    def Z_MMI(Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI):
        return Q_MMI_0 / ((P_MMI_0 / (ER_0 * (1 + TMMI_0) * (1 + NMMI_0))) ** ε_MMI)
    Z_MMI = Z_MMI(Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI)
    result['r_Ω_FDP'] = r_Ω_FDP

    def Z_FDP(Q_FDP_0, P_FDP_0, ε_FDP):
        return Q_FDP_0 / (P_FDP_0) ** ε_FDP
    Z_FDP = Z_FDP(Q_FDP_0, P_FDP_0, ε_FDP)
    result['Z_FDP'] = Z_FDP

    def Z_PDP(Q_PDP_0, P_PDP_0, ε_PDP):
        return Q_PDP_0 / (P_PDP_0) ** ε_PDP
    Z_PDP = Z_PDP(Q_PDP_0, P_PDP_0, ε_PDP)
    result['Z_PDP'] = Z_PDP

    def Z_PXM(Q_PXM_0, ER_0, ε_PXM):
        return Q_PXM_0 / (1 / ER_0) ** ε_PXM
    Z_PXM = Z_PXM(Q_PXM_0, ER_0, ε_PXM)
    result['Z_PXM'] = Z_PXM

    def Z_FXP(Q_FXP_0, P_FXP_0, ER_0, ε_FXP):
        return Q_FXP_0 / (P_FXP_0 / ER_0) ** ε_FXP
    Z_FXP = Z_FXP(Q_FXP_0, P_FXP_0, ER_0, ε_FXP)
    result['Z_FXP'] = Z_FXP

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
        return (Q_MMI_0 / Q_MDI_0) ** (1 - r_σ_MIC) * (P_MMI_0 / P_MDI_0)

    K_MMI = K_MMI(Q_MMI_0, Q_MDI_0, r_σ_MIC, P_MMI_0, P_MDI_0)

    K_MDI = 1

    def E20(Q_MIC_0, K_MMI, Q_MMI_0, r_σ_MIC, K_MDI, Q_MDI_0):
        return Q_MIC_0 / (K_MMI * Q_MMI_0 ** r_σ_MIC + K_MDI * Q_MDI_0 ** r_σ_MIC) ** (1 / r_σ_MIC)

    E20 = E20(Q_MIC_0, K_MMI, Q_MMI_0, r_σ_MIC, K_MDI, Q_MDI_0)

    K_SDP = 1

    def K_FDC(Q_FDC_0, Q_SDP_0, r_σ_PDP, P_FDC_0, P_SDP_0):
        return (Q_FDC_0 / Q_SDP_0) ** (1 - r_σ_PDP) * (P_FDC_0 / P_SDP_0)

    K_FDC = K_FDC(Q_FDC_0, Q_SDP_0, r_σ_PDP, P_FDC_0, P_SDP_0)

    def E23(Q_PDP_0, K_SDP, Q_SDP_0, r_σ_PDP, K_FDC, Q_FDC_0):
        return Q_PDP_0 / (K_SDP * Q_SDP_0 ** r_σ_PDP + K_FDC * Q_FDC_0 ** r_σ_PDP) ** (1 / r_σ_PDP)

    E23 = E23(Q_PDP_0, K_SDP, Q_SDP_0, r_σ_PDP, K_FDC, Q_FDC_0)

    def K_FXP(Q_FXP_0, Q_FDC_0, r_Ω_FDP, P_FXP_0, K_FDC, P_FDC_0):
        return ((Q_FXP_0 / Q_FDC_0) ** (1 - r_Ω_FDP)) * (P_FXP_0 * K_FDC / P_FDC_0)

    K_FXP = K_FXP(Q_FXP_0, Q_FDC_0, r_Ω_FDP, P_FXP_0, K_FDC, P_FDC_0)

    """Уравнения"""

    def MMI_SUPPLY(Q_MMI_1, Z_MMI, P_MMI_1, NMMI_1, TMMI_1, ER_1, ε_MMI):
        return Q_MMI_1 - Z_MMI * (P_MMI_1 / ((1 + NMMI_1) * (1 + TMMI_1) * ER_1)) ** ε_MMI
    MMI_SUPPLY = MMI_SUPPLY(Q_MMI_1, Z_MMI, P_MMI_1, NMMI_1, TMMI_1, ER_1, ε_MMI)

    def MIC_BUD_CES(P_MIC_1, Q_MIC_1, P_MDI_1, Q_MDI_1, P_MMI_1, Q_MMI_1):
        return P_MIC_1 * Q_MIC_1 - P_MDI_1 * Q_MDI_1 - P_MMI_1 * Q_MMI_1
    MIC_BUD_CES = MIC_BUD_CES(P_MIC_1, Q_MIC_1, P_MDI_1, Q_MDI_1, P_MMI_1, Q_MMI_1)

    def MIC_CES(Q_MMI_1, Q_MDI_1, P_MMI_1, P_MDI_1, K_MDI, K_MMI, r_σ_MIC):
        return Q_MMI_1 / Q_MDI_1 - ((P_MMI_1 / (P_MDI_1)) * (K_MDI / K_MMI)) ** (1 / (r_σ_MIC - 1))
    MIC_CES = MIC_CES(Q_MMI_1, Q_MDI_1, P_MMI_1, P_MDI_1, K_MDI, K_MMI, r_σ_MIC)

    def MIC_BAL_CES(Q_MIC_1, Q_MDI_1, Q_MMI_1):
        return Q_MIC_1 - Q_MDI_1 - Q_MMI_1
    MIC_BAL_CES = MIC_BAL_CES(Q_MIC_1, Q_MDI_1, Q_MMI_1)

    def SDP_P(P_SDP_1, P_MIC_1, OUT_1, SVA_1):
        return P_SDP_1 - P_MIC_1 / OUT_1 - SVA_1
    SDP_P = SDP_P(P_SDP_1, P_MIC_1, OUT_1, SVA_1)

    def SDP_Q(Q_SDP_1, Q_MIC_1, OUT_1, SH_1):
        return Q_SDP_1 - Q_MIC_1 * OUT_1 * SH_1
    SDP_Q = SDP_Q(Q_SDP_1, Q_MIC_1, OUT_1, SH_1)

    def FDP_SUPPLY(Q_FDP_1, Z_FDP, P_FDP_1, ε_FDP):
        return Q_FDP_1 - Z_FDP * (P_FDP_1) ** ε_FDP
    FDP_SUPPLY = FDP_SUPPLY(Q_FDP_1, Z_FDP, P_FDP_1, ε_FDP)

    def FDP_BUD_CET(P_FDP_1, Q_FDP_1, P_FDC_1, Q_FDC_1, P_FXP_1, Q_FXP_1):
        return P_FDP_1 * Q_FDP_1 - P_FDC_1 * Q_FDC_1 - P_FXP_1 * Q_FXP_1
    FDP_BUD_CET = FDP_BUD_CET(P_FDP_1, Q_FDP_1, P_FDC_1, Q_FDC_1, P_FXP_1, Q_FXP_1)

    def FDP_CET(Q_FXP_1, Q_FDC_1, P_FXP_1, P_FDC_1, K_FDC, K_FXP, r_Ω_FDP):
        return Q_FXP_1 / Q_FDC_1 - ((P_FXP_1 / (P_FDC_1)) * (K_FDC / K_FXP)) ** (1 / (r_Ω_FDP - 1))
    FDP_CET = FDP_CET(Q_FXP_1, Q_FDC_1, P_FXP_1, P_FDC_1, K_FDC, K_FXP, r_Ω_FDP)

    def FDP_BAL_CET(Q_FDP_1, Q_FDC_1, Q_FXP_1):
        return Q_FDP_1 - Q_FDC_1 - Q_FXP_1
    FDP_BAL_CET = FDP_BAL_CET(Q_FDP_1, Q_FDC_1, Q_FXP_1)

    def FXP_DEMAND(Q_FXP_1, Z_FXP, P_FXP_1, ER_1, ε_FXP):
        return Q_FXP_1 - Z_FXP * (P_FXP_1 / ER_1) ** ε_FXP
    FXP_DEMAND = FXP_DEMAND(Q_FXP_1, Z_FXP, P_FXP_1, ER_1, ε_FXP)

    def PDP_BUD_CES(P_PDP_1, Q_PDP_1, P_SDP_1, Q_SDP_1, P_FDC_1, Q_FDC_1):
        return P_PDP_1 * Q_PDP_1 - P_SDP_1 * Q_SDP_1 - P_FDC_1 * Q_FDC_1
    PDP_BUD_CES = PDP_BUD_CES(P_PDP_1, Q_PDP_1, P_SDP_1, Q_SDP_1, P_FDC_1, Q_FDC_1)

    def PDP_CES(Q_SDP_1, Q_FDC_1, P_SDP_1, P_FDC_1, K_FDC, K_SDP, r_σ_PDP):
        return Q_SDP_1 / Q_FDC_1 - ((P_SDP_1 / (P_FDC_1)) * (K_FDC / K_SDP)) ** (1 / (r_σ_PDP - 1))
    PDP_CES = PDP_CES(Q_SDP_1, Q_FDC_1, P_SDP_1, P_FDC_1, K_FDC, K_SDP, r_σ_PDP)

    def PDP_BAL_CES(Q_PDP_1, Q_SDP_1, Q_FDC_1):
        return Q_PDP_1 - Q_SDP_1 - Q_FDC_1
    PDP_BAL_CES = PDP_BAL_CES(Q_PDP_1, Q_SDP_1, Q_FDC_1)

    def PDP_DEMAND(Q_PDP_1, Z_PDP, P_PDP_1, ε_PDP):
        return Q_PDP_1 - Z_PDP * (P_PDP_1) ** ε_PDP
    PDP_DEMAND = PDP_DEMAND(Q_PDP_1, Z_PDP, P_PDP_1, ε_PDP)

    def PXM_SUPPLY(Q_PXM_1, Z_PXM, ER_1, ε_PXM):
        return Q_PXM_1 - Z_PXM * (1 / ER_1) ** ε_PXM
    PXM_SUPPLY = PXM_SUPPLY(Q_PXM_1, Z_PXM, ER_1, ε_PXM)

    def PDC_BAL(Q_PDC_1, Q_PXM_1, Q_PDP_1):
        return Q_PDC_1 - Q_PXM_1 - Q_PDP_1
    PDC_BAL = PDC_BAL(Q_PDC_1, Q_PXM_1, Q_PDP_1)

    def PDC_P(P_PDC_1, P_MDI_1):
        return P_PDC_1 - P_MDI_1
    PDC_P = PDC_P(P_PDC_1, P_MDI_1)

    def MDI_BAL(Q_MDI_1, Q_PDC_1, P_MDI_1, Λ_1):
        return Q_MDI_1 - Q_PDC_1 * (1 - math.exp(-P_MDI_1 / Λ_1))
    MDI_BAL = MDI_BAL(Q_MDI_1, Q_PDC_1, P_MDI_1, Λ_1)

    def PXM_P(P_PXM_1, P_MDI_1):
        return P_PXM_1 - P_MDI_1
    PXM_P = PXM_P(P_PXM_1, P_MDI_1)

    result_to_front = {
        'Управляющие воздействия модели': [
            {id: '1', title: 'Курс RUB/USD', params: 'ER', basebalance: 'ER_0', newbalance: 'ER_1'},
            {id: '2', title: 'Цена импорта макулатуры USD (без тарифа), долл. США за кг', params: 'P_MMI_USD_0',
             basebalance: '0.18', newbalance: None},
            {id: '3', title: 'Импортный нетарифный барьер на макулатуру', params: 'NMMI', basebalance: 'NMMI_0',
             newbalance: 'NMMI_1'},
            {id: '4', title: 'Импортный тариф на макулатуру', params: 'TMMI', basebalance: 'TMMI_0',
             newbalance: 'TMMI_1'},
            {id: '5', title: 'Собираемость макулатуры', params: 'K', basebalance: 'K_0', newbalance: 'K_1'},
            {id: '6', title: 'Прочие переменные издержки производства макулатурного картона (руб./кг)', params: 'SVA',
             basebalance: 'SVA_0', newbalance: 'SVA_1'},
            {id: '7', title: 'Доля собираемой макулатуры для производства картона', params: 'SH', basebalance: 'SH_0',
             newbalance: 'SH_1'},
            {id: '8', title: 'Общее убывание волокна', params: ' ', basebalance: 'basic_total_fiber_decrease',
             newbalance: 'new_total_fiber_decrease'}
        ],
        'Наименование переменной': [
            {id: '1',
             title: 'Импорт макулатуры',
             params: 'MMI',
             basebalance_pr: 'P_MMI_0',
             basebalance_quan: 'Q_MMI_0',
             newbalance_pr: 'P_MMI_1',
             newbalance_pr: 'Q_MMI_1',
             perc_change_price_good_import: 'perc_change_price_good_import',
             perc_change_quantity_good_import: 'perc_change_quantity_good_import'},

            {id: '2',
             title: 'Потребление отечественной макулатуры',
             params: 'MDI',
             basebalance_pr: 'P_MDI_0',
             basebalance_quan: 'Q_MDI_0',
             newbalance_pr: 'P_MDI_1',
             newbalance_pr: 'Q_MDI_1',
             perc_change_price_consumption_home_goods: 'perc_change_price_consumption_home_goods',
             perc_change_quantity_good_import_consumption_home_goods: 'perc_change_quantity_good_import_consumption_home_goods'},

            {id: '3',
             title: 'Потребление макулатуры',
             params: 'MIC',
             basebalance_pr: 'P_MIC_0',
             basebalance_quan: 'Q_MIC_0',
             newbalance_pr: 'P_MIC_1',
             newbalance_pr: 'Q_MIC_1',
             perc_change_price_good_consumption: 'perc_change_price_good_consumption',
             perc_change_quantity_good_consumption: 'perc_change_quantity_good_consumption'},

            {id: '4',
             title: 'Отечественное производство макулатурных тарных картонов',
             params: 'SDP',
             basebalance_pr: 'P_SDP_0',
             basebalance_quan: 'Q_SDP_1',
             newbalance_pr: 'P_SDP_1',
             newbalance_pr: 'Q_SDP_1',
             perc_change_price_home_production: 'perc_change_price_home_production',
             perc_change_quantity_home_production: 'perc_change_quantity_home_production'},

            {id: '5',
             title: 'Отечественное потребление целлюлозных тарных картонов',
             params: 'FDC',
             basebalance_pr: 'P_FDC_0',
             basebalance_quan: 'Q_FDC_0',
             newbalance_pr: 'P_FDC_1',
             newbalance_pr: 'Q_FDC_1',
             perc_change_price_home_consumption_f: 'perc_change_price_home_consumption_f',
             perc_change_quantity_home_consumption_f: 'perc_change_quantity_home_consumption_f'},

            {id: '6',
             title: 'Отечественное потребление тарных картонов',
             params: 'PDP',
             basebalance_pr: 'P_PDP_0',
             basebalance_quan: 'Q_PDP_0',
             newbalance_pr: 'P_PDP_1',
             newbalance_pr: 'Q_PDP_1',
             perc_change_price_home_consumption_p: 'perc_change_price_home_consumption_p',
             perc_change_quantity_home_consumption_p: 'perc_change_quantity_home_consumption_p'},

            {id: '7',
             title: 'Нетто импорт тарных картнов в составе упакованных товаров',
             params: 'PXM',
             basebalance_pr: 'P_PXM_0',
             basebalance_quan: 'Q_PXM_0',
             newbalance_pr: 'P_PXM_1',
             newbalance_pr: 'Q_PXM_1',
             perc_change_price_netto_import: 'perc_change_price_netto_import',
             perc_change_quantity_netto_import: 'perc_change_quantity_netto_import'},

            {id: '8',
             title: 'Общее образование макулатуры',
             params: 'PDC',
             basebalance_pr: 'P_PDC_0',
             basebalance_quan: 'Q_PDC_0',
             newbalance_pr: 'P_PDC_1',
             newbalance_pr: 'Q_PDC_1',
             perc_change_price_general_education: 'perc_change_price_general_education',
             perc_change_quantity_general_education: 'perc_change_quantity_general_education'},

            {id: '9',
             title: 'Отечественное производство целлюлозных тарных картонов',
             params: 'FDP',
             basebalance_pr: 'P_FDP_0',
             basebalance_quan: 'Q_FDP_0',
             newbalance_pr: 'P_FDP_1',
             newbalance_pr: 'Q_FDP_1',
             perc_change_price_home_production_f: 'perc_change_price_home_production_f',
             perc_change_quantity_home_production_f: 'perc_change_quantity_home_production_f'},

            {id: '10',
             title: 'Экспорт целлюлозных тарных картонов',
             params: 'FXP',
             basebalance_pr: 'P_FXP_0',
             basebalance_quan: 'Q_FXP_0',
             newbalance_pr: 'P_FXP_1',
             newbalance_pr: 'Q_FXP_1',
             perc_change_price_export_goodsself: 'perc_change_price_export_goodsself',
             perc_change_quantity_export_goods: 'perc_change_quantity_export_goods'},

        ]}
    return result_to_front

user_values = [72.14, 0.18, 1.29, 0.01890618906286916, 14.686756, 0.8555, 15.139, 38, 42, 42, 3822, 2999, 1006,
               4186, 2125]
print(calc(user_values))

# -----------------------------------------------------------------------------

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

