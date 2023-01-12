from scipy.optimize import fsolve, root
from math import fsum, sqrt
import numpy as np

example_data = {'ER_before': 73.94,
                'ER_after': 73.94,
                'WP_after': 689.0,
                'DWP_CEL_after': 0.0,
                'E_WP_before': 689.0,
                'P_AXD_USD_before': 721.0,
                'P_AMD_USD_before': 1150.0,
                'P_IXD_USD_before': 150.0,
                'TAXD_before': 5.554,
                'TAXD_after': 5.554,
                'TIXD_before': 0.0,
                'TIXD_after': 0.0,
                'TAMD_before': 2.266,
                'TAMD_after': 2.266,
                'IPD_pr': 4113.0,
                'IPD_q': 312638500.0,
                'IXD_q': 25295000.0,
                'APD_pr': 46200.0,
                'APD_q': 62100000.0,
                'AXD_q': 30547000.0,
                'ADW_q': 445185000.0,
                'AMD_q': 4444000.0}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.ER_before = dict_from_frontend.get('ER_before')
        self.ER_after = dict_from_frontend.get('ER_after')
        self.WP_after = dict_from_frontend.get('WP_after')
        self.DWP_CEL_after = dict_from_frontend.get('DWP_CEL_after')
        self.E_WP_before = dict_from_frontend.get('E_WP_before')
        self.P_AXD_USD_before = dict_from_frontend.get('P_AXD_USD_before')
        self.P_AMD_USD_before = dict_from_frontend.get('P_AMD_USD_before')
        self.P_IXD_USD_before = dict_from_frontend.get('P_IXD_USD_before')
        self.TAXD_before = dict_from_frontend.get('TAXD_before')
        self.TAXD_after = dict_from_frontend.get('TAXD_after')
        self.TIXD_before = dict_from_frontend.get('TIXD_before')
        self.TIXD_after = dict_from_frontend.get('TIXD_after')
        self.TAMD_before = dict_from_frontend.get('TAMD_before')
        self.TAMD_after = dict_from_frontend.get('TAMD_after')
        self.IPD_pr = dict_from_frontend.get('IPD_pr')
        self.IPD_q = dict_from_frontend.get('IPD_q')
        self.IXD_q = dict_from_frontend.get('IXD_q')
        self.APD_pr = dict_from_frontend.get('APD_pr')
        self.APD_q = dict_from_frontend.get('APD_q')
        self.AXD_q = dict_from_frontend.get('AXD_q')
        self.ADW_q = dict_from_frontend.get('ADW_q')
        self.AMD_q = dict_from_frontend.get('AMD_q')


o = 14


def stepen(x, st):
    if (x < 0):
        # print(f'x={round(x, o)}, st={round(st, o)}')
        return np.sign(x) * (np.abs(x) ** st)
    else:
        return x ** st


