from django.db import models
from django.contrib.auth import get_user_model


class Faculty(models.Model):
    """
    Факультет
    """

    short_name = models.CharField(
        max_length=100, verbose_name="Сокращенное наименование"
    )
    full_name = models.CharField(
        max_length=255, verbose_name="Полное наименование"
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"


class Department(models.Model):
    """
    Кафедра
    """

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        verbose_name="Факультет",
        blank=True,
        null=True,
    )
    short_name = models.CharField(
        max_length=100, verbose_name="Сокращенное наименование"
    )
    full_name = models.CharField(
        max_length=255, verbose_name="Полное наименование"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"


class AcademicGroup(models.Model):
    """
    Группа
    """

    tutor = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name="Тьютор",
        blank=True,
        null=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name="Кафедра",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255, verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Академическая группа"
        verbose_name_plural = "Академические группы"


class Student(models.Model):
    """
    Студент
    """

    academic_group = models.ForeignKey(
        AcademicGroup,
        on_delete=models.SET_NULL,
        verbose_name="Группа",
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        verbose_name="Имя", max_length=30, blank=True,
    )
    last_name = models.CharField(
        verbose_name="Фамилия", max_length=150, blank=True
    )
    patronymic = models.CharField(
        verbose_name="Отчество", max_length=150, blank=True,
    )

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
