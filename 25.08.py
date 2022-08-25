import math


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

    SH_1 = SH_0
    result['SH_1'] = SH_1

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

    Q_SDP_0 = user_values[11]
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

    Q_MIC_0 = Q_MDI_0 + Q_MMI_0
    result['Q_MIC_0'] = Q_MIC_0

    OUT_0 = Q_SDP_0 / (Q_MIC_0 * SH_0)
    result['OUT_0'] = OUT_0

    OUT_1 = OUT_0
    result['OUT_1'] = OUT_1

    def basic_total_fiber_decrease(K_0, OUT_0, SH_0):
        return K_0 * OUT_0 * SH_0

    basic_total_fiber_decrease = basic_total_fiber_decrease(K_0, OUT_0, SH_0)
    result['basic_total_fiber_decrease'] = basic_total_fiber_decrease

    def K_1(P_MDI_1, Λ_1):
        K_1 = (1 - math.exp(-P_MDI_1 / Λ_1))
        return K_1

    P_MDI_1 = 15.6016971682569
    result['P_MDI_1'] = P_MDI_1

    K_1 = K_1(P_MDI_1, Λ_1)
    result['K_1'] = K_1

    def new_total_fiber_decrease(K_1, OUT_1, SH_1):
        return K_1 * OUT_1 * SH_1

    new_total_fiber_decrease = new_total_fiber_decrease(K_1, OUT_1, SH_1)
    result['new_total_fiber_decrease'] = new_total_fiber_decrease

    return result


user_values = [72.14, 0.18, 1.29, 0.0189061890628692, 14.686756, 0.8555, 15.139, 38, 42, 42, 3822, 2999, 1006,
               4186, 2125]
print(calc(user_values))