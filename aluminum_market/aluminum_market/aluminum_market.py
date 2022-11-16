import math
import numpy as np
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


user_data = {'ER_before': 72.795, 'ER_after': 72.795, 'WP_before': 2088.0, 'WP_after': 2088.0,
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
    print(model_control_actions.to_markdown())
    # Переменные
    variables = df.iloc[23:34, 0:9]
    variables = variables.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'designation',
                 'Базовое равновесие': 'base_pr',
                 'Новое равновесие': 'base_quan', 'Unnamed: 4': 'relative_quality', 'Unnamed: 5': 'new_pr',
                 'Unnamed: 6': 'new_quan', 'Параметры': 'perc_change_price', 'Unnamed: 8': 'perc_change_quantity'})
    print(variables.to_markdown())
    # Уравнения
    equations = df.iloc[36:61, 0:2]
    equations = equations.rename(
        columns={'Управляющие воздействия модели': 'title', 'Unnamed: 1': 'values'})

    # Параметры
    parameters = df.iloc[0:13, 7:10]
    parameters = parameters.rename(
        columns={'Параметры': 'designation', 'Unnamed: 8': 'values'})

    print(parameters.to_markdown())

    """Вводим новые значения"""

    model_control_actions.at[0, 'before'] = input_data.ER_before
    model_control_actions.at[0, 'after'] = input_data.ER_after
    model_control_actions.at[2, 'before'] = input_data.WP_before
    model_control_actions.at[2, 'after'] = input_data.WP_after
    model_control_actions.at[4, 'before'] = input_data.P_AXD_USD_before
    model_control_actions.at[5, 'before'] = input_data.P_AMD_USD_before
    model_control_actions.at[6, 'before'] = input_data.P_IMD_USD_before
    model_control_actions.at[7, 'before'] = input_data.TAXD_before
    model_control_actions.at[7, 'after'] = input_data.TAXD_after
    model_control_actions.at[8, 'before'] = input_data.TIMD_before
    model_control_actions.at[8, 'after'] = input_data.TIMD_after
    model_control_actions.at[9, 'before'] = input_data.TAMD_before
    model_control_actions.at[9, 'after'] = input_data.TAMD_after
    model_control_actions.at[11, 'after'] = input_data.SS_IPD_SUPPLY_after
    model_control_actions.at[12, 'after'] = input_data.DS_IMD_SUPPLY_after
    model_control_actions.at[13, 'after'] = input_data.SS_AVD_SUPPLY_after
    model_control_actions.at[14, 'after'] = input_data.DS_ADW_DEMAND_after
    model_control_actions.at[15, 'after'] = input_data.SS_AXW_SUPPLY_after
    model_control_actions.at[16, 'after'] = input_data.SS_AMD_SUPPLY_after
    model_control_actions.at[17, 'after'] = input_data.DS_ATD_DEMAND_after

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

    model_control_actions.at[1, 'after'] = model_control_actions['after'].pipe(func_DER_1,
                                                                               model_control_actions.at[0, 'after'],
                                                                               model_control_actions.at[0, 'before'])

    # DWP_CEL_1
    def func_DWP_CEL_1(df, WP_1, WP_0):
        return WP_1 / WP_0 - 1

    model_control_actions.at[3, 'after'] = model_control_actions['after'].pipe(func_DWP_CEL_1,
                                                                               model_control_actions.at[2, 'after'],
                                                                               model_control_actions.at[2, 'before'])

    # P_IMD_0
    def func_P_IMD_0(df, P_IMD_USD_0, ER_0):
        return P_IMD_USD_0 * ER_0

    variables.at[24, 'base_pr'] = variables['base_pr'].pipe(func_P_IMD_0, model_control_actions.at[6, 'before'],
                                                            model_control_actions.at[0, 'before'])
    # Q_AID_0
    def func_Q_AID_0(df, Q_IPD_0, Q_IMD_0):
        return Q_IPD_0 + Q_IMD_0

    variables.at[25, 'base_quan'] = variables['base_quan'].pipe(func_Q_AID_0, variables.at[23, 'base_quan'],
                                                                variables.at[24, 'base_quan'])

    # P_AID_0
    def func_P_AID_0(df, P_IPD_0, Q_IPD_0, P_IMD_0, Q_IMD_0, Q_AID_0):
        return (P_IPD_0*Q_IPD_0+P_IMD_0*Q_IMD_0)/Q_AID_0

    variables.at[25, 'base_pr'] = variables['base_pr'].pipe(func_P_AID_0, variables.at[23, 'base_pr'],
                                                            variables.at[23, 'base_quan'], variables.at[24, 'base_pr'],
                                                            variables.at[24, 'base_quan'], variables.at[25, 'base_quan'])

    # P_AVD_0
    def func_P_AVD_0(df, P_APD_0, Q_APD_0, P_AID_0, Q_AID_0, Q_AVD_0):
        return (P_APD_0*Q_APD_0-P_AID_0*Q_AID_0)/Q_AVD_0

    variables.at[26, 'base_pr'] = variables['base_pr'].pipe(func_P_AVD_0, variables.at[27, 'base_pr'],
                                                            variables.at[27, 'base_quan'], variables.at[25, 'base_pr'],
                                                            variables.at[25, 'base_quan'], variables.at[26, 'base_quan'])

    # P_AXD_0
    def func_P_AXD_0(df, P_AXD_USD_0, ER_0):
        return P_AXD_USD_0 * ER_0

    variables.at[28, 'base_pr'] = variables['base_pr'].pipe(func_P_AXD_0, model_control_actions.at[4, 'before'],
                                                            model_control_actions.at[0, 'before'])

    # Q_AXW_0
    def func_Q_AXW_0(df, Q_ADW_0, Q_AXD_0):
        return Q_ADW_0 - Q_AXD_0

    variables.at[29, 'base_quan'] = variables['base_quan'].pipe(func_Q_AXW_0, variables.at[30, 'base_quan'],
                                                                variables.at[28, 'base_quan'])

    # P_ADW_0
    def func_P_ADW_0(df, WP_0, ER_0):
        return WP_0*ER_0

    variables.at[30, 'base_pr'] = variables['base_pr'].pipe(func_P_ADW_0, model_control_actions.at[2, 'before'],
                                                            model_control_actions.at[0, 'before'])

    # P_AXW_0
    def func_P_AXW_0(df, P_ADW_0, Q_ADW_0, P_AXD_0, TAXD_0, Q_AXD_0, Q_AXW_0):
        return (P_ADW_0*Q_ADW_0-P_AXD_0*(1+TAXD_0)*Q_AXD_0)/Q_AXW_0

    variables.at[29, 'base_pr'] = variables['base_pr'].pipe(func_P_AXW_0, variables.at[30, 'base_pr'],
                                                            variables.at[30, 'base_quan'], variables.at[28, 'base_pr'],
                                                            model_control_actions.at[7, 'before'],
                                                            variables.at[28, 'base_quan'], variables.at[29, 'base_quan'])

    # Q_ASD_0
    def func_Q_ASD_0(df, Q_APD_0, Q_AXD_0):
        return Q_APD_0-Q_AXD_0

    variables.at[31, 'base_quan'] = variables['base_quan'].pipe(func_Q_ASD_0, variables.at[27, 'base_quan'],
                                                                variables.at[28, 'base_quan'])

    # P_ASD_0
    def func_P_ASD_0(df, P_APD_0, Q_APD_0, P_AXD_0, Q_AXD_0, Q_ASD_0):
        return (P_APD_0*Q_APD_0-P_AXD_0*Q_AXD_0)/Q_ASD_0

    variables.at[31, 'base_pr'] = variables['base_pr'].pipe(func_P_ASD_0, variables.at[27, 'base_pr'],
                                                            variables.at[27, 'base_quan'], variables.at[28, 'base_pr'],
                                                            variables.at[28, 'base_quan'], variables.at[31, 'base_quan'])
    # Q_ATD_0
    def func_Q_ATD_0(df, Q_ASD_0, Q_AMD_0):
        return Q_ASD_0+Q_AMD_0

    variables.at[32, 'base_quan'] = variables['base_quan'].pipe(func_Q_ATD_0, variables.at[31, 'base_quan'],
                                                                variables.at[33, 'base_quan'])

    # P_AMD_0
    def func_P_AMD_0(df, P_AMD_USD_0, ER_0):
        return P_AMD_USD_0*ER_0

    variables.at[33, 'base_pr'] = variables['base_pr'].pipe(func_P_AMD_0, model_control_actions.at[5, 'before'],
                                                            model_control_actions.at[0, 'before'])

    # P_ATD_0
    def func_P_ATD_0(df, P_ASD_0, Q_ASD_0, P_AMD_0, TAMD_0, Q_AMD_0, Q_ATD_0):
        return (P_ASD_0*Q_ASD_0+P_AMD_0*(1+TAMD_0)*Q_AMD_0)/Q_ATD_0

    variables.at[32, 'base_pr'] = variables['base_pr'].pipe(func_P_ATD_0, variables.at[31, 'base_pr'],
                                                            variables.at[31, 'base_quan'], variables.at[33, 'base_pr'],
                                                            model_control_actions.at[9, 'before'],
                                                            variables.at[33, 'base_quan'], variables.at[32, 'base_quan'])

    # r_σ_AID
    def func_r_σ_AID(df, σ_AID):
        return (σ_AID-1)/σ_AID

    parameters.at[0, 'rho'] = parameters['rho'].pipe(func_r_σ_AID, parameters.at[0, 'values'])

    # r_σ_APD
    def func_r_σ_APD(df, σ_APD):
        return (σ_APD-1)/σ_APD
    parameters.at[1, 'rho'] = parameters['rho'].pipe(func_r_σ_APD, parameters.at[1, 'values'])


    # r_Ω_APD
    def func_r_Ω_APD(df, Ω_APD):
        return (Ω_APD+1)/Ω_APD
    parameters.at[2, 'rho'] = parameters['rho'].pipe(func_r_Ω_APD, parameters.at[2, 'values'])

    # r_σ_ADW
    def func_r_σ_ADW(df, σ_ADW):
        return (σ_ADW-1)/σ_ADW

    parameters.at[3, 'rho'] = parameters['rho'].pipe(func_r_σ_ADW, parameters.at[3, 'values'])

    # r_σ_ATD
    def func_r_σ_ATD(df, σ_ATD):
        return (σ_ATD-1)/σ_ATD

    parameters.at[4, 'rho'] = parameters['rho'].pipe(func_r_σ_ATD, parameters.at[4, 'values'])

    # Z_IPD
    def func_Z_IPD(df, Q_IPD_0, P_IPD_0, ε_IPD):
        return Q_IPD_0/(P_IPD_0 ** ε_IPD)

    parameters.at[6, 'rho'] = parameters['rho'].pipe(func_Z_IPD, variables.at[23, 'base_quan'],
                                                     variables.at[23, 'base_pr'], parameters.at[6, 'values'])

    # Z_IMD
    def func_Z_IMD(df, Q_IMD_0, P_IMD_0, ER_0, ε_IMD):
        return Q_IMD_0/((P_IMD_0/ER_0) ** ε_IMD)

    parameters.at[7, 'rho'] = parameters['rho'].pipe(func_Z_IMD, variables.at[24, 'base_quan'],
                                                     variables.at[24, 'base_pr'], model_control_actions.at[0, 'before'],
                                                     parameters.at[7, 'values'])

    # Z_AVD
    def func_Z_AVD(df, Q_AVD_0, P_AVD_0, ε_AVD):
        return Q_AVD_0/(P_AVD_0) ** ε_AVD

    parameters.at[8, 'rho'] = parameters['rho'].pipe(func_Z_AVD, variables.at[26, 'base_quan'],
                                                     variables.at[26, 'base_pr'], parameters.at[8, 'values'])

    # Z_ADW
    def func_Z_ADW(df, Q_ADW_0, P_ADW_0, ER_0, ε_ADW):
        return Q_ADW_0/(P_ADW_0/ER_0) ** ε_ADW

    parameters.at[9, 'rho'] = parameters['rho'].pipe(func_Z_ADW, variables.at[30, 'base_quan'], variables.at[30, 'base_pr'],
                                                     model_control_actions.at[0, 'before'], parameters.at[9, 'values'])

    # Z_AXW
    def func_Z_AXW(df, Q_AXW_0, P_AXW_0, ER_0, ε_AXW):
        return Q_AXW_0/(P_AXW_0/ER_0) ** ε_AXW

    parameters.at[10, 'rho'] = parameters['rho'].pipe(func_Z_AXW, variables.at[29, 'base_quan'],
                                                      variables.at[29, 'base_pr'], model_control_actions.at[0, 'before'],
                                                      parameters.at[10, 'values'])

    # Z_AMD
    def func_Z_AMD(df, Q_AMD_0, P_AMD_0, ER_0, ε_AMD):
        return Q_AMD_0/(P_AMD_0/ER_0) ** ε_AMD

    parameters.at[11, 'rho'] = parameters['rho'].pipe(func_Z_AMD, variables.at[33, 'base_quan'],
                                                      variables.at[33, 'base_pr'], model_control_actions.at[0, 'before'],
                                                      parameters.at[11, 'values'])

    # Z_ATD
    def func_Z_ATD(df, Q_ATD_0, P_ATD_0, ε_ATD):
        return Q_ATD_0/(P_ATD_0) ** ε_ATD

    parameters.at[12, 'rho'] = parameters['rho'].pipe(func_Z_ATD, variables.at[32, 'base_quan'],
                                                      variables.at[32, 'base_pr'], parameters.at[12, 'values'])
    # K_IMD
    def func_K_IMD(df, Q_IMD_0, Q_IPD_0, r_σ_AID, P_IMD_0, TIMD_0, P_IPD_0):
        return ((Q_IMD_0/Q_IPD_0) ** (1-r_σ_AID))*(P_IMD_0*(1+TIMD_0)/P_IPD_0)

    variables.at[24, 'relative_quality'] = variables['relative_quality'].pipe(func_K_IMD, variables.at[24, 'base_quan'],
                                                variables.at[23, 'base_quan'], parameters.at[0, 'rho'],
                                                variables.at[24, 'base_pr'], model_control_actions.at[8, 'before'],
                                                                              variables.at[23, 'base_pr'])

    # K_AVD
    def func_K_AVD(df, Q_AVD_0, Q_AID_0, r_σ_APD, P_AVD_0, P_AID_0):
        return (Q_AVD_0/Q_AID_0) ** (1-r_σ_APD)*(P_AVD_0/P_AID_0)

    variables.at[26, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AVD, variables.at[26, 'base_quan'],
                                                                variables.at[25, 'base_quan'], parameters.at[1, 'rho'],
                                                                variables.at[26, 'base_pr'],variables.at[25, 'base_pr'])

    # K_AXD
    def func_K_AXD(df, Q_AXD_0, Q_ASD_0, r_Ω_APD, P_AXD_0, P_ASD_0):
        return (Q_AXD_0/Q_ASD_0) ** (1-r_Ω_APD)*(P_AXD_0/P_ASD_0)

    variables.at[28, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXD, variables.at[28, 'base_quan'],
                                                            variables.at[31, 'base_quan'], parameters.at[2, 'rho'],
                                                            variables.at[28, 'base_pr'], variables.at[31, 'base_pr'])

    # K_AXW
    def func_K_AXW(df, Q_AXW_0, Q_AXD_0, r_σ_ADW, P_AXW_0, P_AXD_0, TAXD_0, K_AXD):
        return (Q_AXW_0/Q_AXD_0) ** (1-r_σ_ADW)*(P_AXW_0/(P_AXD_0*(1+TAXD_0)))*K_AXD

    variables.at[29, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AXW, variables.at[29, 'base_quan'],
                                                                variables.at[28, 'base_quan'], parameters.at[3, 'rho'],
                                                                variables.at[29, 'base_pr'], variables.at[28, 'base_pr'],
                                            model_control_actions.at[7, 'before'], variables.at[28, 'relative_quality'])

    # K_AMD
    def func_K_AMD(df, Q_AMD_0, Q_ASD_0, r_σ_ATD, P_AMD_0, TAMD_0, P_ASD_0):
        return (Q_AMD_0/Q_ASD_0) ** (1-r_σ_ATD)*(P_AMD_0*(1+TAMD_0)/P_ASD_0)

    variables.at[33, 'relative_quality'] = variables['relative_quality'].pipe(func_K_AMD, variables.at[33, 'base_quan'],
                                                                variables.at[31, 'base_quan'], parameters.at[4, 'rho'],
                                                    variables.at[33, 'base_pr'], model_control_actions.at[10, 'before'],
                                                                              variables.at[31, 'base_pr'])



    # # D7
    # def func_D7(df, P_AXD_1, ER_1):
    #     return P_AXD_1 / ER_1
    #
    # model_control_actions.at[4, 'after'] = model_control_actions['after'].pipe(func_D7,
    #                                                                         variables.at[28, 'new_pr'],
    #                                                                         model_control_actions.at[0, 'after'])

input_data = InputDataBase(user_data)
result = aluminum_market(input_data)
# print(result)
