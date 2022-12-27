from rest_framework import serializers

class FertilizersTablesSerializer(serializers.Serializer):
    table1 = serializers.ListField()
    finding_solution = serializers.BooleanField()
    table2 = serializers.ListField()
    table3 = serializers.ListField()
    table4 = serializers.ListField()

class UserFertilizersDataSerializer(serializers.Serializer):
    user_data = serializers.DictField()


