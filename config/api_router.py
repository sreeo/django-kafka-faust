from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from metrics.views import MetricViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("metrics", MetricViewSet)


app_name = "api"
urlpatterns = router.urls
