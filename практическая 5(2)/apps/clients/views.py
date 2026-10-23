from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """CRUD для студентов."""
    queryset = Student.objects.select_related("group").all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["full_name", "phone"]
    ordering_fields = ["full_name"]