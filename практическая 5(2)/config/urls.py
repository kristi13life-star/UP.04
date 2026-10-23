from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/catalog/", include("apps.catalog.urls")),
    path("api/students/", include("apps.clients.urls")),
    path("api/grades/", include("apps.orders.urls")),
    path("api/reports/", include("apps.reports.urls")),
]