from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from steel_market.schemas import tables_to_frontend, tables_from_frontend
from steel_market.serializers import SteelTablesSerializer, UserSteelDataSerializer
from steel_market.steel_market.steel_market import InputDataBase, example_data, steel_market


class SteelTablesView(APIView):
    @swagger_auto_schema(
        responses=tables_to_frontend
    )
    def get(self, request, format=None):
        renderer_classes = [JSONRenderer]
        input_data = InputDataBase(example_data)
        data_steel_market = steel_market(input_data)
        serializer = SteelTablesSerializer(data_steel_market)
        return Response(serializer.data)

class UserSteelDataView(APIView):

    def validate_user_data(self, user_data):
        if float(user_data.get('ER_before')) == 0:
            return {'error': 'Курс RUB/USD (ER): не равно 0'}
        # if float(user_data.get('ER_after')) == 0:
        #     return {'error': 'Курс RUB/USD (ER): не равно 0'}
        if float(user_data.get('WP_before')) == 0:
            return {'error': 'Мировая цена товара стали USD (WP): не равно 0'}
        if float(user_data.get('P_AXD_USD_before')) == 0:
            return {'error': 'Цена экспорта стали USD (без тарифа) (P_AXD_USD): не равно 0'}
        if float(user_data.get('P_AMD_USD_before')) == 0:
            return {'error': 'Цена импорта стали USD (без тарифа) (P_AMD_USD): не равно 0'}
        if float(user_data.get('P_IXD_USD_before')) == 0:
            return {'error': 'Цена экспорта руды USD (без тарифа) (P_IXD_USD): не равно 0'}
        if float(user_data.get('TAXD_before')) == -1:
            return {'error': 'Экспортный тариф сталь (TAXD): не равно -1'}
        if float(user_data.get('TIXD_before')) == -1:
            return {'error': 'Экспортный тариф на руду (TIXD): не равно -1'}
        if float(user_data.get('IPD_pr')) == 0:
            return {'error': 'Отечественное производство руды (IPD), цена: не равно 0'}
        if float(user_data.get('IPD_q')) == 0:
            return {'error': 'Отечественное производство руды (IPD), количество: не равно 0'}
        if float(user_data.get('IXD_q')) == 0:
            return {'error': 'Экспорт руды (IXD), количество: не равно 0'}
        if float(user_data.get('IXD_q')) == 1:
            return {'error': 'Экспорт руды (IXD), количество: не равно 1'}
        if float(user_data.get('APD_pr')) == 0:
            return {'error': 'Отечественное производство стали и изделий из неё (APD), цена: не равно 0'}
        if float(user_data.get('APD_q')) == 0:
            return {'error': 'Отечественное производство стали и изделий из неё (APD), количество: не равно 0'}
        if float(user_data.get('AXD_q')) == 0:
            return {'error': 'Отечественный экспорт стали и изделий из неё (AXD), количество: не равно 0'}
        if float(user_data.get('AXD_q')) == 1:
            return {'error': 'Отечественный экспорт стали и изделий из неё (AXD), количество: не равно 1'}
        if float(user_data.get('ADW_q')) == 0:
            return {'error': 'Мировое потребление (импорт) стали и изделий из неё (ADW), количество: не равно 0'}
        if float(user_data.get('AMD_q')) == 0:
            return {'error': 'Импорт стали и изделий из неё (AMD), количество: не равно 0'}
        if float(user_data.get('Ω_IPD')) == 0:
            return {'error': 'Параметр (Ω_IPD): не равен 0. Рекомендуется использовать значения по умолчанию 1.5'}
        if float(user_data.get('σ_APD')) == 0:
            return {'error': 'Параметр (σ_APD): не равен 0. Рекомендуется использовать значения по умолчанию 1.5'}
        if float(user_data.get('σ_APD')) == 1:
            return {'error': 'Параметр (σ_APD): не равен 1. Рекомендуется использовать значения по умолчанию 1.5'}
        if float(user_data.get('Ω_APD')) == 0:
            return {'error': 'Параметр (Ω_APD): не равен 0. Рекомендуется использовать значения по умолчанию 3.0'}
        if float(user_data.get('σ_ADW')) == 0:
            return {'error': 'Параметр (σ_ADW): не равен 0. Рекомендуется использовать значения по умолчанию 10.0'}
        if float(user_data.get('σ_ATD')) == 0:
            return {'error': 'Параметр (σ_ATD): не равен 0. Рекомендуется использовать значения по умолчанию 3.0'}
        if float(user_data.get('Ω_ATD')) == 0:
            return {'error': 'Параметр (Ω_ATD): не равен 0. Рекомендуется использовать значения по умолчанию 1.5'}
        if float(user_data.get('σ_BDD')) == 0:
            return {'error': 'Параметр (σ_BDD): не равен 0. Рекомендуется использовать значения по умолчанию 1.5'}
        if float(user_data.get('σ_BDD')) == 1:
            return {'error': 'Параметр (σ_BDD): не равен 1. Рекомендуется использовать значения по умолчанию 1.5'}
        return user_data

    @swagger_auto_schema(
        responses=tables_from_frontend,
        request_body=UserSteelDataSerializer
    )
    def post(self, request, format=None):
        user_data = self.validate_user_data(request.data.get('user_data'))
        if user_data.get('error'):
            return Response(user_data)

        serializer = UserSteelDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data.get('user_data')
        input_data = InputDataBase(user_data)
        data_steel_market = steel_market(input_data)
        serializer = SteelTablesSerializer(data_steel_market)
        return Response(serializer.data)

