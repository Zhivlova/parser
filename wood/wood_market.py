from math import fsum, sqrt
import numpy as np
from scipy.optimize import fsolve, root

example_data = {'ER_before': 73.65,
                'ER_after': 73.65,
                'WP_before': 265148.0,
                'WP_after': 265148.0,
                'P_AXD_USD_before': 206366.0,
                'P_AMD_USD_before': 180531.0,
                'P_IXD_USD_before': 86799.0,
                'TAXD_before': 0.0,
                'TAXD_after': 0.0,
                'TIXD_before': 0.0,
                'TIXD_after': 50.0,
                'TAMD_before': 0.0,
                'TAMD_after': 0.0,
                'SS_IPD_SUPPLY_after': 0.0,
                'DS_IXD_DEMAND_after': 0.0,
                'SS_AVD_SUPPLY_after': 0.0,
                'DS_ADW_DEMAND_after': 0.0,
                'SS_AXW_SUPPLY_after': 0.0,
                'SS_AMD_SUPPLY_after': 0.0,
                'DS_ATD_DEMAND': 0.0,
                'IPD_pr': 2811000.0,
                'IPD_q': 118715.6,
                'IXD_q': 5510.0,
                'APD_q': 32333.49,
                'AXD_q': 27877.0,
                'ADW_q': 165750.86,
                'ASD_pr': 12467000.0,
                'AMD_q': 9.24}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.ER_before = dict_from_frontend.get('ER_before')
        self.ER_after = dict_from_frontend.get('ER_after')
        self.WP_before = dict_from_frontend.get('WP_before')
        self.WP_after = dict_from_frontend.get('WP_after')
        self.P_AXD_USD_before = dict_from_frontend.get('P_AXD_USD_before')
        self.P_AMD_USD_before = dict_from_frontend.get('P_AMD_USD_before')
        self.P_IXD_USD_before = dict_from_frontend.get('P_IXD_USD_before')
        self.TAXD_before = dict_from_frontend.get('TAXD_before')
        self.TAXD_after = dict_from_frontend.get('TAXD_after')
        self.TIXD_before = dict_from_frontend.get('TIXD_before')
        self.TIXD_after = dict_from_frontend.get('TIXD_after')
        self.TAMD_before = dict_from_frontend.get('TAMD_before')
        self.TAMD_after = dict_from_frontend.get('TAMD_after')
        self.SS_IPD_SUPPLY_after = dict_from_frontend.get('SS_IPD_SUPPLY_after')
        self.DS_IXD_DEMAND_after = dict_from_frontend.get('DS_IXD_DEMAND_after')
        self.SS_AVD_SUPPLY_after = dict_from_frontend.get('SS_AVD_SUPPLY_after')
        self.DS_ADW_DEMAND_after = dict_from_frontend.get('DS_ADW_DEMAND_after')
        self.SS_AXW_SUPPLY_after = dict_from_frontend.get('SS_AXW_SUPPLY_after')
        self.SS_AMD_SUPPLY_after = dict_from_frontend.get('SS_AMD_SUPPLY_after')
        self.DS_ATD_DEMAND_after = dict_from_frontend.get('DS_ATD_DEMAND_after')
        self.IPD_pr = dict_from_frontend.get('IPD_pr')
        self.IPD_q = dict_from_frontend.get('IPD_q')
        self.IXD_q = dict_from_frontend.get('IXD_q')
        self.APD_q = dict_from_frontend.get('APD_q')
        self.AXD_q = dict_from_frontend.get('AXD_q')
        self.ADW_q = dict_from_frontend.get('ADW_q')
        self.ASD_pr = dict_from_frontend.get('ASD_pr')
        self.AMD_q = dict_from_frontend.get('AMD_q')


o = 14


def stepen(x, st):
    if (x < 0):
        # print(f'x={round(x, o)}, st={round(st, o)}')
        return np.sign(x) * (np.abs(x) ** st)
    else:
        return x ** st


