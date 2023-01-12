from math import fsum, sqrt
import numpy as np
from scipy.optimize import fsolve, root


example_data = {'ER_before': 73.65,
                'ER_after': 73.65,
                'WPK_before': 997.0345963756178,
                'WPK_after': 997.0345963756178,
                'WPN_before': 1615.058823529412,
                'WPN_after': 1615.058823529412,
                'P_KXD_USD_before': 779.0,
                'P_NXD_USD_before': 1717.0,
                'TKXD_before': 0.0,
                'TKXD_after': 0.0,
                'TNXD_before': 0.0,
                'TNXD_after': 0.0,
                'KPD_pr': 49722.0,
                'KPD_q': 9327769.0,
                'KXD_q': 7220000.0,
                'NPD_pr': 92549.0,
                'NPD_q': 10874475.0,
                'NXD_q': 6150000.0,
                'KSW_q': 34599000.0,
                'NSW_q': 39355000.0}

class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.WPK_before = float(dict_from_frontend.get('WPK_before'))
        self.WPK_after = float(dict_from_frontend.get('WPK_after'))
        self.WPN_before = float(dict_from_frontend.get('WPN_before'))
        self.WPN_after = float(dict_from_frontend.get('WPN_after'))
        self.P_KXD_USD_before = float(dict_from_frontend.get('P_KXD_USD_before'))
        self.P_NXD_USD_before = float(dict_from_frontend.get('P_NXD_USD_before'))
        self.TKXD_before = float(dict_from_frontend.get('TKXD_before'))
        self.TKXD_after = float(dict_from_frontend.get('TKXD_after'))
        self.TNXD_before = float(dict_from_frontend.get('TNXD_before'))
        self.TNXD_after = float(dict_from_frontend.get('TNXD_after'))
        self.KPD_pr = float(dict_from_frontend.get('KPD_pr'))
        self.KPD_q = float(dict_from_frontend.get('KPD_q'))
        self.KXD_q = float(dict_from_frontend.get('KXD_q'))
        self.NPD_pr = float(dict_from_frontend.get('NPD_pr'))
        self.NPD_q = float(dict_from_frontend.get('NPD_q'))
        self.NXD_q = float(dict_from_frontend.get('NXD_q'))
        self.KSW_q = float(dict_from_frontend.get('KSW_q'))
        self.NSW_q = float(dict_from_frontend.get('NSW_q'))

o = 14

def stepen(x, st):
    if (x < 0):
        # print(f'x={round(x, o)}, st={round(st, o)}')
        return np.sign(x) * (np.abs(x) ** st)
    else:
        return x ** st


