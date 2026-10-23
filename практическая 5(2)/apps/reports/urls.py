from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("kpi/", views.KPIApiView.as_view(), name="kpi"),
    path("top-students/", views.TopStudentsApiView.as_view(), name="top_students"),
    path("subject-stats/", views.SubjectStatsApiView.as_view(), name="subject_stats"),
]