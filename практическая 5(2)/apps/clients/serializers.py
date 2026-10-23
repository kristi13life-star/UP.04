from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source="group.name", read_only=True)

    class Meta:
        model = Student
        fields = ["id", "full_name", "group", "group_name", "phone", "email"]