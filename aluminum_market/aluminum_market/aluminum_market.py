import math
import numpy as np
from scipy.optimize import fsolve
from math import fsum, sqrt
import pandas as pd
import os

example_data = {'ER_before': 72.795, 'ER_after': 72.795, 'WP_before': 2088.0, 'WP_after': 2088.0,
                'P_AXD_USD_before': 1842.0, 'P_AMD_USD_before': 2377.0, 'P_IMD_USD_before': 353.0, 'TAXD_before': 0.0,
                'TAXD_after': 0.3, 'TIMD_before': 0.0, 'TIMD_after': 0.0, 'TAMD_before': 0.0, 'TAMD_after': 0.0,
                'SS_IPD_SUPPLY_after': 0.0, 'DS_IMD_SUPPLY_after': 0.0, 'SS_AVD_SUPPLY_after': 0.0,
                'DS_ADW_DEMAND_after': 0.0, 'SS_AXW_SUPPLY_after': 0.0, 'SS_AMD_SUPPLY_after': 0.0,
                'DS_ATD_DEMAND_after': 0.0, 'IPD_pr': 32821.0, 'IPD_q': 8200000.0, 'IMD_q': 4722500.0,
                'APD_pr': 173588.0, 'APD_g': 3800000.0, 'AXD_q': 3148500.0, 'ADW_q': 137000000.0,
                'AMD_q': 19900.0, 'σ_AID': 2, 'σ_APD': 1.5, 'Ω_APD': 4.2, 'σ_ADW': 8.4, 'σ_ATD': 1.5,
                'ε_IPD': 0.3, 'ε_IMD': 1.5, 'ε_AVD': 1, 'ε_ADW': -0.8, 'ε_AXW': 2, 'ε_AMD': 3, 'ε_ATD': -0.8}


class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.WP_before = float(dict_from_frontend.get('WP_before'))
        self.WP_after = float(dict_from_frontend.get('WP_after'))
        self.P_AXD_USD_before = float(dict_from_frontend.get('P_AXD_USD_before'))
        self.P_AMD_USD_before = float(dict_from_frontend.get('P_AMD_USD_before'))
        self.P_IMD_USD_before = float(dict_from_frontend.get('P_IMD_USD_before'))
        self.TAXD_before = float(dict_from_frontend.get('TAXD_before'))
        self.TAXD_after = float(dict_from_frontend.get('TAXD_after'))
        self.TIMD_before = float(dict_from_frontend.get('TIMD_before'))
        self.TIMD_after = float(dict_from_frontend.get('TIMD_after'))
        self.TAMD_before = float(dict_from_frontend.get('TAMD_before'))
        self.TAMD_after = float(dict_from_frontend.get('TAMD_after'))
        self.SS_IPD_SUPPLY_after = float(dict_from_frontend.get('SS_IPD_SUPPLY_after'))
        self.DS_IMD_SUPPLY_after = float(dict_from_frontend.get('DS_IMD_SUPPLY_after'))
        self.SS_AVD_SUPPLY_after = float(dict_from_frontend.get('SS_AVD_SUPPLY_after'))
        self.DS_ADW_DEMAND_after = float(dict_from_frontend.get('DS_ADW_DEMAND_after'))
        self.SS_AXW_SUPPLY_after = float(dict_from_frontend.get('SS_AXW_SUPPLY_after'))
        self.SS_AMD_SUPPLY_after = float(dict_from_frontend.get('SS_AMD_SUPPLY_after'))
        self.DS_ATD_DEMAND_after = float(dict_from_frontend.get('DS_ATD_DEMAND_after'))
        self.IPD_pr = float(dict_from_frontend.get('IPD_pr'))
        self.IPD_q = float(dict_from_frontend.get('IPD_q'))
        self.IMD_q = float(dict_from_frontend.get('IMD_q'))
        self.APD_pr = float(dict_from_frontend.get('APD_pr'))
        self.APD_g = float(dict_from_frontend.get('APD_g'))
        self.AXD_q = float(dict_from_frontend.get('AXD_q'))
        self.ADW_q = float(dict_from_frontend.get('ADW_q'))
        self.AMD_q = float(dict_from_frontend.get('AMD_q'))
        self.σ_AID = float(dict_from_frontend.get('σ_AID'))
        self.σ_APD = float(dict_from_frontend.get('σ_APD'))
        self.Ω_APD = float(dict_from_frontend.get('Ω_APD'))
        self.σ_ADW = float(dict_from_frontend.get('σ_ADW'))
        self.σ_ATD = float(dict_from_frontend.get('σ_ATD'))
        self.ε_IPD = float(dict_from_frontend.get('ε_IPD'))
        self.ε_IMD = float(dict_from_frontend.get('ε_IMD'))
        self.ε_AVD = float(dict_from_frontend.get('ε_AVD'))
        self.ε_ADW = float(dict_from_frontend.get('ε_ADW'))
        self.ε_AXW = float(dict_from_frontend.get('ε_AXW'))
        self.ε_AMD = float(dict_from_frontend.get('ε_AMD'))
        self.ε_ATD = float(dict_from_frontend.get('ε_ATD'))

