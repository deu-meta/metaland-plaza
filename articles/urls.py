from django.urls import include, path
from rest_framework_nested import routers  # /articles/:id/comments 구성하는데 쓰임

from .views import *

router = routers.DefaultRouter()

router.register("", ArticleViewSet, basename="article")

comment_router = routers.NestedDefaultRouter(router, "", lookup="article")
comment_router.register("comments", CommentViewSet, basename="comment")


urlpatterns = [path("", include(router.urls)), path("", include(comment_router.urls))]
