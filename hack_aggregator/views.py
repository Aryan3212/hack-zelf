from rest_framework import filters, mixins, viewsets
from .serializers import ContentSerializer
from .models import Content
class ListContentView(viewsets.ModelViewSet):
    """
    API endpoint that allows content to be viewed.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-created_at']

    def get_permissions(self):
        return super().get_permissions()