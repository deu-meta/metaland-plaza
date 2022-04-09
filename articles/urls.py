from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(
    "",
    ArticleViewSet,
)
router.register("comment", CommentViewSet)


urlpatterns = router.urls
