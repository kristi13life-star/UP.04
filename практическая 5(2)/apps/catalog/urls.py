from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, SubjectViewSet

router = DefaultRouter()
router.register("groups", GroupViewSet, basename="groups")
router.register("subjects", SubjectViewSet, basename="subjects")

urlpatterns = [
    path("", include(router.urls)),
]