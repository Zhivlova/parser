import math
from scipy.optimize import fsolve
from sympy import exp
from math import fsum, sqrt

example_data = {'PW_A_const_before': 228.0, 'PW_A_shift_before': 0.0, 'PW_A_shift_after': 0.0, 'ER_before': 72.32,
                'ER_after': 72.32, 'CT_before': 59.0, 'TD_before': 0.0, 'TD_after': 0.0, 'Pb_before': 15000.0,
                'Pb_after': 15000.0, 'Pb2_before': 375.0, 'Pb2_after': 375.0,
                'Pb3_before': 400.0, 'Pb3_after': 400.0, 't1_before': 0.0, 't1_after': 0.7, 't2_before': 0.8,
                't2_after': 0.8, 't3_before': 0.9, 't3_after': 0.9, 'demp_before': 0.1, 'demp_after': 0.1,
                'QSI_A_before': 76.882, 'i_cost_before': 1.0, 'i_cost_after': 1.0, 'shift_QSI_A_before': 0.0,
                'shift_QSI_A_after': 0.0, 'QDI_С1_before': 14.03, 'QDI_A_C1_before': 15.129,
                'SpI_C1_before': 1883521.0, 'QDI_С2_before': 13.297, 'QDI_A_C2_before': 17.736,
                'SpI_C2_before': 3505628.0, 'QS_exRUS_A_before': 678.67, 'QD_A_before': 191.191,
                'QD_exRUS_A_before': 524.002, 'shift_QSW_A_before': 0.0, 'shift_QSW_A_after': 0.0,
                'i_cost_world_before': 1.0, 'i_cost_world_after': 1.0}

class InputDataBase:
    def __init__(self, dict_from_frontend):
        self.PW_A_const_before = float(dict_from_frontend.get('PW_A_const_before'))
        self.PW_A_shift_before = float(dict_from_frontend.get('PW_A_shift_before'))
        self.PW_A_shift_after = float(dict_from_frontend.get('PW_A_shift_after'))
        self.ER_before = float(dict_from_frontend.get('ER_before'))
        self.ER_after = float(dict_from_frontend.get('ER_after'))
        self.CT_before = float(dict_from_frontend.get('CT_before'))
        self.TD_before = float(dict_from_frontend.get('TD_before'))
        self.TD_after = float(dict_from_frontend.get('TD_after'))
        self.Pb_before = float(dict_from_frontend.get('Pb_before'))
        self.Pb_after = float(dict_from_frontend.get('Pb_after'))
        self.Pb2_before = float(dict_from_frontend.get('Pb2_before'))
        self.Pb2_after = float(dict_from_frontend.get('Pb2_after'))
        self.Pb3_before = float(dict_from_frontend.get('Pb3_before'))
        self.Pb3_after = float(dict_from_frontend.get('Pb3_after'))
        self.t1_before = float(dict_from_frontend.get('t1_before'))
        self.t1_after = float(dict_from_frontend.get('t1_after'))
        self.t2_before = float(dict_from_frontend.get('t2_before'))
        self.t2_after = float(dict_from_frontend.get('t2_after'))
        self.t3_before = float(dict_from_frontend.get('t3_before'))
        self.t3_after = float(dict_from_frontend.get('t3_after'))
        self.demp_before = float(dict_from_frontend.get('demp_before'))
        self.demp_after = float(dict_from_frontend.get('demp_after'))
        self.QSI_A_before = float(dict_from_frontend.get('QSI_A_before'))
        self.i_cost_before = float(dict_from_frontend.get('i_cost_before'))
        self.i_cost_after = float(dict_from_frontend.get('i_cost_after'))
        self.shift_QSI_A_before = float(dict_from_frontend.get('shift_QSI_A_before'))
        self.shift_QSI_A_after = float(dict_from_frontend.get('shift_QSI_A_after'))
        self.QDI_С1_before = float(dict_from_frontend.get('QDI_С1_before'))
        self.QDI_A_C1_before = float(dict_from_frontend.get('QDI_A_C1_before'))
        self.SpI_C1_before = float(dict_from_frontend.get('SpI_C1_before'))
        self.QDI_С2_before = float(dict_from_frontend.get('QDI_С2_before'))
        self.QDI_A_C2_before = float(dict_from_frontend.get('QDI_A_C2_before'))
        self.SpI_C2_before = float(dict_from_frontend.get('SpI_C2_before'))
        self.QS_exRUS_A_before = float(dict_from_frontend.get('QS_exRUS_A_before'))
        self.QD_A_before = float(dict_from_frontend.get('QD_A_before'))
        self.QD_exRUS_A_before = float(dict_from_frontend.get('QD_exRUS_A_before'))
        self.shift_QSW_A_before = float(dict_from_frontend.get('shift_QSW_A_before'))
        self.shift_QSW_A_after = float(dict_from_frontend.get('shift_QSW_A_after'))
        self.i_cost_world_before = float(dict_from_frontend.get('i_cost_world_before'))
        self.i_cost_world_after = float(dict_from_frontend.get('i_cost_world_after'))

