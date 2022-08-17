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

    # Базовое равновесие Цена (P), руб за кг
    def good_import(self,P_MMI_USD_0, ER_0,TMMI_0):
        P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
        return P_MMI_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_MMI_0 = 42

    # Новое равновесие Цена (P), руб за кг
    P_MMI_1 = 7.80922017051985
    # Новое равновесие Количество (Q) тыс. тонн
    Q_MMI_1 = 166.487602924277

    # Изменение (%) Цена (P)
    def perc_change_price_good_import(self, P_MMI_1, P_MMI_0):
        return P_MMI_1/P_MMI_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import(self, Q_MMI_1, Q_MMI_0)
        return Q_MMI_1/Q_MMI_0-1

    """Потребление отечественного товара M"""

    # Базовое равновесие
    P_MDI_0 = 15.139
    # Базовое равновесие Количество (Q) тыс. тонн
    def q_consumption_home_goods(self):
        Q_MDI_0 = 3876-54
        return Q_MDI_0

    # Новое равновесие
    P_MDI_1 = 15.6016971682569
    # Новое равновесие Количество (Q) тыс. тонн
    Q_MDI_1 = 3760.9600057833

    # Изменение (%) Цена (P)
    def perc_change_price_consumption_home_goods(self, P_MDI_1, P_MDI_0):
        return P_MDI_1/P_MDI_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_import_consumption_home_goods(self, Q_MDI_1, Q_MDI_0):
        return Q_MDI_1/Q_MDI_0-1

    """Потребление отраслью S товара M"""

    # Базовое равновесие
    def good_consumption(self, P_MDI_0,Q_MDI_0, P_MMI_0, Q_MMI_0,Q_MIC_0):
        P_MIC_0 = (P_MDI_0*Q_MDI_0+P_MMI_0*Q_MMI_0)/Q_MIC_0
        return P_MIC_0
    # Базовое равновесие Количество (Q) тыс. тонн
    def q_good_consumption(self, Q_MDI_0, Q_MMI_0):
        Q_MIC_0 = Q_MDI_0+Q_MMI_0
        return Q_MIC_0

    # Новое равновесие
    P_MIC_1 = 15.2713679199154
    # Новое равновесие Количество (Q) тыс. тонн
    Q_MIC_1 = 3927.44760870758

    # Изменение (%) Цена (P)
    def perc_change_price_good_consumption(self, P_MIC_1, P_MIC_0):
        return P_MIC_1/P_MIC_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_good_consumption(self, Q_MIC_1, Q_MIC_0)
        return Q_MIC_1/Q_MIC_0-1

    """Отечественное производство S"""

    # Базовое равновесие
    def home_production(self, P_MIC_0, OUT_0, SVA_0):
        P_SDP_0 = P_MIC_0/OUT_0+SVA_0
        return P_SDP_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_SDP_0 = 2999

    # Новое равновесие Цена (P), руб за кг
    P_SDP_1 = 31.5196429313786
    # Новое равновесие Количество (Q) тыс. тонн
    Q_SDP_1 = 3048,24414557817

    # Изменение (%) Цена (P)
    def perc_change_price_home_production(self, P_SDP_1, P_SDP_0):
        return P_SDP_1/P_SDP_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production(self, Q_SDP_1, Q_SDP_0)
        return Q_SDP_1/Q_SDP_0-1

    """Отечественное потребление F"""

    # Базовое равновесие
    def home_consumption_f(self, P_FDP_0, Q_FDP_0, P_FXP_0, Q_FXP_0, Q_FDC_0):
        P_FDC_0 = (P_FDP_0*Q_FDP_0-P_FXP_0*Q_FXP_0)/Q_FDC_0
        return P_FDC_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_FDC_0 = 1006

    # Новое равновесие Цена (P), руб за кг
    P_FDC_1 = 35.8411597582987
    # Новое равновесие Количество (Q) тыс. тонн
    Q_FDC_1 = 892.04380089303

    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_f(self, P_FDC_1, P_FDC_0):
        return P_FDC_1/P_FDC_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_f(self, Q_FDC_1, Q_FDC_0)
        return Q_FDC_1/Q_FDC_0-1

    """Отечественное потребление P"""

    # Базовое равновесие Цена (P), руб за кг
    def home_consumption_p(self, P_SDP_0, Q_SDP_0, P_FDC_0, Q_FDC_0, Q_PDP_0):
        P_PDP_0 = (P_SDP_0*Q_SDP_0+P_FDC_0*Q_FDC_0)/Q_PDP_0
        return P_PDP_0
    # Базовое равновесие Количество (Q) тыс. тонн
    def q_home_consumption_p(self, Q_SDP_0, Q_FDC_0):
        Q_PDP_0 = Q_SDP_0+Q_FDC_0
        return Q_PDP_0

    # Новое равновесие Цена (P), руб за кг
    P_PDP_1 = 32.4979933332257
    # Новое равновесие Количество (Q) тыс. тонн
    Q_PDP_1 = 3940.2879464712

    # Изменение (%) Цена (P)
    def perc_change_price_home_consumption_p(self, P_PDP_1,P_PDP_0):
        return P_PDP_1/P_PDP_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_consumption_p(self, Q_PDP_1, Q_PDP_0)
        return Q_PDP_1/Q_PDP_0-1


    """Нетто импорт P"""

    # Базовое равновесие Цена (P), руб за кг
    def netto_import(self, P_MDI_0):
        P_PXM_0 = P_MDI_0
        return P_PXM_0
    # Базовое равновесие Количество (Q) тыс. тонн
    def q_netto_import(self, Q_PDC_0, Q_PDP_0):
        Q_PXM_0 = Q_PDC_0-Q_PDP_0
        return Q_PXM_0

    # Новое равновесие Цена (P), руб за кг
    P_PXM_1 = 15.6016971682569
    # Новое равновесие Количество (Q) тыс. тонн
    Q_PXM_1 = 150.833333333333

    # Изменение (%) Цена (P)
    def perc_change_price_netto_import(self, P_PXM_1, P_PXM_0):
        return P_PXM_1/P_PXM_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_netto_import(self, Q_PXM_1, Q_PXM_0)
        return Q_PXM_1/Q_PXM_0-1

    """Общее образование P"""

    # Базовое равновесие Цена (P), руб за кг
    def general_education(self, P_MDI_0):
        P_PDC_0 = P_MDI_0
        return P_PDC_0
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_PDC_0 = 4186

    # Новое равновесие Цена (P), руб за кг
    P_PDC_1 = 15.6016971682569
    # Новое равновесие Количество (Q) тыс. тонн
    Q_PDC_1 = 4091.12127980453

    # Изменение (%) Цена (P)
    def perc_change_price_general_education(self, P_PDC_1, P_PDC_0):
        return P_PDC_1/P_PDC_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_general_education(self, Q_PDC_1, Q_PDC_0)
        return Q_PDC_1/Q_PDC_0-1

    """Отечественное производство товара F"""

    # Базовое равновесие Цена (P), руб за кг
    P_FDP_0 = 38
    # Базовое равновесие Количество (Q) тыс. тонн
    Q_FDP_0 = 2125

    # Новое равновесие Цена (P), руб за кг
    P_FDP_1 = 44.03846291456
    # Новое равновесие Количество (Q) тыс. тонн
    Q_FDP_1 = 2221,1275608247

    # Изменение (%) Цена (P)
    def perc_change_price_home_production(self, P_FDP_1, P_FDP_0):
        return P_FDP_1/P_FDP_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_home_production(self, Q_FDP_1, Q_FDP_0)
        return Q_FDP_1/Q_FDP_0-1

    """Экспорт товара F"""

    # Базовое равновесие Цена (P), руб за кг
    P_FXP_0 = 42
    # Базовое равновесие Количество (Q) тыс. тонн
    def export_goods(self, Q_FDP_0, Q_FDC_0):
        Q_FXP_0 = Q_FDP_0-Q_FDC_0
        return Q_FXP_0

    # Новое равновесие Цена (P), руб за кг
    P_FXP_1 = 49.5402632412323
    # Новое равновесие Количество (Q) тыс. тонн
    Q_FXP_1 = 1329.08375993167

    # Изменение (%) Цена (P)
    def perc_change_price_export_goodsself (self, P_FXP_1, P_FXP_0):
        return P_FXP_1/P_FXP_0-1
    # Изменение (%) Количество (Q)
    def perc_change_quantity_export_goods(self, Q_FXP_1, Q_FXP_0)
        return Q_FXP_1/Q_FXP_0-1


