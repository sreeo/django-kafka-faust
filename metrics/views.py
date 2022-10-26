from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from metrics.models import Metric
from metrics.serializers import MetricReadOnlySerializer, MetricSerializer
from metrics.services import KafkaPublisher, MessagePublisher

message_publisher = MessagePublisher(client=KafkaPublisher())


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    message_topic = settings.KAFKA_STREAM_TOPIC
    permission_classes = []

    def get_serializer_class(self):
        serializers = {
            "list": MetricReadOnlySerializer,
            "create": MetricSerializer,
            "retrieve": MetricReadOnlySerializer,
            "bulk": MetricSerializer,
            "bulk_raw": MetricSerializer,
        }
        return serializers.get(self.action)

    def list(self, request):
        queryset = Metric.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Metric.objects.all()
        metric = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(metric)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)
        # message_publisher = MessagePublisher(client=KafkaPublisher())
        message_publisher.publish(topic=self.message_topic, data=serializer.data)
        return Response(serializer.data)

    @action(detail=False, methods=["POST"])
    def bulk_raw(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, many=True)

        serializer.is_valid(raise_exception=True)

        metrics = []

        for data in serializer.data:
            metrics.append(Metric(**data))

        Metric.objects.bulk_create(metrics)
        return Response(serializer.data)

    @action(detail=False, methods=["POST"])
    def bulk(self, request, pk=None):
        serializer = self.get_serializer(data=request.data, many=True)

        serializer.is_valid(raise_exception=True)

        for data in serializer.data:
            message_publisher.publish(topic=self.message_topic, data=data)

        return Response(serializer.data)
