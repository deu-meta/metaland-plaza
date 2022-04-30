

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SpaceViewSet

router = DefaultRouter()

router.register("", SpaceViewSet, basename="spaces")

urlpatterns = [
    path("", include(router.urls))
]
