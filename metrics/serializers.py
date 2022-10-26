from rest_framework import serializers


class MetricReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    source = serializers.CharField(read_only=True)
    battery_percentage = serializers.CharField(read_only=True)
    mobile_make_model = serializers.CharField(read_only=True)
    os_version = serializers.CharField(read_only=True)
    mac_id = serializers.CharField(read_only=True)
    latitude = serializers.CharField(read_only=True)
    longitude = serializers.CharField(read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)


class MetricSerializer(serializers.Serializer):
    name = serializers.CharField()
    source = serializers.CharField(required=False)
    battery_percentage = serializers.CharField()
    mobile_make_model = serializers.CharField()
    os_version = serializers.CharField()
    mac_id = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    timestamp = serializers.DateTimeField()
