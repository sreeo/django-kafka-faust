import faust


class Metric(faust.Record, serializer="json"):
    name: str
    source: str
    battery_percentage: str
    mobile_make_model: str
    os_version: str
    mac_id: str
    latitude: str
    longitude: str
    timestamp: str
