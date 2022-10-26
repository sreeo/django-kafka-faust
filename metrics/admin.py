from django.contrib import admin

from metrics.models import Metric


@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    pass
