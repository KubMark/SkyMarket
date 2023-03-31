from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    default_serializer = AdSerializer
    queryset = Ad.objects.all()
    serializer = {"list": AdSerializer}
    default_permission = [IsAuthenticated]



class CommentViewSet(viewsets.ModelViewSet):
    pass

