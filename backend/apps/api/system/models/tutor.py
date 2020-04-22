from django.db import models
from django.utils.translation import gettext_lazy as _
from .student import Student, AcademicGroup
from .other import Hostel


class VisitHostel(models.Model):
    """
    Журнал посещения общежития
    """

    group = models.ForeignKey(
        AcademicGroup,
        verbose_name=_("Группа"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    date = models.DateField(verbose_name=_("Дата посещения"))
    start_time = models.TimeField(verbose_name=_("Время прихода"))
    end_time = models.TimeField(verbose_name=_("Время ухода"))
    hostel = models.ForeignKey(
        Hostel,
        verbose_name=_("Общежитие"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    students = models.TextField(
        verbose_name=_("ФИО Студентов"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Заметки"), blank=True, null=True
    )

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Журнал посещения общежития")
        verbose_name_plural = _("Журнал посещения общежития")


class СuratorHour(models.Model):
    """
    Журнал кураторского часа
    """

    group = models.ForeignKey(
        AcademicGroup,
        verbose_name=_("Группа"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    date_time = models.DateTimeField(verbose_name=_("Дата и время проведения"))
    room = models.CharField(
        verbose_name=_("Аудитория"), max_length=9, blank=True, null=True
    )
    title = models.CharField(verbose_name=_("Тема"), max_length=255)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Журнал кураторского часа")
        verbose_name_plural = _("Журнал кураторского часа")


class IndividualWorkWithStudents(models.Model):
    """
    Индивидуальная работа со студентами
    """

    group = models.ForeignKey(
        AcademicGroup,
        verbose_name=_("Группа"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    student = models.ForeignKey(
        Student,
        verbose_name=_("Общежитие"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    problem = models.CharField(verbose_name=_("Проблема"), max_length=255)
    solution = models.CharField(verbose_name=_("Решение"), max_length=255)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Индивидуальная работа со студентами")
        verbose_name_plural = _("Индивидуальные работы со студентами")
