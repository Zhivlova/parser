import pandas as pd

"""Управляющие воздействия модели"""

class ModelControlActions:

    def __init__(self, ER, P_MMI_USD, NMMI, TMMI, SVA, SH):
        # Курс RUB/USD
        self.ER = ER
        # Цена импорта товара M USD (без тарифа), долл. США за кг
        self.P_MMI_USD = P_MMI_USD
        # Импортный нетарифный барьер на товар M
        self.NMMI = NMMI
        # Импортный тариф на товар M
        self.TMMI = TMMI
        # Прочие переменные издержки производства макулатурного картона (руб./кг)
        self.SVA = SVA
        # Доля собираемой макулатуры для производства картона
        self.SH = SH

    """Курс RUB/USD"""

    # Базовое равновесие
    ER_0 = 72.14
    # Новое равновесие Курс RUB/USD
    def course(self, ER_0):
        ER_1 = ER_0 * 1.2
        return ER_1

    """Цена импорта товара M USD (без тарифа), долл. США за кг"""

    # Базовое равновесие
    P_MMI_USD_0 = 0.18

    """Импортный нетарифный барьер на товар M"""

    # Базовое равновесие
    NMMI_0 = "{:.0%}".format(129 / 100)
    # Новое равновесие
    def import_non_tariff_barrier(self):
        NMMI_1 = "{:.0%}".format(0 / 100)
        return NMMI_1

    """Импортный тариф на товар M"""

    # Базовое равновесие
    TMMI_0 = "{:.14%}".format(1.89061890628692 / 100)
    # Новое равновесие
    def import_tariff(self):
        TMMI_1 = "{:.0%}".format(0 / 100)
        return TMMI_1

    """Собираемость макулатуры"""

    # Базовое равновесие
    def basic_waste_paper_collection(self, Q_MDI_0, Q_PDC_0):
        K_0 = Q_MDI_0 / Q_PDC_0
        return K_0

    # Новое равновесие
    def new_waste_paper_collection(self, -P_MDI_1, Λ_1):
        K_1 = (1 - EXP(-P_MDI_1 / Λ_1))
        return K_1

    """Нормировочная цена для собираемости макулатуры"""

    # Базовое равновесие
    def basic_rationing_price(self, -P_MDI_0, K_0):
        Λ_0 = -P_MDI_0 / LN(1 - K_0)
        return Λ_0

    # Новое равновесие
    def new_rationing_price(self, Λ_0):
        Λ_1 = Λ_0
        return Λ_1

    """Прочие переменные издержки производства макулатурного картона (руб./кг)"""

    # Базовое равновесие
    SVA_0 = 14.686756

    # Новое равновесие
    def SVA_1(self,SVA_0):
        SVA_1 = SVA_0
        return SVA_1

    """Выход продукции из макулатуры"""

    # Базовое равновесие
    def basic_output_of_waste(self, Q_SDP_0, Q_MIC_0, SH_0):
        OUT_0 = Q_SDP_0 / (Q_MIC_0 * SH_0)
        return OUT_0

    # Новое равновесие
    def new_output_of_waste(self, OUT_0):
        OUT_1 = OUT_0
        return OUT_1

    """Доля собираемой макулатуры для производства картона"""

    # Базовое равновесие
    SH_0 = "{:.2%}".format(85.55 / 100)
    # Новое равновесие
    def new_share_of_waste(self, SH_0):
        SH_1 = SH_0
        return SH_1

    """Общее убывание волокна"""

    # Базовое равновесие
    def basic_total_fiber_decrease(self, K_0, OUT_0, SH_0):
        return K_0*OUT_0*SH_0

    # Новое равновесие
    def new_total_fiber_decrease(self, K_1, OUT_1, SH_1):
        return K_1*OUT_1*SH_1



if __name__ == "__main__":
    calculation = ModelControlActions(72.14, 0.18, "{:.0%}".format(129/100), "{:.14%}".format(1.89061890628692/100),
                                      14.686756, "{:.2%}".format(85.55/100))
    print(calculation.basic_total_fiber_decrease())





"""Поведенческие параметры"""
class Behavioral_parameters:
    σ_MIC = 2.5
    σ_PDP = 2.25
    Ω_FDP = 2.95  # комментарий разработчиков GTAP
    ε_MMI = 10
    ε_FDP = 0.3
    ε_PDP = 'Эластичность спроса!C11'
    ε_PXM = 1
    ε_FXP = -10

    def rho_r_σ_MIC(self, σ_MIC):
        r_σ_MIC = (σ_MIC-1)/σ_MIC
        return r_σ_MIC

    def rho_r_σ_PDP(self, σ_PDP):
        r_σ_PDP = (σ_PDP-1)/σ_PDP
        return r_σ_PDP

    def rho_r_Ω_FDP(self, Ω_FDP):
        r_Ω_FDP = (Ω_FDP+1)/Ω_FDP
        return r_Ω_FDP

    def SS_DS_Z_MMI(self, Q_MMI_0, P_MMI_0, ER_0, TMMI_0, NMMI_0, ε_MMI):
        Z_MMI = Q_MMI_0/((P_MMI_0/(ER_0*(1+TMMI_0)*(1+NMMI_0)))^ε_MMI)
        return Z_MMI

    def SS_DS_Z_FDP(self, Q_FDP_0, P_FDP_0, ε_FDP):
        Z_FDP = Q_FDP_0/(P_FDP_0)^ε_FDP
        return Z_FDP

    def SS_DS_Z_PDP(self, Q_PDP_0, P_PDP_0, ε_PDP):
        Z_PDP = Q_PDP_0/(P_PDP_0)^ε_PDP
        return Z_PDP

    def SS_DS_Z_PXM(self, Q_PXM_0, ER_0, ε_PXM):
        Z_PXM = Q_PXM_0/(1/ER_0)^ε_PXM
        return Z_PXM

    def SS_DS_Z_FXP(self, Q_FXP_0, P_FXP_0, ER_0, ε_FXP):
        Z_FXP = Q_FXP_0/(P_FXP_0/ER_0)^ε_FXP
        return Z_FXP


    """Налоги и благосостояние"""
    class Taxes_welfare:

        """Импортный тариф"""
        # Базовое рановесие
        def base_import_tariff(self, P_MMI_0, Q_MMI_0, TMMI_0):
            base = (P_MMI_0*Q_MMI_0)*TMMI_0
            return base
        # Новое равновесие
        def new_import_tariff(self, P_MMI_1, Q_MMI_1, TMMI_1):
            new = (P_MMI_1*Q_MMI_1)*TMMI_1
            return new
        # Изменение млн. руб
        def change_import_tariff(self, new, base):
            return  new - base
        # Изменение % к начальному
        def change_pr_import_tariff(self, new, base):
            return  new / base - 1

        """Производство макулатурных тарных картонов"""
        # Базовое рановесие

        # Новое равновесие
        # Изменение млн. руб
        # Изменение % к начальному




        # Базовое рановесие
        # Новое равновесие
        # Изменение млн. руб
        # Изменение % к начальному

