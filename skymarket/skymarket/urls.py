from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/swagger-ui", SpectacularSwaggerView.as_view(url_name='schema')),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),

    path("api/", include("users.urls")),
    path("api/", include("ads.urls")),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
