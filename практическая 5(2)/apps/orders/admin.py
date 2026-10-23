from django.contrib import admin
from .models import Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "subject", "grade_type", "value", "status", "created_at")
    list_filter = ("status", "grade_type", "subject", "created_at")
    search_fields = ("student__full_name", "subject__name")
    readonly_fields = ("created_at",)