def wheat_exports(input_data):
    PW_A_const_before = input_data.PW_A_const_before
    PW_A_shift_before = input_data.PW_A_shift_before
    PW_A_shift_after = input_data.PW_A_shift_after
    ER_before = input_data.ER_before
    ER_after = input_data.ER_after
    CT_before = input_data.CT_before
    TD_before = input_data.TD_before
    TD_after = input_data.TD_after
    Pb_before = input_data.Pb_before
    Pb_after = input_data.Pb_after
    Pb2_before = input_data.Pb2_before
    Pb2_after = input_data.Pb2_after
    Pb3_before = input_data.Pb3_before
    Pb3_after = input_data.Pb3_after
    t1_before = input_data.t1_before
    t1_after = input_data.t1_after
    t2_before = input_data.t2_before
    t2_after = input_data.t2_after
    t3_before = input_data.t3_before
    t3_after = input_data.t3_after
    demp_before = input_data.demp_before
    demp_after = input_data.demp_after
    QSI_A_before = input_data.QSI_A_before
    i_cost_before = input_data.i_cost_before
    i_cost_after = input_data.i_cost_after
    shift_QSI_A_before = input_data.shift_QSI_A_before
    shift_QSI_A_after = input_data.shift_QSI_A_after
    QDI_С1_before = input_data.QDI_С1_before
    QDI_A_C1_before = input_data.QDI_A_C1_before
    SpI_C1_before = input_data.SpI_C1_before
    QDI_С2_before = input_data.QDI_С2_before
    QDI_A_C2_before = input_data.QDI_A_C2_before
    SpI_C2_before = input_data.SpI_C2_before
    QS_exRUS_A_before = input_data.QS_exRUS_A_before
    QD_A_before = input_data.QD_A_before
    QD_exRUS_A_before = input_data.QD_exRUS_A_before
    shift_QSW_A_before = input_data.shift_QSW_A_before
    shift_QSW_A_after = input_data.shift_QSW_A_after
    i_cost_world_before = input_data.i_cost_world_before
    i_cost_world_after = input_data.i_cost_world_after

    I3 = 228.79869150023526
    B7 = 0.24
    B8 = -0.736
    B9 = -0.5
    B10 = 0.245
    B11 = -0,305

    H5 = PW_A_shift_before + PW_A_const_before

    I5 = PW_A_shift_after + I3

    I7 = CT_before

    H17 = (H5 * ER_before - Pb_before) * t1_before

    I17 = (I5 * ER_after - Pb_after) * t1_after

    H18 = (H5 - Pb2_before) * ER_before * t2_before + (Pb2_before * ER_before-Pb_before) * t1_before

    I18 = (I5 - Pb2_after) * ER_after * t2_after + (Pb2_after * ER_after - Pb_after) * t1_after

    H19 = (H5 - Pb3_before) * ER_before * t3_before + (Pb3_before - Pb2_before) * ER_before * t2_before + \
          (Pb2_before * ER_before - Pb_before) * t1_before

    I19 = (I5 - Pb3_after) * ER_after * t3_after + (Pb3_after - Pb2_after) * ER_after * t2_after + \
          (Pb2_after * ER_after - Pb_after) * t1_after

    def func_h20(H5, Pb2_before, H17, Pb3_before, H18, H19):
        if H5 < Pb2_before:
            H20 = H17
        elif H5 < Pb3_before:
            H20 = H18
        else:
            H20 = H19
        return H20
    H20 = func_h20(H5, Pb2_before, H17, Pb3_before, H18, H19)

    def func_i20(I3, Pb2_after, I17, Pb3_after, I18, I19):
        if I3 < Pb2_after:
            I20 = I17
        elif I3 < Pb3_after:
            I20 = I18
        else:
            I20 = I19
        return I20

    I20 = func_i20(I3, Pb2_after, I17, Pb3_after, I18, I19)

    H21 = H20 / (H5 * ER_before)

    I21 = I20/(I5 * ER_after)

    H24 = ((H5 - CT_before) * ER_before - H20) * (1 - TD_before)

    I24 = ((I5-I7)*ER_after-I20)*(1-TD_after)

    H38 = QDI_A_C1_before / QDI_С1_before

    I38 = H38

    H47 = QDI_A_C2_before / QDI_С2_before

    I47 = H47

    H53 = QSI_A_before * 0.098

    H54 = H53 + QDI_С2_before * H47 + QDI_С1_before * H38

    H55 = QSI_A_before - H54

    H26 = H24 + H20 * H55 / QSI_A_before * demp_before

    I26 = I24 + I20 * H55 / QSI_A_before * demp_after

    H32 = QSI_A_before / (1 + shift_QSI_A_before)/(H26 / i_cost_before) ** B7

    I29 = H32 * (1 + shift_QSI_A_after) * (I26 / i_cost_after) ** B7

    H41 = SpI_C1_before / QDI_С1_before

    H36 = QDI_С1_before / (H41 ** B8)

    H39 = H41 - H38 * H24

    I39 = H39

    I53 = I29 * 0.098

    I41 = I38 * I24 + I39

    I35 = H36 * (I41) ** B8

    I37 = I35 * I38

    I40 = I35 * I41

    H50 = SpI_C2_before / QDI_С2_before

    H45 = QDI_С2_before / (H50 ** B9)

    H48 = H50 - H47 * H24

    I48 = H48

    I50 = I47*I24+I48

    I44 = H45 * (I50) ** B9

    I46 = I44 * I47

    I49 = I44 * I50

    I54 = I53 + I44 * I47 + I35 * I38

    I55 = I29 - I54

    H61 = QS_exRUS_A_before - QD_exRUS_A_before

    H62 = QS_exRUS_A_before / (1 + shift_QSW_A_before) / ((H5-CT_before) / i_cost_world_before) ** B10

    I58 = H62 * (1 + shift_QSW_A_after) * ((I5 - I7) / i_cost_world_after) ** B10

    H63 = QD_A_before / H5 ** B11

    I59 = H63 * I3 ** B11

    H64 = QD_exRUS_A_before / H5 ** B11

    I60 = H64 * I3 ** B11

    I61 = I58 - I60

    H65 = H55 + H61

    I65 = I55 + I61

    H68 = I59 - I65

    I68 = I59 - I65


















input_data = InputDataBase(example_data)
result = wheat_exports(input_data)
print(result)



