from django.db.models import Avg, Count
from django.utils import timezone
from datetime import timedelta
from apps.orders.models import Grade
from apps.clients.models import Student

class ReportService:
    """Сервис отчётов по журналу."""

    @staticmethod
    def kpi(days: int = 30) -> dict:
        """Главные KPI."""
        since = timezone.now() - timedelta(days=days)
        grades = Grade.objects.filter(created_at__gte=since)
        
        avg_grade = grades.aggregate(avg=Avg("value"))["avg"] or 0
        total_grades = grades.count()
        
        return {
            "avg_grade": round(float(avg_grade), 2),
            "total_grades": total_grades,
            "students_count": Student.objects.count(),
            "period_days": days,
        }

    @staticmethod
    def top_students(limit: int = 5) -> list:
        """Топ студентов по среднему баллу."""
        rows = (
            Student.objects.annotate(avg_score=Avg("grades__value"))
            .filter(avg_score__isnull=False)
            .order_by("-avg_score")[:limit]
        )
        return [
            {"name": r.full_name, "group": r.group.name, "avg_score": round(float(r.avg_score), 2)}
            for r in rows
        ]

    @staticmethod
    def subject_stats() -> list:
        """Статистика по предметам."""
        rows = (
            Grade.objects.values("subject__name")
            .annotate(avg_score=Avg("value"), count=Count("id"))
            .order_by("-avg_score")
        )
        return [
            {"subject": r["subject__name"], "avg_score": round(float(r["avg_score"]), 2), "count": r["count"]}
            for r in rows
        ]