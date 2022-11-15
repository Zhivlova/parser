from rest_framework import serializers


class WheatTablesSerializer(serializers.Serializer):
    table1 = serializers.ListField()
    table2 = serializers.ListField()
    table3 = serializers.ListField()
    table4 = serializers.ListField()
    table5 = serializers.ListField()
    table6 = serializers.ListField()
    table7 = serializers.ListField()
    table8 = serializers.ListField()
    fintable1 = serializers.ListField()
    fintable2 = serializers.ListField()
    fintable3 = serializers.ListField()
    fintable4 = serializers.ListField()
    fintable5 = serializers.ListField()
    fintable6 = serializers.ListField()
    fintable7 = serializers.ListField()
    fintable8 = serializers.ListField()
    fintable9 = serializers.ListField()
    finding_solution = serializers.BooleanField()

class UserWheatDataSerializer(serializers.Serializer):
    user_data = serializers.DictField()