def aluminum_market(input_data):
    """Получаем данные из модели"""

    mydir = '/Users/natalazivlova/Desktop/parser/aluminum_market/aluminum_market/'
    myfile = 'PE_алюминий.xlsm'
    file = os.path.join(mydir, myfile)
    df = pd.read_excel(file, usecols='A:J')

    # Управляющие воздействия модели
    model_control_actions = df.iloc[1:19, 0:4]
    model_control_actions = model_control_actions.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'designation',
                 'Базовое равновесие': 'before', 'Новое равновесие': 'after'})

    # Переменные
    variables = df.iloc[23:34, 0:9]
    variables = variables.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'designation',
                 'Базовое равновесие': 'base_pr',
                 'Новое равновесие': 'base_quan', 'Unnamed: 4': 'relative_quality', 'Unnamed: 5': 'new_pr',
                 'Unnamed: 6': 'new_quan', 'Параметры': 'perc_change_price', 'Unnamed: 8': 'perc_change_quantity'})

    # Уравнения
    equations = df.iloc[36:60, 0:2]
    equations = equations.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'values'})

    # Параметры
    parameters = df.iloc[0:13, 7:10]
    parameters = parameters.rename(
        columns={'Параметры': 'designation', 'Unnamed: 8': 'values'})

    """Вводим новые значения"""

    model_control_actions.at[1, 'before'] = input_data.ER_before
    model_control_actions.at[1, 'after'] = input_data.ER_after
    model_control_actions.at[3, 'before'] = input_data.WP_before
    model_control_actions.at[3, 'after'] = input_data.WP_after
    model_control_actions.at[5, 'before'] = input_data.P_AXD_USD_before
    model_control_actions.at[6, 'before'] = input_data.P_AMD_USD_before
    model_control_actions.at[7, 'before'] = input_data.P_IMD_USD_before
    model_control_actions.at[8, 'before'] = input_data.TAXD_before
    model_control_actions.at[8, 'after'] = input_data.TAXD_after
    model_control_actions.at[9, 'before'] = input_data.TIMD_before
    model_control_actions.at[9, 'after'] = input_data.TIMD_after
    model_control_actions.at[10, 'before'] = input_data.TAMD_before
    model_control_actions.at[10, 'after'] = input_data.TAMD_after
    model_control_actions.at[12, 'after'] = input_data.SS_IPD_SUPPLY_after
    model_control_actions.at[13, 'after'] = input_data.DS_IMD_SUPPLY_after
    model_control_actions.at[14, 'after'] = input_data.SS_AVD_SUPPLY_after
    model_control_actions.at[15, 'after'] = input_data.DS_ADW_DEMAND_after
    model_control_actions.at[16, 'after'] = input_data.SS_AXW_SUPPLY_after
    model_control_actions.at[17, 'after'] = input_data.SS_AMD_SUPPLY_after
    model_control_actions.at[18, 'after'] = input_data.DS_ATD_DEMAND_after

    variables.at[23, 'base_pr'] = input_data.IPD_pr
    variables.at[23, 'base_quan'] = input_data.IPD_q
    variables.at[24, 'base_quan'] = input_data.IMD_q
    variables.at[27, 'base_pr'] = input_data.APD_pr
    variables.at[27, 'base_quan'] = input_data.APD_g
    variables.at[28, 'base_quan'] = input_data.AXD_q
    variables.at[30, 'base_quan'] = input_data.ADW_q
    variables.at[33, 'base_quan'] = input_data.AMD_q

    parameters.at[0, 'values'] = input_data.σ_AID
    parameters.at[1, 'values'] = input_data.σ_APD
    parameters.at[2, 'values'] = input_data.Ω_APD
    parameters.at[3, 'values'] = input_data.σ_ADW
    parameters.at[4, 'values'] = input_data.σ_ATD
    parameters.at[6, 'values'] = input_data.ε_IPD
    parameters.at[7, 'values'] = input_data.ε_IMD
    parameters.at[8, 'values'] = input_data.ε_AVD
    parameters.at[9, 'values'] = input_data.ε_ADW
    parameters.at[10, 'values'] = input_data.ε_AXW
    parameters.at[11, 'values'] = input_data.ε_AMD
    parameters.at[12, 'values'] = input_data.ε_ATD

    """Перерасчет ячеек с новыми значениями"""

    # DER_1
    def func_DER_1(df, ER_1, ER_0):
        return ER_1 / ER_0 - 1

    model_control_actions.at[2, 'after'] = model_control_actions['after'].pipe(func_DER_1,
                                                                               model_control_actions.at[1, 'after'],
                                                                               model_control_actions.at[1, 'before'])

    # DWP_CEL_1
    def func_DWP_CEL_1(df, WP_1, WP_0):
        return WP_1 / WP_0 - 1

    model_control_actions.at[4, 'after'] = model_control_actions['after'].pipe(func_DWP_CEL_1,
                                                                               model_control_actions.at[3, 'after'],
                                                                               model_control_actions.at[3, 'before'])

    # P_IMD_0
    def func_P_IMD_0(df, P_IMD_USD_0, ER_0):
        return P_IMD_USD_0 * ER_0

    variables.at[24, 'base_pr'] = variables['base_pr'].pipe(func_P_IMD_0, model_control_actions.at[7, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # Q_AID_0
    def func_Q_AID_0(df, Q_IPD_0, Q_IMD_0):
        return Q_IPD_0 + Q_IMD_0

    variables.at[25, 'base_quan'] = variables['base_quan'].pipe(func_Q_AID_0, variables.at[23, 'base_quan'],
                                                                variables.at[24, 'base_quan'])

    # P_AID_0
    def func_P_AID_0(df, P_IPD_0, Q_IPD_0, P_IMD_0, Q_IMD_0, Q_AID_0):
        return (P_IPD_0 * Q_IPD_0 + P_IMD_0 * Q_IMD_0) / Q_AID_0

    variables.at[25, 'base_pr'] = variables['base_pr'].pipe(func_P_AID_0, variables.at[23, 'base_pr'],
                                                            variables.at[23, 'base_quan'], variables.at[24, 'base_pr'],
                                                            variables.at[24, 'base_quan'],
                                                            variables.at[25, 'base_quan'])

    # P_AVD_0
    def func_P_AVD_0(df, P_APD_0, Q_APD_0, P_AID_0, Q_AID_0, Q_AVD_0):
        return (P_APD_0 * Q_APD_0 - P_AID_0 * Q_AID_0) / Q_AVD_0

    variables.at[26, 'base_pr'] = variables['base_pr'].pipe(func_P_AVD_0, variables.at[27, 'base_pr'],
                                                            variables.at[27, 'base_quan'], variables.at[25, 'base_pr'],
                                                            variables.at[25, 'base_quan'],
                                                            variables.at[26, 'base_quan'])

    # P_AXD_0
    def func_P_AXD_0(df, P_AXD_USD_0, ER_0):
        return P_AXD_USD_0 * ER_0

    variables.at[28, 'base_pr'] = variables['base_pr'].pipe(func_P_AXD_0, model_control_actions.at[5, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # Q_AXW_0
    def func_Q_AXW_0(df, Q_ADW_0, Q_AXD_0):
        return Q_ADW_0 - Q_AXD_0

    variables.at[29, 'base_quan'] = variables['base_quan'].pipe(func_Q_AXW_0, variables.at[30, 'base_quan'],
                                                                variables.at[28, 'base_quan'])

    # P_ADW_0
    def func_P_ADW_0(df, WP_0, ER_0):
        return WP_0 * ER_0

    variables.at[30, 'base_pr'] = variables['base_pr'].pipe(func_P_ADW_0, model_control_actions.at[3, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # P_AXW_0
    def func_P_AXW_0(df, P_ADW_0, Q_ADW_0, P_AXD_0, TAXD_0, Q_AXD_0, Q_AXW_0):
        return (P_ADW_0 * Q_ADW_0 - P_AXD_0 * (1 + TAXD_0) * Q_AXD_0) / Q_AXW_0

    variables.at[29, 'base_pr'] = variables['base_pr'].pipe(func_P_AXW_0, variables.at[30, 'base_pr'],
                                                            variables.at[30, 'base_quan'], variables.at[28, 'base_pr'],
                                                            model_control_actions.at[8, 'before'],
                                                            variables.at[28, 'base_quan'],
                                                            variables.at[29, 'base_quan'])

    # Q_ASD_0
    def func_Q_ASD_0(df, Q_APD_0, Q_AXD_0):
        return Q_APD_0 - Q_AXD_0

    variables.at[31, 'base_quan'] = variables['base_quan'].pipe(func_Q_ASD_0, variables.at[27, 'base_quan'],
                                                                variables.at[28, 'base_quan'])

    # P_ASD_0
    def func_P_ASD_0(df, P_APD_0, Q_APD_0, P_AXD_0, Q_AXD_0, Q_ASD_0):
        return (P_APD_0 * Q_APD_0 - P_AXD_0 * Q_AXD_0) / Q_ASD_0

    variables.at[31, 'base_pr'] = variables['base_pr'].pipe(func_P_ASD_0, variables.at[27, 'base_pr'],
                                                            variables.at[27, 'base_quan'], variables.at[28, 'base_pr'],
                                                            variables.at[28, 'base_quan'],
                                                            variables.at[31, 'base_quan'])

    # Q_ATD_0
    def func_Q_ATD_0(df, Q_ASD_0, Q_AMD_0):
        return Q_ASD_0 + Q_AMD_0

    variables.at[32, 'base_quan'] = variables['base_quan'].pipe(func_Q_ATD_0, variables.at[31, 'base_quan'],
                                                                variables.at[33, 'base_quan'])

    # P_AMD_0
    def func_P_AMD_0(df, P_AMD_USD_0, ER_0):
        return P_AMD_USD_0 * ER_0

    variables.at[33, 'base_pr'] = variables['base_pr'].pipe(func_P_AMD_0, model_control_actions.at[6, 'before'],
                                                            model_control_actions.at[1, 'before'])

    # P_ATD_0
    def func_P_ATD_0(df, P_ASD_0, Q_ASD_0, P_AMD_0, TAMD_0, Q_AMD_0, Q_ATD_0):
        return (P_ASD_0 * Q_ASD_0 + P_AMD_0 * (1 + TAMD_0) * Q_AMD_0) / Q_ATD_0

    variables.at[32, 'base_pr'] = variables['base_pr'].pipe(func_P_ATD_0, variables.at[31, 'base_pr'],
                                                            variables.at[31, 'base_quan'], variables.at[33, 'base_pr'],
                                                            model_control_actions.at[10, 'before'],
                                                            variables.at[33, 'base_quan'],
                                                            variables.at[32, 'base_quan'])

    # r_σ_AID
    def func_r_σ_AID(df, σ_AID):
        return (σ_AID - 1) / σ_AID

    parameters.at[0, 'rho'] = parameters['rho'].pipe(func_r_σ_AID, parameters.at[0, 'values'])

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

    # Z_IPD
    def func_Z_IPD(df, Q_IPD_0, P_IPD_0, ε_IPD):
        return Q_IPD_0 / (P_IPD_0 ** ε_IPD)

    parameters.at[6, 'rho'] = parameters['rho'].pipe(func_Z_IPD, variables.at[23, 'base_quan'],
                                                     variables.at[23, 'base_pr'], parameters.at[6, 'values'])

    # Z_IMD
    def func_Z_IMD(df, Q_IMD_0, P_IMD_0, ER_0, ε_IMD):
        return Q_IMD_0 / ((P_IMD_0 / ER_0) ** ε_IMD)

    parameters.at[7, 'rho'] = parameters['rho'].pipe(func_Z_IMD, variables.at[24, 'base_quan'],
                                                     variables.at[24, 'base_pr'], model_control_actions.at[1, 'before'],
                                                     parameters.at[7, 'values'])

    # Z_AVD
    def func_Z_AVD(df, Q_AVD_0, P_AVD_0, ε_AVD):
        return Q_AVD_0 / (P_AVD_0) ** ε_AVD

    parameters.at[8, 'rho'] = parameters['rho'].pipe(func_Z_AVD, variables.at[26, 'base_quan'],
                                                     variables.at[26, 'base_pr'], parameters.at[8, 'values'])

    # Z_ADW
    def func_Z_ADW(df, Q_ADW_0, P_ADW_0, ER_0, ε_ADW):
        return Q_ADW_0 / (P_ADW_0 / ER_0) ** ε_ADW

    parameters.at[9, 'rho'] = parameters['rho'].pipe(func_Z_ADW, variables.at[30, 'base_quan'],
                                                     variables.at[30, 'base_pr'],
                                                     model_control_actions.at[1, 'before'], parameters.at[9, 'values'])

    # Z_AXW
    def func_Z_AXW(df, Q_AXW_0, P_AXW_0, ER_0, ε_AXW):
        return Q_AXW_0 / (P_AXW_0 / ER_0) ** ε_AXW

    parameters.at[10, 'rho'] = parameters['rho'].pipe(func_Z_AXW, variables.at[29, 'base_quan'],
                                                      variables.at[29, 'base_pr'],
                                                      model_control_actions.at[1, 'before'],
                                                      parameters.at[10, 'values'])

    # Z_AMD
    def func_Z_AMD(df, Q_AMD_0, P_AMD_0, ER_0, ε_AMD):
        return Q_AMD_0 / (P_AMD_0 / ER_0) ** ε_AMD

    parameters.at[11, 'rho'] = parameters['rho'].pipe(func_Z_AMD, variables.at[33, 'base_quan'],
                                                      variables.at[33, 'base_pr'],
                                                      model_control_actions.at[1, 'before'],
                                                      parameters.at[11, 'values'])

    # Z_ATD
    def func_Z_ATD(df, Q_ATD_0, P_ATD_0, ε_ATD):
        return Q_ATD_0 / (P_ATD_0) ** ε_ATD

    parameters.at[12, 'rho'] = parameters['rho'].pipe(func_Z_ATD, variables.at[32, 'base_quan'],
                                                      variables.at[32, 'base_pr'], parameters.at[12, 'values'])

    # K_IMD
    def func_K_IMD(df, Q_IMD_0, Q_IPD_0, r_σ_AID, P_IMD_0, TIMD_0, P_IPD_0):
        return ((Q_IMD_0 / Q_IPD_0) ** (1 - r_σ_AID)) * (P_IMD_0 * (1 + TIMD_0) / P_IPD_0)

    variables.at[24, 'relative_quality'] = variables['relative_quality'].pipe(func_K_IMD, variables.at[24, 'base_quan'],
                                                                              variables.at[23, 'base_quan'],
                                                                              parameters.at[0, 'rho'],
                                                                              variables.at[24, 'base_pr'],
                                                                              model_control_actions.at[9, 'before'],
                                                                              variables.at[23, 'base_pr'])

    # K_AVD
    def func_K_AVD(df, Q_AVD_0, Q_AID_0, r_σ_APD, P_AVD_0, P_AID_0):
        return (Q_AVD_0 / Q_AID_0) ** (1 - r_σ_APD) * (P_AVD_0 / P_AID_0)

    variables.at[26, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AVD, variables.at[26, 'base_quan'],
                                                                              variables.at[25, 'base_quan'],
                                                                              parameters.at[1, 'rho'],
                                                                              variables.at[26, 'base_pr'],
                                                                              variables.at[25, 'base_pr'])

    # A_APD
    def func_A_APD(df, Q_APD_0, K_AID, Q_AID_0, r_σ_APD, K_AVD, Q_AVD_0):
        return Q_APD_0 / (K_AID * Q_AID_0 ** r_σ_APD + K_AVD * Q_AVD_0 ** r_σ_APD) ** (1 / r_σ_APD)

    variables.at[27, 'relative_quality'] = variables['relative_quality'].pipe(func_A_APD,
                                                                              variables.at[27, 'base_quan'],
                                                                              variables.at[25, 'relative_quality'],
                                                                              variables.at[25, 'base_quan'],
                                                                              parameters.at[1, 'rho'],
                                                                              variables.at[26, 'relative_quality'],
                                                                              variables.at[26, 'base_quan'])

    # K_AXD
    def func_K_AXD(df, Q_AXD_0, Q_ASD_0, r_Ω_APD, P_AXD_0, P_ASD_0):
        return (Q_AXD_0 / Q_ASD_0) ** (1 - r_Ω_APD) * (P_AXD_0 / P_ASD_0)

    variables.at[28, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXD, variables.at[28, 'base_quan'],
                                                                              variables.at[31, 'base_quan'],
                                                                              parameters.at[2, 'rho'],
                                                                              variables.at[28, 'base_pr'],
                                                                              variables.at[31, 'base_pr'])

    # K_AXW
    def func_K_AXW(df, Q_AXW_0, Q_AXD_0, r_σ_ADW, P_AXW_0, P_AXD_0, TAXD_0, K_AXD):
        return (Q_AXW_0 / Q_AXD_0) ** (1 - r_σ_ADW) * (P_AXW_0 / (P_AXD_0 * (1 + TAXD_0))) * K_AXD

    variables.at[29, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXW, variables.at[29, 'base_quan'],
                                                                              variables.at[28, 'base_quan'],
                                                                              parameters.at[3, 'rho'],
                                                                              variables.at[29, 'base_pr'],
                                                                              variables.at[28, 'base_pr'],
                                                                              model_control_actions.at[8, 'before'],
                                                                              variables.at[28, 'relative_quality'])

    # K_AMD
    def func_K_AMD(df, Q_AMD_0, Q_ASD_0, r_σ_ATD, P_AMD_0, TAMD_0, P_ASD_0):
        return (Q_AMD_0 / Q_ASD_0) ** (1 - r_σ_ATD) * (P_AMD_0 * (1 + TAMD_0) / P_ASD_0)

    variables.at[33, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AMD, variables.at[33, 'base_quan'],
                                                                              variables.at[31, 'base_quan'],
                                                                              parameters.at[4, 'rho'],
                                                                              variables.at[33, 'base_pr'],
                                                                              model_control_actions.at[10, 'before'],
                                                                              variables.at[31, 'base_pr'])

    def func(z):
        variables.at[23, 'new_quan'] = z[0]
        variables.at[23, 'new_pr'] = z[1]
        variables.at[24, 'new_quan'] = z[2]
        variables.at[24, 'new_pr'] = z[3]
        variables.at[25, 'new_pr'] = z[4]
        variables.at[25, 'new_quan'] = z[5]
        variables.at[26, 'new_quan'] = z[6]
        variables.at[26, 'new_pr'] = z[7]
        variables.at[27, 'new_pr'] = z[8]
        variables.at[27, 'new_quan'] = z[9]
        variables.at[28, 'new_pr'] = z[10]
        variables.at[28, 'new_quan'] = z[11]
        variables.at[31, 'new_pr'] = z[12]
        variables.at[31, 'new_quan'] = z[12]
        variables.at[30, 'new_pr'] = z[14]
        variables.at[30, 'new_quan'] = z[15]
        variables.at[29, 'new_pr'] = z[16]
        variables.at[29, 'new_quan'] = z[17]
        variables.at[32, 'new_pr'] = z[18]
        variables.at[32, 'new_quan'] = z[19]
        variables.at[33, 'new_pr'] = z[20]
        variables.at[33, 'new_quan'] = z[21]

        IPD_SUPPLY = variables.at[23, 'new_quan'] - parameters.at[6, 'rho'] * (
                1 + model_control_actions.at[12, 'after']) * (variables.at[23, 'new_pr']) ** parameters.at[6, 'values']

        IMD_SUPPLY = variables.at[24, 'new_quan'] - parameters.at[7, 'rho'] * (1 + model_control_actions.at[13, 'after'])\
                     * (variables.at[24, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[7, 'values']

        AID_BUD_CES = variables.at[25, 'new_pr'] * variables.at[25, 'new_quan'] - variables.at[24, 'new_pr'] * \
                      (1 + model_control_actions.at[9, 'after']) * variables.at[24, 'new_quan'] - variables.at[
                          23, 'new_pr'] * variables.at[23, 'new_quan']

        AID_CES = variables.at[23, 'new_quan'] / variables.at[24, 'new_quan'] - ((variables.at[23, 'new_pr'] /
                (variables.at[24, 'new_pr'] * (1 + model_control_actions.at[9, 'after']))) *
                        (variables.at[24, 'relative_quality'] / variables.at[23, 'relative_quality'])) ** (
                          1 / (parameters.at[0, 'rho'] - 1))

        AID_BAL_CES = variables.at[25, 'new_quan'] - variables.at[23, 'new_quan'] - variables.at[24, 'new_quan']

        AVD_SUPPLY = variables.at[26, 'new_quan'] - parameters.at[8, 'rho'] * (
                1 + model_control_actions.at[14, 'after']) * (variables.at[26, 'new_pr']) ** parameters.at[8, 'values']

        APD_BUD_CES = variables.at[27, 'new_pr'] * variables.at[27, 'new_quan'] - variables.at[25, 'new_pr'] \
                      * variables.at[25, 'new_quan'] - variables.at[26, 'new_pr'] * variables.at[26, 'new_quan']

        APD_CES = variables.at[26, 'new_quan'] / variables.at[25, 'new_quan'] - ((variables.at[26, 'new_pr'] /
                (variables.at[25, 'new_pr'])) * (variables.at[25, 'relative_quality'] /
                            variables.at[26, 'relative_quality'])) ** (1 / (parameters.at[1, 'rho'] - 1))

        APD_BAL_CES = variables.at[27, 'new_quan'] - variables.at[27, 'relative_quality'] * (
                variables.at[25, 'relative_quality'] * variables.at[25, 'new_quan'] ** parameters.at[1, 'rho'] +
                variables.at[26, 'relative_quality'] * variables.at[26, 'new_quan'] **
                parameters.at[1, 'rho']) ** (1 / parameters.at[1, 'rho'])

        APD_BUD_CET = variables.at[27, 'new_pr'] * variables.at[27, 'new_quan'] - variables.at[28, 'new_pr'] * \
                      variables.at[28, 'new_quan'] - variables.at[31, 'new_pr'] * variables.at[31, 'new_quan']

        APD_CET = variables.at[28, 'new_quan'] / variables.at[31, 'new_quan'] - ((variables.at[28, 'new_pr'] /
                (variables.at[31, 'new_pr'])) * (variables.at[31, 'relative_quality'] /
                        variables.at[28, 'relative_quality'])) ** (1 / (parameters.at[2, 'rho'] - 1))

        APD_BAL_CET = variables.at[27, 'new_quan'] - variables.at[28, 'new_quan'] - variables.at[31, 'new_quan']

        ADW_BUD_CES = variables.at[30, 'new_pr'] * variables.at[30, 'new_quan'] - variables.at[28, 'new_pr'] * (
                1 + model_control_actions.at[8, 'after']) * variables.at[28, 'new_quan'] - variables.at[29, 'new_pr'] * \
                      variables.at[29, 'new_quan']

        ADW_CES = variables.at[29, 'new_quan'] / variables.at[28, 'new_quan'] - (((variables.at[29, 'new_pr']) /
                      (variables.at[28, 'new_pr'] * (1 + model_control_actions.at[8, 'after']))) *
                            (variables.at[28, 'relative_quality'] / variables.at[29, 'relative_quality'])) ** (
                          1 / (parameters.at[3, 'rho'] - 1))

        ADW_BAL_CES = variables.at[30, 'new_quan'] - variables.at[28, 'new_quan'] - variables.at[29, 'new_quan']

        AXW_SUPPLY = variables.at[29, 'new_quan'] - parameters.at[10, 'rho'] * (1 + model_control_actions.at[16, 'after']) * (
            variables.at[29, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[10, 'values']

        ADW_DEMAND = variables.at[30, 'new_quan'] - parameters.at[9, 'rho'] * (1 + model_control_actions.at[15, 'after']) * (
                    variables.at[30, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[9, 'values']

        ATD_BUD_CES = variables.at[32, 'new_pr'] * variables.at[32, 'new_quan'] - variables.at[33, 'new_pr'] * (
                1 + model_control_actions.at[10, 'after']) * variables.at[33, 'new_quan'] - variables.at[31, 'new_pr'] \
                      * variables.at[31, 'new_quan']

        ATD_CES = variables.at[31, 'new_quan'] / variables.at[33, 'new_quan'] - ((variables.at[31, 'new_pr'] /
                (variables.at[33, 'new_pr'] * (1 + model_control_actions.at[10, 'after']))) *
                (variables.at[33, 'relative_quality'] / variables.at[31, 'relative_quality'])) ** (
                          1 / (parameters.at[4, 'rho'] - 1))

        ATD_BAL_CES = variables.at[32, 'new_quan'] - variables.at[31, 'new_quan'] - variables.at[33, 'new_quan']

        AMD_SUPPLY = variables.at[33, 'new_quan'] - parameters.at[11, 'rho'] * (
                1 + model_control_actions.at[17, 'after']) * (variables.at[33, 'new_pr'] /
                                        (model_control_actions.at[1, 'after'])) ** parameters.at[11, 'values']

        ADW_DEMAND_2 = variables.at[32, 'new_quan'] - parameters.at[12, 'rho'] * \
                       (1 + model_control_actions.at[18, 'after']) * (variables.at[32, 'new_pr']) ** \
                       parameters.at[12, 'values']

        return IPD_SUPPLY, IMD_SUPPLY, AID_BUD_CES, AID_CES, AID_BAL_CES, AVD_SUPPLY, APD_BUD_CES, APD_CES, APD_BAL_CES, \
               APD_BUD_CET, APD_CET, APD_BAL_CET, ADW_BUD_CES, ADW_CES, ADW_BAL_CES, AXW_SUPPLY, ADW_DEMAND, \
               ATD_BUD_CES, ATD_CES, ATD_BAL_CES, AMD_SUPPLY, ADW_DEMAND_2

    z0 = [variables.at[23, 'new_quan'], variables.at[23, 'new_pr'], variables.at[24, 'new_quan'],
          variables.at[24, 'new_pr'], variables.at[25, 'new_pr'], variables.at[25, 'new_quan'],
          variables.at[26, 'new_quan'], variables.at[26, 'new_pr'], variables.at[27, 'new_pr'],
          variables.at[27, 'new_quan'], variables.at[28, 'new_pr'], variables.at[28, 'new_quan'],
          variables.at[31, 'new_pr'], variables.at[31, 'new_quan'], variables.at[30, 'new_pr'],
          variables.at[30, 'new_quan'], variables.at[29, 'new_pr'], variables.at[29, 'new_quan'],
          variables.at[32, 'new_pr'], variables.at[32, 'new_quan'], variables.at[33, 'new_pr'],
          variables.at[33, 'new_quan']]

    solved_value = fsolve(func, z0)

    # Q_IPD_1
    variables.at[23, 'new_quan'] = solved_value[0]

    # P_IPD_1
    variables.at[23, 'new_pr'] = solved_value[1]

    # Q_IMD_1
    variables.at[24, 'new_quan'] = solved_value[2]

    # P_IMD_1
    variables.at[24, 'new_pr'] = solved_value[3]

    # P_AID_1
    variables.at[25, 'new_pr'] = solved_value[4]

    # Q_AID_1
    variables.at[25, 'new_quan'] = solved_value[5]

    # Q_AVD_1
    variables.at[26, 'new_quan'] = solved_value[6]

    # P_AVD_1
    variables.at[26, 'new_pr'] = solved_value[7]

    # P_APD_1
    variables.at[27, 'new_pr'] = solved_value[8]

    # Q_APD_1
    variables.at[27, 'new_quan'] = solved_value[9]

    # P_AXD_1
    variables.at[28, 'new_pr'] = solved_value[10]

    # Q_AXD_1
    variables.at[28, 'new_quan'] = solved_value[11]

    # P_ASD_1
    variables.at[31, 'new_pr'] = solved_value[12]

    # Q_ASD_1
    variables.at[31, 'new_quan'] = solved_value[13]

    # P_ADW_1
    variables.at[30, 'new_pr'] = solved_value[14]

    # Q_ADW_1
    variables.at[30, 'new_quan'] = solved_value[15]

    # P_AXW_1
    variables.at[29, 'new_pr'] = solved_value[16]

    # Q_AXW_1
    variables.at[29, 'new_quan'] = solved_value[17]

    # P_ATD_1
    variables.at[32, 'new_pr'] = solved_value[18]

    # Q_ATD_1
    variables.at[32, 'new_quan'] = solved_value[19]

    # P_AMD_1
    variables.at[33, 'new_pr'] = solved_value[20]

    # Q_AMD_1
    variables.at[33, 'new_quan'] = solved_value[21]

    eqs = []

    IPD_SUPPLY = variables.at[23, 'new_quan'] - parameters.at[6, 'rho'] * (
            1 + model_control_actions.at[12, 'after']) * (variables.at[23, 'new_pr']) ** \
                 parameters.at[6, 'values']

    eqs.append(IPD_SUPPLY)

    IMD_SUPPLY = variables.at[24, 'new_quan'] - parameters.at[7, 'rho'] * (1 + model_control_actions.at[13, 'after']) \
                 * (variables.at[24, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[7, 'values']

    eqs.append(IMD_SUPPLY)

    AID_BUD_CES = variables.at[25, 'new_pr'] * variables.at[25, 'new_quan'] - variables.at[24, 'new_pr'] * (
            1 + model_control_actions.at[9, 'after']) * variables.at[24, 'new_quan'] - variables.at[23, 'new_pr'] * \
                  variables.at[23, 'new_quan']

    eqs.append(AID_BUD_CES)

    AID_CES = variables.at[23, 'new_quan'] / variables.at[24, 'new_quan'] - ((variables.at[23, 'new_pr'] / (
            variables.at[24, 'new_pr'] * (1 + model_control_actions.at[9, 'after']))) *
                    (variables.at[24, 'relative_quality'] / variables.at[23, 'relative_quality'])) ** (
                      1 / (parameters.at[0, 'rho'] - 1))
    eqs.append(AID_CES)

    AID_BAL_CES = variables.at[25, 'new_quan'] - variables.at[23, 'new_quan'] - variables.at[24, 'new_quan']
    eqs.append(AID_BAL_CES)

    AVD_SUPPLY = variables.at[26, 'new_quan'] - parameters.at[8, 'rho'] * (
            1 + model_control_actions.at[14, 'after']) * (variables.at[26, 'new_pr']) ** \
                 parameters.at[8, 'values']
    eqs.append(AVD_SUPPLY)

    APD_BUD_CES = variables.at[27, 'new_pr'] * variables.at[27, 'new_quan'] - variables.at[25, 'new_pr'] * variables.at[
        25, 'new_quan'] - variables.at[26, 'new_pr'] * variables.at[26, 'new_quan']
    eqs.append(APD_BUD_CES)

    APD_CES = variables.at[26, 'new_quan'] / variables.at[25, 'new_quan'] - (
            (variables.at[26, 'new_pr'] / (variables.at[25, 'new_pr'])) * (
            variables.at[25, 'relative_quality'] / variables.at[26, 'relative_quality'])) ** (
                      1 / (parameters.at[1, 'rho'] - 1))
    eqs.append(APD_CES)

    APD_BAL_CES = variables.at[27, 'new_quan'] - variables.at[27, 'relative_quality'] * (
            variables.at[25, 'relative_quality'] * variables.at[25, 'new_quan'] ** parameters.at[1, 'rho'] +
            variables.at[26, 'relative_quality'] * variables.at[26, 'new_quan'] **
            parameters.at[1, 'rho']) ** (1 / parameters.at[1, 'rho'])
    eqs.append(APD_BAL_CES)

    APD_BUD_CET = variables.at[27, 'new_pr'] * variables.at[27, 'new_quan'] - variables.at[28, 'new_pr'] * variables.at[
        28, 'new_quan'] - variables.at[31, 'new_pr'] * variables.at[31, 'new_quan']
    eqs.append(APD_BUD_CET)

    APD_CET = variables.at[28, 'new_quan'] / variables.at[31, 'new_quan'] - (
            (variables.at[28, 'new_pr'] / (variables.at[31, 'new_pr'])) * (
            variables.at[31, 'relative_quality'] / variables.at[28, 'relative_quality'])) ** (
                      1 / (parameters.at[2, 'rho'] - 1))
    eqs.append(APD_CET)

    APD_BAL_CET = variables.at[27, 'new_quan'] - variables.at[28, 'new_quan'] - variables.at[31, 'new_quan']
    eqs.append(APD_BAL_CET)

    ADW_BUD_CES = variables.at[30, 'new_pr'] * variables.at[30, 'new_quan'] - variables.at[28, 'new_pr'] * (
            1 + model_control_actions.at[8, 'after']) * variables.at[28, 'new_quan'] - variables.at[29, 'new_pr'] * \
                  variables.at[29, 'new_quan']
    eqs.append(ADW_BUD_CES)

    ADW_CES = variables.at[29, 'new_quan'] / variables.at[28, 'new_quan'] - (((variables.at[29, 'new_pr']) / (
            variables.at[28, 'new_pr'] * (1 + model_control_actions.at[8, 'after']))) * (
                                                                                     variables.at[
                                                                                         28, 'relative_quality'] /
                                                                                     variables.at[
                                                                                         29, 'relative_quality'])) ** (
                      1 / (parameters.at[3, 'rho'] - 1))
    eqs.append(ADW_CES)

    ADW_BAL_CES = variables.at[30, 'new_quan'] - variables.at[28, 'new_quan'] - variables.at[29, 'new_quan']
    eqs.append(ADW_BAL_CES)

    AXW_SUPPLY = variables.at[29, 'new_quan'] - parameters.at[10, 'rho'] * (
            1 + model_control_actions.at[16, 'after']) * (
                         variables.at[29, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[
                     10, 'values']
    eqs.append(AXW_SUPPLY)

    ADW_DEMAND = variables.at[30, 'new_quan'] - parameters.at[9, 'rho'] * (
            1 + model_control_actions.at[15, 'after']) * (
                         variables.at[30, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[
                     9, 'values']
    eqs.append(ADW_DEMAND)

    ATD_BUD_CES = variables.at[32, 'new_pr'] * variables.at[32, 'new_quan'] - variables.at[33, 'new_pr'] * (
            1 + model_control_actions.at[10, 'after']) * variables.at[33, 'new_quan'] - variables.at[31, 'new_pr'] * \
                  variables.at[31, 'new_quan']
    eqs.append(ATD_BUD_CES)

    ATD_CES = variables.at[31, 'new_quan'] / variables.at[33, 'new_quan'] - ((variables.at[31, 'new_pr'] / (
            variables.at[33, 'new_pr'] * (1 + model_control_actions.at[10, 'after']))) * (
                                                                                     variables.at[
                                                                                         33, 'relative_quality'] /
                                                                                     variables.at[
                                                                                         31, 'relative_quality'])) ** (
                      1 / (parameters.at[4, 'rho'] - 1))
    eqs.append(ATD_CES)

    ATD_BAL_CES = variables.at[32, 'new_quan'] - variables.at[31, 'new_quan'] - variables.at[33, 'new_quan']
    eqs.append(ATD_BAL_CES)

    AMD_SUPPLY = variables.at[33, 'new_quan'] - parameters.at[11, 'rho'] * (
            1 + model_control_actions.at[17, 'after']) * (
                         variables.at[33, 'new_pr'] / (model_control_actions.at[1, 'after'])) ** parameters.at[
                     11, 'values']
    eqs.append(AMD_SUPPLY)

    ADW_DEMAND_2 = variables.at[32, 'new_quan'] - parameters.at[12, 'rho'] * (
            1 + model_control_actions.at[18, 'after']) * (variables.at[32, 'new_pr']) ** \
                   parameters.at[12, 'values']
    eqs.append(ADW_DEMAND_2)

    sqrt_eq = []

    for item in eqs:
        sqrt_eq.append(item ** 2)

    eq_result = sqrt(fsum(sqrt_eq))

    if eq_result < 0.000001:
        solution = True
    else:
        solution = False

    # D7
    def func_D7(df, P_AXD_1, ER_1):
        return P_AXD_1 / ER_1

    model_control_actions.at[5, 'after'] = model_control_actions['after'].pipe(func_D7,
                                                                               variables.at[28, 'new_pr'],
                                                                               model_control_actions.at[1, 'after'])

    # D8
    def func_D8(df, P_AMD_1, ER_1):
        return P_AMD_1 / ER_1

    model_control_actions.at[6, 'after'] = model_control_actions['after'].pipe(func_D8, variables.at[33, 'new_pr'],
                                                                               model_control_actions.at[1, 'after'])

    # D9
    def func_D9(df, P_IMD_1, ER_1):
        return P_IMD_1 / ER_1

    model_control_actions.at[7, 'after'] = model_control_actions['after'].pipe(func_D9, variables.at[24, 'new_pr'],
                                                                               model_control_actions.at[1, 'after'])

    # H25
    def func_H25(df, P_IPD_1, P_IPD_0):
        return P_IPD_1 / P_IPD_0 - 1

    variables.at[23, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H25, variables.at[23, 'new_pr'],
                                                                                variables.at[23, 'base_pr'])

    # I25
    def func_I25(df, Q_IPD_1, Q_IPD_0):
        return Q_IPD_1 / Q_IPD_0 - 1

    variables.at[23, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I25,
                                                                                      variables.at[23, 'new_quan'],
                                                                                      variables.at[23, 'base_quan'])

    # H26
    def func_H26(df, P_IMD_1, P_IMD_0):
        return P_IMD_1 / P_IMD_0 - 1

    variables.at[24, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H26, variables.at[24, 'new_pr'],
                                                                                variables.at[24, 'base_pr'])

    # I26
    def func_I26(df, Q_IMD_1, Q_IMD_0):
        return Q_IMD_1 / Q_IMD_0 - 1

    variables.at[24, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I26,
                                                                                      variables.at[24, 'new_quan'],
                                                                                      variables.at[24, 'base_quan'])

    # H27
    def func_H27(df, P_AID_1, P_AID_0):
        return P_AID_1 / P_AID_0 - 1

    variables.at[25, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H27, variables.at[25, 'new_pr'],
                                                                                variables.at[25, 'base_pr'])

    # I27
    def func_I27(df, Q_AID_1, Q_AID_0):
        return Q_AID_1 / Q_AID_0 - 1

    variables.at[25, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I27,
                                                                                      variables.at[25, 'new_quan'],
                                                                                      variables.at[25, 'base_quan'])

    # H28
    def func_H28(df, P_AVD_1, P_AVD_0):
        return P_AVD_1 / P_AVD_0 - 1

    variables.at[26, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H28, variables.at[26, 'new_pr'],
                                                                                variables.at[26, 'base_pr'])

    # I28
    def func_I28(df, Q_AVD_1, Q_AVD_0):
        return Q_AVD_1 / Q_AVD_0 - 1

    variables.at[26, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I28,
                                                                                      variables.at[26, 'new_quan'],
                                                                                      variables.at[26, 'base_quan'])

    # H29
    def func_H29(df, P_APD_1, P_APD_0):
        return P_APD_1 / P_APD_0 - 1

    variables.at[27, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H29, variables.at[27, 'new_pr'],
                                                                                variables.at[27, 'base_pr'])

    # I29
    def func_I29(df, Q_APD_1, Q_APD_0):
        return Q_APD_1 / Q_APD_0 - 1

    variables.at[27, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I29,
                                                                                      variables.at[27, 'new_quan'],
                                                                                      variables.at[27, 'base_quan'])

    # H30
    def func_H30(df, P_AXD_1, P_AXD_0):
        return P_AXD_1 / P_AXD_0 - 1

    variables.at[28, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H30, variables.at[28, 'new_pr'],
                                                                                variables.at[28, 'base_pr'])

    # I30
    def func_I30(df, Q_AXD_1, Q_AXD_0):
        return Q_AXD_1 / Q_AXD_0 - 1

    variables.at[28, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I30,
                                                                                      variables.at[28, 'new_quan'],
                                                                                      variables.at[28, 'base_quan'])

    # H31
    def func_H31(df, P_AXW_1, P_AXW_0):
        return P_AXW_1 / P_AXW_0 - 1

    variables.at[29, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H31, variables.at[29, 'new_pr'],
                                                                                variables.at[29, 'base_pr'])

    # I31
    def func_I31(df, Q_AXW_1, Q_AXW_0):
        return Q_AXW_1 / Q_AXW_0 - 1

    variables.at[29, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I31,
                                                                                      variables.at[29, 'new_quan'],
                                                                                      variables.at[29, 'base_quan'])

    # H32
    def func_H32(df, P_ADW_1, P_ADW_0):
        return P_ADW_1 / P_ADW_0 - 1

    variables.at[30, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H32, variables.at[30, 'new_pr'],
                                                                                variables.at[30, 'base_pr'])

    # I32
    def func_I32(df, Q_ADW_1, Q_ADW_0):
        return Q_ADW_1 / Q_ADW_0 - 1

    variables.at[30, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I32,
                                                                                      variables.at[30, 'new_quan'],
                                                                                      variables.at[30, 'base_quan'])

    # H33
    def func_H33(df, P_ASD_1, P_ASD_0):
        return P_ASD_1 / P_ASD_0 - 1

    variables.at[31, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H33, variables.at[31, 'new_pr'],
                                                                                variables.at[31, 'base_pr'])

    # I33
    def func_I33(df, Q_ASD_1, Q_ASD_0):
        return Q_ASD_1 / Q_ASD_0 - 1

    variables.at[31, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I33,
                                                                                      variables.at[31, 'new_quan'],
                                                                                      variables.at[31, 'base_quan'])

    # H34
    def func_H34(df, P_ATD_1, P_ATD_0):
        return P_ATD_1 / P_ATD_0 - 1

    variables.at[32, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H34, variables.at[32, 'new_pr'],
                                                                                variables.at[32, 'base_pr'])

    # I34
    def func_I34(df, Q_ATD_1, Q_ATD_0):
        return Q_ATD_1 / Q_ATD_0 - 1

    variables.at[32, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I34,
                                                                                      variables.at[32, 'new_quan'],
                                                                                      variables.at[32, 'base_quan'])

    # H35
    def func_H35(df, P_AMD_1, P_AMD_0):
        return P_AMD_1 / P_AMD_0 - 1

    variables.at[33, 'perc_change_price'] = variables['perc_change_price'].pipe(func_H35, variables.at[33, 'new_pr'],
                                                                                variables.at[33, 'base_pr'])

    # I35
    def func_I35(df, Q_AMD_1, Q_AMD_0):
        return Q_AMD_1 / Q_AMD_0 - 1

    variables.at[33, 'perc_change_quantity'] = variables['perc_change_quantity'].pipe(func_I35,
                                                                                      variables.at[33, 'new_quan'],
                                                                                      variables.at[33, 'base_quan'])

    result_to_front = {
        'table1': [
            {
                'id': '1',
                'title': model_control_actions.at[1, 'title'],
                'params': model_control_actions.at[1, 'designation'],
                'basebalance': round(model_control_actions.at[1, 'before'], 2),
                'newbalance': round(model_control_actions.at[1, 'after'], 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '2',
                'title': model_control_actions.at[2, 'title'],
                'params': model_control_actions.at[2, 'designation'],
                'basebalance': round(model_control_actions.at[2, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[2, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '3',
                'title': 'Мировая цена товара алюминий, USD',
                'params': model_control_actions.at[3, 'designation'],
                'basebalance': round(model_control_actions.at[3, 'before']),
                'newbalance': round(model_control_actions.at[3, 'after']),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '4',
                'title': 'Изменение мировой цены товара алюминий, USD',
                'params': model_control_actions.at[4, 'designation'],
                'basebalance': round(model_control_actions.at[4, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[4, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': 'Цена экспорта товара алюминий (без тарифа), USD',
                'params': model_control_actions.at[5, 'designation'],
                'basebalance': round(model_control_actions.at[5, 'before']),
                'newbalance': round(model_control_actions.at[5, 'after']),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '6',
                'title': 'Цена импорта товара алюминий (без тарифа), USD',
                'params': model_control_actions.at[6, 'designation'],
                'basebalance': round(model_control_actions.at[6, 'before']),
                'newbalance': round(model_control_actions.at[6, 'after']),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '7',
                'title': 'Цена импорта товара бокситы (без тарифа), USD',
                'params': model_control_actions.at[7, 'designation'],
                'basebalance': round(model_control_actions.at[7, 'before']),
                'newbalance':round(model_control_actions.at[7, 'after']),
                "editBase": 'true',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Экспортный тариф на товар алюминий, %',
                'params': model_control_actions.at[8, 'designation'],
                'basebalance': round(model_control_actions.at[8, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[8, 'after'] * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '9',
                'title': 'Импортный тариф на промежуточный товар бокситы, %',
                'params': model_control_actions.at[9, 'designation'],
                'basebalance': round(model_control_actions.at[9, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[9, 'after'] * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '10',
                'title': 'Импортный тариф на товар алюминий, %',
                'params': model_control_actions.at[10, 'designation'],
                'basebalance': round(model_control_actions.at[10, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[10, 'after'] * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '11',
                'title': model_control_actions.at[12, 'title'],
                'params': model_control_actions.at[12, 'designation'],
                'basebalance': round(model_control_actions.at[12, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[12, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '12',
                'title': model_control_actions.at[13, 'title'],
                'params': model_control_actions.at[13, 'designation'],
                'basebalance': round(model_control_actions.at[13, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[13, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '13',
                'title': model_control_actions.at[14, 'title'],
                'params': model_control_actions.at[14, 'designation'],
                'basebalance': round(model_control_actions.at[14, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[14, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '14',
                'title': model_control_actions.at[15, 'title'],
                'params': model_control_actions.at[15, 'designation'],
                'basebalance': round(model_control_actions.at[15, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[15, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '15',
                'title': model_control_actions.at[16, 'title'],
                'params': model_control_actions.at[16, 'designation'],
                'basebalance': round(model_control_actions.at[16, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[16, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '16',
                'title': model_control_actions.at[17, 'title'],
                'params': model_control_actions.at[17, 'designation'],
                'basebalance': round(model_control_actions.at[17, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[17, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '17',
                'title': model_control_actions.at[18, 'title'],
                'params': model_control_actions.at[18, 'designation'],
                'basebalance': round(model_control_actions.at[18, 'before'] * 100, 2),
                'newbalance': round(model_control_actions.at[18, 'after'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            }
        ],
        'finding_solution': 'solution',
        'table2': [
            {
                'id': '1',
                'title': 'Отечественное производство промежуточного товара бокситы',
                'params': variables.at[23, 'designation'],
                'basebalance_pr': round(variables.at[23, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[23, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[23, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[23, 'new_quan'], 2),
                'perc_change_price': round(variables.at[23, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[23, 'perc_change_quantity'] * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '2',
                'title': 'Импорт промежуточного товара бокситы',
                'params': variables.at[24, 'designation'],
                'basebalance_pr': round(variables.at[24, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[24, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[24, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[24, 'new_quan'], 2),
                'perc_change_price': round(variables.at[24, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[24, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '3',
                'title': 'Потребление отраслью алюминий промежуточного товара бокситы',
                'params': variables.at[25, 'designation'],
                'basebalance_pr': round(variables.at[25, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[25, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[25, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[25, 'new_quan'], 2),
                'perc_change_price': round(variables.at[25, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[25, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '4',
                'title': 'Потребление отраслью алюминий добавленной стоимости',
                'params': variables.at[26, 'designation'],
                'basebalance_pr': round(variables.at[26, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[26, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[26, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[26, 'new_quan'], 2),
                'perc_change_price': round(variables.at[26, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[26, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '5',
                'title': 'Отечественное производство алюминия',
                'params': variables.at[27, 'designation'],
                'basebalance_pr': round(variables.at[27, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[27, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[27, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[27, 'new_quan'], 2),
                'perc_change_price': round(variables.at[27, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[27, 'perc_change_quantity'] * 100, 2),
                "editBase": 'true',
                "editNew": 'true'
            },
            {
                'id': '6',
                'title': 'Отечественный экспорт алюминия',
                'params': variables.at[28, 'designation'],
                'basebalance_pr': round(variables.at[28, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[28, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[28, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[28, 'new_quan'], 2),
                'perc_change_price': round(variables.at[28, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[28, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '7',
                'title': 'Мировое производство (без отечественного экспорта) алюминия',
                'params': variables.at[29, 'designation'],
                'basebalance_pr': round(variables.at[29, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[29, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[29, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[29, 'new_quan'], 2),
                'perc_change_price': round(variables.at[29, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[29, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '8',
                'title': 'Мировое потребление алюминия',
                'params': variables.at[30, 'designation'],
                'basebalance_pr': round(variables.at[30, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[30, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[30, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[30, 'new_quan'], 2),
                'perc_change_price': round(variables.at[30, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[30, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            },
            {
                'id': '9',
                'title': 'Отечественное производство для внутреннего потребления алюминия',
                'params': variables.at[31, 'designation'],
                'basebalance_pr': round(variables.at[31, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[31, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[31, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[31, 'new_quan'], 2),
                'perc_change_price': round(variables.at[31, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[31, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '10',
                'title': 'Отечественное совокупное потребление алюминия',
                'params': variables.at[32, 'designation'],
                'basebalance_pr': round(variables.at[32, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[32, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[32, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[32, 'new_quan'], 2),
                'perc_change_price': round(variables.at[32, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[32, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'false'
            },
            {
                'id': '11',
                'title': 'Импорт товара алюминий',
                'params': variables.at[33, 'designation'],
                'basebalance_pr': round(variables.at[33, 'base_pr'], 2),
                'basebalance_quan': round(variables.at[33, 'base_quan'], 2),
                'newbalance_pr': round(variables.at[33, 'new_pr'], 2),
                'newbalance_quan': round(variables.at[33, 'new_quan'], 2),
                'perc_change_price': round(variables.at[33, 'perc_change_price'] * 100, 2),
                'perc_change_quantity': round(variables.at[33, 'perc_change_quantity'] * 100, 2),
                "editBase": 'false',
                "editNew": 'true'
            }
        ],
        'table3': [
            {
                'id': '1',
                'params': parameters.at[0, 'designation'],
                'value': round(parameters.at[0, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '2',
                'params': parameters.at[1, 'designation'],
                'value': round(parameters.at[1, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '3',
                'params': parameters.at[2, 'designation'],
                'value': round(parameters.at[2, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '4',
                'params': parameters.at[3, 'designation'],
                'value': round(parameters.at[3, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '5',
                'params': parameters.at[4, 'designation'],
                'value': round(parameters.at[4, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '6',
                'params': parameters.at[6, 'designation'],
                'value': round(parameters.at[6, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '7',
                'params': parameters.at[7, 'designation'],
                'value': round(parameters.at[7, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '8',
                'params': parameters.at[8, 'designation'],
                'value': round(parameters.at[8, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '9',
                'params': parameters.at[9, 'designation'],
                'value': round(parameters.at[9, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '10',
                'params': parameters.at[10, 'designation'],
                'value': round(parameters.at[10, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '11',
                'params': parameters.at[11, 'designation'],
                'value': round(parameters.at[11, 'values'], 1),
                "edit": 'true'
            },
            {
                'id': '12',
                'params': parameters.at[12, 'designation'],
                'value': round(parameters.at[12, 'values'], 1),
                "edit": 'true'
            }
        ]
    }

    return result_to_front


input_data = InputDataBase(example_data)
result = aluminum_market(input_data)
print(result)
