from rest_framework.views import APIView
from rest_framework.response import Response
from .services import ReportService

class KPIApiView(APIView):
    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.kpi(days))

class TopStudentsApiView(APIView):
    def get(self, request):
        limit = int(request.GET.get("limit", 5))
        return Response(ReportService.top_students(limit))

class SubjectStatsApiView(APIView):
    def get(self, request):
        return Response(ReportService.subject_stats())