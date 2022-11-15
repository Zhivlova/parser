from drf_yasg.utils import swagger_auto_schema
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


from vavt_wheat_exports.schemas import tables_to_frontend, tables_from_frontend
from vavt_wheat_exports.serializers import WheatTablesSerializer, UserWheatDataSerializer
from vavt_wheat_exports.wheat_exports.wheat_exports import InputDataBase, example_data, wheat_exports


class WheatTablesView(APIView):
    @swagger_auto_schema(
        responses=tables_to_frontend
    )
    def get(self, request, format=None):
        renderer_classes = [JSONRenderer]
        input_data = InputDataBase(example_data)
        data_wheat_export = wheat_exports(input_data)
        serializer = WheatTablesSerializer(data_wheat_export)
        return Response(serializer.data)

class UserWheatDataView(APIView):

    def validate_user_data(self, user_data):
        if float(user_data.get('PW_A_const_before')) < 60:
            return {'error': 'Мировая цена пшеницы до сдвига (PW_A_const): от 60'}
        if float(user_data.get('PW_A_const_after')) < 59:
            return {'error': 'Мировая цена пшеницы после сдвига (PW_A_const): от 59'}
        if float(user_data.get('ER_before')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('ER_after')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('CT_before')) < 0:
            return {'error': 'Стоимость услуг трейдеров (CT): больше 0 (положительное число)'}
        if float(user_data.get('TD_before')) < 0:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0 (положительное число)'}
        if float(user_data.get('TD_before')) >= 1:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0, меньше 1, не равно 1'}
        if float(user_data.get('TD_after')) < 0:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0 (положительное число)'}
        if float(user_data.get('TD_after')) >= 1:
            return {'error': 'Дисконт к эквивалентной цене (TD): больше 0, меньше 1, не равно 1'}
        if float(user_data.get('Pb_before')) < 0:
            return {'error': 'Первая базовая цена (Pb): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('Pb_after')) < 0:
            return {'error': 'Первая базовая цена (Pb): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('Pb2_before')) < 7:
            return {'error': 'Вторая базовая цена (Pb2): от 7'}
        if float(user_data.get('Pb2_after')) < 0:
            return {'error': 'Вторая базовая цена (Pb2): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('Pb3_before')) < 222:
            return {'error': 'Третья базовая цена (Pb3): от 222'}
        if float(user_data.get('Pb3_after')) < 0:
            return {'error': 'Третья базовая цена (Pb3): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('t1_before')) < 0:
            return {'error': 'Ставка вывозной пошлины к первой базовой цене (t1): больше или равно 0 '
                             '(неотрицательное число)'}
        if float(user_data.get('t1_before')) > 1:
            return {'error': 'Ставка вывозной пошлины к первой базовой цене (t1): больше или равно 0, '
                             'меньше или равно 1'}
        if float(user_data.get('t1_after')) <= 0:
            return {'error': 'Ставка вывозной пошлины к первой базовой цене (t1): больше  0'}
        if float(user_data.get('t1_after')) > 1:
            return {'error': 'Ставка вывозной пошлины к первой базовой цене (t1): больше 0, меньше или равно 1'}

        if float(user_data.get('t2_before')) < 0:
            return {'error': 'Ставка вывозной пошлины ко второй базовой цене (t2): больше или равно 0 '
                             '(неотрицательное число)'}
        if float(user_data.get('t2_before')) > 1:
            return {'error': 'Ставка вывозной пошлины ко второй базовой цене (t2): больше или равно 0, '
                             'меньше или равно 1'}
        if float(user_data.get('t2_after')) < 0:
            return {'error': 'Ставка вывозной пошлины ко второй базовой цене (t2): больше или равно 0 '
                             '(неотрицательное число)'}
        if float(user_data.get('t2_after')) > 1:
            return {'error': 'Ставка вывозной пошлины ко второй базовой цене (t2): больше или равно 0, '
                             'меньше или равно 1'}
        if float(user_data.get('t3_before')) < 0:
            return {'error': 'Ставка вывозной пошлины к третьей базовой цене (t3) больше или равно 0 '
                             '(неотрицательное число)'}
        if float(user_data.get('t3_before')) > 1:
            return {'error': 'Ставка вывозной пошлины к третьей базовой цене (t3) больше или равно 0, '
                             'меньше или равно 1'}
        if float(user_data.get('t3_after')) < 0:
            return {'error': 'Ставка вывозной пошлины к третьей базовой цене (t3) больше или равно 0 '
                             '(неотрицательное число)'}
        if float(user_data.get('t3_after')) > 1:
            return {'error': 'Ставка вывозной пошлины к третьей базовой цене (t3): больше или равно 0, '
                             'меньше или равно 1'}
        if float(user_data.get('demp_before')) < 0:
            return {'error': 'Ставка зернового демпфера (demp): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('demp_before')) > 1:
            return {'error': 'Ставка зернового демпфера (demp): больше или равно 0, меньше или равно 1'}
        if float(user_data.get('demp_after')) < 0:
            return {'error': 'Ставка зернового демпфера (demp): больше или равно 0 (неотрицательное число)'}
        if float(user_data.get('demp_after')) > 1:
            return {'error': 'Ставка зернового демпфера (demp): больше или равно 0, меньше или равно 1'}
        if float(user_data.get('QSI_A_before')) <= 0:
            return {'error': 'Объем внутреннего производства пшеницы (QSI_A): больше 0 (положительное число)'}
        if float(user_data.get('i_cost_before')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost): больше 0, не равно 0'}
        if float(user_data.get('i_cost_after')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost): больше 0, не равно 0'}
        if float(user_data.get('shift_QSI_A_before')) <= -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении пшеницы (shift_QSI_A): больше -1'}
        if float(user_data.get('shift_QSI_A_after')) <= -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении пшеницы (shift_QSI_A): больше -1'}
        if float(user_data.get('QDI_С1_before')) <= 0:
            return {'error': 'Внутренний спрос на хлеб (QDI_С1): больше 0'}
        if float(user_data.get('QDI_A_C1_before')) <= 0:
            return {'error': 'Объем пшеницы на производство хлеба (QDI_A_C1): больше 0'}
        if float(user_data.get('SpI_C1_before')) <= 0:
            return {'error': 'Внутренние затраты потребителей на хлеб (SpI_C1): больше 0'}
        if float(user_data.get('QDI_С2_before')) <= 0:
            return {'error': 'Внутренний спрос на мясо (QDI_С2): больше 0'}
        if float(user_data.get('QDI_A_C2_before')) <= 0:
            return {'error': 'Объем пшеницы на производство мяса (QDI_A_C2): больше 0'}
        if float(user_data.get('SpI_C2_before')) <= 0:
            return {'error': 'Внутренние затраты потребителей на мясо (SpI_C1): больше 0'}
        if float(user_data.get('QS_exRUS_A_before')) <= 0:
            return {'error': 'Производство пшеницы (остальной мир) (QS_exRUS_A): больше 0'}
        if float(user_data.get('QD_A_before')) <= 0:
            return {'error': 'Глобальный спрос со стороны импортеров (QD_A): больше 0'}
        if float(user_data.get('QD_exRUS_A_before')) <= 0:
            return {'error': 'Внутренний спрос экспортеров (остальной мир) (QD_exRUS_A): больше 0'}
        if float(user_data.get('shift_QSW_A_before')) <= -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении пшеницы (shift_QSW_A): больше -1'}
        if float(user_data.get('shift_QSW_A_after')) <= -1:
            return {'error': 'Экзогенный сдвиг во внутреннем предложении пшеницы (shift_QSW_A): больше -1'}
        if float(user_data.get('i_cost_world_before')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost_world): больше 0, не равно 0'}
        if float(user_data.get('i_cost_world_after')) <= 0:
            return {'error': 'Индекс превышения затрат на производство над ценами (i_cost_world): больше 0, не равно 0'}
        return user_data

    @swagger_auto_schema(
        responses=tables_from_frontend,
        request_body=UserWheatDataSerializer
    )
    def post(self, request, format=None):
        user_data = self.validate_user_data(request.data.get('user_data'))
        if user_data.get('error'):
            return Response(user_data)

        serializer = UserWheatDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data.get('user_data')
        input_data = InputDataBase(user_data)
        data_wheat_export = wheat_exports(input_data)
        serializer = WheatTablesSerializer(data_wheat_export)
        return Response(serializer.data)
