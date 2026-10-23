from django.db import models

class Group(models.Model):
    """Учебная группа."""
    name = models.CharField("Название группы", max_length=50, unique=True)
    course = models.PositiveIntegerField("Курс", default=1)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Subject(models.Model):
    """Учебный предмет."""
    name = models.CharField("Название предмета", max_length=100)
    teacher = models.ForeignKey(
    'accounts.User', on_delete=models.PROTECT,  
    related_name="subjects", verbose_name="Преподаватель"
)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ["name"]

    def __str__(self):
        return self.name