from asgiref.sync import sync_to_async

from metrics.models import Metric


@sync_to_async
def persist_metric_event(event):
    Metric.objects.create(
        name=event.name,
        source=event.source,
        battery_percentage=event.battery_percentage,
        mobile_make_model=event.mobile_make_model,
        os_version=event.os_version,
        mac_id=event.mac_id,
        latitude=event.latitude,
        longitude=event.longitude,
        timestamp=event.timestamp,
    )