def fertilizers_market(input_data):
    """Вводим новые значения"""

    ER_0 = input_data.ER_before
    ER_1 = input_data.ER_after
    WPK_0 = input_data.WPK_before
    WPK_1 = input_data.WPK_after
    WPN_0 = input_data.WPN_before
    WPN_1 = input_data.WPN_after
    P_KXD_USD_0 = input_data.P_KXD_USD_before
    P_NXD_USD_0 = input_data.P_NXD_USD_before
    TKXD_0 = input_data.TKXD_before
    TKXD_1 = input_data.TKXD_after
    TNXD_0 = input_data.TNXD_before
    TNXD_1 = input_data.TNXD_after
    P_KPD_0 = input_data.KPD_pr
    Q_KPD_0 = input_data.KPD_q
    Q_KXD_0 = input_data.KXD_q
    P_NPD_0 = input_data.NPD_pr
    Q_NPD_0 = input_data.NPD_q
    Q_NXD_0 = input_data.NXD_q
    Q_KSW_0 = input_data.KSW_q
    Q_NSW_0 = input_data.NSW_q

    # Параметры

    Ω_KPD = 5.0
    Ω_NPD = 5.0
    σ_FCD = 2.0
    σ_KSW = 5.0
    σ_NSW = 5.0
    σ_FCW = 3.0
    ε_KPD = 0.3
    ε_NPD = 0.3
    ε_KXW = 0.7
    ε_NXW = 0.7
    ε_FCD = -0.15
    ε_FCW = -0.3

    SS_KPD_SUPPLY_0 = 0.0
    SS_KPD_SUPPLY_1 = 0.0
    SS_NPD_SUPPLY_0 = 0.0
    SS_NPD_SUPPLY_1 = 0.0
    SS_KXW_SUPPLY_0 = 0.0
    SS_NXW_SUPPLY_0 = 0.0
    DS_FCD_DEMAND_0 = 0.0
    DS_FCD_DEMAND_1 = 0.0
    DS_FCW_DEMAND_0 = 0.0

    DER_0 = 0.0
    DWPK_0 = 0.0
    DWPN_0 = 0.0
    B_KXD = 1.0
    B_KCD = 1.0
    B_NXD = 1.0
    B_KSW = 1.0
    K_KCD = 1.0
    K_NCD = 1.0

    """Переводим значения, введенные пользователем, в проценты"""
    TKXD_0 = TKXD_0 / 100
    TKXD_1 = TKXD_1 / 100
    TNXD_0 = TNXD_0 / 100
    TNXD_1 = TNXD_1 / 100

    """Перерасчет ячеек с новыми значениями"""

    DER_1 = ER_1 / ER_0 - 1

    WPK_0 =

    DWPK_1 = WPK_1/WPK_0-1

    SS_KXW_SUPPLY_1 = (1 + DWPK_1) ** -ε_KXW - 1

    DWPN_1 = WPN_1 / WPN_0 - 1

    SS_NXW_SUPPLY_1 = (1 + DWPN_1) ** -ε_NXW - 1

    DS_FCW_DEMAND_1 = (1 + (DWPK_1 * Q_KSW_0 + DWPN_1 * Q_NSW_0) / (Q_NSW_0 + Q_KSW_0)) ** -ε_FCW - 1

    P_KXD_0 = P_KXD_USD_0 * ER_0

    Q_KCD_0 = Q_KPD_0 - Q_KXD_0

    P_KCD_0 = (P_KPD_0 * Q_KPD_0 - P_KXD_0 * Q_KXD_0) / Q_KCD_0

    P_NXD_0 = P_NXD_USD_0 * ER_0

    Q_NCD_0 = Q_NPD_0 - Q_NXD_0

    P_NCD_0 = (P_NPD_0 * Q_NPD_0 - P_NXD_0 * Q_NXD_0) / Q_NCD_0

    Q_FCD_0 = Q_NCD_0 + Q_KCD_0

    P_FCD_0 = (P_KCD_0 * Q_KCD_0 + P_NCD_0 * Q_NCD_0) / Q_FCD_0

    Q_KXW_0 = Q_KSW_0 - Q_KXD_0

    P_KSW_0 = WPK_0 * ER_0

    P_KXW_0 = (P_KSW_0 * Q_KSW_0 - P_KXD_0 * (1 + TKXD_0) * Q_KXD_0) / Q_KXW_0

    Q_NXW_0 = Q_NSW_0 - Q_NXD_0

    P_NSW_0 = WPN_0 * ER_0

    P_NXW_0 = (P_NSW_0 * Q_NSW_0 - P_NXD_0 * (1 + TNXD_0) * Q_NXD_0) / Q_NXW_0

    Q_FCW_0 = Q_NSW_0 + Q_KSW_0

    P_FCW_0 = (P_NSW_0 * Q_NSW_0 + P_KSW_0 * Q_KSW_0) / Q_FCW_0

    r_Ω_KPD = (Ω_KPD + 1) / Ω_KPD

    K_KXD = ((Q_KXD_0 / Q_KCD_0) ** (1 - r_Ω_KPD)) * (P_KXD_0 / P_KCD_0) * K_KCD

    r_Ω_NPD = (Ω_NPD + 1) / Ω_NPD

    K_NXD = ((Q_NXD_0 / Q_NCD_0) ** (1 - r_Ω_NPD)) * (P_NXD_0 / P_NCD_0) * K_NCD

    r_σ_FCD = (σ_FCD - 1) / σ_FCD

    B_NCD = (Q_NCD_0 / Q_KCD_0) ** (1 - r_σ_FCD) * (P_NCD_0 / P_KCD_0) * B_KCD

    r_σ_KSW = (σ_KSW - 1) / σ_KSW

    B_KXW = ((Q_KXW_0 / Q_KXD_0) ** (1 - r_σ_KSW)) * (P_KXW_0 / (P_KXD_0 * (1 + TKXD_0))) * B_KXD

    r_σ_NSW = (σ_NSW - 1) / σ_NSW

    B_NXW = (Q_NXW_0 / Q_NXD_0) ** (1 - r_σ_NSW) * (P_NXW_0 / (P_NXD_0 * (1 + TNXD_0))) * B_NXD

    r_σ_FCW = (σ_FCW - 1) / σ_FCW

    B_NSW = ((Q_NSW_0 / Q_KSW_0) ** (1 - r_σ_FCW)) * (P_NSW_0 / P_KSW_0) * B_KSW

    Z_KPD = stepen(K_KCD * stepen(Q_KCD_0, r_Ω_KPD) + K_KXD * stepen(Q_KXD_0, r_Ω_KPD), (1 / r_Ω_KPD)) / \
            stepen(stepen(K_KCD * stepen(P_KCD_0 / K_KCD, (1 + Ω_KPD)) + K_KXD * stepen(P_KXD_0 / K_KXD, (1 + Ω_KPD)),
                          (1 / (1 + Ω_KPD))), ε_KPD)

    Z_NPD = stepen(K_NCD * stepen(Q_NCD_0, r_Ω_NPD) + K_NXD * stepen(Q_NXD_0, r_Ω_NPD), (1 / r_Ω_NPD)) / \
            stepen(stepen(K_NCD * stepen(P_NCD_0 / K_KCD, (1 + Ω_NPD)) + K_NXD * stepen(P_NXD_0 / K_NXD, (1 + Ω_NPD)),
                          (1 / (1 + Ω_NPD))), ε_NPD)

    Z_KXW = Q_KXW_0 / ((P_KXW_0 / ER_0) ** ε_KXW)

    Z_NXW = Q_NXW_0 / ((P_NXW_0 / ER_0) ** ε_NXW)

    Z_FCD = stepen(B_KCD * stepen(Q_KCD_0, r_σ_FCD) + B_NCD * stepen(Q_NCD_0, r_σ_FCD), (1 / r_σ_FCD)) / \
            stepen(stepen(B_KCD * stepen(P_KCD_0 / B_KCD, (1 - σ_FCD)) + B_NCD * stepen(P_NCD_0 / B_NCD, (1 - σ_FCD)),
                          (1 / (1 - σ_FCD))), ε_FCD)

    Z_FCW = ((B_KSW * Q_KSW_0 ** r_σ_FCW + B_NSW * Q_NSW_0 ** r_σ_FCW) ** (1 / r_σ_FCW)) / \
            ((((B_KSW * (P_KSW_0 / B_KSW) ** (1 - σ_FCW) + B_NSW * (P_NSW_0 / B_NSW) ** (1 - σ_FCW)) ** (
                    1 / (1 - σ_FCW))) / ER_0) ** ε_FCW)

    def func(z):

        P_KPD_1 = z[0]
        Q_KPD_1 = z[1]
        P_KXD_1 = z[2]
        Q_KXD_1 = z[3]
        P_KCD_1 = z[4]
        Q_KCD_1 = z[5]
        P_NPD_1 = z[6]
        Q_NPD_1 = z[7]
        P_NXD_1 = z[8]
        Q_NXD_1 = z[9]
        P_NCD_1 = z[10]
        Q_NCD_1 = z[11]
        P_FCD_1 = z[12]
        Q_FCD_1 = z[13]
        P_KXW_1 = z[14]
        Q_KXW_1 = z[15]
        P_KSW_1 = z[16]
        Q_KSW_1 = z[17]
        P_NXW_1 = z[18]
        Q_NXW_1 = z[19]
        P_NSW_1 = z[20]
        Q_NSW_1 = z[21]
        P_FCW_1 = z[22]
        Q_FCW_1 = z[23]

        KPD_SUPPLY = (K_KCD * np.abs(Q_KCD_1) ** r_Ω_KPD + K_KXD * np.abs(Q_KXD_1) ** r_Ω_KPD) ** (1 / r_Ω_KPD) / (
                Z_KPD * (1 + SS_KPD_SUPPLY_1) * ((K_KCD * (np.abs(P_KCD_1) / K_KCD) ** (1 + Ω_KPD) + K_KXD *
                                                  (np.abs(P_KXD_1) / K_KXD) ** (1 + Ω_KPD)) ** (
                                                             1 / (1 + Ω_KPD))) ** ε_KPD) - 1
        # print("{:20}".format('KPD_SUPPLY ='), "{:>32f}".format(KPD_SUPPLY))

        KPD_BUD_CET = np.abs(P_KPD_1) * np.abs(Q_KPD_1) / (
                np.abs(P_KXD_1) * np.abs(Q_KXD_1) + np.abs(P_KCD_1) * np.abs(Q_KCD_1)) - 1
        # print("{:20}".format('KPD_BUD_CET ='), "{:>32f}".format(KPD_BUD_CET))

        KPD_CET = (np.abs(Q_KXD_1) / np.abs(Q_KCD_1)) / ((np.abs(P_KXD_1) / np.abs(P_KCD_1)) * (K_KCD / K_KXD)) ** (
                1 / (r_Ω_KPD - 1)) - 1
        # print("{:20}".format('KPD_CET ='), "{:>32f}".format(KPD_CET))

        KPD_BAL_CET = np.abs(Q_KPD_1) / (np.abs(Q_KCD_1) + np.abs(Q_KXD_1)) - 1
        # print("{:20}".format('KPD_BAL_CET ='), "{:>32f}".format(KPD_BAL_CET))

        NPD_SUPPLY = (K_NCD * np.abs(Q_NCD_1) ** r_Ω_NPD + K_NXD * np.abs(Q_NXD_1) ** r_Ω_NPD) ** (1 / r_Ω_NPD) / (
                Z_NPD * (1 + SS_NPD_SUPPLY_1) * ((K_NCD * (np.abs(P_NCD_1) / K_KCD) ** (1 + Ω_NPD) + K_NXD *
                                                  (np.abs(P_NXD_1) / K_NXD) ** (1 + Ω_NPD)) ** (
                                                             1 / (1 + Ω_NPD))) ** ε_NPD) - 1
        # print("{:20}".format('NPD_SUPPLY ='), "{:>32f}".format(NPD_SUPPLY))

        NPD_BUD_CET = np.abs(P_NPD_1) * np.abs(Q_NPD_1) / (
                np.abs(P_NXD_1) * np.abs(Q_NXD_1) + np.abs(P_NCD_1) * np.abs(Q_NCD_1)) - 1
        # print("{:20}".format('NPD_BUD_CET ='), "{:>32f}".format(NPD_BUD_CET))

        NPD_CET = (np.abs(Q_NXD_1) / np.abs(Q_NCD_1)) / ((np.abs(P_NXD_1) / (np.abs(P_NCD_1))) * (K_NCD / K_NXD)) ** (
                1 / (r_Ω_NPD - 1)) - 1
        # print("{:20}".format('NPD_CET ='), "{:>32f}".format(NPD_CET))

        NPD_BAL_CET = np.abs(Q_NPD_1) / (np.abs(Q_NCD_1) + np.abs(Q_NXD_1)) - 1
        # print("{:20}".format('NPD_BAL_CET ='), "{:>32f}".format(NPD_BAL_CET))

        FCD_BUD_CES = np.abs(P_FCD_1) * np.abs(Q_FCD_1) / (
                np.abs(P_KCD_1) * np.abs(Q_KCD_1) + np.abs(P_NCD_1) * np.abs(Q_NCD_1)) - 1
        # print("{:20}".format('FCD_BUD_CES ='), "{:>32f}".format(FCD_BUD_CES))

        FCD_CES = (np.abs(Q_KCD_1) / np.abs(Q_NCD_1)) / ((np.abs(P_KCD_1) / (np.abs(P_NCD_1))) * (B_NCD / B_KCD)) ** (
                1 / (r_σ_FCD - 1)) - 1
        # print("{:20}".format('FCD_CES ='), "{:>32f}".format(FCD_CES))

        FCD_BAL_CES = np.abs(Q_FCD_1) / (np.abs(Q_KCD_1) + np.abs(Q_NCD_1)) - 1
        # print("{:20}".format('FCD_BAL_CES ='), "{:>32f}".format(FCD_BAL_CES))

        FCD_DEMAND = (B_KCD * np.abs(Q_KCD_1) ** r_σ_FCD + B_NCD * np.abs(Q_NCD_1) ** r_σ_FCD) ** (1 / r_σ_FCD) / (
                Z_FCD * (1 + DS_FCD_DEMAND_1) * (((B_KCD * (np.abs(P_KCD_1) / B_KCD) ** (1 - σ_FCD) + B_NCD *
                                                   (np.abs(P_NCD_1) / B_NCD) ** (1 - σ_FCD)) ** (
                                                              1 / (1 - σ_FCD))) ** ε_FCD)) - 1
        # print("{:20}".format('FCD_DEMAND ='), "{:>32f}".format(FCD_DEMAND))

        KSW_BUD_CES = np.abs(P_KSW_1) * np.abs(Q_KSW_1) / (
                np.abs(P_KXD_1) * (1 + TKXD_1) * np.abs(Q_KXD_1) + np.abs(P_KXW_1) * np.abs(Q_KXW_1)) - 1
        # print("{:20}".format('KSW_BUD_CES ='), "{:>32f}".format(KSW_BUD_CES))

        KSW_CES = (np.abs(Q_KXW_1) / np.abs(Q_KXD_1)) / (
                (np.abs(P_KXW_1) / (np.abs(P_KXD_1) * (1 + TKXD_1))) * (B_KXD / B_KXW)) ** (1 / (r_σ_KSW - 1)) - 1
        # print("{:20}".format('KSW_CES ='), "{:>32f}".format(KSW_CES))

        KSW_BAL_CES = np.abs(Q_KSW_1) / (np.abs(Q_KXD_1) + np.abs(Q_KXW_1)) - 1
        # print("{:20}".format('KSW_BAL_CES ='), "{:>32f}".format(KSW_BAL_CES))

        KXW_SUPPLY = np.abs(Q_KXW_1) / (Z_KXW * (1 + SS_KXW_SUPPLY_1) * (np.abs(P_KXW_1) / ER_1) ** ε_KXW) - 1
        # print("{:20}".format('KXW_SUPPLY ='), "{:>32f}".format(KXW_SUPPLY))

        NSW_BUD_CES = np.abs(P_NSW_1) * np.abs(Q_NSW_1) / (
                np.abs(P_NXD_1) * (1 + TNXD_1) * np.abs(Q_NXD_1) + np.abs(P_NXW_1) * np.abs(Q_NXW_1)) - 1
        # print("{:20}".format('NSW_BUD_CES ='), "{:>32f}".format(NSW_BUD_CES))

        NSW_CES = (np.abs(Q_NXW_1) / np.abs(Q_NXD_1)) / (
                ((np.abs(P_NXW_1)) / (np.abs(P_NXD_1) * (1 + TNXD_1))) * (B_NXD / B_NXW)) ** (1 / (r_σ_NSW - 1)) - 1
        # print("{:20}".format('NSW_CES ='), "{:>32f}".format(NSW_CES))

        NSW_BAL_CES = np.abs(Q_NSW_1) / (np.abs(Q_NXD_1) + np.abs(Q_NXW_1)) - 1
        # print("{:20}".format('NSW_BAL_CES ='), "{:>32f}".format(NSW_BAL_CES))

        NXW_SUPPLY = np.abs(Q_NXW_1) / (Z_NXW * (1 + SS_NXW_SUPPLY_1) * (np.abs(P_NXW_1) / ER_1) ** ε_NXW) - 1
        # print("{:20}".format('NXW_SUPPLY ='), "{:>32f}".format(NXW_SUPPLY))

        FCW_BUD_CES = np.abs(P_FCW_1) * np.abs(Q_FCW_1) / (
                np.abs(P_KSW_1) * np.abs(Q_KSW_1) + np.abs(P_NSW_1) * np.abs(Q_NSW_1)) - 1
        # print("{:20}".format('FCW_BUD_CES ='), "{:>32f}".format(FCW_BUD_CES))

        FCW_CES = (np.abs(Q_KSW_1) / np.abs(Q_NSW_1)) / ((np.abs(P_KSW_1) / (np.abs(P_NSW_1))) * (B_NSW / B_KSW)) ** (
                1 / (r_σ_FCW - 1)) - 1
        # print("{:20}".format('FCW_CES ='), "{:>32f}".format(FCW_CES))

        FCW_BAL_CES = np.abs(Q_FCW_1) / (np.abs(Q_NSW_1) + np.abs(Q_KSW_1)) - 1
        # print("{:20}".format('FCW_BAL_CES ='), "{:>32f}".format(FCW_BAL_CES))

        FCW_DEMAND = ((B_KSW * np.abs(Q_KSW_1) ** r_σ_FCW + B_NSW * np.abs(Q_NSW_1) ** r_σ_FCW) ** (1 / r_σ_FCW)) / (
                Z_FCW * (1 + DS_FCW_DEMAND_1) * ((B_KSW * (np.abs(P_KSW_1) / B_KSW) ** (1 - σ_FCW) + B_NSW *
                                                  (P_NSW_1 / B_NSW) ** (1 - σ_FCW)) ** (
                                                             1 / (1 - σ_FCW)) / ER_1) ** ε_FCW) - 1
        # print("{:20}".format('FCW_DEMAND ='), "{:>32f}".format(FCW_DEMAND))

        return [KPD_SUPPLY, KPD_BUD_CET, KPD_CET, KPD_BAL_CET, NPD_SUPPLY, NPD_BUD_CET, NPD_CET, NPD_BAL_CET,
                FCD_BUD_CES, FCD_CES, FCD_BAL_CES, FCD_DEMAND, KSW_BUD_CES, KSW_CES, KSW_BAL_CES, KXW_SUPPLY,
                NSW_BUD_CES, NSW_CES, NSW_BAL_CES, NXW_SUPPLY, FCW_BUD_CES, FCW_CES, FCW_BAL_CES, FCW_DEMAND]

    P_KPD_1 = P_KPD_0
    Q_KPD_1 = Q_KPD_0
    P_KXD_1 = P_KXD_0
    Q_KXD_1 = Q_KXD_0
    P_KCD_1 = P_KCD_0
    Q_KCD_1 = Q_KCD_0
    P_NPD_1 = P_NPD_0
    Q_NPD_1 = Q_NPD_0
    P_NXD_1 = P_NXD_0
    Q_NXD_1 = Q_NXD_0
    P_NCD_1 = P_NCD_0
    Q_NCD_1 = Q_NCD_0
    P_FCD_1 = P_FCD_0
    Q_FCD_1 = Q_FCD_0
    P_KXW_1 = P_KXW_0
    Q_KXW_1 = Q_KXW_0
    P_KSW_1 = P_KSW_0
    Q_KSW_1 = Q_KSW_0
    P_NXW_1 = P_NXW_0
    Q_NXW_1 = Q_NXW_0
    P_NSW_1 = P_NSW_0
    Q_NSW_1 = Q_NSW_0
    P_FCW_1 = P_FCW_0
    Q_FCW_1 = Q_FCW_0

    solved_value: list = []
    max_eq = 0.1

    z0 = [P_KPD_1, Q_KPD_1, P_KXD_1, Q_KXD_1, P_KCD_1, Q_KCD_1, P_NPD_1, Q_NPD_1, P_NXD_1, Q_NXD_1, P_NCD_1,
          Q_NCD_1, P_FCD_1, Q_FCD_1, P_KXW_1, Q_KXW_1, P_KSW_1, Q_KSW_1, P_NXW_1, Q_NXW_1, P_NSW_1, Q_NSW_1,
          P_FCW_1, Q_FCW_1]

    solved = root(func, z0, method='lm')
    solved_value = solved.x
    accuracy = solved.fun

    P_KPD_1 = np.abs(solved_value[0])
    Q_KPD_1 = np.abs(solved_value[1])
    P_KXD_1 = np.abs(solved_value[2])
    Q_KXD_1 = np.abs(solved_value[3])
    P_KCD_1 = np.abs(solved_value[4])
    Q_KCD_1 = np.abs(solved_value[5])
    P_NPD_1 = np.abs(solved_value[6])
    Q_NPD_1 = np.abs(solved_value[7])
    P_NXD_1 = np.abs(solved_value[8])
    Q_NXD_1 = np.abs(solved_value[9])
    P_NCD_1 = np.abs(solved_value[10])
    Q_NCD_1 = np.abs(solved_value[11])
    P_FCD_1 = np.abs(solved_value[12])
    Q_FCD_1 = np.abs(solved_value[13])
    P_KSW_1 = np.abs(solved_value[14])
    Q_KSW_1 = np.abs(solved_value[15])
    P_KXW_1 = np.abs(solved_value[16])
    Q_KXW_1 = np.abs(solved_value[17])
    P_NSW_1 = np.abs(solved_value[18])
    Q_NSW_1 = np.abs(solved_value[19])
    P_NXW_1 = np.abs(solved_value[20])
    Q_NXW_1 = np.abs(solved_value[21])
    P_FCW_1 = np.abs(solved_value[22])
    Q_FCW_1 = np.abs(solved_value[23])

    eqs = []
    for item in accuracy:
        eqs.append(item)

    qrt_eq = []
    for item in eqs:
        qrt_eq.append(item ** 2)
    eq_result = sqrt(fsum(qrt_eq))

    if eq_result <= max_eq:
        solution = True
    else:
        solution = False

    if P_KPD_0 == P_KPD_1:
        solution = False

    solution = solution

    if solution == False:
        P_KPD_1 = 49722.0
        Q_KPD_1 = 9327769.0
        P_KXD_1 = 57373.350000000006
        Q_KXD_1 = 7220000.0
        P_KCD_1 = 23512.891221950762
        Q_KCD_1 = 2107769.0
        P_NPD_1 = 92549.0
        Q_NPD_1 = 10874475.0
        P_NXD_1 = 126457.05
        Q_NXD_1 = 6150000
        P_NCD_1 = 48409.80834378423
        Q_NCD_1 = 4724475.0
        P_FCD_1 = 40729.03024145507
        Q_FCD_1 = 6832244.0
        P_KXW_1 = 77666.2505204719
        Q_KXW_1 = 27379000.0
        P_KSW_1 = 73431.59802306426
        Q_KSW_1 = 34599000.0
        P_NXW_1 = 117558.5086131607
        Q_NXW_1 = 33205000.0
        P_NSW_1 = 118949.0823529412
        Q_NSW_1 = 39355000.0
        P_FCW_1 = 97653.96051599646
        Q_FCW_1 = 73954000

    P_KXD_USD_1 = P_KXD_1 / ER_1

    P_NXD_USD_1 = P_NXD_1 / ER_1

    I26 = P_KPD_1 / P_KPD_0 - 1

    J26 = Q_KPD_1 / Q_KPD_0 - 1

    I27 = P_KXD_1 / P_KXD_0 - 1

    J27 = Q_KXD_1 / Q_KXD_0 - 1

    I28 = P_KCD_1 / P_KCD_0 - 1

    J28 = Q_KCD_1 / Q_KCD_0 - 1

    I29 = P_NPD_1 / P_NPD_0 - 1

    J29 = Q_NPD_1 / Q_NPD_0 - 1

    I30 = P_NXD_1 / P_NXD_0 - 1

    J30 = Q_NXD_1 / Q_NXD_0 - 1

    I31 = P_NCD_1 / P_NCD_0 - 1

    J31 = Q_NCD_1 / Q_NCD_0 - 1

    I32 = P_FCD_1 / P_FCD_0 - 1

    J32 = Q_FCD_1 / Q_FCD_0 - 1

    I33 = P_KXW_1 / P_KXW_0 - 1

    J33 = Q_KXW_1 / Q_KXW_0 - 1

    I34 = P_KSW_1 / P_KSW_0 - 1

    J34 = Q_KSW_1 / Q_KSW_0 - 1

    I35 = P_NXW_1 / P_NXW_0 - 1

    J35 = Q_NXW_1 / Q_NXW_0 - 1

    I36 = P_NSW_1 / P_NSW_0 - 1

    J36 = Q_NSW_1 / Q_NSW_0 - 1

    I37 = P_FCW_1 / P_FCW_0 - 1

    J37 = Q_FCW_1 / Q_FCW_0 - 1

    result_to_front = {
        'table1': [
            {
                'id': '1',
                'title': 'Курс RUB/USD',
                'params': 'ER',
                'basebalance': round(ER_0, 2),
                'newbalance': round(ER_1, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '2',
                'title': 'Изменение курса RUB/USD, %',
                'params': 'DER',
                'basebalance': round(DER_0 * 100, 2),
                'newbalance': round(DER_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': 'Мировая цена калийных удобрений, USD за тонну',
                'params': 'WPK',
                'basebalance': round(WPK_0),
                'newbalance': round(WPK_1),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '4',
                'title': 'Изменение мировой цены калийных удобрений, USD за тонну, %',
                'params': 'DWPK',
                'basebalance': round(DWPK_0 * 100, 2),
                'newbalance': round(DWPK_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': 'Мировая цена азотных удобрений, USD за тонну',
                'params': 'WPN',
                'basebalance': round(WPN_0),
                'newbalance': round(WPN_1),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '6',
                'title': 'Изменение мировой цены азотных удобрений, USD за тонну, %',
                'params': 'DWPN',
                'basebalance': round(DWPN_0 * 100),
                'newbalance': round(DWPN_1 * 100),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '7',
                'title': 'Цена экспорта калийных удобрений (без тарифа), USD за тонну',
                'params': 'P_KXD_USD',
                'basebalance': round(P_KXD_USD_0),
                'newbalance': round(P_KXD_USD_1),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Цена экспорта азотных удобрений (без тарифа), USD за тонну',
                'params': 'P_NXD_USD',
                'basebalance': round(P_NXD_USD_0, 2),
                'newbalance': round(P_NXD_USD_1, 2),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '9',
                'title': 'Экспортный тариф на калийные удобрения, %',
                'params': 'TKXD',
                'basebalance': round(TKXD_0 * 100, 2),
                'newbalance': round(TKXD_1 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '10',
                'title': 'Экспортный тариф на азотные удобрения, %',
                'params': 'TNXD',
                'basebalance': round(TNXD_0 * 100, 2),
                'newbalance': round(TNXD_1 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '11',
                'title': 'Шок предложения на внутреннем рынке калийных удобрений, %',
                'params': 'SS_KPD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_KPD_SUPPLY_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': 'Шок предложения на внутреннем рынке азотных удобрений, %',
                'params': 'SS_NPD_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_NPD_SUPPLY_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '13',
                'title': 'Шок предложения на мировом рынке калийных удобрений, %',
                'params': 'SS_KXW_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_KXW_SUPPLY_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '14',
                'title': 'Шок предложения на мировом рынке азотных удобрений, %',
                'params': 'SS_NXW_SUPPLY',
                'basebalance': 0,
                'newbalance': round(SS_NXW_SUPPLY_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '15',
                'title': 'Шок спроса на удобрения на внутреннем рынке, %',
                'params': 'DS_FCD_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_FCD_DEMAND_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '16',
                'title': 'Шок спроса на удобрения на мировом рынке, %',
                'params': 'DS_FCW_DEMAND',
                'basebalance': 0,
                'newbalance': round(DS_FCW_DEMAND_1 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            }
        ],
        'finding_solution': solution,
        'table2': [
            {
                'id': '1',
                'title': 'Российское производство калийных удобрений',
                'params': 'KPD',
                'basebalance_pr': round(P_KPD_0, 2),
                'basebalance_quan': round(Q_KPD_0, 2),
                'newbalance_pr': round(P_KPD_1, 2),
                'newbalance_quan': round(Q_KPD_1, 2),
                'perc_change_price': round(I26 * 100, 2),
                'perc_change_quantity': round(J26 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '2',
                'title': 'Российский экспорт калийных удобрений',
                'params': 'KXD',
                'basebalance_pr': round(P_KXD_0, 2),
                'basebalance_quan': round(Q_KXD_0, 2),
                'newbalance_pr': round(P_KXD_1, 2),
                'newbalance_quan': round(Q_KXD_1, 2),
                'perc_change_price': round(I27 * 100, 2),
                'perc_change_quantity': round(J27 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '3',
                'title': 'Внутреннее потребление калийных удобрений',
                'params': 'KCD',
                'basebalance_pr': round(P_KCD_0, 2),
                'basebalance_quan': round(Q_KCD_0, 2),
                'newbalance_pr': round(P_KCD_1, 2),
                'newbalance_quan': round(Q_KCD_1, 2),
                'perc_change_price': round(I28 * 100, 2),
                'perc_change_quantity': round(J28 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '4',
                'title': 'Российское производство азотных удобрений',
                'params': 'NPD',
                'basebalance_pr': round(P_NPD_0, 2),
                'basebalance_quan': round(Q_NPD_0, 2),
                'newbalance_pr': round(P_NPD_1, 2),
                'newbalance_quan': round(Q_NPD_1, 2),
                'perc_change_price': round(I29 * 100, 2),
                'perc_change_quantity': round(J29 * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '5',
                'title': 'Российский экспорт азотных удобрений',
                'params': 'NXD',
                'basebalance_pr': round(P_NXD_0, 2),
                'basebalance_quan': round(Q_NXD_0, 2),
                'newbalance_pr': round(P_NXD_1, 2),
                'newbalance_quan': round(Q_NXD_1, 2),
                'perc_change_price': round(I30 * 100, 2),
                'perc_change_quantity': round(J30 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '6',
                'title': 'Внутреннее потребление азотных удобрений',
                'params': 'NCD',
                'basebalance_pr': round(P_NCD_0, 2),
                'basebalance_quan': round(Q_NCD_0, 2),
                'newbalance_pr': round(P_NCD_1, 2),
                'newbalance_quan': round(Q_NCD_1, 2),
                'perc_change_price': round(I31 * 100, 2),
                'perc_change_quantity': round(J31 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '7',
                'title': 'Российское совокупное потребление двух типов удобрений',
                'params': 'FCD',
                'basebalance_pr': round(P_FCD_0, 2),
                'basebalance_quan': round(Q_FCD_0, 2),
                'newbalance_pr': round(P_FCD_1, 2),
                'newbalance_quan': round(Q_FCD_1, 2),
                'perc_change_price': round(I32 * 100, 2),
                'perc_change_quantity': round(J32 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Мировой экспорт калийных удобрений',
                'params': 'KXW',
                'basebalance_pr': round(P_KXW_0, 2),
                'basebalance_quan': round(Q_KXW_0, 2),
                'newbalance_pr': round(P_KXW_1, 2),
                'newbalance_quan': round(Q_KXW_1, 2),
                'perc_change_price': round(I33 * 100, 2),
                'perc_change_quantity': round(J33 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '9',
                'title': 'Мировое потребление калийных удобрений ',
                'params': 'KSW',
                'basebalance_pr': round(P_KSW_0, 2),
                'basebalance_quan': round(Q_KSW_0, 2),
                'newbalance_pr': round(P_KSW_1, 2),
                'newbalance_quan': round(Q_KSW_1, 2),
                'perc_change_price': round(I34 * 100, 2),
                'perc_change_quantity': round(J34 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '10',
                'title': 'Мировой экспорт азотных удобрений',
                'params': 'NXW',
                'basebalance_pr': round(P_NXW_0, 2),
                'basebalance_quan': round(Q_NXW_0, 2),
                'newbalance_pr': round(P_NXW_1, 2),
                'newbalance_quan': round(Q_NXW_1, 2),
                'perc_change_price': round(I35 * 100, 2),
                'perc_change_quantity': round(J35 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '11',
                'title': 'Мировое потребление азотных удобрений',
                'params': 'NSW',
                'basebalance_pr': round(P_NSW_0, 2),
                'basebalance_quan': round(Q_NSW_0, 2),
                'newbalance_pr': round(P_NSW_1, 2),
                'newbalance_quan': round(Q_NSW_1, 2),
                'perc_change_price': round(I36 * 100, 2),
                'perc_change_quantity': round(J36 * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': 'Мировое потребление двух типов удобрений ',
                'params': 'FCW',
                'basebalance_pr': round(P_FCW_0, 2),
                'basebalance_quan': round(Q_FCW_0, 2),
                'newbalance_pr': round(P_FCW_1, 2),
                'newbalance_quan': round(Q_FCW_1, 2),
                'perc_change_price': round(I37 * 100, 2),
                'perc_change_quantity': round(J37 * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            }
        ],
        'table3': [
            {
                'id': '1',
                'name': 'Эластичность трансформации калийных удобрений',
                'params': 'Ω_KPD',
                'value': round(Ω_KPD, 1),
                "edit": 'true'
            },
            {
                'id': '2',
                'name': 'Эластичность трансформации азотных удобрений',
                'params': 'Ω_NPD',
                'value': round(Ω_NPD, 1),
                "edit": 'true'
            },
            {
                'id': '3',
                'name': 'Эластичность замещение двух типов удобрений на внутреннем рынке',
                'params': 'σ_FCD',
                'value': round(σ_FCD, 1),
                "edit": 'true'
            },
            {
                'id': '4',
                'name': 'Эластичность Армингтона для калийных удобрений на мировом рынке',
                'params': 'σ_KSW',
                'value': round(σ_KSW, 1),
                "edit": 'true'
            },
            {
                'id': '5',
                'name': 'Эластичность Армингтона для азотных удобрений на мировом рынке',
                'params': 'σ_NSW',
                'value': round(σ_NSW, 1),
                "edit": 'true'
            },
            {
                'id': '6',
                'name': 'Эластичность замещение двух типов удобрений на внешнем рынке',
                'params': 'σ_FCW',
                'value': round(σ_FCW, 1),
                "edit": 'true'
            }
        ],
        'table4': [
            {
                'id': '1',
                'name': 'Эластичность предложения калийных удобрений отечественными производителями',
                'params': 'ε_KPD',
                'value': round(ε_KPD, 1),
                "edit": 'true'
            },
            {
                'id': '2',
                'name': 'Эластичность предложения азотных удобрений отечественными производителями',
                'params': 'ε_NPD',
                'value': round(ε_NPD, 1),
                "edit": 'true'
            },
            {
                'id': '3',
                'name': 'Эластичность предложения (мирового экспорта) калийных удобрений мировыми производителями',
                'params': 'ε_KXW',
                'value': round(ε_KXW, 1),
                "edit": 'true'
            },
            {
                'id': '4',
                'name': 'Эластичность предложения (мирового экспорта) азотных удобрений мировыми производителями',
                'params': 'ε_NXW',
                'value': round(ε_NXW, 1),
                "edit": 'true'
            },
            {
                'id': '5',
                'name': 'Эластичность спроса на удобрения в России',
                'params': 'ε_FCD',
                'value': round(ε_FCD, 1),
                "edit": 'true'
            },
            {
                'id': '6',
                'name': 'Эластичность спроса (импорта) на удобрения в мире',
                'params': 'ε_FCW',
                'value': round(ε_FCW, 1),
                "edit": 'true'
            }
        ]
    }

    return result_to_front