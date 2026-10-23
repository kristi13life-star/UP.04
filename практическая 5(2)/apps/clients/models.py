from django.db import models

class Student(models.Model):
    """Студент."""
    full_name = models.CharField("ФИО", max_length=100)
    group = models.ForeignKey(
        'catalog.Group', on_delete=models.CASCADE,
        related_name="students", verbose_name="Группа"
    )
    phone = models.CharField("Телефон", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.group.name})"