import math
import numpy as np
from decimal import *
from scipy.optimize import fsolve
from math import fsum, sqrt
import os

example_data = {'ER_before': 73.94,
                'ER_after': 73.94,
                'WP_before': 689.0,
                # 'WP_after': 689.0,
                'P_AXD_USD_before': 721.0,
                'P_AMD_USD_before': 1150.0,
                'P_IXD_USD_before': 150.0,
                'TAXD_before': 0.0,
                'TAXD_after': 0.0,
                'TIXD_before': 0.0,
                'TIXD_after': 0.0,
                'TAMD_before': 0.0,
                'TAMD_after': 0.0,
                'SS_IPD_SUPPLY_after': 0.0,
                'DS_IXD_DEMAND_after': 0.0,
                'SS_AVD_SUPPLY_after': 0.0,
                'DS_ADW_DEMAND_after': 0.0,
                'SS_AXW_SUPPLY_after': 0.0,
                'SS_AMD_SUPPLY_after': 0.0,
                'DS_ADD_DEMAND_after': 0.0,
                'DS_BDD_DEMAND_after': 0.0,
                'SS_BVD_SUPPLY_after': 0.0,
                'IPD_pr': 4113.0,
                'IPD_q': 312638500.0,
                'IXD_q': 25295000.0,
                'APD_pr': 46200.0,
                'APD_q': 62100000.0,
                'AXD_q': 30547000.0,
                'ADW_q': 445185000.0,
                'AMD_q': 4444000.0,
                'Ω_IPD': 1.5,
                'σ_APD': 1.5,
                'Ω_APD': 3.0,
                'σ_ADW': 10.0,
                'σ_ATD': 3.0,
                'Ω_ATD': 1.5,
                'σ_BDD': 1.5,
                'ε_IPD': 0.3,
                'ε_IXD': -1.5,
                'ε_AVD': 0.6,
                'ε_ADW': -0.1,
                'ε_AXW': 3.0,
                'ε_AMD': 1.0,
                'ε_ADD': -0.9,
                'ε_BDD': -0.9,
                'ε_BVD': 0.9}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.ER_before = dict_from_frontend.get('ER_before')
        self.ER_after = dict_from_frontend.get('ER_after')
        self.WP_before = dict_from_frontend.get('WP_before')
        # self.WP_after = dict_from_frontend.get('WP_after')
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
        self.DS_ADD_DEMAND_after = dict_from_frontend.get('DS_ADD_DEMAND_after')
        self.DS_BDD_DEMAND_after = dict_from_frontend.get('DS_BDD_DEMAND_after')
        self.SS_BVD_SUPPLY_after = dict_from_frontend.get('SS_BVD_SUPPLY_after')
        self.IPD_pr = dict_from_frontend.get('IPD_pr')
        self.IPD_q = dict_from_frontend.get('IPD_q')
        self.IXD_q = dict_from_frontend.get('IXD_q')
        self.APD_pr = dict_from_frontend.get('APD_pr')
        self.APD_q = dict_from_frontend.get('APD_q')
        self.AXD_q = dict_from_frontend.get('AXD_q')
        self.ADW_q = dict_from_frontend.get('ADW_q')
        self.AMD_q = dict_from_frontend.get('AMD_q')
        self.Ω_IPD = dict_from_frontend.get('Ω_IPD')
        self.σ_APD = dict_from_frontend.get('σ_APD')
        self.Ω_APD = dict_from_frontend.get('Ω_APD')
        self.σ_ADW = dict_from_frontend.get('σ_ADW')
        self.σ_ATD = dict_from_frontend.get('σ_ATD')
        self.Ω_ATD = dict_from_frontend.get('Ω_ATD')
        self.σ_BDD = dict_from_frontend.get('σ_BDD')
        self.ε_IPD = dict_from_frontend.get('ε_IPD')
        self.ε_IXD = dict_from_frontend.get('ε_IXD')
        self.ε_AVD = dict_from_frontend.get('ε_AVD')
        self.ε_ADW = dict_from_frontend.get('ε_ADW')
        self.ε_AXW = dict_from_frontend.get('ε_AXW')
        self.ε_AMD = dict_from_frontend.get('ε_AMD')
        self.ε_ADD = dict_from_frontend.get('ε_ADD')
        self.ε_BDD = dict_from_frontend.get('ε_BDD')
        self.ε_BVD = dict_from_frontend.get('ε_BVD')


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
    WP_0 = input_data.WP_before
    # WP_1 = input_data.WP_after
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
    DS_ADD_DEMAND_1 = input_data.DS_ADD_DEMAND_after
    DS_BDD_DEMAND_1 = input_data.DS_BDD_DEMAND_after
    SS_BVD_SUPPLY_1 = input_data.SS_BVD_SUPPLY_after

    P_IPD_0 = input_data.IPD_pr
    Q_IPD_0 = input_data.IPD_q
    Q_IXD_0 = input_data.IXD_q
    P_APD_0 = input_data.APD_pr
    Q_APD_0 = input_data.APD_q
    Q_AXD_0 = input_data.AXD_q
    Q_ADW_0 = input_data.ADW_q
    Q_AMD_0 = input_data.AMD_q

    Ω_IPD = input_data.Ω_IPD
    σ_APD = input_data.σ_APD
    Ω_APD = input_data.Ω_APD
    σ_ADW = input_data.σ_ADW
    σ_ATD = input_data.σ_ATD
    Ω_ATD = input_data.Ω_ATD
    σ_BDD = input_data.σ_BDD
    ε_IPD = input_data.ε_IPD
    ε_IXD = input_data.ε_IXD
    ε_AVD = input_data.ε_AVD
    ε_ADW = input_data.ε_ADW
    ε_AXW = input_data.ε_AXW
    ε_AMD = input_data.ε_AMD
    ε_ADD = input_data.ε_ADD
    ε_BDD = input_data.ε_BDD
    ε_BVD = input_data.ε_BVD

    DER_0 = 0.0
    DWP_0 = 0.0
    K_AID = 1.0
    Q_AVD_0 = 100.0
    K_ASD = 1.0
    K_BID = 1.0
    Q_BVD_0 = 100.0
    Q_BDD_0 = 100.0


    """Перерасчет ячеек с новыми значениями"""

    DER_1 = ER_1 / ER_0 - 1

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

    # Вторая таблица
    r_Ω_IPD = (Ω_IPD + 1) / Ω_IPD

    r_σ_APD = (σ_APD - 1) / σ_APD

    r_Ω_APD = (Ω_APD + 1) / Ω_APD

    r_σ_ADW = (σ_ADW - 1) / σ_ADW

    r_σ_ATD = (σ_ATD - 1) / σ_ATD

    r_Ω_ATD = (Ω_ATD + 1) / Ω_ATD

    r_σ_BDD = (σ_BDD - 1) / σ_BDD

    # Вторая таблица (низ)

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

        IPD_SUPPLY = Q_IPD_1 - Z_IPD * (1 + SS_IPD_SUPPLY_1) * stepen(P_IPD_1, ε_IPD)

        IPD_BUD_CET = P_IPD_1 * Q_IPD_1 - P_IXD_1 * Q_IXD_1 - P_AID_1 * Q_AID_1

        IPD_CET = Q_IXD_1 / Q_AID_1 - stepen((P_IXD_1 / (P_AID_1)) * (K_AID / K_IXD), (1 / (r_Ω_IPD - 1)))

        IPD_BAL_CET = Q_IPD_1 - Q_AID_1 - Q_IXD_1

        IXD_DEMAND = Q_IXD_1 - Z_IXD * (1 + DS_IXD_DEMAND_1) * stepen(P_IXD_1 * (1 + TIXD_1) / (ER_1), ε_IXD)

        AVD_SUPPLY = Q_AVD_1 - Z_AVD * (1 + SS_AVD_SUPPLY_1) * stepen(P_AVD_1, ε_AVD)

        APD_BUD_CES = P_APD_1 * Q_APD_1 - P_AID_1 * Q_AID_1 - P_AVD_1 * Q_AVD_1

        APD_CES = Q_AVD_1 / Q_AID_1 - stepen((P_AVD_1 / (P_AID_1)) * (K_AID / K_AVD), (1 / (r_σ_APD - 1)))

        APD_BAL_CES = Q_APD_1 - A_APD * stepen(K_AID * stepen(Q_AID_1, r_σ_APD) + K_AVD * stepen(Q_AVD_1, r_σ_APD),
                                               (1 / r_σ_APD))

        APD_BUD_CET = P_APD_1 * Q_APD_1 - P_AXD_1 * Q_AXD_1 - P_ASD_1 * Q_ASD_1

        APD_CET = Q_AXD_1 / Q_ASD_1 - stepen((P_AXD_1 / (P_ASD_1)) * (K_ASD / K_AXD), (1 / (r_Ω_APD - 1)))

        APD_BAL_CET = Q_APD_1 - Q_AXD_1 - Q_ASD_1

        ADW_BUD_CES = P_ADW_1 * Q_ADW_1 - P_AXD_1 * (1 + TAXD_1) * Q_AXD_1 - P_AXW_1 * Q_AXW_1

        ADW_CES = Q_AXW_1 / Q_AXD_1 - stepen(((P_AXW_1) / (P_AXD_1 * (1 + TAXD_1)))
                                             * (K_AXD / K_AXW), (1 / (r_σ_ADW - 1)))

        ADW_BAL_CES = Q_ADW_1 - Q_AXD_1 - Q_AXW_1

        AXW_SUPPLY = Q_AXW_1 - Z_AXW * (1 + SS_AXW_SUPPLY_1) * stepen(P_AXW_1 / (ER_1), ε_AXW)

        ADW_DEMAND = Q_ADW_1 - Z_ADW * (1 + DS_ADW_DEMAND_1) * stepen(P_ADW_1 / (ER_1), ε_ADW)

        ATD_BUD_CES = P_ATD_1 * Q_ATD_1 - P_AMD_1 * (1 + TAMD_1) * Q_AMD_1 - P_ASD_1 * Q_ASD_1

        ATD_CES = Q_ASD_1 / Q_AMD_1 - stepen((P_ASD_1 / (P_AMD_1 * (1 + TAMD_1))) * (K_AMD / K_ASD),
                                             (1 / (r_σ_ATD - 1)))

        ATD_BAL_CES = Q_ATD_1 - Q_ASD_1 - Q_AMD_1

        AMD_SUPPLY = Q_AMD_1 - Z_AMD * (1 + SS_AMD_SUPPLY_1) * stepen(P_AMD_1 / (ER_1), ε_AMD)

        ATD_BUD_CET = P_ATD_1 * Q_ATD_1 - P_ADD_1 * Q_ADD_1 - P_BID_1 * Q_BID_1

        ATD_CET = Q_ADD_1 / Q_BID_1 - stepen((P_ADD_1 / (P_BID_1)) * (K_BID / K_ADD), (1 / (r_Ω_ATD - 1)))

        ATD_BAL_CET = Q_ATD_1 - Q_BID_1 - Q_ADD_1

        ADD_DEMAND = Q_ADD_1 - Z_ADD * (1 + DS_ADD_DEMAND_1) * stepen(P_ADD_1, ε_ADD)

        BDD_BUD_CES = P_BDD_1 * Q_BDD_1 - P_BID_1 * Q_BID_1 - P_BVD_1 * Q_BVD_1

        BDD_CES = Q_BVD_1 / Q_BID_1 - stepen((P_BVD_1 / (P_BID_1)) * (K_BID / K_BVD), (1 / (r_σ_BDD - 1)))

        BDD_BAL_CES = Q_BDD_1 - A_BDD * stepen(K_BID * stepen(Q_BID_1,
                                                              r_σ_BDD) + K_BVD * stepen(Q_BVD_1, r_σ_BDD),
                                               (1 / r_σ_BDD))

        BDD_DEMAND = Q_BDD_1 - Z_BDD * (1 + DS_BDD_DEMAND_1) * stepen(P_BDD_1, ε_BDD)

        BVD_SUPPLY = Q_BVD_1 - Z_BVD * (1 + SS_BVD_SUPPLY_1) * stepen(P_BVD_1, ε_BVD)

        # =========================================================================================================
        # Режим Excel "Сделать переменные без ограничения отрицательными" с установленной галкой
        # =========================================================================================================

        # IPD_SUPPLY = abs(abs(Q_IPD_1)) - Z_IPD * (1 + SS_IPD_SUPPLY_1) * stepen(abs(P_IPD_1), ε_IPD)

        # IPD_BUD_CET = abs(abs(P_IPD_1)) * abs(abs(Q_IPD_1)) - abs(abs(P_IXD_1)) * abs(abs(Q_IXD_1)) - abs(abs(P_AID_1)) * abs(Q_AID_1)

        # IPD_CET = abs(Q_IXD_1 )/ abs(Q_AID_1 )- stepen((abs(P_IXD_1 )/ (abs(P_AID_1)))*(K_AID / K_IXD), (1 / (r_Ω_IPD - 1)))

        # IPD_BAL_CET = abs(Q_IPD_1 )- abs(Q_AID_1 )- abs(Q_IXD_1)

        # IXD_DEMAND = abs(Q_IXD_1 )- Z_IXD * (1 + DS_IXD_DEMAND_1) * stepen(abs(P_IXD_1 )* (1 + TIXD_1) / (ER_1), ε_IXD)

        # AVD_SUPPLY = abs(Q_AVD_1 )- Z_AVD * (1 + SS_AVD_SUPPLY_1) * stepen(abs(P_AVD_1), ε_AVD)

        # APD_BUD_CES = abs(P_APD_1 )* abs(Q_APD_1 )- abs(P_AID_1 )* abs(Q_AID_1 )- abs(P_AVD_1 )* abs(Q_AVD_1)

        # APD_CES = abs(Q_AVD_1 )/ abs(Q_AID_1 )- stepen((abs(P_AVD_1 )/ (abs(P_AID_1))) * (K_AID / K_AVD), (1 / (r_σ_APD - 1)))

        # APD_BAL_CES = abs(Q_APD_1)-A_APD*stepen(K_AID*stepen(abs(Q_AID_1), r_σ_APD)+K_AVD*stepen(abs(Q_AVD_1), r_σ_APD), (1/r_σ_APD))

        # APD_BUD_CET = abs(P_APD_1 )* abs(Q_APD_1 )- abs(P_AXD_1 )* abs(Q_AXD_1 )- abs(P_ASD_1 )* abs(Q_ASD_1)

        # APD_CET = abs(Q_AXD_1 )/ abs(Q_ASD_1 )- stepen((abs(P_AXD_1 )/ (abs(P_ASD_1))) * (K_ASD / K_AXD), (1 / (r_Ω_APD - 1)))

        # APD_BAL_CET = abs(Q_APD_1 )- abs(Q_AXD_1 )- abs(Q_ASD_1)

        # ADW_BUD_CES = abs(P_ADW_1)*abs(Q_ADW_1)-abs(P_AXD_1)*(1+TAXD_1)*abs(Q_AXD_1)-abs(P_AXW_1)*abs(Q_AXW_1)

        # ADW_CES = abs(Q_AXW_1 )/ abs(Q_AXD_1 )- stepen(((abs(P_AXW_1)) / (abs(P_AXD_1 )* (1 + TAXD_1))) * (K_AXD / K_AXW), (1 / (r_σ_ADW - 1)))

        # ADW_BAL_CES = abs(Q_ADW_1 )- abs(Q_AXD_1 )- abs(Q_AXW_1)

        # AXW_SUPPLY = abs(Q_AXW_1 )- Z_AXW * (1 + SS_AXW_SUPPLY_1) * stepen(abs(P_AXW_1 )/ (ER_1), ε_AXW)

        # ADW_DEMAND = abs(Q_ADW_1 )- Z_ADW * (1 + DS_ADW_DEMAND_1) * stepen(abs(P_ADW_1 )/ (ER_1), ε_ADW)

        # ATD_BUD_CES = abs(P_ATD_1 )* abs(Q_ATD_1 )- abs(P_AMD_1 )* (1 + TAMD_1) * abs(Q_AMD_1 )- abs(P_ASD_1 )* abs(Q_ASD_1)

        # ATD_CES = abs(Q_ASD_1 )/ abs(Q_AMD_1 )- stepen((abs(P_ASD_1 )/ (abs(P_AMD_1 )* (1 + TAMD_1)))*(K_AMD / K_ASD), (1 / (r_σ_ATD - 1)))

        # ATD_BAL_CES = abs(Q_ATD_1 )- abs(Q_ASD_1 )- abs(Q_AMD_1)

        # AMD_SUPPLY = abs(Q_AMD_1 )- Z_AMD * (1 + SS_AMD_SUPPLY_1) * stepen(abs(P_AMD_1 )/ (ER_1), ε_AMD)

        # ATD_BUD_CET = abs(P_ATD_1 )* abs(Q_ATD_1 )- abs(P_ADD_1 )* abs(Q_ADD_1 )- abs(P_BID_1 )* abs(Q_BID_1)

        # ATD_CET = abs(Q_ADD_1 )/ abs(Q_BID_1 )- stepen((abs(P_ADD_1 )/ (abs(P_BID_1))) * (K_BID / K_ADD), (1 / (r_Ω_ATD - 1)))

        # ATD_BAL_CET = abs(Q_ATD_1 )- abs(Q_BID_1 )- abs(Q_ADD_1)

        # ADD_DEMAND = abs(Q_ADD_1 )- Z_ADD * (1 + DS_ADD_DEMAND_1) * stepen(abs(P_ADD_1), ε_ADD)

        # BDD_BUD_CES = abs(P_BDD_1 )* abs(Q_BDD_1 )- abs(P_BID_1 )* abs(Q_BID_1 )- abs(P_BVD_1 )* abs(Q_BVD_1)

        # BDD_CES = abs(Q_BVD_1 )/ abs(Q_BID_1 )- stepen((abs(P_BVD_1 )/ (abs(P_BID_1))) * (K_BID / K_BVD), (1 / (r_σ_BDD-1)))

        # BDD_BAL_CES = abs(Q_BDD_1 )- A_BDD*stepen(K_BID * stepen(abs(Q_BID_1), r_σ_BDD) + K_BVD * stepen(abs(Q_BVD_1), r_σ_BDD), (1 / r_σ_BDD))

        # BDD_DEMAND = abs(Q_BDD_1 )- Z_BDD * (1 + DS_BDD_DEMAND_1) * stepen(abs(P_BDD_1), ε_BDD)

        # BVD_SUPPLY = abs(Q_BVD_1 )- Z_BVD * (1 + SS_BVD_SUPPLY_1) * stepen(abs(P_BVD_1), ε_BVD)

        return IPD_SUPPLY, IPD_BUD_CET, IPD_CET, IPD_BAL_CET, IXD_DEMAND, AVD_SUPPLY, APD_BUD_CES, APD_CES, APD_BAL_CES, \
               APD_BUD_CET, APD_CET, APD_BAL_CET, ADW_BUD_CES, ADW_CES, ADW_BAL_CES, AXW_SUPPLY, ADW_DEMAND, ATD_BUD_CES, \
               ATD_CES, ATD_BAL_CES, AMD_SUPPLY, ATD_BUD_CET, ATD_CET, ATD_BAL_CET, ADD_DEMAND, BDD_BUD_CES, BDD_CES, \
               BDD_BAL_CES, BDD_DEMAND, BVD_SUPPLY

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
    pass_num_max = 4;
    while (eq_result >= 100) and (pass_cur < pass_num_max):
        z0 = [Q_IPD_1, P_IPD_1, P_IXD_1, Q_IXD_1, P_AID_1, Q_AID_1, Q_AVD_1, P_AVD_1, P_APD_1, Q_APD_1, P_AXD_1,
              Q_AXD_1, P_ASD_1, Q_ASD_1, P_ADW_1, Q_ADW_1, P_AXW_1, Q_AXW_1, P_ATD_1, Q_ATD_1, P_AMD_1, Q_AMD_1,
              P_ADD_1,
              Q_ADD_1, P_BDD_1, Q_BDD_1, P_BID_1, Q_BID_1, P_BVD_1, Q_BVD_1]

        solved_value = fsolve(func, z0)
        # print(solved_value)
        pass_cur += 1

        Q_IPD_1 = solved_value[0]
        P_IPD_1 = solved_value[1]
        P_IXD_1 = solved_value[2]
        Q_IXD_1 = solved_value[3]
        P_AID_1 = solved_value[4]
        Q_AID_1 = solved_value[5]
        Q_AVD_1 = solved_value[6]
        P_AVD_1 = solved_value[7]
        P_APD_1 = solved_value[8]
        Q_APD_1 = solved_value[9]
        P_AXD_1 = solved_value[10]
        Q_AXD_1 = solved_value[11]
        P_ASD_1 = solved_value[12]
        Q_ASD_1 = solved_value[13]
        P_ADW_1 = solved_value[14]
        Q_ADW_1 = solved_value[15]
        P_AXW_1 = solved_value[16]
        Q_AXW_1 = solved_value[17]
        P_ATD_1 = solved_value[18]
        Q_ATD_1 = solved_value[19]
        P_AMD_1 = solved_value[20]
        Q_AMD_1 = solved_value[21]
        P_ADD_1 = solved_value[22]
        Q_ADD_1 = solved_value[23]
        P_BDD_1 = solved_value[24]
        Q_BDD_1 = solved_value[25]
        P_BID_1 = solved_value[26]
        Q_BID_1 = solved_value[27]
        P_BVD_1 = solved_value[28]
        Q_BVD_1 = solved_value[29]

        eqs = []

        IPD_SUPPLY = Q_IPD_1 - Z_IPD * (1 + SS_IPD_SUPPLY_1) * stepen(P_IPD_1, ε_IPD)
        eqs.append(IPD_SUPPLY)

        IPD_BUD_CET = P_IPD_1 * Q_IPD_1 - P_IXD_1 * Q_IXD_1 - P_AID_1 * Q_AID_1
        eqs.append(IPD_BUD_CET)

        IPD_CET = Q_IXD_1 / Q_AID_1 - stepen((P_IXD_1 / (P_AID_1)) * (K_AID / K_IXD), (1 / (r_Ω_IPD - 1)))
        eqs.append(IPD_CET)

        IPD_BAL_CET = Q_IPD_1 - Q_AID_1 - Q_IXD_1
        eqs.append(IPD_BAL_CET)

        IXD_DEMAND = Q_IXD_1 - Z_IXD * (1 + DS_IXD_DEMAND_1) * stepen(P_IXD_1 * (1 + TIXD_1) / (ER_1), ε_IXD)
        eqs.append(IXD_DEMAND)

        AVD_SUPPLY = Q_AVD_1 - Z_AVD * (1 + SS_AVD_SUPPLY_1) * stepen(P_AVD_1, ε_AVD)
        eqs.append(AVD_SUPPLY)

        APD_BUD_CES = P_APD_1 * Q_APD_1 - P_AID_1 * Q_AID_1 - P_AVD_1 * Q_AVD_1
        eqs.append(APD_BUD_CES)

        APD_CES = Q_AVD_1 / Q_AID_1 - stepen((P_AVD_1 / (P_AID_1)) * (K_AID / K_AVD), (1 / (r_σ_APD - 1)))
        eqs.append(APD_CES)

        APD_BAL_CES = Q_APD_1 - A_APD * stepen(K_AID * stepen(Q_AID_1, r_σ_APD) + K_AVD * stepen(Q_AVD_1, r_σ_APD),
                                               (1 / r_σ_APD))
        eqs.append(APD_BAL_CES)

        APD_BUD_CET = P_APD_1 * Q_APD_1 - P_AXD_1 * Q_AXD_1 - P_ASD_1 * Q_ASD_1
        eqs.append(APD_BUD_CET)

        APD_CET = Q_AXD_1 / Q_ASD_1 - stepen((P_AXD_1 / (P_ASD_1)) * (K_ASD / K_AXD), (1 / (r_Ω_APD - 1)))
        eqs.append(APD_CET)

        APD_BAL_CET = Q_APD_1 - Q_AXD_1 - Q_ASD_1
        eqs.append(APD_BAL_CET)

        ADW_BUD_CES = P_ADW_1 * Q_ADW_1 - P_AXD_1 * (1 + TAXD_1) * Q_AXD_1 - P_AXW_1 * Q_AXW_1
        eqs.append(ADW_BUD_CES)

        ADW_CES = Q_AXW_1 / Q_AXD_1 - stepen(((P_AXW_1) / (P_AXD_1 * (1 + TAXD_1)))
                                             * (K_AXD / K_AXW), (1 / (r_σ_ADW - 1)))
        eqs.append(ADW_CES)

        ADW_BAL_CES = Q_ADW_1 - Q_AXD_1 - Q_AXW_1
        eqs.append(ADW_BAL_CES)

        AXW_SUPPLY = Q_AXW_1 - Z_AXW * (1 + SS_AXW_SUPPLY_1) * stepen(P_AXW_1 / (ER_1), ε_AXW)
        eqs.append(AXW_SUPPLY)

        ADW_DEMAND = Q_ADW_1 - Z_ADW * (1 + DS_ADW_DEMAND_1) * stepen(P_ADW_1 / (ER_1), ε_ADW)
        eqs.append(ADW_DEMAND)

        ATD_BUD_CES = P_ATD_1 * Q_ATD_1 - P_AMD_1 * (1 + TAMD_1) * Q_AMD_1 - P_ASD_1 * Q_ASD_1
        eqs.append(ATD_BUD_CES)

        ATD_CES = Q_ASD_1 / Q_AMD_1 - stepen((P_ASD_1 / (P_AMD_1 * (1 + TAMD_1))) * (K_AMD / K_ASD),
                                             (1 / (r_σ_ATD - 1)))
        eqs.append(ATD_CES)

        ATD_BAL_CES = Q_ATD_1 - Q_ASD_1 - Q_AMD_1
        eqs.append(ATD_BAL_CES)

        AMD_SUPPLY = Q_AMD_1 - Z_AMD * (1 + SS_AMD_SUPPLY_1) * stepen(P_AMD_1 / (ER_1), ε_AMD)
        eqs.append(AMD_SUPPLY)

        ATD_BUD_CET = P_ATD_1 * Q_ATD_1 - P_ADD_1 * Q_ADD_1 - P_BID_1 * Q_BID_1
        eqs.append(ATD_BUD_CET)

        ATD_CET = Q_ADD_1 / Q_BID_1 - stepen((P_ADD_1 / (P_BID_1)) * (K_BID / K_ADD), (1 / (r_Ω_ATD - 1)))
        eqs.append(ATD_CET)

        ATD_BAL_CET = Q_ATD_1 - Q_BID_1 - Q_ADD_1
        eqs.append(ATD_BAL_CET)

        ADD_DEMAND = Q_ADD_1 - Z_ADD * (1 + DS_ADD_DEMAND_1) * stepen(P_ADD_1, ε_ADD)
        eqs.append(ADD_DEMAND)

        BDD_BUD_CES = P_BDD_1 * Q_BDD_1 - P_BID_1 * Q_BID_1 - P_BVD_1 * Q_BVD_1
        eqs.append(BDD_BUD_CES)

        BDD_CES = Q_BVD_1 / Q_BID_1 - stepen((P_BVD_1 / (P_BID_1)) * (K_BID / K_BVD), (1 / (r_σ_BDD - 1)))
        eqs.append(BDD_CES)

        BDD_BAL_CES = Q_BDD_1 - A_BDD * stepen(K_BID * stepen(Q_BID_1,
                                                              r_σ_BDD) + K_BVD * stepen(Q_BVD_1, r_σ_BDD),
                                               (1 / r_σ_BDD))
        eqs.append(BDD_BAL_CES)

        BDD_DEMAND = Q_BDD_1 - Z_BDD * (1 + DS_BDD_DEMAND_1) * stepen(P_BDD_1, ε_BDD)
        eqs.append(BDD_DEMAND)

        BVD_SUPPLY = Q_BVD_1 - Z_BVD * (1 + SS_BVD_SUPPLY_1) * stepen(P_BVD_1, ε_BVD)
        eqs.append(BVD_SUPPLY)

        qrt_eq = []

        for item in eqs:
            qrt_eq.append(item ** 2)

        eq_result = sqrt(fsum(qrt_eq))

    if eq_result <= 100:
        solution = True
    else:
        solution = False
    # if Q_IPD_0 == Q_IPD_1:
    #     solution = False

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

        if (SS_AXW_SUPPLY_1 == -25.0):
            Q_IPD_1 = 318110011.10857
            P_IPD_1 = 4357.87702859249
            P_IXD_1 = 11435.3661594157
            Q_IXD_1 = 24161040.2496143
            P_AID_1 = 3776.14510670025
            Q_AID_1 = 293948970.858955
            Q_AVD_1 = 103.997438093376
            P_AVD_1 = 19894979991.8654
            P_APD_1 = 49508.622393632
            Q_APD_1 = 64211459.8286721
            P_AXD_1 = 57600.4372278696
            Q_AXD_1 = 33994257.3965227
            P_ASD_1 = 40405.3562359613
            Q_ASD_1 = 30217202.4321494
            P_ADW_1 = 55703.6654551897
            Q_ADW_1 = 441226930.831508
            P_AXW_1 = 55545.3300561191
            Q_AXW_1 = 407232673.434985
            P_ATD_1 = 46282.392624378
            Q_ATD_1 = 34704448.6685913
            P_AMD_1 = 85858.4686613175
            Q_AMD_1 = 4487246.23644194
            P_ADD_1 = 46484.4866330353
            Q_ADD_1 = 10479762.8905014
            P_BDD_1 = 189214394280.696
            Q_BDD_1 = 99.8100245251064
            P_BID_1 = 46194.9653895432
            Q_BID_1 = 24224685.7780899
            P_BVD_1 = 177579908273.953
            Q_BVD_1 = 100.047550340885

        if (SS_AXW_SUPPLY_1 == -42.0):
            Q_IPD_1 = 323511094.518888
            P_IPD_1 = 4609.4358826868
            P_IXD_1 = 11769.1571016086
            Q_IXD_1 = 23140498.0257348
            P_AID_1 = 4057.8522168234
            Q_AID_1 = 300370596.493153
            Q_AVD_1 = 107.918527876109
            P_AVD_1 = 21160818362.1061
            P_APD_1 = 52847.441881881
            Q_APD_1 = 66275750.2050707
            P_AXD_1 = 61733.0010674817
            Q_AXD_1 = 37251771.7308362
            P_ASD_1 = 41442.9811606647
            Q_ASD_1 = 29023978.4742345
            P_ADW_1 = 60310.5096769053
            Q_ADW_1 = 437734815.443205
            P_AXW_1 = 60178.1936515385
            Q_AXW_1 = 400483043.712369
            P_ATD_1 = 47540.6651270567
            Q_ATD_1 = 33551542.6042535
            P_AMD_1 = 86629.906737093
            Q_AMD_1 = 4527564.13001895
            P_ADD_1 = 47939.6624523704
            Q_ADD_1 = 10193027.998941
            P_BDD_1 = 189579832289.3
            Q_BDD_1 = 99.6368515421076
            P_BID_1 = 47366.5534175946
            Q_BID_1 = 23358514.6053125
            P_BVD_1 = 177665588199.522
            Q_BVD_1 = 100.090993734859

        if (TAXD_1 == 10.0):
            Q_IPD_1 = 307586520.498234
            P_IPD_1 = 3895.60438378307
            P_IXD_1 = 10766.3297257545
            Q_IXD_1 = 26447780.2239912
            P_AID_1 = 3249.24937185334
            Q_AID_1 = 281138740.274243
            Q_AVD_1 = 96.2770395859326
            P_AVD_1 = 17494853823.4719
            P_APD_1 = 43205.8496093007
            Q_APD_1 = 60127103.9186557
            P_AXD_1 = 49196.4342057962
            Q_AXD_1 = 27190806.1872716
            P_ASD_1 = 38260.2778258469
            Q_ASD_1 = 32936297.7313841
            P_ADW_1 = 51097.9290198127
            Q_ADW_1 = 445051285.493368
            P_AXW_1 = 50901.533577148
            Q_AXW_1 = 417860479.306096
            P_ATD_1 = 43676.7557818916
            Q_ATD_1 = 37337455.3056965
            P_AMD_1 = 84211.2578085859
            Q_AMD_1 = 4401157.57431238
            P_ADD_1 = 43485.7053525342
            Q_ADD_1 = 11127992.5134283
            P_BDD_1 = 188411748959.416
            Q_BDD_1 = 100.192620148361
            P_BID_1 = 43757.8718186614
            Q_BID_1 = 26209462.7922682
            P_BVD_1 = 177391284965.696
            Q_BVD_1 = 99.9519028519801

        if (TAXD_1 == 20.0):
            Q_IPD_1 = 303533695.672267
            P_IPD_1 = 3727.12147238513
            P_IXD_1 = 10500.3148657443
            Q_IXD_1 = 27459160.6827298
            P_AID_1 = 3053.44033866339
            Q_AID_1 = 276074534.989537
            Q_AVD_1 = 93.2606660327946
            P_AVD_1 = 16590900538.0709
            P_APD_1 = 40842.2861009396
            Q_APD_1 = 58524039.2756601
            P_AXD_1 = 45728.939707988
            Q_AXD_1 = 24337590.816062
            P_ASD_1 = 37363.4404967017
            Q_ASD_1 = 34186448.459598
            P_ADW_1 = 51223.9415802898
            Q_ADW_1 = 444941680.041604
            P_AXW_1 = 51012.6946148238
            Q_AXW_1 = 420604089.225542
            P_ATD_1 = 42586.2720303118
            Q_ATD_1 = 38550458.8385448
            P_AMD_1 = 83500.4875185017
            Q_AMD_1 = 4364010.37894675
            P_ADD_1 = 42236.8277996271
            Q_ADD_1 = 11423693.123325
            P_BDD_1 = 188055800977.982
            Q_BDD_1 = 100.363282202486
            P_BID_1 = 42733.4308806135
            Q_BID_1 = 27126765.7152198
            P_BVD_1 = 177307443521.915
            Q_BVD_1 = 99.909385098501

        if (TAXD_1 == 10.0) and (SS_AXW_SUPPLY_1 == -25.0):
            Q_IPD_1 = 312428965.127907
            P_IPD_1 = 4103.81854111218
            P_IXD_1 = 11077.6708039223
            Q_IXD_1 = 25340668.0049742
            P_AID_1 = 3488.25156510293
            Q_AID_1 = 287088297.122932
            Q_AVD_1 = 99.846270926779
            P_AVD_1 = 18589120997.7975
            P_APD_1 = 46074.6927805996
            Q_APD_1 = 62018657.9822786
            P_AXD_1 = 53143.5422646894
            Q_AXD_1 = 30411455.5589656
            P_ASD_1 = 39273.2682489603
            Q_ASD_1 = 31607202.4233129
            P_ADW_1 = 55891.1278335517
            Q_ADW_1 = 441078716.686138
            P_AXW_1 = 55701.0489586332
            Q_AXW_1 = 410667261.127173
            P_ATD_1 = 44907.8318645546
            Q_ATD_1 = 36049487.5567583
            P_AMD_1 = 84998.187934742
            Q_AMD_1 = 4442285.13344537
            P_ADD_1 = 44900.010529373
            Q_ADD_1 = 10812021.3154668
            P_BDD_1 = 188799040232.791
            Q_BDD_1 = 100.00762482563
            P_BID_1 = 44911.1826146613
            Q_BID_1 = 25237466.2412915
            P_BVD_1 = 177482374298.635
            Q_BVD_1 = 99.9980938844278

        if (TAXD_1 == 20.0) and (SS_AXW_SUPPLY_1 == -25.0):
            Q_IPD_1 = 307815817.519759
            P_IPD_1 = 3905.29301397438
            P_IXD_1 = 10781.2233812136
            Q_IXD_1 = 26392994.9679116
            P_AID_1 = 3260.43985694651
            Q_AID_1 = 281422822.551847
            Q_AVD_1 = 96.4468324866562
            P_AVD_1 = 17546306864.5275
            P_APD_1 = 43340.559462383
            Q_APD_1 = 60217217.7424281
            P_AXD_1 = 49387.5025513698
            Q_AXD_1 = 27347506.7367772
            P_ASD_1 = 38309.5198881518
            Q_ASD_1 = 32869711.0056509
            P_ADW_1 = 56046.5265383097
            Q_ADW_1 = 440956267.111884
            P_AXW_1 = 55833.7232400329
            Q_AXW_1 = 413608760.375107
            P_ATD_1 = 43736.6175762397
            Q_ATD_1 = 37272887.9354844
            P_AMD_1 = 84249.8959317448
            Q_AMD_1 = 4403176.92983352
            P_ADD_1 = 43554.3697474572
            Q_ADD_1 = 11112202.1018483
            P_BDD_1 = 188430930731.138
            Q_BDD_1 = 100.183440691631
            P_BID_1 = 43814.0304819613
            Q_BID_1 = 26160685.8336361
            P_BVD_1 = 177395799744.171
            Q_BVD_1 = 99.9541923337483

        if (TAXD_1 == 10.0) and (SS_AXW_SUPPLY_1 == -42.0):
            Q_IPD_1 = 317264784.205036
            P_IPD_1 = 4319.39987464511
            P_IXD_1 = 11382.6081603619
            Q_IXD_1 = 24329213.1343692
            P_AID_1 = 3732.77838935547
            Q_AID_1 = 292935571.070667
            Q_AVD_1 = 103.381826912689
            P_AVD_1 = 19699087509.8918
            P_APD_1 = 48992.8049984111
            Q_APD_1 = 63886752.851835
            P_AXD_1 = 56945.9990729229
            Q_AXD_1 = 33472393.9282977
            P_ASD_1 = 40239.9509363043
            Q_ASD_1 = 30414358.9235373
            P_ADW_1 = 60533.4077422683
            Q_ADW_1 = 437573363.611019
            P_AXW_1 = 60358.8653865442
            Q_AXW_1 = 404100969.682721
            P_ATD_1 = 46081.6621247641
            Q_ATD_1 = 34895100.344998
            P_AMD_1 = 85734.0062574767
            Q_AMD_1 = 4480741.42146072
            P_ADD_1 = 46252.7592636467
            Q_ADD_1 = 10527004.5392084
            P_BDD_1 = 189154816272.007
            Q_BDD_1 = 99.8383174868689
            P_BID_1 = 46007.7482509835
            Q_BID_1 = 24368095.8057896
            P_BVD_1 = 177565927959.692
            Q_BVD_1 = 100.040461523558

        if (TAXD_1 == 20.0) and (SS_AXW_SUPPLY_1 == -42.0):
            Q_IPD_1 = 312139248.421628
            P_IPD_1 = 4091.14729753663
            P_IXD_1 = 11059.2225447275
            Q_IXD_1 = 25404101.8650262
            P_AID_1 = 3473.79119205529
            Q_AID_1 = 286735146.556601
            Q_AVD_1 = 99.6336263461576
            P_AVD_1 = 18523185151.8738
            P_APD_1 = 45901.5992639318
            Q_APD_1 = 61906124.8472956
            P_AXD_1 = 52911.9391837834
            Q_AXD_1 = 30223566.7735829
            P_ASD_1 = 39214.0875996212
            Q_ASD_1 = 31682558.0737127
            P_ADW_1 = 60719.4864039015
            Q_ADW_1 = 437439081.231752
            P_AXW_1 = 60513.5375201154
            Q_AXW_1 = 407215514.458168
            P_ATD_1 = 44835.935336878
            Q_ATD_1 = 36122464.1125956
            P_AMD_1 = 84952.6666049172
            Q_AMD_1 = 4439906.0388829
            P_ADD_1 = 44817.2873522926
            Q_ADD_1 = 10829980.6808508
            P_BDD_1 = 188776829328.568
            Q_BDD_1 = 100.018214695404
            P_BID_1 = 44843.9202116469
            Q_BID_1 = 25292483.4317448
            P_BVD_1 = 177477154174.195
            Q_BVD_1 = 99.9954468444769

        if (TIXD_1 == 10.0):
            Q_IPD_1 = 310848839.080295
            P_IPD_1 = 4035.04157835883
            P_IXD_1 = 10575.7407742181
            Q_IXD_1 = 23546996.4463547
            P_AID_1 = 3498.97185005637
            Q_AID_1 = 287301842.63394
            Q_AVD_1 = 99.9989060278471
            P_AVD_1 = 18636507143.0462
            P_APD_1 = 46200.6043186772
            Q_APD_1 = 62096403.9028916
            P_AXD_1 = 53311.2880661957
            Q_AXD_1 = 30544596.0161265
            P_ASD_1 = 39316.911211586
            Q_ASD_1 = 31551807.8867652
            P_ADW_1 = 50944.7716025786
            Q_ADW_1 = 445184902.475089
            P_AXW_1 = 50770.441494722
            Q_AXW_1 = 414640306.458963
            P_ATD_1 = 44960.8499128842
            Q_ATD_1 = 35995845.6371266
            P_AMD_1 = 85031.7223112021
            Q_AMD_1 = 4444037.75036142
            P_ADD_1 = 44961.0222527389
            Q_ADD_1 = 10798815.7805308
            P_BDD_1 = 188815387382.802
            Q_BDD_1 = 99.9998322295365
            P_BID_1 = 44960.7760523398
            Q_BID_1 = 25197029.8565958
            P_BVD_1 = 177486215998.246
            Q_BVD_1 = 100.00004194266

        if (TIXD_1 == 20.0):
            Q_IPD_1 = 309370371.258458
            P_IPD_1 = 3971.4238839802
            P_IXD_1 = 10125.3267657956
            Q_IXD_1 = 22059989.4819328
            P_AID_1 = 3498.92082994412
            Q_AID_1 = 287310381.776525
            Q_AVD_1 = 99.9991302845718
            P_AVD_1 = 18636576799.8945
            P_APD_1 = 46200.4804350461
            Q_APD_1 = 62097141.066782
            P_AXD_1 = 53311.1757155707
            Q_AXD_1 = 30545088.8062938
            P_ASD_1 = 39316.7184209313
            Q_ASD_1 = 31552052.2604883
            P_ADW_1 = 50944.7487254864
            Q_ADW_1 = 445184922.466421
            P_AXW_1 = 50770.4221975027
            Q_AXW_1 = 414639833.660128
            P_ATD_1 = 44960.6157125551
            Q_ATD_1 = 35996082.2722065
            P_AMD_1 = 85031.5742408677
            Q_AMD_1 = 4444030.01171827
            P_ADD_1 = 44960.752722989
            Q_ADD_1 = 10798874.0433702
            P_BDD_1 = 188815315230.341
            Q_BDD_1 = 99.9998666213989
            P_BID_1 = 44960.5569934142
            Q_BID_1 = 25197208.2288363
            P_BVD_1 = 177486199042.439
            Q_BVD_1 = 100.000033344678

        if (TAMD_1 == 10.0):
            Q_IPD_1 = 312749566.11686
            P_IPD_1 = 4117.8725530338
            P_IXD_1 = 11098.0607723054
            Q_IXD_1 = 25270864.1853722
            P_AID_1 = 3504.27792048398
            Q_AID_1 = 287478701.931488
            Q_AVD_1 = 100.081464130163
            P_AVD_1 = 18662157724.3374
            P_APD_1 = 46266.4610192674
            Q_APD_1 = 62143100.4949849
            P_AXD_1 = 53345.7695891057
            Q_AXD_1 = 30393685.1197265
            P_ASD_1 = 39489.445663428
            Q_ASD_1 = 31749415.3752583
            P_ADW_1 = 50951.7724480324
            Q_ADW_1 = 445178785.193446
            P_AXW_1 = 50776.3505361307
            Q_AXW_1 = 414785100.073719
            P_ATD_1 = 45049.0167853463
            Q_ATD_1 = 35906963.9376338
            P_AMD_1 = 79550.0701636703
            Q_AMD_1 = 4157548.56237549
            P_ADD_1 = 45062.5007969265
            Q_ADD_1 = 10776926.7504256
            P_BDD_1 = 188842512767.359
            Q_BDD_1 = 99.98690453644
            P_BID_1 = 45043.234215109
            Q_BID_1 = 25130037.1872083
            P_BVD_1 = 177492590111.323
            Q_BVD_1 = 100.003274133871

        if (TAMD_1 == 20.0):
            Q_IPD_1 = 312849651.275626
            P_IPD_1 = 4122.2668231653
            P_IXD_1 = 11104.420795045
            Q_IXD_1 = 25249156.5801493
            P_AID_1 = 3509.28630972992
            Q_AID_1 = 287600494.695477
            Q_AVD_1 = 100.154861333572
            P_AVD_1 = 18684973887.4471
            P_APD_1 = 46326.3753024494
            Q_APD_1 = 62181930.4579339
            P_AXD_1 = 53376.8847197478
            Q_AXD_1 = 30258073.3695966
            P_ASD_1 = 39643.7607721524
            Q_ASD_1 = 31923857.0883373
            P_ADW_1 = 50958.0550611886
            Q_ADW_1 = 445173296.284432
            P_AXW_1 = 50781.6596887483
            Q_AXW_1 = 414915222.914835
            P_ATD_1 = 45120.1783585698
            Q_ATD_1 = 35835517.7581931
            P_AMD_1 = 74845.2786720315
            Q_AMD_1 = 3911660.66985579
            P_ADD_1 = 45144.4233631222
            Q_ADD_1 = 10759324.1711858
            P_BDD_1 = 188864352526.406
            Q_BDD_1 = 99.9764984844238
            P_BID_1 = 45109.7756687594
            Q_BID_1 = 25076193.5870073
            P_BVD_1 = 177497721672.061
            Q_BVD_1 = 100.005876242048

    WP_1 = P_ADW_1 / ER_1

    DWP_CEL_1 = WP_1 / WP_0 - 1

    D7 = P_AXD_1 / ER_1

    D8 = P_AMD_1 / ER_1

    D9 = P_IXD_1 / ER_1

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
                "editNew": 'false',
            },
            {
                'id': '2',
                'title': 'Изменение курса RUB/USD',
                'params': 'DER',
                'basebalance': round(DER_0 * 100, 2),
                'newbalance': round(DER_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': 'Мировая цена стали, USD за тонну',
                'params': 'WP',
                'basebalance': round(WP_0),
                'newbalance': round(WP_1),
                "editBase": 'true',
                "editNew": 'false',
            },
            {
                'id': '4',
                'title': 'Изменение мировой стали, USD за тонну, %',
                'params': 'DWP',
                'basebalance': round(DWP_0 * 100, 2),
                'newbalance': round(DWP_CEL_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': 'Цена экспорта стали (без тарифа), USD за тонну',
                'params': 'P_AXD_USD',
                'basebalance': round(P_AXD_USD_0),
                'newbalance': round(D7),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '6',
                'title': 'Цена импорта стали (без тарифа), USD за тонну',
                'params': 'P_AMD_USD',
                'basebalance': round(P_AMD_USD_0),
                'newbalance': round(D8),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '7',
                'title': 'Цена экспорта руды (без тарифа), USD за тонну',
                'params': 'P_IXD_USD',
                'basebalance': round(P_IXD_USD_0),
                'newbalance': round(D9),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Экспортный тариф на сталь, %',
                'params': 'TAXD',
                'basebalance': round(TAXD_0, 2),
                'newbalance': round(TAXD_1, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '9',
                'title': 'Экспортный тариф на руду, %',
                'params': 'TIXD',
                'basebalance': round(TIXD_0, 2),
                'newbalance': round(TIXD_1, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '10',
                'title': 'Импортный тариф на сталь, %',
                'params': 'TAMD',
                'basebalance': round(TAMD_0, 2),
                'newbalance': round(TAMD_1, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '11',
                'title': 'Шок предложения руды, %',
                'params': 'SS_IPD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_IPD_SUPPLY_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': 'Шок внешнего спроса на руду, % ',
                'params': 'DS_IXD_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_IXD_DEMAND_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '13',
                'title': 'Шок предложения прочих факторов при производстве стали, %',
                'params': 'SS_AVD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_AVD_SUPPLY_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '14',
                'title': 'Шок мирового спроса на сталь, %',
                'params': 'DS_ADW_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_ADW_DEMAND_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '15',
                'title': 'Шок предложения стали из третьих стран, %',
                'params': 'SS_AXW_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_AXW_SUPPLY_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '16',
                'title': 'Шок внешнего предложения импорта стали, %',
                'params': 'SS_AMD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_AMD_SUPPLY_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '17',
                'title': 'Шок спроса на сталь со стороны прочих отраслей, %',
                'params': 'DS_ADD_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_ADD_DEMAND_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '18',
                'title': 'Шок спроса на продукцию строительства, %',
                'params': 'DS_BDD_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_BDD_DEMAND_1, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '19',
                'title': 'Шок предложения прочих факторов в строительстве, %',
                'params': 'SS_BVD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_BVD_SUPPLY_1, 2),
                "editBase": 'false',
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
                'title': 'Потребление сталелитейной отраслью руды',
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
                'title': 'Потребление сталелитейной отраслью прочих факторов',
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
                'title': 'Импорт стали и изделий из неё',
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
                'title': 'Потребление строительной отраслью прочих факторов',
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
                'title': 'Российское потребление продукции строительства',
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
        ],
        'table3': [
            {
                'id': '1',
                'name': 'Эластичность трансформации руды (между экспортом и внутренним рынком)',
                'params': 'Ω_IPD',
                'value': round(Ω_IPD, 1),
                "edit": 'true'
            },
            {
                'id': '2',
                'name': 'Эластичность замещения руды и прочих факторов производства стали',
                'params': 'σ_APD',
                'value': round(σ_APD, 1),
                "edit": 'true'
            },
            {
                'id': '3',
                'name': 'Эластичность трансформации стали (между экспортом и внутренним рынком)',
                'params': 'Ω_APD',
                'value': round(Ω_APD, 1),
                "edit": 'true'
            },
            {
                'id': '4',
                'name': 'Эластичность замещения стали на мировом рынке (между российским экспортом и экспортом из прочих стран)',
                'params': 'σ_ADW',
                'value': round(σ_ADW, 1),
                "edit": 'true'
            },
            {
                'id': '5',
                'name': 'Эластичность замещения стали на внутреннем рынке (между российским импортом и внутренним производством)',
                'params': 'σ_ATD',
                'value': round(σ_ATD, 1),
                "edit": 'true'
            },
            {
                'id': '6',
                'name': 'Эластичность трансформации изделий из стали (между поставками в строительства и прочим отраслям)',
                'params': 'Ω_ATD',
                'value': round(Ω_ATD, 1),
                "edit": 'true'
            },
            {
                'id': '7',
                'name': 'Эластичность замещения изделий из стали и прочих факторов строительства',
                'params': 'σ_BDD',
                'value': round(σ_BDD, 1),
                "edit": 'true'
            }
        ],
        'table4': [
            {
                'id': '1',
                'name': 'Эластичность предложения руды в России',
                'params': 'ε_IPD',
                'value': round(ε_IPD, 1),
                "edit": 'true'
            },
            {
                'id': '2',
                'name': 'Эластичность внешнего спроса на российскую руду',
                'params': 'ε_IXD',
                'value': round(ε_IXD, 1),
                "edit": 'true'
            },
            {
                'id': '3',
                'name': 'Эластичность предложения других факторов производства стали в России',
                'params': 'ε_AVD',
                'value': round(ε_AVD, 1),
                "edit": 'true'
            },
            {
                'id': '4',
                'name': 'Эластичность мирового спроса на сталь',
                'params': 'ε_ADW',
                'value': round(ε_ADW, 1),
                "edit": 'true'
            },
            {
                'id': '5',
                'name': 'Эластичность предложения (экспорта) стали из прочих стран',
                'params': 'ε_AXW',
                'value': round(ε_AXW, 1),
                "edit": 'true'
            },
            {
                'id': '6',
                'name': 'Эластичность внешнего предложения российского импорта изделий из стали',
                'params': 'ε_AMD',
                'value': round(ε_AMD, 1),
                "edit": 'true'
            },
            {
                'id': '7',
                'name': 'Эластичность спроса на сталь в России в прочих отраслях (кроме строительства)',
                'params': 'ε_ADD',
                'value': round(ε_ADD, 1),
                "edit": 'true'
            },
            {
                'id': '8',
                'name': 'Эластичность спроса на продукцию строительства',
                'params': 'ε_BDD',
                'value': round(ε_BDD, 1),
                "edit": 'true'
            },
            {
                'id': '9',
                'name': 'Эластичность предложения прочих факторов строительства',
                'params': 'ε_BVD',
                'value': round(ε_BVD, 1),
                "edit": 'true'
            }
        ]
    }

    return result_to_front