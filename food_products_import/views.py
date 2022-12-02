from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from sympy.codegen.ast import none

from food_products_import.food_products_import.food_products_import import InputDataBase, food_products_import
from food_products_import.serializers import UserFoodDataSerializer, FoodTablesSerializer


class UserFoodDataView(APIView):

    def validate_user_data(self, user_data):
        if float(user_data.get('Pcif_before')) <= 0:
            return {'error': 'Цена на границе (Pcif): больше 0 (положительное число)'}
        if float(user_data.get('Pcif_after')) <= 0:
            return {'error': 'Цена на границе (Pcif): больше 0 (положительное число)'}
        if float(user_data.get('ER_before')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('ER_after')) <= 0:
            return {'error': 'Обменный курс (ER): больше 0 (положительное число)'}
        if float(user_data.get('Qt_before')) <= -1:
            return {'error': 'Тарифная квота (Qt): больше -1'}
        if float(user_data.get('Qt_after')) <= -1:
            return {'error': 'Тарифная квота (Qt): больше -1'}
        if float(user_data.get('ER_before')) == none:
            return {'error': 'Цена на границе (Pcif): введите значение'}
        return user_data


    def post(self, request, format=None):
        user_data = self.validate_user_data(request.data.get('user_data'))
        if user_data.get('error'):
            return Response(user_data)
        try:
            serializer = UserFoodDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_data = serializer.data.get('user_data')
            input_data = InputDataBase(user_data)
            data_food_import = food_products_import(input_data)
            serializer = FoodTablesSerializer(data_food_import)
        except Exception as e:
            print(type(e))
        else:
            return Response(serializer.data)

class UserDataEmpty(UserFoodDataView):
    def __init__(self, user_data):
        self. user_data = user_data
        super().__init__(
            f" There is no data for calculation"
        )
