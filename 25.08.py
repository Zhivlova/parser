import math
import json

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

    P_MMI_0 = P_MMI_USD_0 * ER_0 * (1 + TMMI_0)
    result['P_MMI_0'] = P_MMI_0

    P_MIC_0 = (P_MDI_0*Q_MDI_0+P_MMI_0*Q_MMI_0)/Q_MIC_0
    result['P_MIC_0'] = P_MIC_0

    P_SDP_0 = P_MIC_0/OUT_0+SVA_0
    result['P_SDP_0'] = P_SDP_0

    Q_PDP_0 = Q_SDP_0+Q_FDC_0
    result['Q_PDP_0'] = Q_PDP_0

    P_PXM_0 = P_MDI_0
    result['P_PXM_0'] = P_PXM_0

    P_PDC_0 = P_MDI_0
    result['P_PDC_0'] = P_PDC_0

    Q_FDP_0 = user_values[14]
    print(f' от пользователя получено значение Q_FDP_0  {Q_FDP_0}')
    result['Q_FDP_0'] = Q_FDP_0

    Q_FXP_0 = Q_FDP_0-Q_FDC_0
    result['Q_FXP_0'] = Q_FXP_0

    Q_PXM_0 = Q_PDC_0-Q_PDP_0
    result['Q_PXM_0'] = Q_PXM_0

    P_FDC_0 = (P_FDP_0*Q_FDP_0-P_FXP_0*Q_FXP_0)/Q_FDC_0
    result['P_FDC_0'] = P_FDC_0

    P_PDP_0 = (P_SDP_0*Q_SDP_0+P_FDC_0*Q_FDC_0)/Q_PDP_0
    result['P_PDP_0'] = P_PDP_0

    P_MMI_1 = 7.809220170519853
    result['P_MMI_1'] = P_MMI_1

    P_MDI_1 = 15.601697168256912
    result['P_MDI_1'] = P_MDI_1

    P_MIC_1 = 15.271367919915447
    result['P_MIC_1'] = P_MIC_1

    P_SDP_1 = 31.519642931378577
    result['P_SDP_1'] = P_SDP_1

    P_FDC_1 = 35.84115975829865
    result['P_FDC_1'] = P_FDC_1

    P_PDP_1 = 32.49799333322565
    result['P_PDP_1'] = P_PDP_1

    P_PXM_1 = 15.601697168256912
    result['P_PXM_1'] = P_PXM_1

    P_PDC_1 = 15.601697168256912
    result['P_PDC_1'] = P_PDC_1

    P_FDP_1 = 44.03846291455995
    result['P_FDP_1'] = P_FDP_1

    P_FXP_1 = 49.540263241232324
    result['P_FXP_1'] = P_FXP_1

    Q_MMI_1 = 166.4876029242774
    result['Q_MMI_1'] = Q_MMI_1

    Q_MDI_1 = 3760.960005783304
    result['Q_MDI_1'] = Q_MDI_1

    Q_MIC_1 = 3927.447608707581
    result['Q_MIC_1'] = Q_MIC_1

    Q_SDP_1 = 3048.2441455781654
    result['Q_SDP_1'] = Q_SDP_1

    Q_FDC_1 = 892.0438008930299
    result['Q_FDC_1'] = Q_FDC_1

    Q_PDP_1 = 3940.287946471196
    result['Q_PDP_1'] = Q_PDP_1

    Q_PXM_1 = 150.8333333333333
    result['Q_PXM_1'] = Q_PXM_1

    Q_PDC_1 = 4091.1212798045276
    result['Q_PDC_1'] = Q_PDC_1

    Q_FDP_1 = 2221.1275608246965
    result['Q_FDP_1'] = Q_FDP_1

    Q_FXP_1 = 1329.0837599316676
    result['Q_FXP_1'] = Q_FXP_1

    print(result)
    # result_to_front = {
    #     'Базовое равновесие': [
    #         ER_0,
    #         P_MMI_USD_0,
    #         NMMI_0,
    #         TMMI_0,
    #         K_0,
    #         SVA_0,
    #         SH_0,
    #         basic_total_fiber_decrease
    #     ],
    #     ' Новое равновесие':[
    #         ER_1,
    #         NMMI_1,
    #         TMMI_0,
    #         K_1,
    #         SVA_1,
    #         SH_1,
    #         new_total_fiber_decrease
    #     ]
    # }
    # return result_to_front

user_values = [72.14, 0.18, 1.29, 0.0189061890628692, 14.686756, 0.8555, 15.139, 38, 42, 42, 3822, 2999, 1006,
               4186, 2125]
print(calc(user_values))