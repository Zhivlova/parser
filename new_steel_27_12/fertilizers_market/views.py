from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from fertilizers_market.fertilizers_market.fertilizers_market import InputDataBase, example_data, fertilizers_market
from fertilizers_market.schemas import tables_to_frontend, tables_from_frontend
from fertilizers_market.serializers import FertilizersTablesSerializer, UserFertilizersDataSerializer


class FertilizersTablesView(APIView):
    @swagger_auto_schema(
        responses=tables_to_frontend
    )
    def get(self, request, format=None):
        renderer_classes = [JSONRenderer]
        input_data = InputDataBase(example_data)
        data_fertilizers_market = fertilizers_market(input_data)
        serializer = FertilizersTablesSerializer(data_fertilizers_market)
        return Response(serializer.data)


class UserFertilizersDataView(APIView):

    def validate_user_data(self, user_data):
        if float(user_data.get('ER_before')) == 0:
            return {'error': 'Курс RUB/USD (ER): не равно 0'}
        if float(user_data.get('ER_after')) == 0:
            return {'error': 'Курс RUB/USD (ER): не равно 0'}
        if float(user_data.get('WPK_before')) == 0:
            return {'error': 'Мировая цена товара K USD (WPK): не равно 0'}
        if float(user_data.get('WPN_before')) == 0:
            return {'error': 'Мировая цена товара N USD (WPN): не равно 0'}
        if float(user_data.get('P_KXD_USD_before')) == 0:
            return {'error': 'Цена экспорта товара K USD (без тарифа) (P_KXD_USD): не равно 0'}
        if float(user_data.get('P_NXD_USD_before')) == 0:
            return {'error': 'Цена экспорта товара N USD (без тарифа) (P_NXD_USD): не равно 0'}
        if float(user_data.get('KPD_pr')) == 0:
            return {'error': 'Отечественное производство товара K (KPD), цена: не равно 0'}
        if float(user_data.get('KPD_q')) <= 0:
            return {'error': 'Отечественное производство товара K (KPD), количество: больше 0 (положительное число)'}
        if float(user_data.get('KXD_q')) <= 0:
            return {'error': 'Экспорт товара K (KXD), количество: больше 0 (положительное число)'}
        if float(user_data.get('NPD_pr')) == 0:
            return {'error': 'Отечественное производство товара N (NPD), цена: не равно 0'}
        if float(user_data.get('NPD_q')) <= 0:
            return {'error': 'Отечественное производство товара N (NPD), количество: больше 0 (положительное число)'}
        if float(user_data.get('NXD_q')) <= 0:
            return {'error': 'Экспорт товара N (NXD), количество: больше 0 (положительное число)'}
        if float(user_data.get('KSW_q')) <= 0:
            return {'error': 'Мировое потребление товара K (KSW), количество: больше 0 (положительное число)'}
        if float(user_data.get('NSW_q')) <= 0:
            return {'error': 'Мировое потребление товара N (NSW), количество: больше 0 (положительное число)'}
        if float(user_data.get('Ω_KPD')) <= 0:
            return {'error': 'Параметр (Ω_KPD): больше 0. Рекомендуется использовать значения по умолчанию 5.0'}
        if float(user_data.get('Ω_NPD')) <= 0:
            return {'error': 'Параметр (Ω_NPD): больше 0. Рекомендуется использовать значения по умолчанию 5.0'}
        if float(user_data.get('σ_FCD')) == 0:
            return {'error': 'Параметр (σ_FCD): не равен 0. Рекомендуется использовать значения по умолчанию 2.0'}
        if float(user_data.get('σ_FCD')) == 1:
            return {'error': 'Параметр (σ_FCD): не равен 1. Рекомендуется использовать значения по умолчанию 2.0'}
        if float(user_data.get('σ_KSW')) == 0:
            return {'error': 'Параметр (σ_KSW): не равен 0. Рекомендуется использовать значения по умолчанию 5.0'}
        if float(user_data.get('σ_NSW')) == 0:
            return {'error': 'Параметр (σ_NSW): не равен 0. Рекомендуется использовать значения по умолчанию 5.0'}
        if float(user_data.get('σ_FCW')) == 0:
            return {'error': 'Параметр (σ_FCW): не равен 0. Рекомендуется использовать значения по умолчанию 3.0'}
        if float(user_data.get('σ_FCW')) == 1:
            return {'error': 'Параметр (σ_FCW): не равен 1. Рекомендуется использовать значения по умолчанию 3.0'}
        return user_data

    @swagger_auto_schema(
        responses=tables_from_frontend,
        request_body=UserFertilizersDataSerializer
    )
    def post(self, request, format=None):
        user_data = self.validate_user_data(request.data.get('user_data'))
        if user_data.get('error'):
            return Response(user_data)

        serializer = UserFertilizersDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data.get('user_data')
        input_data = InputDataBase(user_data)
        data_fertilizers_market = fertilizers_market(input_data)
        serializer = FertilizersTablesSerializer(data_fertilizers_market)
        return Response(serializer.data)