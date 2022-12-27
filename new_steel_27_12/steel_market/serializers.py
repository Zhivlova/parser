from rest_framework import serializers

class SteelTablesSerializer(serializers.Serializer):
    table1 = serializers.ListField()
    finding_solution = serializers.BooleanField()
    table2 = serializers.ListField()
    table3 = serializers.ListField()
    table4 = serializers.ListField()

class UserSteelDataSerializer(serializers.Serializer):
    user_data = serializers.DictField()


