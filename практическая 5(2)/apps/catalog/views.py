from rest_framework import viewsets, filters
from .models import Group, Subject
from .serializers import GroupSerializer, SubjectSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ["name"]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    search_fields = ["name"]