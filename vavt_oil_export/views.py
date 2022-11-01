from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from vavt_oil_export.oil_export.oil_export import InputDataBase, example_data, oil_export
from vavt_oil_export.schemas import tables_to_frontend, tables_from_frontend
from vavt_oil_export.serializers import OilTablesSerializer, UserOilDataSerializer


class OilTablesView(APIView):
    @swagger_auto_schema(
        responses=tables_to_frontend
    )
    def get(self, request, format=None):
        renderer_classes = [JSONRenderer]
        input_data = InputDataBase(example_data)
        data_oil_export = oil_export(input_data)
        serializer = OilTablesSerializer(data_oil_export)
        return Response(serializer.data)


class UserOilDataView(APIView):

    def validate_user_data(self, user_data):
        if float(user_data.get('PW_B1_before')) <= 0:
            return {'error': 'Мировая цена товара В1 (PW_B1): больше 0 (положительное число)'}
        if float(user_data.get('PW_B1_after')) <= 0:
            return {'error': 'Мировая цена товара В1 (PW_B1): больше 0 (положительное число)'}
        if float(user_data.get('PW_B2_before')) <= 0:
            return {'error': 'Мировая цена товара В2 (PW_B2): больше 0 (положительное число)'}
        if float(user_data.get('PW_B2_after')) <= 0:
            return {'error': 'Мировая цена товара В2 (PW_B2): больше 0 (положительное число)'}
        if float(user_data.get('ER_before')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('ER_after')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('TD_before')) < 0:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0 (положительное число)'}
        if float(user_data.get('TD_before')) >= 1:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0, меньше 1, не равно 1'}
        if float(user_data.get('TD_after')) < 0:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0 (положительное число)'}
        if float(user_data.get('TD_after')) >= 1:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0, меньше 1, не равно 1'}
        if float(user_data.get('Pb_B1_before')) < 0:
            return {'error': 'Базовая цена товара B1 (Pb_B1): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('Pb_B1_after')) < 0:
            return {'error': 'Базовая цена товара B1 (Pb_B1): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B1_before')) < 0:
            return {'error': 'Ставка вывозной пошлины товара B1 (tb_B1): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B1_before')) > 1:
            return {'error': 'Ставка вывозной пошлины товара B1 (tb_B1): больше или равно 0, меньше или равно 1'}
        if float(user_data.get('tb_B1_after')) < 0:
            return {'error': 'Ставка вывозной пошлины товара B1 (tb_B1): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B1_after')) > 1:
            return {'error': 'Ставка вывозной пошлины товара B1 (tb_B1): больше или равно 0, меньше или равно 1'}
        if float(user_data.get('Pb_B2_before')) < 0:
            return {'error': 'Базовая цена товара B2 (Pb_B2): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('Pb_B2_after')) < 0:
            return {'error': 'Базовая цена товара B2 (Pb_B2): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B2_before')) < 0:
            return {'error': 'Ставка вывозной пошлины товара B2 (tb_B2): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B2_before')) > 1:
            return {'error': 'Ставка вывозной пошлины товара B2 (tb_B2): больше или равно 0, меньше или равно 1'}
        if float(user_data.get('tb_B2_after')) < 0:
            return {'error': 'Ставка вывозной пошлины товара B2 (tb_B2): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('tb_B2_after')) >= 1:
            return {'error': 'Ставка вывозной пошлины товара B2 (tb_B2): больше или равно 0, меньше 1'}
        if float(user_data.get('PI_B1_before')) <= 1:
            return {'error': 'Внутренняя цена товара B1 (PI_B1): больше 1'}
        if float(user_data.get('PI_B2_before')) <= 1:
            return {'error': 'Внутренняя цена товара B2 (PI_B2): больше 1'}
        if float(user_data.get('PI_A_before')) <= 1:
            return {'error': 'Внутренняя цена товара А (PI_А): больше 1'}
        if float(user_data.get('QSI_A_before')) <= 0:
            return {'error': 'Объем внутреннего производства товара А (QSI_A): больше 0 (положительное число)'}
        if float(user_data.get('QSW_RUS_A_before')) < 0:
            return {'error': 'Объем экспорта товара А (QSW_RUS_A): больше 0 (положительное число)'}
        if float(user_data.get('QSW_RUS_A_after')) < 0:
            return {'error': 'Объем экспорта товара А (QSW_RUS_A): больше 0 (положительное число)'}
        if float(user_data.get('i_cost_before')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost): больше 0, не равно 0'}
        if float(user_data.get('i_cost_after')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost): больше 0, не равно 0'}
        if float(user_data.get('shift_QSI_A_before')) <= -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении товара А (shift_QSI_A): больше -1'}
        if float(user_data.get('shift_QSI_A_after')) < -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении товара А (shift_QSI_A): больше -1'}
        if float(user_data.get('PI_С_before')) <= 0:
            return {'error': 'Внутренняя цена товара С (PI_С): больше 0 (положительное число)'}
        if float(user_data.get('QDI_С_before')) <= 0:
            return {'error': 'Внутренний спрос на товар С (QDI_С): больше 0 (положительное число)'}
        if float(user_data.get('QDI_B2_before')) <= 0:
            return {'error': 'Внутренний спрос на товар В2 (QDI_B2): больше 0 (положительное число)'}
        return user_data

    @swagger_auto_schema(
        responses=tables_from_frontend,
        request_body=UserOilDataSerializer
    )
    def post(self, request, format=None):
        user_data = self.validate_user_data(request.data.get('user_data'))
        if user_data.get('error'):
            return Response(user_data)

        serializer = UserOilDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data.get('user_data')
        input_data = InputDataBase(user_data)
        data_oil_export = oil_export(input_data)
        serializer = OilTablesSerializer(data_oil_export)
        return Response(serializer.data)