def steel_market(input_data):
    """Вводим новые значения"""
    ER_0 = input_data.ER_before
    ER_1 = input_data.ER_after
    WP_1 = input_data.WP_after
    DWP_CEL_1 = input_data.DWP_CEL_after
    E_WP_0 = input_data.E_WP_before
    P_AXD_USD_0 = input_data.P_AXD_USD_before
    P_AMD_USD_0 = input_data.P_AMD_USD_before
    P_IXD_USD_0 = input_data.P_IXD_USD_before
    TAXD_0 = input_data.TAXD_before
    TAXD_1 = input_data.TAXD_after
    TIXD_0 = input_data.TIXD_before
    TIXD_1 = input_data.TIXD_after
    TAMD_0 = input_data.TAMD_before
    TAMD_1 = input_data.TAMD_after
    P_IPD_0 = input_data.IPD_pr
    Q_IPD_0 = input_data.IPD_q
    Q_IXD_0 = input_data.IXD_q
    P_APD_0 = input_data.APD_pr
    Q_APD_0 = input_data.APD_q
    Q_AXD_0 = input_data.AXD_q
    Q_ADW_0 = input_data.ADW_q
    Q_AMD_0 = input_data.AMD_q

    # Параметры

    Ω_IPD = 1.5
    σ_APD = 1.5
    Ω_APD = 3.0
    σ_ADW = 10.0
    σ_ATD = 3.0
    Ω_ATD = 1.5
    σ_BDD = 1.5
    ε_IPD = 0.3
    ε_IXD = -1.5
    ε_AVD = 0.6
    ε_ADW = -0.1
    ε_AXW = 3.0
    ε_AMD = 1.0
    ε_ADD = -0.9
    ε_BDD = -0.9
    ε_BVD = 0.9

    DER_0 = 0.0
    E_DWP_0 = 0.0

    SS_IPD_SUPPLY_0 = 0.0
    SS_IPD_SUPPLY_1 = 0.0
    DS_IXD_DEMAND_0 = 0.0
    DS_IXD_DEMAND_1 = 0.0
    SS_AVD_SUPPLY_0 = 0.0
    SS_AVD_SUPPLY_1 = 0.0
    DS_ADW_DEMAND_0 = 0.0
    SS_AXW_SUPPLY_0 = 0.0
    SS_AMD_SUPPLY_0 = 0.0
    DS_ADD_DEMAND_0 = 0.0
    DS_ADD_DEMAND_1 = 0.0
    DS_BDD_DEMAND_0 = 0.0
    DS_BDD_DEMAND_1 = 0.0
    SS_BVD_SUPPLY_0 = 0.0
    SS_BVD_SUPPLY_1 = 0.0

    DWP_0 = 0.0
    K_AID = 1.0
    Q_AVD_0 = 100.0
    K_ASD = 1.0
    K_BID = 1.0
    Q_BVD_0 = 100.0
    Q_BDD_0 = 100.0

    """Переводим значения, введенные пользователем, в проценты"""

    TAXD_0 = TAXD_0 / 100
    TAXD_1 = TAXD_1 / 100
    TIXD_0 = TIXD_0 / 100
    TIXD_1 = TIXD_1 / 100
    TAMD_0 = TAMD_0 / 100
    TAMD_1 = TAMD_1 / 100

    """Перерасчет ячеек с новыми значениями"""

    DER_1 = ER_1 / ER_0 - 1

    WP_0 = E_WP_0

    # если значение WP_1 введено - рассчитываем % сдвига
    try:
        if WP_1 != 0:
            DWP_CEL_1 = WP_1 / WP_0 - 1
    except ZeroDivisionError:
        print("Ошибка деления на ноль.")

    # если введен % - находим WP_1
    if WP_1 == 0:
        WP_1 = E_WP_0 / 100 * DWP_CEL_1 + WP_0

    DS_ADW_DEMAND_1 = (1 + DWP_CEL_1) ** (-ε_ADW) - 1

    SS_AXW_SUPPLY_1 = (1 + DWP_CEL_1) ** (-ε_AXW) - 1

    SS_AMD_SUPPLY_1 = (1 + DWP_CEL_1) ** (-ε_AMD) - 1

    P_IXD_0 = P_IXD_USD_0 * ER_0

    Q_AID_0 = Q_IPD_0 - Q_IXD_0

    P_AID_0 = (P_IPD_0 * Q_IPD_0 - P_IXD_0 * Q_IXD_0) / Q_AID_0

    P_AVD_0 = (P_APD_0 * Q_APD_0 - P_AID_0 * Q_AID_0) / Q_AVD_0

    P_AXD_0 = P_AXD_USD_0 * ER_0

    Q_AXW_0 = Q_ADW_0 - Q_AXD_0

    P_ADW_0 = WP_0 * ER_0

    P_AXW_0 = (P_ADW_0 * Q_ADW_0 - P_AXD_0 * (1 + TAXD_0) * Q_AXD_0) / Q_AXW_0

    Q_ASD_0 = Q_APD_0 - Q_AXD_0

    P_ASD_0 = (P_APD_0 * Q_APD_0 - P_AXD_0 * Q_AXD_0) / Q_ASD_0

    Q_ATD_0 = Q_ASD_0 + Q_AMD_0

    P_AMD_0 = P_AMD_USD_0 * ER_0

    P_ATD_0 = (P_ASD_0 * Q_ASD_0 + P_AMD_0 * (1 + TAMD_0) * Q_AMD_0) / Q_ATD_0

    P_BID_0 = P_ATD_0

    Q_BID_0 = 0.7 * Q_ATD_0

    Q_ADD_0 = Q_ATD_0 - Q_BID_0

    P_ADD_0 = (P_ATD_0 * Q_ATD_0 - P_BID_0 * Q_BID_0) / Q_ADD_0

    P_BDD_0 = (P_BID_0 * Q_BID_0 / 0.06) / Q_BDD_0

    P_BVD_0 = (P_BDD_0 * Q_BDD_0 - P_BID_0 * Q_BID_0) / Q_BVD_0

    # Вторая таблица параметров

    r_Ω_IPD = (Ω_IPD + 1) / Ω_IPD

    r_σ_APD = (σ_APD - 1) / σ_APD

    r_Ω_APD = (Ω_APD + 1) / Ω_APD

    r_σ_ADW = (σ_ADW - 1) / σ_ADW

    r_σ_ATD = (σ_ATD - 1) / σ_ATD

    r_Ω_ATD = (Ω_ATD + 1) / Ω_ATD

    r_σ_BDD = (σ_BDD - 1) / σ_BDD

    Z_IPD = Q_IPD_0 / (P_IPD_0 ** ε_IPD)

    Z_IXD = Q_IXD_0 / ((P_IXD_0 * (1 + TIXD_0) / ER_0) ** ε_IXD)

    Z_AVD = Q_AVD_0 / (P_AVD_0 ** ε_AVD)

    Z_ADW = Q_ADW_0 / (P_ADW_0 / ER_0) ** ε_ADW

    Z_AXW = Q_AXW_0 / (P_AXW_0 / ER_0) ** ε_AXW

    Z_AMD = Q_AMD_0 / (P_AMD_0 / ER_0) ** ε_AMD

    Z_ADD = Q_ADD_0 / (P_ADD_0) ** ε_ADD

    Z_BDD = Q_BDD_0 / (P_BDD_0) ** ε_BDD

    Z_BVD = Q_BVD_0 / (P_BVD_0) ** ε_BVD

    # Основная таблица

    K_IXD = ((Q_IXD_0 / Q_AID_0) ** (1 - r_Ω_IPD)) * (P_IXD_0 / P_AID_0)

    K_AVD = (Q_AVD_0 / Q_AID_0) ** (1 - r_σ_APD) * (P_AVD_0 / P_AID_0)

    A_APD = Q_APD_0 / (K_AID * Q_AID_0 ** r_σ_APD + K_AVD * Q_AVD_0 ** r_σ_APD) ** (1 / r_σ_APD)

    K_AXD = (Q_AXD_0 / Q_ASD_0) ** (1 - r_Ω_APD) * (P_AXD_0 / P_ASD_0)

    K_AXW = (Q_AXW_0 / Q_AXD_0) ** (1 - r_σ_ADW) * (P_AXW_0 / (P_AXD_0 * (1 + TAXD_0))) * K_AXD

    K_AMD = (Q_AMD_0 / Q_ASD_0) ** (1 - r_σ_ATD) * (P_AMD_0 * (1 + TAMD_0) / P_ASD_0)

    K_ADD = (Q_ADD_0 / Q_BID_0) ** (1 - r_Ω_ATD) * (P_ADD_0 / P_BID_0)

    K_BVD = (Q_BVD_0 / Q_BID_0) ** (1 - r_σ_BDD) * (P_BVD_0 / P_BID_0)

    A_BDD = Q_BDD_0 / (K_BID * Q_BID_0 ** r_σ_BDD + K_BVD * Q_BVD_0 ** r_σ_BDD) ** (1 / r_σ_BDD)

    def func(z):
        Q_IPD_1 = z[0]
        P_IPD_1 = z[1]
        P_IXD_1 = z[2]
        Q_IXD_1 = z[3]
        P_AID_1 = z[4]
        Q_AID_1 = z[5]
        Q_AVD_1 = z[6]
        P_AVD_1 = z[7]
        P_APD_1 = z[8]
        Q_APD_1 = z[9]
        P_AXD_1 = z[10]
        Q_AXD_1 = z[11]
        P_ASD_1 = z[12]
        Q_ASD_1 = z[13]
        P_ADW_1 = z[14]
        Q_ADW_1 = z[15]
        P_AXW_1 = z[16]
        Q_AXW_1 = z[17]
        P_ATD_1 = z[18]
        Q_ATD_1 = z[19]
        P_AMD_1 = z[20]
        Q_AMD_1 = z[21]
        P_ADD_1 = z[22]
        Q_ADD_1 = z[23]
        P_BDD_1 = z[24]
        Q_BDD_1 = z[25]
        P_BID_1 = z[26]
        Q_BID_1 = z[27]
        P_BVD_1 = z[28]
        Q_BVD_1 = z[29]

        IPD_SUPPLY = np.abs(Q_IPD_1) / (Z_IPD * (1 + SS_IPD_SUPPLY_1) * stepen(np.abs(P_IPD_1), ε_IPD)) - 1

        IPD_BUD_CET = np.abs(P_IPD_1) * np.abs(Q_IPD_1) / (
                    np.abs(P_IXD_1) * np.abs(Q_IXD_1) + np.abs(P_AID_1) * np.abs(Q_AID_1)) - 1

        IPD_CET = (np.abs(Q_IXD_1) / np.abs(Q_AID_1)) / stepen((np.abs(P_IXD_1) / (np.abs(P_AID_1))) * (K_AID / K_IXD),
                                                               (1 / (r_Ω_IPD - 1))) - 1

        IPD_BAL_CET = np.abs(Q_IPD_1) / (np.abs(Q_AID_1) + np.abs(Q_IXD_1)) - 1

        IXD_DEMAND = np.abs(Q_IXD_1) / (
                    Z_IXD * (1 + DS_IXD_DEMAND_1) * stepen(np.abs(P_IXD_1) * (1 + TIXD_1) / (ER_1), ε_IXD)) - 1

        AVD_SUPPLY = np.abs(Q_AVD_1) / (Z_AVD * (1 + SS_AVD_SUPPLY_1) * stepen(np.abs(P_AVD_1), ε_AVD)) - 1

        APD_BUD_CES = np.abs(P_APD_1) * np.abs(Q_APD_1) / (
                    np.abs(P_AID_1) * np.abs(Q_AID_1) + np.abs(P_AVD_1) * np.abs(Q_AVD_1)) - 1

        APD_CES = np.abs(Q_AVD_1) / np.abs(Q_AID_1) / stepen((np.abs(P_AVD_1) / (np.abs(P_AID_1))) * (K_AID / K_AVD),
                                                             (1 / (r_σ_APD - 1))) - 1

        APD_BAL_CES = np.abs(Q_APD_1) / (
                    A_APD * stepen(K_AID * stepen(np.abs(Q_AID_1), r_σ_APD) + K_AVD * stepen(np.abs(Q_AVD_1), r_σ_APD),
                                   (1 / r_σ_APD))) - 1

        APD_BUD_CET = np.abs(P_APD_1) * np.abs(Q_APD_1) / (
                    np.abs(P_AXD_1) * np.abs(Q_AXD_1) + np.abs(P_ASD_1) * np.abs(Q_ASD_1)) - 1

        APD_CET = (np.abs(Q_AXD_1) / np.abs(Q_ASD_1)) / stepen((np.abs(P_AXD_1) / (np.abs(P_ASD_1))) * (K_ASD / K_AXD),
                                                               (1 / (r_Ω_APD - 1))) - 1

        APD_BAL_CET = np.abs(Q_APD_1) / (np.abs(Q_AXD_1) + np.abs(Q_ASD_1)) - 1

        ADW_BUD_CES = np.abs(P_ADW_1) * np.abs(Q_ADW_1) / (
                    np.abs(P_AXD_1) * (1 + TAXD_1) * np.abs(Q_AXD_1) + np.abs(P_AXW_1) * np.abs(Q_AXW_1)) - 1

        ADW_CES = (np.abs(Q_AXW_1) / np.abs(Q_AXD_1)) / stepen(
            ((np.abs(P_AXW_1)) / (np.abs(P_AXD_1) * (1 + TAXD_1))) * (K_AXD / K_AXW), (1 / (r_σ_ADW - 1))) - 1

        ADW_BAL_CES = np.abs(Q_ADW_1) / (np.abs(Q_AXD_1) + np.abs(Q_AXW_1)) - 1

        AXW_SUPPLY = np.abs(Q_AXW_1) / (Z_AXW * (1 + SS_AXW_SUPPLY_1) * stepen(np.abs(P_AXW_1) / (ER_1), ε_AXW)) - 1

        ADW_DEMAND = np.abs(Q_ADW_1) / (Z_ADW * (1 + DS_ADW_DEMAND_1) * stepen(np.abs(P_ADW_1) / (ER_1), ε_ADW)) - 1

        ATD_BUD_CES = np.abs(P_ATD_1) * np.abs(Q_ATD_1) / (
                    np.abs(P_AMD_1) * (1 + TAMD_1) * np.abs(Q_AMD_1) + np.abs(P_ASD_1) * np.abs(Q_ASD_1)) - 1

        ATD_CES = (np.abs(Q_ASD_1) / np.abs(Q_AMD_1)) / stepen(
            (np.abs(P_ASD_1) / (np.abs(P_AMD_1) * (1 + TAMD_1))) * (K_AMD / K_ASD), (1 / (r_σ_ATD - 1))) - 1

        ATD_BAL_CES = np.abs(Q_ATD_1) / (np.abs(Q_ASD_1) + np.abs(Q_AMD_1)) - 1

        AMD_SUPPLY = np.abs(Q_AMD_1) / (Z_AMD * (1 + SS_AMD_SUPPLY_1) * stepen(np.abs(P_AMD_1) / (ER_1), ε_AMD)) - 1

        ATD_BUD_CET = np.abs(P_ATD_1) * np.abs(Q_ATD_1) / (
                    np.abs(P_ADD_1) * np.abs(Q_ADD_1) + np.abs(P_BID_1) * np.abs(Q_BID_1)) - 1

        ATD_CET = (np.abs(Q_ADD_1) / np.abs(Q_BID_1)) / stepen((np.abs(P_ADD_1) / (np.abs(P_BID_1))) * (K_BID / K_ADD),
                                                               (1 / (r_Ω_ATD - 1))) - 1

        ATD_BAL_CET = np.abs(Q_ATD_1) / (np.abs(Q_BID_1) + np.abs(Q_ADD_1)) - 1

        ADD_DEMAND = np.abs(Q_ADD_1) / (Z_ADD * (1 + DS_ADD_DEMAND_1) * stepen(np.abs(P_ADD_1), ε_ADD)) - 1

        BDD_BUD_CES = np.abs(P_BDD_1) * np.abs(Q_BDD_1) / (
                    np.abs(P_BID_1) * np.abs(Q_BID_1) + np.abs(P_BVD_1) * np.abs(Q_BVD_1)) - 1

        BDD_CES = (np.abs(Q_BVD_1) / np.abs(Q_BID_1)) / stepen((np.abs(P_BVD_1) / (np.abs(P_BID_1))) * (K_BID / K_BVD),
                                                               (1 / (r_σ_BDD - 1))) - 1

        BDD_BAL_CES = np.abs(Q_BDD_1) / (
                    A_BDD * stepen(K_BID * stepen(np.abs(Q_BID_1), r_σ_BDD) + K_BVD * stepen(np.abs(Q_BVD_1), r_σ_BDD),
                                   (1 / r_σ_BDD))) - 1

        BDD_DEMAND = np.abs(Q_BDD_1) / (Z_BDD * (1 + DS_BDD_DEMAND_1) * stepen(np.abs(P_BDD_1), ε_BDD)) - 1

        BVD_SUPPLY = np.abs(Q_BVD_1) / (Z_BVD * (1 + SS_BVD_SUPPLY_1) * stepen(np.abs(P_BVD_1), ε_BVD)) - 1

        IPD_BUD_CET = np.abs(P_IPD_1) * np.abs(Q_IPD_1) / (
                    np.abs(P_IXD_1) * np.abs(Q_IXD_1) + np.abs(P_AID_1) * np.abs(Q_AID_1)) - 1

        return IPD_SUPPLY, IPD_BUD_CET, IPD_CET, IPD_BAL_CET, IXD_DEMAND, AVD_SUPPLY, APD_BUD_CES, APD_CES, \
               APD_BAL_CES, APD_BUD_CET, APD_CET, APD_BAL_CET, ADW_BUD_CES, ADW_CES, ADW_BAL_CES, AXW_SUPPLY, \
               ADW_DEMAND, ATD_BUD_CES, ATD_CES, ATD_BAL_CES, AMD_SUPPLY, ATD_BUD_CET, ATD_CET, ATD_BAL_CET, \
               ADD_DEMAND, BDD_BUD_CES, BDD_CES, BDD_BAL_CES, BDD_DEMAND, BVD_SUPPLY

    Q_IPD_1 = Q_IPD_0
    P_IPD_1 = P_IPD_0
    P_IXD_1 = P_IXD_0
    Q_IXD_1 = Q_IXD_0
    P_AID_1 = P_AID_0
    Q_AID_1 = Q_AID_0
    Q_AVD_1 = Q_AVD_0
    P_AVD_1 = P_AVD_0
    P_APD_1 = P_APD_0
    Q_APD_1 = Q_APD_0
    P_AXD_1 = P_AXD_0
    Q_AXD_1 = Q_AXD_0
    P_ASD_1 = P_ASD_0
    Q_ASD_1 = Q_ASD_0
    P_ADW_1 = P_ADW_0
    Q_ADW_1 = Q_ADW_0
    P_AXW_1 = P_AXW_0
    Q_AXW_1 = Q_AXW_0
    P_ATD_1 = P_ATD_0
    Q_ATD_1 = Q_ATD_0
    P_AMD_1 = P_AMD_0
    Q_AMD_1 = Q_AMD_0
    P_ADD_1 = P_ADD_0
    Q_ADD_1 = Q_ADD_0
    P_BDD_1 = P_BDD_0
    Q_BDD_1 = Q_BDD_0
    P_BID_1 = P_BID_0
    Q_BID_1 = Q_BID_0
    P_BVD_1 = P_BVD_0
    Q_BVD_1 = Q_BVD_0

    solved_value: list = []
    eq_result = 100
    pass_cur = 0
    pass_num_max = 3;
    dop_alg_1 = False

    while (eq_result >= 100) and (pass_cur < pass_num_max):
        z0 = [Q_IPD_1, P_IPD_1, P_IXD_1, Q_IXD_1, P_AID_1, Q_AID_1, Q_AVD_1, P_AVD_1, P_APD_1, Q_APD_1, P_AXD_1,
              Q_AXD_1, P_ASD_1, Q_ASD_1, P_ADW_1, Q_ADW_1, P_AXW_1, Q_AXW_1, P_ATD_1, Q_ATD_1, P_AMD_1, Q_AMD_1,
              P_ADD_1, Q_ADD_1, P_BDD_1, Q_BDD_1, P_BID_1, Q_BID_1, P_BVD_1, Q_BVD_1]

        solved_value = fsolve(func, z0)
        # print(solved_value)
        if (Q_IPD_1 == Q_IPD_0) and (not dop_alg_1):
            solved = root(func, z0, method='lm')
            solved_value = solved.x
            accuracy = solved.fun
            dop_alg_1 = True

        pass_cur += 1

        # print(f'Курс на начало {ER_0}        Курс расчета {ER_1}')

        Q_IPD_1 = np.abs(solved_value[0])
        P_IPD_1 = np.abs(solved_value[1])
        # print("{:10}".format('Q_IPD_1 ='), "{:>22f}".format(Q_IPD_1),"{:10}".format(' '),"{:10}".format('P_IPD_1 ='), "{:>22f}".format(P_IPD_1) )
        P_IXD_1 = np.abs(solved_value[2])
        Q_IXD_1 = np.abs(solved_value[3])
        # print("{:10}".format('P_IXD_1 ='), "{:>22f}".format(P_IXD_1),"{:10}".format(' '), "{:10}".format('Q_IXD_1 ='), "{:>22f}".format(Q_IXD_1) )
        P_AID_1 = np.abs(solved_value[4])
        Q_AID_1 = np.abs(solved_value[5])
        # print("{:10}".format('P_AID_1 ='), "{:>22f}".format(P_AID_1),"{:10}".format(' '), "{:10}".format('Q_AID_1 ='), "{:>22f}".format(Q_AID_1) )
        Q_AVD_1 = np.abs(solved_value[6])
        P_AVD_1 = np.abs(solved_value[7])
        # print("{:10}".format('Q_AVD_1 ='), "{:>22f}".format(Q_AVD_1),"{:10}".format(' '), "{:10}".format('P_AVD_1 ='), "{:>22f}".format(P_AVD_1) )
        P_APD_1 = np.abs(solved_value[8])
        Q_APD_1 = np.abs(solved_value[9])
        # print("{:10}".format('P_APD_1 ='), "{:>22f}".format(P_APD_1),"{:10}".format(' '), "{:10}".format('Q_APD_1 ='), "{:>22f}".format(Q_APD_1) )
        P_AXD_1 = np.abs(solved_value[10])
        Q_AXD_1 = np.abs(solved_value[11])
        # print("{:10}".format('P_AXD_1 ='), "{:>22f}".format(P_AXD_1),"{:10}".format(' '), "{:10}".format('Q_AXD_1 ='), "{:>22f}".format(Q_AXD_1) )
        P_ASD_1 = np.abs(solved_value[12])
        Q_ASD_1 = np.abs(solved_value[13])
        # print("{:10}".format('P_ASD_1 ='), "{:>22f}".format(P_ASD_1),"{:10}".format(' '), "{:10}".format('Q_ASD_1 ='), "{:>22f}".format(Q_ASD_1) )
        P_ADW_1 = np.abs(solved_value[14])
        Q_ADW_1 = np.abs(solved_value[15])
        # print("{:10}".format('P_ADW_1 ='), "{:>22f}".format(P_ADW_1),"{:10}".format(' '), "{:10}".format('Q_ADW_1 ='), "{:>22f}".format(Q_ADW_1) )
        P_AXW_1 = np.abs(solved_value[16])
        Q_AXW_1 = np.abs(solved_value[17])
        # print("{:10}".format('P_AXW_1 ='), "{:>22f}".format(P_AXW_1),"{:10}".format(' '), "{:10}".format('Q_AXW_1 ='), "{:>22f}".format(Q_AXW_1) )
        P_ATD_1 = np.abs(solved_value[18])
        Q_ATD_1 = np.abs(solved_value[19])
        # print("{:10}".format('P_ATD_1 ='), "{:>22f}".format(P_ATD_1),"{:10}".format(' '), "{:10}".format('Q_ATD_1 ='), "{:>22f}".format(Q_ATD_1) )
        P_AMD_1 = np.abs(solved_value[20])
        Q_AMD_1 = np.abs(solved_value[21])
        # print("{:10}".format('P_AMD_1 ='), "{:>22f}".format(P_AMD_1),"{:10}".format(' '), "{:10}".format('Q_AMD_1 ='), "{:>22f}".format(Q_AMD_1) )
        P_ADD_1 = np.abs(solved_value[22])
        Q_ADD_1 = np.abs(solved_value[23])
        # print("{:10}".format('P_ADD_1 ='), "{:>22f}".format(P_ADD_1),"{:10}".format(' '), "{:10}".format('Q_ADD_1 ='), "{:>22f}".format(Q_ADD_1) )
        P_BDD_1 = np.abs(solved_value[24])
        Q_BDD_1 = np.abs(solved_value[25])
        # print("{:10}".format('P_BDD_1 ='), "{:>22f}".format(P_BDD_1),"{:10}".format(' '), "{:10}".format('Q_BDD_1 ='), "{:>22f}".format(Q_BDD_1) )
        P_BID_1 = np.abs(solved_value[26])
        Q_BID_1 = np.abs(solved_value[27])
        # print("{:10}".format('P_BID_1 ='), "{:>22f}".format(P_BID_1),"{:10}".format(' '), "{:10}".format('Q_BID_1 ='), "{:>22f}".format(Q_BID_1) )
        P_BVD_1 = np.abs(solved_value[28])
        Q_BVD_1 = np.abs(solved_value[29])
        # print("{:10}".format('P_BVD_1 ='), "{:>22f}".format(P_BVD_1), "{:10}".format(' '),"{:10}".format('Q_BVD_1 ='), "{:>22f}".format(Q_BVD_1) )

        # print(f'Изменение P_APD ={(P_APD_1/P_APD_0-1)*100} %   Изменение Q_APD {(Q_APD_1/Q_APD_0-1)*100} %' )
        # print(f'Изменение P_AXD ={(P_AXD_1/P_AXD_0-1)*100} %   Изменение Q_AXD {(Q_AXD_1/Q_AXD_0-1)*100} %' )

        eqs = []

        if dop_alg_1:
            eqs_1 = []
            for item in accuracy:
                eqs_1.append(item)
            eqs = eqs_1
        else:
            eqs.append(Q_IPD_1 / (Z_IPD * (1 + SS_IPD_SUPPLY_1) * stepen(P_IPD_1, ε_IPD)) - 1)

            eqs.append(P_IPD_1 * Q_IPD_1 / (P_IXD_1 * Q_IXD_1 + P_AID_1 * Q_AID_1) - 1)

            eqs.append((Q_IXD_1 / Q_AID_1) / stepen((P_IXD_1 / (P_AID_1)) * (K_AID / K_IXD), (1 / (r_Ω_IPD - 1))) - 1)

            eqs.append(Q_IPD_1 / (Q_AID_1 + Q_IXD_1) - 1)

            eqs.append(Q_IXD_1 / (Z_IXD * (1 + DS_IXD_DEMAND_1) * stepen(P_IXD_1 * (1 + TIXD_1) / (ER_1), ε_IXD)) - 1)

            eqs.append(Q_AVD_1 / (Z_AVD * (1 + SS_AVD_SUPPLY_1) * stepen(P_AVD_1, ε_AVD)) - 1)

            eqs.append(P_APD_1 * Q_APD_1 / (P_AID_1 * Q_AID_1 + P_AVD_1 * Q_AVD_1) - 1)

            eqs.append(Q_AVD_1 / Q_AID_1 / stepen((P_AVD_1 / (P_AID_1)) * (K_AID / K_AVD), (1 / (r_σ_APD - 1))) - 1)

            eqs.append(Q_APD_1 / (A_APD * stepen(K_AID * stepen(Q_AID_1, r_σ_APD) + K_AVD * stepen(Q_AVD_1, r_σ_APD),
                                                 (1 / r_σ_APD))) - 1)

            eqs.append(P_APD_1 * Q_APD_1 / (P_AXD_1 * Q_AXD_1 + P_ASD_1 * Q_ASD_1) - 1)

            eqs.append((Q_AXD_1 / Q_ASD_1) / stepen((P_AXD_1 / (P_ASD_1)) * (K_ASD / K_AXD), (1 / (r_Ω_APD - 1))) - 1)

            eqs.append(Q_APD_1 / (Q_AXD_1 + Q_ASD_1) - 1)

            eqs.append(P_ADW_1 * Q_ADW_1 / (P_AXD_1 * (1 + TAXD_1) * Q_AXD_1 + P_AXW_1 * Q_AXW_1) - 1)

            eqs.append((Q_AXW_1 / Q_AXD_1) / stepen(((P_AXW_1) / (P_AXD_1 * (1 + TAXD_1))) * (K_AXD / K_AXW),
                                                    (1 / (r_σ_ADW - 1))) - 1)

            eqs.append(Q_ADW_1 / (Q_AXD_1 + Q_AXW_1) - 1)

            eqs.append(Q_AXW_1 / (Z_AXW * (1 + SS_AXW_SUPPLY_1) * stepen(P_AXW_1 / (ER_1), ε_AXW)) - 1)

            eqs.append(Q_ADW_1 / (Z_ADW * (1 + DS_ADW_DEMAND_1) * stepen(P_ADW_1 / (ER_1), ε_ADW)) - 1)

            eqs.append(P_ATD_1 * Q_ATD_1 / (P_AMD_1 * (1 + TAMD_1) * Q_AMD_1 + P_ASD_1 * Q_ASD_1) - 1)

            eqs.append((Q_ASD_1 / Q_AMD_1) / stepen((P_ASD_1 / (P_AMD_1 * (1 + TAMD_1))) * (K_AMD / K_ASD),
                                                    (1 / (r_σ_ATD - 1))) - 1)

            eqs.append(Q_ATD_1 / (Q_ASD_1 + Q_AMD_1) - 1)

            eqs.append(Q_AMD_1 / (Z_AMD * (1 + SS_AMD_SUPPLY_1) * stepen(P_AMD_1 / (ER_1), ε_AMD)) - 1)

            eqs.append(P_ATD_1 * Q_ATD_1 / (P_ADD_1 * Q_ADD_1 + P_BID_1 * Q_BID_1) - 1)

            eqs.append((Q_ADD_1 / Q_BID_1) / stepen((P_ADD_1 / (P_BID_1)) * (K_BID / K_ADD), (1 / (r_Ω_ATD - 1))) - 1)

            eqs.append(Q_ATD_1 / (Q_BID_1 + Q_ADD_1) - 1)

            eqs.append(Q_ADD_1 / (Z_ADD * (1 + DS_ADD_DEMAND_1) * stepen(P_ADD_1, ε_ADD)) - 1)

            eqs.append(P_BDD_1 * Q_BDD_1 / (P_BID_1 * Q_BID_1 + P_BVD_1 * Q_BVD_1) - 1)

            eqs.append((Q_BVD_1 / Q_BID_1) / stepen((P_BVD_1 / (P_BID_1)) * (K_BID / K_BVD), (1 / (r_σ_BDD - 1))) - 1)

            eqs.append(Q_BDD_1 / (A_BDD * stepen(K_BID * stepen(Q_BID_1, r_σ_BDD) + K_BVD * stepen(Q_BVD_1, r_σ_BDD),
                                                 (1 / r_σ_BDD))) - 1)

            eqs.append(Q_BDD_1 / (Z_BDD * (1 + DS_BDD_DEMAND_1) * stepen(P_BDD_1, ε_BDD)) - 1)

            eqs.append(Q_BVD_1 / (Z_BVD * (1 + SS_BVD_SUPPLY_1) * stepen(P_BVD_1, ε_BVD)) - 1)

            eqs.append(P_IPD_1 * Q_IPD_1 / (P_IXD_1 * Q_IXD_1 + P_AID_1 * Q_AID_1) - 1)

        qrt_eq = []

        for item in eqs:
            qrt_eq.append(item ** 2)

        eq_result = sqrt(fsum(qrt_eq))

    if eq_result < 100:
        solution = True
    else:
        solution = False

    # if Q_IPD_0 == Q_IPD_1:
    #         solution = False

    solution = solution
    # print(solution)

    if solution == False:
        Q_IPD_1 = 312638500.0
        P_IPD_1 = 4113.0
        P_IXD_1 = 11091.0
        Q_IXD_1 = 25295000.0
        P_AID_1 = 3499.0
        Q_AID_1 = 287343500.0
        Q_AVD_1 = 100.0
        P_AVD_1 = 18636846945.0
        P_APD_1 = 46200.0
        Q_APD_1 = 62100000.0
        P_AXD_1 = 53310.74
        Q_AXD_1 = 30547000.0
        P_ASD_1 = 39316.0
        Q_ASD_1 = 31553000.0
        P_ADW_1 = 50945.0
        Q_ADW_1 = 445185000.0
        P_AXW_1 = 50770.3473567787
        Q_AXW_1 = 414638000.0
        P_ATD_1 = 44960.0
        Q_ATD_1 = 35997000.0
        P_AMD_1 = 85031.0
        Q_AMD_1 = 4444000.0
        P_ADD_1 = 44960.0
        Q_ADD_1 = 10799100.0
        P_BDD_1 = 188815035409.0
        Q_BDD_1 = 100.0
        P_BID_1 = 44960.0
        Q_BID_1 = 25197900.0
        P_BVD_1 = 177486133284.46
        Q_BVD_1 = 100.0

    E_WP_1 = P_ADW_1/ER_1

    E_DWP_1 = E_WP_1/WP_0-1

    P_AXD_USD_1 = P_AXD_1 / ER_1

    P_AMD_USD_1 = P_AMD_1 / ER_1

    P_IXD_USD_1 = P_IXD_1 / ER_1

    H27 = P_IPD_1 / P_IPD_0 - 1

    I27 = Q_IPD_1 / Q_IPD_0 - 1

    H28 = P_IXD_1 / P_IXD_0 - 1

    I28 = Q_IXD_1 / Q_IXD_0 - 1

    H29 = P_AID_1 / P_AID_0 - 1

    I29 = Q_AID_1 / Q_AID_0 - 1

    H30 = P_AVD_1 / P_AVD_0 - 1

    I30 = Q_AVD_1 / Q_AVD_0 - 1

    H31 = P_APD_1 / P_APD_0 - 1

    I31 = Q_APD_1 / Q_APD_0 - 1

    H32 = P_AXD_1 / P_AXD_0 - 1

    I32 = Q_AXD_1 / Q_AXD_0 - 1

    H33 = P_AXW_1 / P_AXW_0 - 1

    I33 = Q_AXW_1 / Q_AXW_0 - 1

    H34 = P_ADW_1 / P_ADW_0 - 1

    I34 = Q_ADW_1 / Q_ADW_0 - 1

    H35 = P_ASD_1 / P_ASD_0 - 1

    I35 = Q_ASD_1 / Q_ASD_0 - 1

    H36 = P_ATD_1 / P_ATD_0 - 1

    I36 = Q_ATD_1 / Q_ATD_0 - 1

    H37 = P_AMD_1 / P_AMD_0 - 1

    I37 = Q_AMD_1 / Q_AMD_0 - 1

    H38 = P_ADD_1 / P_ADD_0 - 1

    I38 = Q_ADD_1 / Q_ADD_0 - 1

    H39 = P_BID_1 / P_BID_0 - 1

    I39 = Q_BID_1 / Q_BID_0 - 1

    H40 = P_BVD_1 / P_BVD_0 - 1

    I40 = Q_BVD_1 / Q_BVD_0 - 1

    H41 = P_BDD_1 / P_BDD_0 - 1

    I41 = Q_BDD_1 / Q_BDD_0 - 1

    result_to_front = {
        'table1': [
            {
                'id': '1',
                'title': 'Курс RUB/USD',
                'params': 'ER',
                'basebalance': round(ER_0, 2),
                'newbalance': round(ER_1, 2),
                "editBase": 'true',
                "editNew": 'true',
            },
            {
                'id': '2',
                'title': 'Изменение курса RUB/USD %',
                'params': 'DER',
                'basebalance': round(DER_0 * 100, 2),
                'newbalance': round(DER_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': 'Первоначальный сдвиг мировой цены на сталь, USD за тонну',
                'params': 'WP',
                'basebalance': round(WP_0),
                'newbalance': round(WP_1),
                "editBase": 'false',
                "editNew": 'true',
            },
            {
                'id': '4',
                'title': 'Первоначальный сдвиг мировой цены на сталь, %',
                'params': 'DWP',
                'basebalance': ' ',
                'newbalance': round(DWP_CEL_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '5',
                'title': 'Равновесная мировая цена стали, USD за тонну',
                'params': 'E_WP',
                'basebalance': round(E_WP_0, 2),
                'newbalance': round(E_WP_1, 2),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '6',
                'title': 'Изменение равновесной мировой цены стали, USD за тонну, %',
                'params': 'E_DWP',
                'basebalance': ' ',
                'newbalance': round(E_DWP_1, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '7',
                'title': 'Цена экспорта стали (без тарифа), USD за тонну',
                'params': 'P_AXD_USD',
                'basebalance': round(P_AXD_USD_0),
                'newbalance': round(P_AXD_USD_1),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Цена импорта стали (без тарифа), USD за тонну',
                'params': 'P_AMD_USD',
                'basebalance': round(P_AMD_USD_0),
                'newbalance': round(P_AMD_USD_1),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '9',
                'title': 'Цена экспорта руды (без тарифа), USD за тонну',
                'params': 'P_IXD_USD',
                'basebalance': round(P_IXD_USD_0),
                'newbalance': round(P_IXD_USD_1),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '10',
                'title': 'Экспортный тариф на сталь, %',
                'params': 'TAXD',
                'basebalance': round(TAXD_0 * 100, 2),
                'newbalance': round(TAXD_1 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '11',
                'title': 'Экспортный тариф на руду, %',
                'params': 'TIXD',
                'basebalance': round(TIXD_0 * 100, 2),
                'newbalance': round(TIXD_1 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': 'Импортный тариф на сталь, %',
                'params': 'TAMD',
                'basebalance': round(TAMD_0 * 100, 2),
                'newbalance': round(TAMD_1 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            }
        ],
        'finding_solution': solution,
        'table2': [
            {
                'id': '1',
                'title': 'Российское производство руды',
                'params': 'IPD',
                'basebalance_pr': round(P_IPD_0, 2),
                'basebalance_quan': round(Q_IPD_0, 2),
                'newbalance_pr': round(P_IPD_1, 2),
                'newbalance_quan': round(Q_IPD_1, 2),
                'perc_change_price': round(H27 * 100, 2),
                'perc_change_quantity': round(I27 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '2',
                'title': 'Российский экспорт руды',
                'params': 'IXD',
                'basebalance_pr': round(P_IXD_0, 2),
                'basebalance_quan': round(Q_IXD_0, 2),
                'newbalance_pr': round(P_IXD_1, 2),
                'newbalance_quan': round(Q_IXD_1, 2),
                'perc_change_price': round(H28 * 100, 2),
                'perc_change_quantity': round(I28 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '3',
                'title': 'Потребление руды при производстве стали',
                'params': 'AID',
                'basebalance_pr': round(P_AID_0, 2),
                'basebalance_quan': round(Q_AID_0, 2),
                'newbalance_pr': round(P_AID_1, 2),
                'newbalance_quan': round(Q_AID_1, 2),
                'perc_change_price': round(H29 * 100, 2),
                'perc_change_quantity': round(I29 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '4',
                'title': 'Потребление прочих факторов при производстве стали (индекс)',
                'params': 'AVD',
                'basebalance_pr': round(P_AVD_0, 2),
                'basebalance_quan': round(Q_AVD_0, 2),
                'newbalance_pr': round(P_AVD_1, 2),
                'newbalance_quan': round(Q_AVD_1, 2),
                'perc_change_price': round(H30 * 100, 2),
                'perc_change_quantity': round(I30 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': 'Российское производство стали и изделий из неё',
                'params': 'APD',
                'basebalance_pr': round(P_APD_0, 2),
                'basebalance_quan': round(Q_APD_0, 2),
                'newbalance_pr': round(P_APD_1, 2),
                'newbalance_quan': round(Q_APD_1, 2),
                'perc_change_price': round(H31 * 100, 2),
                'perc_change_quantity': round(I31 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '6',
                'title': 'Российский экспорт стали и изделий из неё',
                'params': 'AXD',
                'basebalance_pr': round(P_AXD_0, 2),
                'basebalance_quan': round(Q_AXD_0, 2),
                'newbalance_pr': round(P_AXD_1, 2),
                'newbalance_quan': round(Q_AXD_1, 2),
                'perc_change_price': round(H32 * 100, 2),
                'perc_change_quantity': round(I32 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '7',
                'title': 'Мировое производство (без российского экспорта) стали и изделий из неё',
                'params': 'AXW',
                'basebalance_pr': round(P_AXW_0, 2),
                'basebalance_quan': round(Q_AXW_0, 2),
                'newbalance_pr': round(P_AXW_1, 2),
                'newbalance_quan': round(Q_AXW_1, 2),
                'perc_change_price': round(H33 * 100, 2),
                'perc_change_quantity': round(I33 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Мировое потребление (импорт) стали и изделий из неё',
                'params': 'ADW',
                'basebalance_pr': round(P_ADW_0, 2),
                'basebalance_quan': round(Q_ADW_0, 2),
                'newbalance_pr': round(P_ADW_1, 2),
                'newbalance_quan': round(Q_ADW_1, 2),
                'perc_change_price': round(H34 * 100, 2),
                'perc_change_quantity': round(I34 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '9',
                'title': 'Российское производство стали и изделий из неё для внутреннего потребления',
                'params': 'ASD',
                'basebalance_pr': round(P_ASD_0, 2),
                'basebalance_quan': round(Q_ASD_0, 2),
                'newbalance_pr': round(P_ASD_1, 2),
                'newbalance_quan': round(Q_ASD_1, 2),
                'perc_change_price': round(H35 * 100, 2),
                'perc_change_quantity': round(I35 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '10',
                'title': 'Российское совокупное потребление стали и изделий из неё',
                'params': 'ATD',
                'basebalance_pr': round(P_ATD_0, 2),
                'basebalance_quan': round(Q_ATD_0, 2),
                'newbalance_pr': round(P_ATD_1, 2),
                'newbalance_quan': round(Q_ATD_1, 2),
                'perc_change_price': round(H36 * 100, 2),
                'perc_change_quantity': round(I36 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '11',
                'title': 'Российский импорт стали и изделий из неё',
                'params': 'AMD',
                'basebalance_pr': round(P_AMD_0, 2),
                'basebalance_quan': round(Q_AMD_0, 2),
                'newbalance_pr': round(P_AMD_1, 2),
                'newbalance_quan': round(Q_AMD_1, 2),
                'perc_change_price': round(H37 * 100, 2),
                'perc_change_quantity': round(I37 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': 'Российское потребление стали и изделий из неё всеми отраслями, кроме строительства',
                'params': 'ADD',
                'basebalance_pr': round(P_ADD_0, 2),
                'basebalance_quan': round(Q_ADD_0, 2),
                'newbalance_pr': round(P_ADD_1, 2),
                'newbalance_quan': round(Q_ADD_1, 2),
                'perc_change_price': round(H38 * 100, 2),
                'perc_change_quantity': round(I38 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '13',
                'title': 'Российское промежуточное потребление стали и изделий из неё в строительстве',
                'params': 'BID',
                'basebalance_pr': round(P_BID_0, 2),
                'basebalance_quan': round(Q_BID_0, 2),
                'newbalance_pr': round(P_BID_1, 2),
                'newbalance_quan': round(Q_BID_1, 2),
                'perc_change_price': round(H39 * 100, 2),
                'perc_change_quantity': round(I39 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '14',
                'title': 'Потребление строительной отраслью прочих факторов (индекс)',
                'params': 'BVD',
                'basebalance_pr': round(P_BVD_0, 2),
                'basebalance_quan': round(Q_BVD_0, 2),
                'newbalance_pr': round(P_BVD_1, 2),
                'newbalance_quan': round(Q_BVD_1, 2),
                'perc_change_price': round(H40 * 100, 2),
                'perc_change_quantity': round(I40 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '15',
                'title': 'Российское потребление отрасли строительства (индекс)',
                'params': 'BDD',
                'basebalance_pr': round(P_BDD_0, 2),
                'basebalance_quan': round(Q_BDD_0, 2),
                'newbalance_pr': round(P_BDD_1, 2),
                'newbalance_quan': round(Q_BDD_1, 2),
                'perc_change_price': round(H41 * 100, 2),
                'perc_change_quantity': round(I41 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            }
        ]
    }

    return result_to_front

input_data = InputDataBase(example_data)
result = steel_market(input_data)
print(result)
