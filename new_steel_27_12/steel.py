import math
import numpy as np
from decimal import *
from scipy.optimize import fsolve
from math import fsum, sqrt
import os

example_data = {'ER_before': 73.94,
                # 'ER_after': 73.94,
                'WP_before': 689.0,
                'WP_after': 1500.0,
                'P_AXD_USD_before': 721.0,
                'P_AMD_USD_before': 1150.0,
                'P_IXD_USD_before': 150.0,
                'TAXD_before': 0.0,
                'TAXD_after': 95.0,
                'TIXD_before': 0.0,
                'TIXD_after': 80.0,
                'TAMD_before': 0.0,
                'TAMD_after': 90.0,
                # 'SS_IPD_SUPPLY_after': 0.0,
                # 'DS_IXD_DEMAND_after': 0.0,
                # 'SS_AVD_SUPPLY_after': 0.0,
                # 'DS_ADW_DEMAND_after': 0.0,
                # 'SS_AXW_SUPPLY_after': 0.0,
                # 'SS_AMD_SUPPLY_after': 0.0,
                # 'DS_ADD_DEMAND_after': 0.0,
                # 'DS_BDD_DEMAND_after': 0.0,
                # 'SS_BVD_SUPPLY_after': 0.0,
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
        # self.ER_after = dict_from_frontend.get('ER_after')
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
        # self.SS_IPD_SUPPLY_after = dict_from_frontend.get('SS_IPD_SUPPLY_after')
        # self.DS_IXD_DEMAND_after = dict_from_frontend.get('DS_IXD_DEMAND_after')
        # self.SS_AVD_SUPPLY_after = dict_from_frontend.get('SS_AVD_SUPPLY_after')
        # self.DS_ADW_DEMAND_after = dict_from_frontend.get('DS_ADW_DEMAND_after')
        # self.SS_AXW_SUPPLY_after = dict_from_frontend.get('SS_AXW_SUPPLY_after')
        # self.SS_AMD_SUPPLY_after = dict_from_frontend.get('SS_AMD_SUPPLY_after')
        # self.DS_ADD_DEMAND_after = dict_from_frontend.get('DS_ADD_DEMAND_after')
        # self.DS_BDD_DEMAND_after = dict_from_frontend.get('DS_BDD_DEMAND_after')
        # self.SS_BVD_SUPPLY_after = dict_from_frontend.get('SS_BVD_SUPPLY_after')
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
    # ER_1 = input_data.ER_after
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
    # SS_IPD_SUPPLY_1 = input_data.SS_IPD_SUPPLY_after
    # DS_IXD_DEMAND_1 = input_data.DS_IXD_DEMAND_after
    # SS_AVD_SUPPLY_1 = input_data.SS_AVD_SUPPLY_after
    # DS_ADW_DEMAND_1 = input_data.DS_ADW_DEMAND_after
    # SS_AXW_SUPPLY_1 = input_data.SS_AXW_SUPPLY_after
    # SS_AMD_SUPPLY_1 = input_data.SS_AMD_SUPPLY_after
    # DS_ADD_DEMAND_1 = input_data.DS_ADD_DEMAND_after
    # DS_BDD_DEMAND_1 = input_data.DS_BDD_DEMAND_after
    # SS_BVD_SUPPLY_1 = input_data.SS_BVD_SUPPLY_after
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
    Q_AVD_0 = 100.0

    """Перерасчет ячеек с новыми значениями"""

    ER_1 = ER_0 * 3

    DER_1 = ER_1 / ER_0 - 1

    DWP_CEL_1 = WP_1 / WP_0 - 1

    DS_ADW_DEMAND_1 = (1+DWP_CEL_1)**-ε_ADW-1

    SS_AXW_SUPPLY_1 = (1+DWP_CEL_1)**-ε_AXW-1

    SS_AMD_SUPPLY_1 =(1+DWP_CEL_1)**-ε_AMD-1
    print(DER_1)

input_data = InputDataBase(example_data)
result = steel_market(input_data)
print(result)