from rest_framework import viewsets, filters
from .models import Grade
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    """CRUD для оценок."""
    queryset = Grade.objects.select_related("student", "subject", "teacher").all()
    serializer_class = GradeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["student__full_name", "subject__name"]
    ordering_fields = ["created_at", "value"]