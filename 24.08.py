import math

"""Управляющие воздействия модели"""

class ModelControlActions:
    """Курс RUB/USD"""
    # Базовое равновесие
    ER_0 = 72.14
    # Новое равновесие Курс RUB/USD
    def ER_1(self, ER_0):
        ER_1 = ER_0 * 1.2
        return ER_1
# создаем экземпляр класса
table = ModelControlActions()


# получаем данные от пользователя - Базовое равновесие
class InputDataBase:
    def __init__(self, ER_0, P_MMI_USD_0, NMMI_0, TMMI_0, SVA_0, SH_0, P_MDI_0, P_FDP_0, P_FXP_0):
        self.ER_0 = ER_0
        self.P_MMI_USD_0 = P_MMI_USD_0
        self.NMMI_0 = NMMI_0
        self.TMMI_0 = TMMI_0
        self.SVA_0 = SVA_0
        self.SH_0 = SH_0
        self.P_MDI_0 = P_MDI_0
        self.P_FDP_0 = P_FDP_0
        self.P_FXP_0 = P_FXP_0

input_base = InputDataBase(72.14, 0.18, 1.29, 0.0189061890628692,
                             14.686756, 0.8555, 15.139, 38, 42)


# получаем данные от пользователя - Новое равновесие
class InputDataNew:
    def __init__(self, ER_1, NMMI_1, TMMI_1):
        self.ER_1 = ER_1
        self.NMMI_1 = NMMI_1
        self.TMMI_1 = TMMI_1

input_new = InputDataNew(table.ER_1(72.14), 0, 0)


# получаем данные от пользователя - Количество
class InputDataQuantity:
    def __init__(self, Q_MMI_0, Q_MDI_0, Q_SDP_0, Q_FDC_0, Q_PDC_0, Q_FDP_0):
        self.Q_MMI_0 = Q_MMI_0
        self.Q_MDI_0 = Q_MDI_0
        self.Q_SDP_0 = Q_SDP_0
        self.Q_FDC_0 = Q_FDC_0
        self.Q_PDC_0 = Q_PDC_0
        self.Q_FDP_0 = Q_FDP_0

input_quantity = InputDataQuantity(42, 3876 - 54, 2999, 1006, 4186, 2125)

"""Собираемость макулатуры"""

# Базовое равновесие
def K_0(Q_MDI_0, Q_PDC_0):
    K_0 = Q_MDI_0 / Q_PDC_0
    return K_0

K_0 = K_0(input_quantity.Q_MDI_0, input_quantity.Q_PDC_0)
print(f'K_0 = {K_0}')

"""Нормировочная цена для собираемости макулатуры"""

# Базовое равновесие
def Λ_0(P_MDI_0, K_0):
    Λ_0 = -P_MDI_0 / math.log(1 - K_0)
    return Λ_0

Λ_0 = Λ_0(input_base.P_MDI_0, K_0)
print(f'Λ_0 = {Λ_0}')

# Новое равновесие
Λ_1 = Λ_0
print(f'Λ_1 = {Λ_1}')

"""Прочие переменные издержки производства макулатурного картона (руб./кг)"""
# Новое равновесие
SVA_1 = input_base.SVA_0
print(f'SVA_1 = {SVA_1}')

"""Доля собираемой макулатуры для производства картона"""
# Новое равновесие
SH_1 = input_base.SH_0
print(f'SH_1 = {SH_1}')

"""Потребление отраслью S товара M"""
# Базовое равновесие Количество (Q) тыс. тонн
def Q_MIC_0(Q_MDI_0, Q_MMI_0):
    Q_MIC_0 = Q_MDI_0+Q_MMI_0
    return Q_MIC_0

Q_MIC_0 = Q_MIC_0(input_quantity.Q_MDI_0, input_quantity.Q_MMI_0)
print(f'Q_MIC_0 = {Q_MIC_0}')

"""Выход продукции из макулатуры"""

# Базовое равновесие
def OUT_0(Q_SDP_0, Q_MIC_0, SH_0):
    OUT_0 = Q_SDP_0/(Q_MIC_0*SH_0)
    return OUT_0
OUT_0 = OUT_0(input_quantity.Q_SDP_0, Q_MIC_0, input_base.SH_0)
print(f'OUT_0 = {OUT_0}')
# Новое равновесие
OUT_1 = OUT_0
print(f'OUT_1 = {OUT_1}')

"""Общее убывание волокна"""

