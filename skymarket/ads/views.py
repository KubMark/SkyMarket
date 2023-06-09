from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer

from ads.permissions import IsOwner


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('author').all()
    pagination_class = AdPagination

    serializers = {
        "retrieve": AdDetailSerializer,
        "list": AdSerializer,
    }

    default_permission = [IsAuthenticated]
    serializer_class_actions = {
        "retrieve": [IsAuthenticated],
        "list": [AllowAny],
    }

    def get_permissions(self):
        return [permission() for permission in self.serializer_class_actions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, AdSerializer)

    def create(self, request, *args, **kwargs):
        request.data['author_id'] = int(self.request.user.id)
        return super().create(request, *args, **kwargs)


class AdOwnerListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author_id=request.user.id)
        return super().get(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination
    default_permission = [IsAuthenticated]
    permissions = {
        "list": [IsAuthenticated, ],
        "retrieve": [IsAuthenticated, ],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]


class CommentPagination(pagination.PageNumberPagination):
    def pagination_queryset(self, queryset, request, view=None):
        self.page_size = len(queryset) or self.page_size
        return super().paginate_queryset(queryset, request, view)