x = "{:.0%}".format(0 / 100)
print(x)

"""Переменные"""


class Variable:
    def __init__(self, MDI, FDP, FXP):
        # Потребление отечественной макулатуры
        self.MDI = MDI
        # Отечественное производство товара F
        self.FDP = FDP
        # Экспорт товара F
        self.FXP = FXP

    """Импорт товара M"""

    # Базовое равновесие
    def good_import(self,P_MMI_USD_0, ER_0,TMMI_0):
        P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
        return P_MMI_0
    # Новое равновесие
    P_MMI_1 = 7.80922017051985

    """Потребление отечественного товара M"""

    # Базовое равновесие
    P_MDI_0 = 15.139
    # Новое равновесие
    P_MDI_1 = 15.6016971682569

    """Потребление отраслью S товара M"""

    # Базовое равновесие
    def good_consumption(self, P_MDI_0,Q_MDI_0, P_MMI_0, Q_MMI_0,Q_MIC_0):
        P_MIC_0 = (P_MDI_0*Q_MDI_0+P_MMI_0*Q_MMI_0)/Q_MIC_0
        return P_MIC_0
    # Новое равновесие
    P_MIC_1 = 15.2713679199154

    """Отечественное производство S"""

    # Базовое равновесие
    def home_production(self, P_MIC_0, OUT_0, SVA_0):
        P_SDP_0 = P_MIC_0/OUT_0+SVA_0
        return P_SDP_0
    # Новое равновесие
    P_SDP_1 = 31.5196429313786

    """Отечественное потребление F"""

    # Базовое равновесие
    def home_consumption_f(self, P_FDP_0, Q_FDP_0, P_FXP_0, Q_FXP_0, Q_FDC_0):
        P_FDC_0 = (P_FDP_0*Q_FDP_0-P_FXP_0*Q_FXP_0)/Q_FDC_0
        return P_FDC_0
    # Новое равновесие
    P_FDC_1 = 35.8411597582987

    """Отечественное потребление P"""

    # Базовое равновесие
    def home_consumption_p(self, P_SDP_0, Q_SDP_0, P_FDC_0, Q_FDC_0, Q_PDP_0):
        P_PDP_0 = (P_SDP_0*Q_SDP_0+P_FDC_0*Q_FDC_0)/Q_PDP_0
        return P_PDP_0
    # Новое равновесие
    P_PDP_1 = 32.4979933332257

    """Нетто импорт P"""

    # Базовое равновесие
    def netto_import(self, P_MDI_0):
        P_PXM_0 = P_MDI_0
        return P_PXM_0
    # Новое равновесие
    P_PXM_1 = 15.6016971682569

    """Общее образование P"""

    # Базовое равновесие
    def general_education(self, P_MDI_0):
        P_PDC_0 = P_MDI_0
        return P_PDC_0
    # Новое равновесие
    P_PDC_1 = 15.6016971682569

    """Отечественное производство товара F"""

    # Базовое равновесие
    P_FDP_0 = 38
    # Новое равновесие
    P_FDP_1 = 44.03846291456

    """Экспорт товара F"""

    # Базовое равновесие
    P_FXP_0 = 42
    # Новое равновесие
    P_FXP_1 = 49.5402632412323