# Базовое равновесие
def basic_total_fiber_decrease(K_0, OUT_0, SH_0):
    return K_0*OUT_0*SH_0
basic_total_fiber_decrease = basic_total_fiber_decrease(K_0, OUT_0, input_base.SH_0)
print(f'Общее убывание волокна  {basic_total_fiber_decrease}')

"""Потребление отечественного товара M"""
# Новое равновесие
P_MDI_1 = 15.6016971682569
print(f'P_MDI_1 = {P_MDI_1}')

"""Собираемость макулатуры"""
# Новое равновесие
def K_1(P_MDI_1, Λ_1):
    K_1 = (1-math.exp(-P_MDI_1/Λ_1))
    return K_1
K_1 = K_1(P_MDI_1, Λ_1)
print(f'K_1 = {K_1}')

"""Общее убывание волокна"""
# Новое равновесие
def new_total_fiber_decrease(K_1, OUT_1, SH_1):
    return K_1*OUT_1*SH_1
new_total_fiber_decrease = new_total_fiber_decrease(K_1, OUT_1, SH_1)
print(f'Общее убывание волокна {new_total_fiber_decrease}')

print('______________________________________________________________')

def calc(user_values):

    result = dict()
    ER_0 = user_values[0]
    result['ER_0'] = ER_0
    print(f' от пользователя получено значение ER_0  {ER_0}')


    ER_1 = ER_0 * 1.2
    result['ER_1'] = ER_1

    P_MMI_USD_0 = user_values[1]
    print(f' от пользователя получено значение P_MMI_USD_0  {P_MMI_USD_0}')
    result['P_MMI_USD_0'] = P_MMI_USD_0

    NMMI_0 = user_values[2]
    print(f' от пользователя получено значение NMMI_0  {NMMI_0}')
    result['NMMI_0'] = NMMI_0
    NMMI_1 = 0
    result['NMMI_1'] = NMMI_1
    
    TMMI_0 = user_values[3]
    print(f' от пользователя получено значение TMMI_0  {TMMI_0}')
    result['TMMI_0'] = TMMI_0
    TMMI_1 = 0
    result['TMMI_1'] = TMMI_1

    SVA_0 = user_values[4]
    print(f' от пользователя получено значение SVA_0  {SVA_0}')
    result['SVA_0'] = SVA_0

    SVA_1 = SVA_0
    result['SVA_1'] = SVA_1

    SH_0 = user_values[5]
    print(f' от пользователя получено значение SH_0  {SH_0}')
    result['SH_0'] = SH_0

    P_MDI_0 = user_values[6]
    print(f' от пользователя получено значение P_MDI_0  {P_MDI_0}')
    result['P_MDI_0'] = P_MDI_0

    P_FDP_0 = user_values[7]
    print(f' от пользователя получено значение P_FDP_0  {P_FDP_0}')
    result['P_FDP_0'] = P_FDP_0

    P_FXP_0 = user_values[8]
    print(f' от пользователя получено значение P_FXP_0  {P_FXP_0}')
    result['P_FXP_0'] = P_FXP_0

    Q_MMI_0 = user_values[9]
    print(f' от пользователя получено значение Q_MMI_0  {Q_MMI_0}')
    result['Q_MMI_0'] = Q_MMI_0

    Q_MDI_0 = user_values[10]
    print(f' от пользователя получено значение Q_MDI_0  {Q_MDI_0}')
    result['Q_MDI_0'] = Q_MDI_0

    Q_SDP_0 =  user_values[11]
    print(f' от пользователя получено значение Q_SDP_0  {Q_SDP_0}')
    result['Q_SDP_0'] = Q_SDP_0

    Q_FDC_0 = user_values[12]
    print(f' от пользователя получено значение Q_FDC_0  {Q_FDC_0}')
    result['Q_FDC_0'] = Q_FDC_0

    Q_PDC_0 = user_values[13]
    print(f' от пользователя получено значение Q_PDC_0  {Q_PDC_0}')
    result['Q_PDC_0'] = Q_PDC_0

    K_0 = Q_MDI_0 / Q_PDC_0
    result['K_0'] = K_0

    Λ_0 = -P_MDI_0 / math.log(1 - K_0)
    result['Λ_0'] = Λ_0

    Λ_1 = Λ_0
    result['Λ_1'] = Λ_1

    print(result)
user_values = [72.14, 0.18, 1.29, 0.0189061890628692, 14.686756, 0.8555, 15.139, 38, 42, 42, 3822, 2999, 1006,
               4186, 2125]
calc(user_values)