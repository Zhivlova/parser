from models import ModelControlActions

table = ModelControlActions()

input_data_base = {'ER_0': 72.14,
                   'P_MMI_USD_0': 0.18,
                   'NMMI_0': "{:.0%}".format(129 / 100),
                   'TMMI_0': "{:.14%}".format(1.89061890628692 / 100),
                   'SVA_0': 14.686756,
                   'SH_0': "{:.2%}".format(85.55 / 100),
                   'P_MDI_0': 15.139,
                   'P_FDP_0': 38,
                   'P_FXP_0': 42}

input_data_new = {'ER_1': table.course(72.14),
                  'NMMI_1': table.import_non_tariff_barrier(),
                  'TMMI_1': table.import_tariff()
                  }


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
def calc_basic_waste_paper_collection(Q_MDI_0, Q_PDC_0):
    K_0 = Q_MDI_0 / Q_PDC_0
    return K_0

K_0 = (calc_basic_waste_paper_collection(input_quantity.Q_MDI_0, input_quantity.Q_PDC_0))
print(K_0)
# Новое равновесие
def new_waste_paper_collection(self, -P_MDI_1, Λ_1):
    K_1 = (1 - EXP(-P_MDI_1 / Λ_1))
    return K_1