def wood_market(input_data):
    """Вводим новые значения"""
    ER_0 = input_data.ER_before
    ER_1 = input_data.ER_after
    WP_0 = input_data.WP_before
    WP_1 = input_data.WP_after
    P_AXD_USD_0 = input_data.P_AXD_USD_before
    P_AMD_USD_0 = input_data.P_AMD_USD_before
    P_IXD_USD_0 = input_data.P_IXD_USD_before
    TAXD_0 = input_data.TAXD_before
    TAXD_1 = input_data.TAXD_after
    TIXD_0 = input_data.TIXD_before
    TIXD_1 = input_data.TIXD_after
    TAMD_0 = input_data.TAMD_before
    TAMD_1 = input_data.TAMD_after
    SS_IPD_SUPPLY_1 = input_data.SS_IPD_SUPPLY_after
    DS_IXD_DEMAND_1 = input_data.DS_IXD_DEMAND_after
    SS_AVD_SUPPLY_1 = input_data.SS_AVD_SUPPLY_after
    DS_ADW_DEMAND_1 = input_data.DS_ADW_DEMAND_after
    SS_AXW_SUPPLY_1 = input_data.SS_AXW_SUPPLY_after
    SS_AMD_SUPPLY_1 = input_data.SS_AMD_SUPPLY_after
    DS_ATD_DEMAND_1 = input_data.DS_ATD_DEMAND_after

    P_IPD_0 = input_data.IPD_pr
    Q_IPD_0 = input_data.IPD_q
    Q_IXD_0 = input_data.IXD_q
    Q_APD_0 = input_data.APD_q
    Q_AXD_0 = input_data.AXD_q
    Q_ADW_0 = input_data.ADW_q
    P_ASD_0 = input_data.ASD_pr
    Q_AMD_0 = input_data.AMD_q

    DER_0 = 0.0
    DWP_0 = 0.0

    """Перерасчет ячеек с новыми значениями"""

    DER_1 = ER_1 / ER_0 - 1

    DWP_CEL_1 = WP_1 / WP_0 - 1

    P_IXD_0 = P_IXD_USD_0 * ER_0

    Q_AID_0 = Q_IPD_0 - Q_IXD_0

    P_AID_0 = (P_IPD_0 * Q_IPD_0 - P_IXD_0 * Q_IXD_0) / Q_AID_0

    Q_AVD_0 = 100000

    P_AXD_0 = P_AXD_USD_0 * ER_0

    Q_AXW_0 = Q_ADW_0 - Q_AXD_0

    P_ADW_0 = WP_0 * ER_0

    Q_ASD_0 = Q_APD_0 - Q_AXD_0

    P_AXW_0 = (P_ADW_0 * Q_ADW_0 - P_AXD_0 * (1 + TAXD_0) * Q_AXD_0) / Q_AXW_0

    P_APD_0 = (P_ASD_0 * Q_ASD_0 + P_AXD_0 * Q_AXD_0) / (Q_AXD_0 + Q_ASD_0)

    P_AVD_0 = (P_APD_0 * Q_APD_0 - P_AID_0 * Q_AID_0) / Q_AVD_0

    Q_ATD_0 = Q_ASD_0 + Q_AMD_0

    P_AMD_0 = P_AMD_USD_0 * ER_0

    P_ATD_0 = (P_ASD_0 * Q_ASD_0 + P_AMD_0 * (1 + TAMD_0) * Q_AMD_0) / Q_ATD_0

    C36 = WP_1 / WP_0

    """Параметры"""

    Ω_IPD = 10.0
    σ_APD = 1.1
    Ω_APD = 5.0
    σ_ADW = 5.0
    σ_ATD = 2.5
    ε_IPD = 0.5
    ε_IXD = -1.5
    ε_AVD = 1
    ε_ADW = -0.5
    ε_AXW = 1
    ε_AMD = 1
    ε_ATD = -0.5

    r_Ω_IPD = (Ω_IPD + 1) / Ω_IPD

    r_σ_APD = (σ_APD - 1) / σ_APD

    r_Ω_APD = (Ω_APD + 1) / Ω_APD

    r_σ_ADW = (σ_ADW - 1) / σ_ADW

    r_σ_ATD = (σ_ATD - 1) / σ_ATD

    Z_IPD = Q_IPD_0 / (P_IPD_0 ** ε_IPD)

    Z_IXD = Q_IXD_0 / ((P_IXD_0 * (1 + TIXD_0) / ER_0) ** ε_IXD)

    Z_AVD = Q_AVD_0 / (P_AVD_0) ** ε_AVD

    Z_ADW = Q_ADW_0 / (P_ADW_0 / ER_0) ** ε_ADW

    Z_AXW = Q_AXW_0 / (P_AXW_0 / ER_0) ** ε_AXW

    Z_AMD = Q_AMD_0 / stepen(P_AMD_0 / ER_0, ε_AMD)

    Z_ATD = Q_ATD_0 / (P_ATD_0) ** ε_ATD

    """Относительное качество"""

    K_IXD = ((Q_IXD_0 / Q_AID_0) ** (1 - r_Ω_IPD)) * (P_IXD_0 / P_AID_0)

    K_AID = 1.0

    K_AVD = (Q_AVD_0 / Q_AID_0) ** (1 - r_σ_APD) * (P_AVD_0 / P_AID_0)

    A_APD = Q_APD_0 / (K_AID * Q_AID_0 ** r_σ_APD + K_AVD * Q_AVD_0 ** r_σ_APD) ** (1 / r_σ_APD)

    K_AXD = (Q_AXD_0 / Q_ASD_0) ** (1 - r_Ω_APD) * (P_AXD_0 / P_ASD_0)

    K_AXW = (Q_AXW_0 / Q_AXD_0) ** (1 - r_σ_ADW) * (P_AXW_0 / (P_AXD_0 * (1 + TAXD_0))) * K_AXD

    K_ASD = 1.0

    K_AMD = (Q_AMD_0 / Q_ASD_0) ** (1 - r_σ_ATD) * (P_AMD_0 * (1 + TAMD_0) / P_ASD_0)

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

        IPD_SUPPLY = np.abs(Q_IPD_1) - Z_IPD * (1 + SS_IPD_SUPPLY_1) * (np.abs(P_IPD_1)) ** ε_IPD

        IPD_BUD_CET = np.abs(P_IPD_1) * np.abs(Q_IPD_1) - np.abs(P_IXD_1) * np.abs(Q_IXD_1) - np.abs(P_AID_1) * np.abs(
            Q_AID_1)

        IPD_CET = np.abs(Q_IXD_1) / np.abs(Q_AID_1) - ((np.abs(P_IXD_1) / (np.abs(P_AID_1))) * (K_AID / K_IXD)) ** (
                1 / (r_Ω_IPD - 1))

        IPD_BAL_CET = np.abs(Q_IPD_1) - np.abs(Q_AID_1) - np.abs(Q_IXD_1)

        IXD_DEMAND = np.abs(Q_IXD_1) - Z_IXD * (1 + DS_IXD_DEMAND_1) * (
                np.abs(P_IXD_1) * (1 + TIXD_1) / (ER_1)) ** ε_IXD

        AVD_SUPPLY = np.abs(Q_AVD_1) - Z_AVD * (1 + SS_AVD_SUPPLY_1) * (np.abs(P_AVD_1)) ** ε_AVD

        APD_BUD_CES = np.abs(P_APD_1) * np.abs(Q_APD_1) - np.abs(P_AID_1) * np.abs(Q_AID_1) - np.abs(P_AVD_1) * np.abs(
            Q_AVD_1)

        APD_CES = np.abs(Q_AVD_1) / np.abs(Q_AID_1) - ((np.abs(P_AVD_1) / (np.abs(P_AID_1))) * (K_AID / K_AVD)) ** (
                1 / (r_σ_APD - 1))

        APD_BAL_CES = np.abs(Q_APD_1) - A_APD * (
                K_AID * np.abs(Q_AID_1) ** r_σ_APD + K_AVD * np.abs(Q_AVD_1) ** r_σ_APD) ** (1 / r_σ_APD)

        AVD_SUPPLY = np.abs(Q_AVD_1) - Z_AVD * (1 + SS_AVD_SUPPLY_1) * (np.abs(P_AVD_1)) ** ε_AVD

        APD_BUD_CET = np.abs(P_APD_1) * np.abs(Q_APD_1) - np.abs(P_AXD_1) * np.abs(Q_AXD_1) - np.abs(P_ASD_1) * np.abs(
            Q_ASD_1)

        APD_CET = np.abs(Q_AXD_1) / np.abs(Q_ASD_1) - ((np.abs(P_AXD_1) / (np.abs(P_ASD_1))) * (K_ASD / K_AXD)) ** (
                1 / (r_Ω_APD - 1))

        APD_BAL_CET = np.abs(Q_APD_1) - np.abs(Q_AXD_1) - np.abs(Q_ASD_1)

        ADW_BUD_CES = np.abs(P_ADW_1) * np.abs(Q_ADW_1) - np.abs(P_AXD_1) * (1 + TAXD_1) * np.abs(Q_AXD_1) - np.abs(
            P_AXW_1) * np.abs(Q_AXW_1)

        ADW_CES = np.abs(Q_AXW_1) / np.abs(Q_AXD_1) - (
                ((np.abs(P_AXW_1)) / (np.abs(P_AXD_1) * (1 + TAXD_1))) * (K_AXD / K_AXW)) ** (1 / (r_σ_ADW - 1))

        ADW_BAL_CES = np.abs(Q_ADW_1) - np.abs(Q_AXD_1) - np.abs(Q_AXW_1)

        AXW_SUPPLY = np.abs(Q_AXW_1) - Z_AXW * (1 + SS_AXW_SUPPLY_1) * (np.abs(P_AXW_1) / (ER_1)) ** ε_AXW

        ADW_DEMAND = np.abs(Q_ADW_1) - Z_ADW * (1 + DS_ADW_DEMAND_1) * (np.abs(P_ADW_1) / (ER_1)) ** ε_ADW

        ATD_BUD_CES = np.abs(P_ATD_1) * np.abs(Q_ATD_1) - np.abs(P_AMD_1) * (1 + TAMD_1) * np.abs(Q_AMD_1) - np.abs(
            P_ASD_1) * np.abs(Q_ASD_1)

        ATD_CES = np.abs(Q_ASD_1) / np.abs(Q_AMD_1) - (
                (np.abs(P_ASD_1) / (np.abs(P_AMD_1) * (1 + TAMD_1))) * (K_AMD / K_ASD)) ** (1 / (r_σ_ATD - 1))

        ATD_BAL_CES = np.abs(Q_ATD_1) - np.abs(Q_ASD_1) - np.abs(Q_AMD_1)

        AMD_SUPPLY = np.abs(Q_AMD_1) - Z_AMD * (1 + SS_AMD_SUPPLY_1) * (np.abs(P_AMD_1) / (ER_1)) ** ε_AMD

        ATD_DEMAND = np.abs(Q_ATD_1) - Z_ATD * (1 + DS_ATD_DEMAND_1) * (np.abs(P_ATD_1)) ** ε_ATD

    ###############################################

    # P_AXD_USD_1 = P_AXD_1/ER_1

    # P_AMD_USD_1 = P_AMD_1/ER_1

    # P_IXD_USD_1 = P_IXD_1/ER_1

    # H25 = P_IPD_1 / P_IPD_0 - 1

    # H26 = P_IXD_1 / P_IXD_0 - 1

    # H27 = P_AID_1 / P_AID_0 - 1

    # H28 = P_AVD_1 / P_AVD_0 - 1

    # H29 = P_APD_1 / P_APD_0 - 1

    # H30 = P_AXD_1 / P_AXD_0 - 1

    # H31 = P_AXW_1 / P_AXW_0 - 1

    # H32 = P_ADW_1 / P_ADW_0 - 1

    # H33 = P_ASD_1 / P_ASD_0 - 1

    # H34 = P_ATD_1 / P_ATD_0 - 1

    # H35 = P_AMD_1 / P_AMD_0 - 1

    # I25 = Q_IPD_1 / Q_IPD_0 - 1

    # I26 = Q_IXD_1 / Q_IXD_0 - 1

    # I27 = Q_AID_1 / Q_AID_0 - 1

    # I28 = Q_AVD_1 / Q_AVD_0 - 1

    # I29 = Q_APD_1 / Q_APD_0 - 1

    # I30 = Q_AXD_1 / Q_AXD_0 - 1

    # I31 = Q_AXW_1 / Q_AXW_0 - 1

    # I32 = Q_ADW_1 / Q_ADW_0 - 1

    # I33 = Q_ASD_1 / Q_ASD_0 - 1

    # I34 = Q_ATD_1 / Q_ATD_0 - 1

    # I35 = Q_AMD_1 / Q_AMD_0 - 1


input_data = InputDataBase(example_data)
result = wood_market(input_data)
