from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.api.other.enums import GENDERS, FORM_TRAINING, DISABILITY_GROUP


class Faculty(models.Model):
    """
    Факультет
    """

    short_name = models.CharField(
        max_length=100, verbose_name=_("Сокращенное наименование")
    )
    full_name = models.CharField(
        max_length=255, verbose_name=_("Полное наименование")
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
    is_correspondence = models.BooleanField(
        default=False, verbose_name=_("Это заочная группа?")
    )
    is_abbreviated = models.BooleanField(
        default=False, verbose_name=_("Это сокращенная группа?")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Академическая группа"
        verbose_name_plural = "Академические группы"


class Student(models.Model):
    """
    Студент
    """

    # TODO: Добавить поля и справочники -
    # Citizenship(Гражданство),
    # Nationality(Национальность),
    # Native language(Родной язык)
    academic_group = models.ForeignKey(
        AcademicGroup, on_delete=models.SET_NULL, verbose_name="Группа"
    )
    first_name = models.CharField(verbose_name=_("Имя"), max_length=30)
    last_name = models.CharField(verbose_name=_("Фамилия"), max_length=150)
    patronymic = models.CharField(
        verbose_name=_("Отчество"), max_length=150, blank=True, null=True
    )
    gender = models.IntegerField(choices=GENDERS, verbose_name=_("Пол"))
    birth_place = models.CharField(
        verbose_name=_("Место рождения"), max_length=255
    )
    address = models.CharField(
        verbose_name=_("Адрес по прописке"), max_length=255
    )
    address_fact = models.CharField(
        verbose_name=_("Адрес фактический"), max_length=255
    )
    series = models.IntegerField(verbose_name=_("Серия пасспорта"))
    number = models.IntegerField(verbose_name=_("Номер пасспорта"))
    form_training = models.IntegerField(
        choices=FORM_TRAINING, verbose_name=_("Форма обучения")
    )
    disability_group = models.IntegerField(
        choices=DISABILITY_GROUP,
        verbose_name=_("Форма инвалидности"),
        blank=True,
        null=True,
    )

    is_orphan = models.BooleanField(
        default=False,
        verbose_name=_(
            "Студенты-сироты и студенты, оставшихся без попечения родителей"
        ),
    )
    is_military = models.BooleanField(
        default=False,
        verbose_name=_("Студенты-ветераны и инвалиды боевых действий"),
    )
    is_radioactive = models.BooleanField(
        default=False,
        verbose_name=_(
            "Студенты из районов, подвергшихся радиоактивному заражению"
        ),
    )
    is_parents_retired = models.BooleanField(
        default=False,
        verbose_name=_("Студенты, у которых оба родителя пенсионеры"),
    )
    is_parents_disabilities = models.BooleanField(
        default=False,
        verbose_name=_("Студенты, у которых родители - инвалиды"),
    )
    is_many_kids_family = models.BooleanField(
        default=False, verbose_name=_("Студенты из многодетных семей")
    )
    is_from_broken_home = models.BooleanField(
        default=False, verbose_name=_("Студенты из неполных семей")
    )
    is_poor = models.BooleanField(
        default=False, verbose_name=_("Относится к категории малообеспеченных")
    )
    is_chronic_disease = models.BooleanField(
        default=False,
        verbose_name=_("Студенты, страдающих хроническими заболеваниями"),
    )
    is_wed = models.BooleanField(
        default=False, verbose_name=_("Студенты, состоящие в браке")
    )
    is_status_student_family = models.BooleanField(
        default=False, verbose_name=_("Имеют статус 'студенческая семья'")
    )
    is_have_kids = models.BooleanField(
        default=False, verbose_name=_("Студенты, имеющие детей")
    )
    is_unwed_mother = models.BooleanField(
        default=False, verbose_name=_("В том числе матери-одиночки")
    )
    is_south_east_ukraine = models.BooleanField(
        default=False,
        verbose_name=_(
            "Студенты, прибывшие на обучение из Юго-востока Украины"
        ),
    )
    # TODO: Добавить поля
    # Студенты, проживающих в общежитии:
    #     из них:
    #     бюджетная ф.о.
    #     контрактная ф.о.
    #     семейные

    # variables = models.BooleanField(default=False, verbose_name=_(""))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
