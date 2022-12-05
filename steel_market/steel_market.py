import math
import numpy as np
from scipy.optimize import fsolve
from math import fsum, sqrt
import pandas as pd
import os

example_data = {'ER_before': 73.94,
                'ER_after': 73.94,
                'WP_before': 689.0,
                'WP_after': 689.0,
                'P_AXD_USD_before': 721.0,
                'P_AMD_USD_before': 1150.0,
                'P_IXD_USD_before': 150.0,
                'TAXD_before': 0.0,
                'TAXD_after': 0.15,
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
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.WP_before = float(dict_from_frontend.get('WP_before'))
        self.WP_after = float(dict_from_frontend.get('WP_after'))
        self.P_AXD_USD_before = float(dict_from_frontend.get('P_AXD_USD_before'))
        self.P_AMD_USD_before = float(dict_from_frontend.get('P_AMD_USD_before'))
        self.P_IXD_USD_before = float(dict_from_frontend.get('P_IXD_USD_before'))
        self.TAXD_before = float(dict_from_frontend.get('TAXD_before'))
        self.TAXD_after = float(dict_from_frontend.get('TAXD_after'))
        self.TIXD_before = float(dict_from_frontend.get('TIXD_before'))
        self.TIXD_after = float(dict_from_frontend.get('TIXD_after'))
        self.TAMD_before = float(dict_from_frontend.get('TAMD_before'))
        self.TAMD_after = float(dict_from_frontend.get('TAMD_after'))
        self.SS_IPD_SUPPLY_after = float(dict_from_frontend.get('SS_IPD_SUPPLY_after'))
        self.DS_IXD_DEMAND_after = float(dict_from_frontend.get('DS_IXD_DEMAND_after'))
        self.SS_AVD_SUPPLY_after = float(dict_from_frontend.get('SS_AVD_SUPPLY_after'))
        self.DS_ADW_DEMAND_after = float(dict_from_frontend.get('DS_ADW_DEMAND_after'))
        self.SS_AXW_SUPPLY_after = float(dict_from_frontend.get('SS_AXW_SUPPLY_after'))
        self.SS_AMD_SUPPLY_after = float(dict_from_frontend.get('SS_AMD_SUPPLY_after'))
        self.DS_ADD_DEMAND_after = float(dict_from_frontend.get('DS_ADD_DEMAND_after'))
        self.DS_BDD_DEMAND_after = float(dict_from_frontend.get('DS_BDD_DEMAND_after'))
        self.SS_BVD_SUPPLY_after = float(dict_from_frontend.get('SS_BVD_SUPPLY_after'))
        self.IPD_pr = float(dict_from_frontend.get('IPD_pr'))
        self.IPD_q = float(dict_from_frontend.get('IPD_q'))
        self.IXD_q = float(dict_from_frontend.get('IXD_q'))
        self.APD_pr = float(dict_from_frontend.get('APD_pr'))
        self.APD_q = float(dict_from_frontend.get('APD_q'))
        self.AXD_q = float(dict_from_frontend.get('AXD_q'))
        self.ADW_q = float(dict_from_frontend.get('ADW_q'))
        self.AMD_q = float(dict_from_frontend.get('AMD_q'))
        self.Ω_IPD = float(dict_from_frontend.get('Ω_IPD'))
        self.σ_APD = float(dict_from_frontend.get('σ_APD'))
        self.Ω_APD = float(dict_from_frontend.get('Ω_APD'))
        self.σ_ADW = float(dict_from_frontend.get('σ_ADW'))
        self.σ_ATD = float(dict_from_frontend.get('σ_ATD'))
        self.Ω_ATD = float(dict_from_frontend.get('Ω_ATD'))
        self.σ_BDD = float(dict_from_frontend.get('σ_BDD'))
        self.ε_IPD = float(dict_from_frontend.get('ε_IPD'))
        self.ε_IXD = float(dict_from_frontend.get('ε_IXD'))
        self.ε_AVD = float(dict_from_frontend.get('ε_AVD'))
        self.ε_ADW = float(dict_from_frontend.get('ε_ADW'))
        self.ε_AXW = float(dict_from_frontend.get('ε_AXW'))
        self.ε_AMD = float(dict_from_frontend.get('ε_AMD'))
        self.ε_ADD = float(dict_from_frontend.get('ε_ADD'))
        self.ε_BDD = float(dict_from_frontend.get('ε_BDD'))
        self.ε_BVD = float(dict_from_frontend.get('ε_BVD'))


def steel_market(input_data):
    """Получаем данные из модели"""

    mydir = '/Users/natalazivlova/Desktop/parser/steel_market/'
    myfile = 'PE_сталь_основной.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:J')

    # Управляющие воздействия модели
    model_control_actions = df.iloc[1:21, 0:4]
    model_control_actions = model_control_actions.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'designation',
                 'Unnamed: 2': 'before', 'Unnamed: 3': 'after'})
    print(model_control_actions.to_markdown())

    # Переменные
    variables = df.iloc[25:41, 0:9]
    variables = variables.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'designation',
                 'Unnamed: 2': 'base_pr',
                 'Unnamed: 3': 'base_quan', 'Unnamed: 4': 'relative_quality', 'Unnamed: 5': 'new_pr',
                 'Unnamed: 6': 'new_quan', 'Параметры': 'perc_change_price', 'Unnamed: 8': 'perc_change_quantity'})
    print(variables.to_markdown())

    # Уравнения
    equations = df.iloc[42:74, 0:2]
    equations = equations.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'values'})
    # print(equations.to_markdown())

    # Параметры
    parameters = df.iloc[0:17, 7:10]
    parameters = parameters.rename(
        columns={'Параметры': 'designation', 'Unnamed: 8': 'values'})
    print(parameters.to_markdown())

    """Вводим новые значения"""

    model_control_actions.at[1, 'before'] = input_data.ER_before
    model_control_actions.at[1, 'after'] = input_data.ER_after
    model_control_actions.at[3, 'before'] = input_data.WP_before
    model_control_actions.at[3, 'after'] = input_data.WP_after
    model_control_actions.at[5, 'before'] = input_data.P_AXD_USD_before
    model_control_actions.at[6, 'before'] = input_data.P_AMD_USD_before
    model_control_actions.at[7, 'before'] = input_data.P_IXD_USD_before
    model_control_actions.at[8, 'before'] = input_data.TAXD_before
    model_control_actions.at[8, 'after'] = input_data.TAXD_after
    model_control_actions.at[9, 'before'] = input_data.TIXD_before
    model_control_actions.at[9, 'after'] = input_data.TIXD_after
    model_control_actions.at[10, 'before'] = input_data.TAMD_before
    model_control_actions.at[10, 'after'] = input_data.TAMD_after
    model_control_actions.at[12, 'after'] = input_data.SS_IPD_SUPPLY_after
    model_control_actions.at[13, 'after'] = input_data.DS_IXD_DEMAND_after
    model_control_actions.at[14, 'after'] = input_data.SS_AVD_SUPPLY_after
    model_control_actions.at[15, 'after'] = input_data.DS_ADW_DEMAND_after
    model_control_actions.at[16, 'after'] = input_data.SS_AXW_SUPPLY_after
    model_control_actions.at[17, 'after'] = input_data.SS_AMD_SUPPLY_after
    model_control_actions.at[18, 'after'] = input_data.DS_ADD_DEMAND_after
    model_control_actions.at[19, 'after'] = input_data.DS_BDD_DEMAND_after
    model_control_actions.at[20, 'after'] = input_data.SS_BVD_SUPPLY_after

    variables.at[25, 'base_pr'] = input_data.IPD_pr
    variables.at[25, 'base_quan'] = input_data.IPD_q
    variables.at[26, 'base_quan'] = input_data.IXD_q
    variables.at[29, 'base_pr'] = input_data.APD_pr
    variables.at[29, 'base_quan'] = input_data.APD_q
    variables.at[30, 'base_quan'] = input_data.AXD_q
    variables.at[32, 'base_quan'] = input_data.ADW_q
    variables.at[35, 'base_quan'] = input_data.AMD_q

    parameters.at[0, 'values'] = input_data.Ω_IPD
    parameters.at[1, 'values'] = input_data.σ_APD
    parameters.at[2, 'values'] = input_data.Ω_APD
    parameters.at[3, 'values'] = input_data.σ_ADW
    parameters.at[4, 'values'] = input_data.σ_ATD
    parameters.at[5, 'values'] = input_data.Ω_ATD
    parameters.at[6, 'values'] = input_data.σ_BDD
    parameters.at[8, 'values'] = input_data.ε_IPD
    parameters.at[9, 'values'] = input_data.ε_IXD
    parameters.at[10, 'values'] = input_data.ε_AVD
    parameters.at[11, 'values'] = input_data.ε_ADW
    parameters.at[12, 'values'] = input_data.ε_AXW
    parameters.at[13, 'values'] = input_data.ε_AMD
    parameters.at[14, 'values'] = input_data.ε_ADD
    parameters.at[15, 'values'] = input_data.ε_BDD
    parameters.at[16, 'values'] = input_data.ε_BVD

    """Перерасчет ячеек с новыми значениями"""

    # DER_1
    def func_DER_1(df, D3, C3):
        return D3/C3-1

    model_control_actions.at[2, 'after'] = model_control_actions['after'].pipe(func_DER_1,
                                                                               model_control_actions.at[1, 'after'],
                                                                               model_control_actions.at[1, 'before'])

    # DWP_CEL_1
    def func_DWP_CEL_1(df, WP_1, WP_0):
        return WP_1 / WP_0 - 1

    model_control_actions.at[4, 'after'] = model_control_actions['after'].pipe(func_DWP_CEL_1,
                                                                               model_control_actions.at[3, 'after'],
                                                                               model_control_actions.at[3, 'before'])

    # P_IXD_0
    def func_P_IXD_0(df, P_IXD_USD_0, ER_0):
        return P_IXD_USD_0 * ER_0

    variables.at[26, 'base_pr'] = variables['base_pr'].pipe(func_P_IXD_0, model_control_actions.at[7, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # Q_AID_0
    def func_Q_AID_0(df, Q_IPD_0, Q_IXD_0):
        return Q_IPD_0 - Q_IXD_0

    variables.at[27, 'base_quan'] = variables['base_quan'].pipe(func_Q_AID_0, variables.at[25, 'base_quan'],
                                                                variables.at[26, 'base_quan'])

    # P_AID_0
    def func_P_AID_0(df, P_IPD_0, Q_IPD_0, P_IXD_0, Q_IXD_0, Q_AID_0):
        return (P_IPD_0 * Q_IPD_0 - P_IXD_0 * Q_IXD_0) / Q_AID_0

    variables.at[27, 'base_pr'] = variables['base_pr'].pipe(func_P_AID_0, variables.at[25, 'base_pr'],
                                                            variables.at[25, 'base_quan'], variables.at[26, 'base_pr'],
                                                            variables.at[26, 'base_quan'],
                                                            variables.at[27, 'base_quan'])

    # P_AVD_0
    def func_P_AVD_0(df, P_APD_0, Q_APD_0, P_AID_0, Q_AID_0, Q_AVD_0):
        return (P_APD_0 * Q_APD_0 - P_AID_0 * Q_AID_0) / Q_AVD_0

    variables.at[28, 'base_pr'] = variables['base_pr'].pipe(func_P_AVD_0, variables.at[29, 'base_pr'],
                                                            variables.at[29, 'base_quan'], variables.at[27, 'base_pr'],
                                                            variables.at[27, 'base_quan'],
                                                            variables.at[28, 'base_quan'])

    # P_AXD_0
    def func_P_AXD_0(df, P_AXD_USD_0, ER_0):
        return P_AXD_USD_0 * ER_0

    variables.at[30, 'base_pr'] = variables['base_pr'].pipe(func_P_AXD_0, model_control_actions.at[5, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # Q_AXW_0
    def func_Q_AXW_0(df, Q_ADW_0, Q_AXD_0):
        return Q_ADW_0 - Q_AXD_0

    variables.at[31, 'base_quan'] = variables['base_quan'].pipe(func_Q_AXW_0, variables.at[32, 'base_quan'],
                                                                variables.at[30, 'base_quan'])

    # P_ADW_0
    def func_P_ADW_0(df, WP_0, ER_0):
        return WP_0 * ER_0

    variables.at[32, 'base_pr'] = variables['base_pr'].pipe(func_P_ADW_0, model_control_actions.at[3, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # P_AXW_0
    def func_P_AXW_0(df, P_ADW_0, Q_ADW_0, P_AXD_0, TAXD_0, Q_AXD_0, Q_AXW_0):
        return (P_ADW_0 * Q_ADW_0 - P_AXD_0 * (1 + TAXD_0) * Q_AXD_0) / Q_AXW_0

    variables.at[31, 'base_pr'] = variables['base_pr'].pipe(func_P_AXW_0, variables.at[32, 'base_pr'],
                                                            variables.at[32, 'base_quan'], variables.at[30, 'base_pr'],
                                                            model_control_actions.at[8, 'before'],
                                                            variables.at[30, 'base_quan'],
                                                            variables.at[31, 'base_quan'])

    # Q_ASD_0
    def func_Q_ASD_0(df, Q_APD_0, Q_AXD_0):
        return Q_APD_0 - Q_AXD_0

    variables.at[33, 'base_quan'] = variables['base_quan'].pipe(func_Q_ASD_0, variables.at[29, 'base_quan'],
                                                                variables.at[30, 'base_quan'])

    # P_ASD_0
    def func_P_ASD_0(df, P_APD_0, Q_APD_0, P_AXD_0, Q_AXD_0, Q_ASD_0):
        return (P_APD_0 * Q_APD_0 - P_AXD_0 * Q_AXD_0) / Q_ASD_0

    variables.at[33, 'base_pr'] = variables['base_pr'].pipe(func_P_ASD_0, variables.at[29, 'base_pr'],
                                                            variables.at[29, 'base_quan'], variables.at[30, 'base_pr'],
                                                            variables.at[30, 'base_quan'],
                                                            variables.at[33, 'base_quan'])

    # Q_ATD_0
    def func_Q_ATD_0(df, Q_ASD_0, Q_AMD_0):
        return Q_ASD_0 + Q_AMD_0

    variables.at[34, 'base_quan'] = variables['base_quan'].pipe(func_Q_ATD_0, variables.at[33, 'base_quan'],
                                                                variables.at[35, 'base_quan'])

    # P_AMD_0
    def func_P_AMD_0(df, P_AMD_USD_0, ER_0):
        return P_AMD_USD_0 * ER_0

    variables.at[35, 'base_pr'] = variables['base_pr'].pipe(func_P_AMD_0, model_control_actions.at[6, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # P_ATD_0
    def func_P_ATD_0(df, P_ASD_0, Q_ASD_0, P_AMD_0, TAMD_0, Q_AMD_0, Q_ATD_0):
        return (P_ASD_0 * Q_ASD_0 + P_AMD_0 * (1 + TAMD_0) * Q_AMD_0) / Q_ATD_0

    variables.at[34, 'base_pr'] = variables['base_pr'].pipe(func_P_ATD_0, variables.at[33, 'base_pr'],
                                                            variables.at[33, 'base_quan'], variables.at[35, 'base_pr'],
                                                            model_control_actions.at[10, 'before'],
                                                            variables.at[35, 'base_quan'],
                                                            variables.at[34, 'base_quan'])

    # P_BID_0
    variables.at[37, 'base_pr'] = variables.at[34, 'base_pr']

    # Q_BID_0
    variables.at[37, 'base_quan'] = 0.7 * variables.at[34, 'base_quan']

    # Q_ADD_0
    variables.at[36, 'base_quan'] = variables.at[34, 'base_quan'] - variables.at[37, 'base_quan']

    # P_ADD_0
    def func_P_ADD_0(df, P_ATD_0, Q_ATD_0, P_BID_0, Q_BID_0, Q_ADD_0):
        return (P_ATD_0*Q_ATD_0-P_BID_0*Q_BID_0)/Q_ADD_0

    variables.at[36, 'base_pr'] = variables['base_pr'].pipe(func_P_ADD_0, variables.at[34, 'base_pr'],
                                                            variables.at[34, 'base_quan'], variables.at[37, 'base_pr'],
                                                            variables.at[37, 'base_quan'], variables.at[36, 'base_quan'])

    # P_BDD_0
    def func_P_BDD_0(df, P_BID_0, Q_BID_0, Q_BDD_0):
        return (P_BID_0*Q_BID_0/0.06)/Q_BDD_0

    variables.at[39, 'base_pr'] = variables['base_pr'].pipe(func_P_BDD_0, variables.at[37, 'base_pr'],
                                                            variables.at[37, 'base_quan'], variables.at[39, 'base_quan'])
    
    # P_BVD_0
    def func_P_BVD_0(df, P_BDD_0, Q_BDD_0, P_BID_0, Q_BID_0, Q_BVD_0):
        return (P_BDD_0*Q_BDD_0-P_BID_0*Q_BID_0)/Q_BVD_0

    variables.at[38, 'base_pr'] = variables['base_pr'].pipe(func_P_BVD_0, variables.at[39, 'base_pr'],
                                                            variables.at[39, 'base_quan'], variables.at[37, 'base_pr'],
                                                            variables.at[37, 'base_quan'], variables.at[38, 'base_quan'])

    # C42
    def func_C36(df, WP_1, WP_0):
        return WP_1 / WP_0

    variables.at[40, 'base_pr'] = variables['base_pr'].pipe(func_C36, model_control_actions.at[3, 'after'],
                                                            model_control_actions.at[3, 'before'])

    # r_Ω_IPD
    def func_r_Ω_IPD(df, Ω_IPD):
        return (Ω_IPD + 1) / Ω_IPD

    parameters.at[0, 'rho'] = parameters['rho'].pipe(func_r_Ω_IPD, parameters.at[0, 'values'])

    # r_σ_APD
    def func_r_σ_APD(df, σ_APD):
        return (σ_APD - 1) / σ_APD

    parameters.at[1, 'rho'] = parameters['rho'].pipe(func_r_σ_APD, parameters.at[1, 'values'])

    # r_Ω_APD
    def func_r_Ω_APD(df, Ω_APD):
        return (Ω_APD + 1) / Ω_APD

    parameters.at[2, 'rho'] = parameters['rho'].pipe(func_r_Ω_APD, parameters.at[2, 'values'])

    # r_σ_ADW
    def func_r_σ_ADW(df, σ_ADW):
        return (σ_ADW - 1) / σ_ADW

    parameters.at[3, 'rho'] = parameters['rho'].pipe(func_r_σ_ADW, parameters.at[3, 'values'])

    # r_σ_ATD
    def func_r_σ_ATD(df, σ_ATD):
        return (σ_ATD - 1) / σ_ATD

    parameters.at[4, 'rho'] = parameters['rho'].pipe(func_r_σ_ATD, parameters.at[4, 'values'])

    # r_Ω_ATD
    def func_r_Ω_ATD(df, Ω_ATD):
        return (Ω_ATD+1)/Ω_ATD

    parameters.at[5, 'rho'] = parameters['rho'].pipe(func_r_Ω_ATD, parameters.at[5, 'values'])

    # r_σ_BDD
    def func_r_σ_BDD(df, σ_BDD):
        return (σ_BDD-1)/σ_BDD

    parameters.at[6, 'rho'] = parameters['rho'].pipe(func_r_σ_BDD, parameters.at[6, 'values'])

    # Z_IPD
    def func_Z_IPD(df, Q_IPD_0, P_IPD_0, ε_IPD):
        return Q_IPD_0 / (P_IPD_0 ** ε_IPD)

    parameters.at[8, 'rho'] = parameters['rho'].pipe(func_Z_IPD, variables.at[25, 'base_quan'],
                                                     variables.at[25, 'base_pr'], parameters.at[8, 'values'])

    # Z_IXD
    def func_Z_IXD(df, Q_IXD_0, P_IXD_0, TIXD_0, ER_0, ε_IXD):
        return Q_IXD_0 / ((P_IXD_0 * (1 + TIXD_0) / ER_0) ** ε_IXD)

    parameters.at[9, 'rho'] = parameters['rho'].pipe(func_Z_IXD, variables.at[26, 'base_quan'],
                                                     variables.at[26, 'base_pr'], model_control_actions.at[9, 'before'],
                                                     model_control_actions.at[1, 'before'],
                                                     parameters.at[9, 'values'])

    # Z_AVD
    def func_Z_AVD(df, Q_AVD_0, P_AVD_0, ε_AVD):
        return Q_AVD_0 / (P_AVD_0) ** ε_AVD

    parameters.at[10, 'rho'] = parameters['rho'].pipe(func_Z_AVD, variables.at[28, 'base_quan'],
                                                     variables.at[28, 'base_pr'], parameters.at[10, 'values'])

    # Z_ADW
    def func_Z_ADW(df, Q_ADW_0, P_ADW_0, ER_0, ε_ADW):
        return Q_ADW_0 / (P_ADW_0 / ER_0) ** ε_ADW

    parameters.at[11, 'rho'] = parameters['rho'].pipe(func_Z_ADW, variables.at[32, 'base_quan'],
                                                     variables.at[32, 'base_pr'],
                                                     model_control_actions.at[1, 'before'], parameters.at[11, 'values'])

    # Z_AXW
    def func_Z_AXW(df, Q_AXW_0, P_AXW_0, ER_0, ε_AXW):
        return Q_AXW_0 / (P_AXW_0 / ER_0) ** ε_AXW

    parameters.at[12, 'rho'] = parameters['rho'].pipe(func_Z_AXW, variables.at[31, 'base_quan'],
                                                      variables.at[31, 'base_pr'],
                                                      model_control_actions.at[1, 'before'],
                                                      parameters.at[12, 'values'])

    # Z_AMD
    def func_Z_AMD(df, Q_AMD_0, P_AMD_0, ER_0, ε_AMD):
        return Q_AMD_0 / (P_AMD_0 / ER_0) ** ε_AMD

    parameters.at[13, 'rho'] = parameters['rho'].pipe(func_Z_AMD, variables.at[35, 'base_quan'],
                                                      variables.at[35, 'base_pr'],
                                                      model_control_actions.at[1, 'before'],
                                                      parameters.at[13, 'values'])

    # Z_ADD
    def func_Z_ADD(df, Q_ADD_0, P_ADD_0, ε_ADD):
        return Q_ADD_0/(P_ADD_0) ** ε_ADD

    parameters.at[14, 'rho'] = parameters['rho'].pipe(func_Z_ADD, variables.at[36, 'base_quan'],
                                                      variables.at[36, 'base_pr'], parameters.at[14, 'values'])
    # Z_BDD
    def func_Z_BDD(df, Q_BDD_0, P_BDD_0, ε_BDD):
        return Q_BDD_0/(P_BDD_0) ** ε_BDD

    parameters.at[15, 'rho'] = parameters['rho'].pipe(func_Z_BDD, variables.at[39, 'base_quan'],
                                                      variables.at[39, 'base_pr'], parameters.at[15, 'values'])

    # Z_BVD
    def func_Z_BVD(df, Q_BVD_0, P_BVD_0, ε_BVD):
        return Q_BVD_0/(P_BVD_0) ** ε_BVD

    parameters.at[16, 'rho'] = parameters['rho'].pipe(func_Z_BVD, variables.at[38, 'base_quan'],
                                                      variables.at[38, 'base_pr'], parameters.at[16, 'values'])

    # K_IXD
    def func_K_IXD(df, Q_IXD_0, Q_AID_0, r_Ω_IPD, P_IXD_0, P_AID_0):
        return ((Q_IXD_0 / Q_AID_0) ** (1 - r_Ω_IPD)) * (P_IXD_0 / P_AID_0)

    variables.at[28, 'relative_quality'] = variables['relative_quality'].pipe(func_K_IXD, variables.at[26, 'base_quan'],
                                                                              variables.at[27, 'base_quan'],
                                                                              parameters.at[0, 'rho'],
                                                                              variables.at[26, 'base_pr'],
                                                                              variables.at[27, 'base_pr'])

    # K_AVD
    def func_K_AVD(df, Q_AVD_0, Q_AID_0, r_σ_APD, P_AVD_0, P_AID_0):
        return (Q_AVD_0 / Q_AID_0) ** (1 - r_σ_APD) * (P_AVD_0 / P_AID_0)

    variables.at[28, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AVD, variables.at[28, 'base_quan'],
                                                                              variables.at[27, 'base_quan'],
                                                                              parameters.at[1, 'rho'],
                                                                              variables.at[28, 'base_pr'],
                                                                              variables.at[27, 'base_pr'])

    # A_APD
    def func_A_APD(df, Q_APD_0, K_AID, Q_AID_0, r_σ_APD, K_AVD, Q_AVD_0):
        return Q_APD_0 / (K_AID * Q_AID_0 ** r_σ_APD + K_AVD * Q_AVD_0 ** r_σ_APD) ** (1 / r_σ_APD)

    variables.at[29, 'relative_quality'] = variables['relative_quality'].pipe(func_A_APD,
                                                                              variables.at[29, 'base_quan'],
                                                                              variables.at[27, 'relative_quality'],
                                                                              variables.at[27, 'base_quan'],
                                                                              parameters.at[1, 'rho'],
                                                                              variables.at[28, 'relative_quality'],
                                                                              variables.at[28, 'base_quan'])

    # K_AXD
    def func_K_AXD(df, Q_AXD_0, Q_ASD_0, r_Ω_APD, P_AXD_0, P_ASD_0):
        return (Q_AXD_0 / Q_ASD_0) ** (1 - r_Ω_APD) * (P_AXD_0 / P_ASD_0)

    variables.at[30, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXD, variables.at[30, 'base_quan'],
                                                                              variables.at[33, 'base_quan'],
                                                                              parameters.at[2, 'rho'],
                                                                              variables.at[30, 'base_pr'],
                                                                              variables.at[33, 'base_pr'])

    # K_AXW
    def func_K_AXW(df, Q_AXW_0, Q_AXD_0, r_σ_ADW, P_AXW_0, P_AXD_0, TAXD_0, K_AXD):
        return (Q_AXW_0 / Q_AXD_0) ** (1 - r_σ_ADW) * (P_AXW_0 / (P_AXD_0 * (1 + TAXD_0))) * K_AXD

    variables.at[31, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXW, variables.at[31, 'base_quan'],
                                                                              variables.at[30, 'base_quan'],
                                                                              parameters.at[3, 'rho'],
                                                                              variables.at[31, 'base_pr'],
                                                                              variables.at[30, 'base_pr'],
                                                                              model_control_actions.at[8, 'before'],
                                                                              variables.at[30, 'relative_quality'])

    # K_AMD
    def func_K_AMD(df, Q_AMD_0, Q_ASD_0, r_σ_ATD, P_AMD_0, TAMD_0, P_ASD_0):
        return (Q_AMD_0 / Q_ASD_0) ** (1 - r_σ_ATD) * (P_AMD_0 * (1 + TAMD_0) / P_ASD_0)

    variables.at[35, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AMD, variables.at[35, 'base_quan'],
                                                                              variables.at[33, 'base_quan'],
                                                                              parameters.at[4, 'rho'],
                                                                              variables.at[35, 'base_pr'],
                                                                              model_control_actions.at[10, 'before'],
                                                                              variables.at[33, 'base_pr'])

    # K_ADD
    def func_K_ADD(df, Q_ADD_0, Q_BID_0, r_Ω_ATD, P_ADD_0, P_BID_0):
        return (Q_ADD_0/Q_BID_0) ** (1-r_Ω_ATD)*(P_ADD_0/P_BID_0)

    variables.at[36, 'relative_quality'] = variables['relative_quality'].pipe(func_K_ADD, variables.at[36, 'base_quan'],
                                                                              variables.at[37, 'base_quan'],
                                                                              parameters.at[5, 'rho'],
                                                                              variables.at[36, 'base_pr'],
                                                                              variables.at[37, 'base_pr'])

    # K_BVD
    def func_K_BVD(df, Q_BVD_0, Q_BID_0, r_σ_BDD, P_BVD_0, P_BID_0):
        return (Q_BVD_0/Q_BID_0) ** (1-r_σ_BDD)*(P_BVD_0/P_BID_0)

    variables.at[38, 'relative_quality'] = variables['relative_quality'].pipe(func_K_BVD, variables.at[38, 'base_quan'],
                                                                              variables.at[37, 'base_quan'],
                                                                              parameters.at[6, 'rho'],
                                                                              variables.at[38, 'base_pr'],
                                                                              variables.at[37, 'base_pr'])

    # A_BDD
    def func_A_BDD(df, Q_BDD_0, K_BID, Q_BID_0, r_σ_BDD, K_BVD, Q_BVD_0):
        return Q_BDD_0/(K_BID*Q_BID_0 ** r_σ_BDD+K_BVD*Q_BVD_0 ** r_σ_BDD) ** (1/r_σ_BDD)

    variables.at[39, 'relative_quality'] = variables['relative_quality'].pipe(func_A_BDD, variables.at[39, 'base_quan'],
                                                                              variables.at[37, 'relative_quality'],
                                                                              variables.at[37, 'base_quan'],
                                                                              parameters.at[6, 'rho'],
                                                                              variables.at[38, 'relative_quality'],
                                                                              variables.at[38, 'base_quan'])




































input_data = InputDataBase(example_data)
result = steel_market(input_data)
print(result)