from rest_framework import serializers

class OilTablesSerializer(serializers.Serializer):
    table1 = serializers.ListField()
    table2 = serializers.ListField()
    table3 = serializers.ListField()
    table4 = serializers.ListField()
    table5 = serializers.ListField()
    table6 = serializers.ListField()
    table7 = serializers.ListField()
    fintable1 = serializers.ListField()
    fintable2 = serializers.ListField()
    fintable3 = serializers.ListField()
    fintable4 = serializers.ListField()


class UserOilDataSerializer(serializers.Serializer):
    user_data = serializers.DictField()


