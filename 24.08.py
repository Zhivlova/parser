from models import ModelControlActions
import math

# создаем экземпляр класса
table = ModelControlActions()


# получаем данные от пользователя - Базовое равновесие
class Input_data_base:
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


input_base = Input_data_base(72.14, 0.18, 1.29, 0.018906189062869,
                             14.686756, 0.8555, 15.139, 38, 42)


# получаем данные от пользователя - Новое равновесие
class Input_data_new:
    def __init__(self, ER_1, NMMI_1, TMMI_1):
        self.ER_1 = ER_1
        self.NMMI_1 = NMMI_1
        self.TMMI_1 = TMMI_1


input_new = Input_data_new(table.course(72.14), table.import_non_tariff_barrier(), table.import_tariff())


# получаем данные от пользователя - Количество
class Input_data_quantity:
    def __init__(self, Q_MMI_0, Q_MDI_0, Q_SDP_0, Q_FDC_0, Q_PDC_0, Q_FDP_0):
        self.Q_MMI_0 = Q_MMI_0
        self.Q_MDI_0 = Q_MDI_0
        self.Q_SDP_0 = Q_SDP_0
        self.Q_FDC_0 = Q_FDC_0
        self.Q_PDC_0 = Q_PDC_0
        self.Q_FDP_0 = Q_FDP_0


input_quantity = Input_data_quantity(42, 3876 - 54, 2999, 1006, 4186, 2125)

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

# """Общее убывание волокна"""
#
# # Базовое равновесие
# def basic_total_fiber_decrease(K_0, OUT_0, SH_0):
#     return K_0*OUT_0*SH_0