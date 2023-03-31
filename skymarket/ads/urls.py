from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet)
comment_router = NestedSimpleRouter(ads_router, "ads", )
comment_router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comment_router.urls)),
]

