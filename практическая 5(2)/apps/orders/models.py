from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.catalog.models import Group, Subject
from apps.clients.models import Student

class Grade(models.Model):
    """Оценка в электронном журнале."""

    class GradeType(models.TextChoices):
        TEST = "test", "Тест"
        PRACTICE = "practice", "Практика"
        PROJECT = "project", "Проект"

    class Status(models.TextChoices):
        NEW = "new", "Новая"
        CONFIRMED = "confirmed", "Подтверждена"

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name="grades", verbose_name="Студент",
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name="grades", verbose_name="Предмет",
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="given_grades", verbose_name="Преподаватель",
    )
    grade_type = models.CharField("Тип работы", max_length=20, choices=GradeType.choices)
    value = models.PositiveIntegerField("Оценка (баллы)", default=0)
    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.NEW)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата выставления", auto_now_add=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки (Журнал)"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name}: {self.value}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)