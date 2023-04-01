from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer

from ads.serializers import CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()

    serializer_class = AdSerializer

    serializer = {"list": AdSerializer}
    default_permission = [IsAuthenticated]
    pagination_class = AdPagination


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

