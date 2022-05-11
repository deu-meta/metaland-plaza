from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NavLinkViewSet

router = DefaultRouter()
router.register("", NavLinkViewSet, basename="navlinks")

urlpatterns = [
    path("", include(router.urls)),
]
