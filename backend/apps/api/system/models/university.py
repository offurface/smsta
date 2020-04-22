from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .enums import (
    FORM_TRAINING,
    FormTraining,
    TYPE_TRAINING,
    TypeTraining,
)


class Faculty(models.Model):
    """
    Факультет
    """

    public_id = models.IntegerField(
        verbose_name=_("Цифра факультета"), blank=True, null=True
    )
    short_name = models.CharField(
        max_length=100, verbose_name=_("Сокращенное наименование")
    )
    full_name = models.CharField(
        max_length=255, verbose_name=_("Полное наименование")
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("Факультет")
        verbose_name_plural = _("Факультеты")


class Department(models.Model):
    """
    Кафедра
    """

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        verbose_name=_("Факультет"),
        blank=True,
        null=True,
    )
    short_name = models.CharField(
        max_length=100, verbose_name=_("Сокращенное наименование")
    )
    full_name = models.CharField(
        max_length=255, verbose_name=_("Полное наименование")
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("Кафедра")
        verbose_name_plural = _("Кафедры")


class AcademicGroup(models.Model):
    """
    Группа
    """

    start_date = models.DateField(
        verbose_name="Дата начала обучения", blank=True, null=True,
    )
    tutor = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        verbose_name=_("Тьютор"),
        blank=True,
        null=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name=_("Кафедра"),
        blank=True,
        null=True,
    )
    payment_training = models.IntegerField(
        choices=FORM_TRAINING, verbose_name=_("Форма обучения"), default=1
    )
    type_training = models.IntegerField(
        choices=TYPE_TRAINING,
        verbose_name=_("Не сокращенная/Сокращенная"),
        default=1,
    )
    subgroup_number = models.IntegerField(
        verbose_name=_("Номер подгруппы"), default=1,
    )
    letters = models.CharField(
        max_length=6,
        verbose_name=_("Сокращенное наименование группы"),
        default="",
    )

    @property
    def name(self):
        """
        Возвращает название группы
        TODO: Написать свойство возвращающее названия группы
        """
        numbers = ""
        letters = self.letters
        if self.payment_training == FormTraining.EXTRAMURAL.value:
            letters += "Z"
        if self.payment_training == FormTraining.INTRAMURAL_EXTRAMURAL.value:
            letters += "OZ"
        if self.type_training == TypeTraining.ABRIDGED.value:
            letters += "S"
        return letters + "-" + numbers

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Академическая группа")
        verbose_name_plural = _("Академические группы")
