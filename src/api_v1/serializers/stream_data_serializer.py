from rest_framework import serializers


class StreamDataSerializer(serializers.Serializer):
    datetime = serializers.DateTimeField()
    value = serializers.DecimalField(
        decimal_places=4,
        max_digits=16,
    )