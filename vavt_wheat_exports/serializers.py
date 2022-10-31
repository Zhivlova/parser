from rest_framework import serializers


class WheatTablesSerializer(serializers.Serializer):
    finding_solution = serializers.BooleanField()

class UserWheatDataSerializer(serializers.Serializer):
    user_data = serializers.DictField()
