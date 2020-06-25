from datetime import datetime
from django.db import models
from django.utils import dateformat
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .enums import (
    FORM_TRAINING,
    FormTraining,
    TYPE_TRAINING,
    TypeTraining,
)
import math


class TrainingDirection(models.Model):
    """
    Направление Обучения
    """

    letters = models.CharField(verbose_name=_("Символы"), max_length=25)
    code = models.CharField(verbose_name=_("Код"), max_length=25)
    name = models.CharField(verbose_name=_("Направление"), max_length=255)
    target = models.CharField(verbose_name=_("Профиль"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Направление")
        verbose_name_plural = _("Направления")


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
    training_direction = models.ForeignKey(
        TrainingDirection,
        on_delete=models.SET_NULL,
        verbose_name=_("Направление"),
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

    @property
    def start_date_ru(self):
        return dateformat.format(self.start_date, ("d E Y"))

    @property
    def name(self):
        """
        Возвращает название группы
        """
        numbers = ""
        letters = self.training_direction.letters
        # letters = ""
        if self.payment_training == FormTraining.EXTRAMURAL.value:
            letters += "Z"
        if self.payment_training == FormTraining.INTRAMURAL_EXTRAMURAL.value:
            letters += "OZ"
        if self.type_training == TypeTraining.ABRIDGED.value:
            letters += "S"
        numbers += str(self.department.faculty.public_id)
        subtr_date = datetime.now().date() - self.start_date
        year = subtr_date.days / 365
        if year < 1:
            numbers += "1"
        elif year < 2:
            numbers += "2"
        elif year < 3:
            numbers += "3"
        else:
            numbers += "4"
        return letters + "-" + numbers + "1"

    @property
    def course(self):
        subtr_date = datetime.now().date() - self.start_date
        year = subtr_date.days / 365
        course = math.ceil(year)
        if course < 5:
            return course
        else:
            return 5

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Академическая группа")
        verbose_name_plural = _("Академические группы")
