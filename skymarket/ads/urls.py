from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter


from ads.views import AdViewSet, CommentViewSet, AdOwnerListView


ads_router = routers.SimpleRouter()
ads_router.register("ads", AdViewSet)
ads_router.register(r"ads/(?P<ad_pk>[^/.]+)/comments", CommentViewSet, basename="comments")

comment_router = NestedSimpleRouter(ads_router, "ads", )
comment_router.register("comments", CommentViewSet)

urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comment_router.urls)),
    path("ads/me/", AdOwnerListView.as_view()),
]

