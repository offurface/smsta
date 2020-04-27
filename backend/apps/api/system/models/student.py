from django.db import models
from django.utils.translation import gettext_lazy as _
from .university import AcademicGroup
from .other import Hostel, Citizenship, Nationality, NativeLanguage
from .enums import (
    GENDERS,
    DISABILITY_GROUP,
    PAYMENT_TRAINING,
)


class Student(models.Model):
    """
    Студент (абстрактный класс)
    """

    academic_group = models.ForeignKey(
        AcademicGroup,
        on_delete=models.SET_NULL,
        verbose_name="Группа",
        blank=True,
        null=True,
        related_name="students",
    )
    citizenship = models.ForeignKey(
        Citizenship,
        on_delete=models.SET_NULL,
        verbose_name=_("Гражданство"),
        blank=True,
        null=True,
    )
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.SET_NULL,
        verbose_name=_("Национальность"),
        blank=True,
        null=True,
    )
    native_language = models.ForeignKey(
        NativeLanguage,
        on_delete=models.SET_NULL,
        verbose_name=_("Родной язык"),
        blank=True,
        null=True,
    )
    name = models.CharField(verbose_name=_("Имя"), max_length=30)
    surname = models.CharField(verbose_name=_("Фамилия"), max_length=150)
    patronymic = models.CharField(
        verbose_name=_("Отчество"), max_length=150, default=""
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
    payment_training = models.IntegerField(
        choices=PAYMENT_TRAINING,
        verbose_name=_("Способ финансирования"),
        default=0,
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

    @property
    def full_name(self):
        """
        Возвращает ФИО полностью
        """
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    @property
    def initials_name(self):
        """
        Возвращает фамилию и инициалы
        """
        return "%s %s. %s." % (
            self.surname,
            self.name[:1],
            self.patronymic[:1],
        )

    def __str__(self):
        return self.surname + " " + self.name

    class Meta:
        # abstract = True
        verbose_name = _("Студент")
        verbose_name_plural = _("Студенты")


# class Student(AbstractStudent):
#     """
#     Студент
#     """

#     class Meta:
#         verbose_name = _("Студент")
#         verbose_name_plural = _("Студенты")


# class StudentArchive(AbstractStudent):
#     """
#     Студент (Архив)
#     """

#     date_archiving = models.DateTimeField(
#         verbose_name=_("Дата архивирования"), auto_now_add=True, blank=True
#     )

#     class Meta:
#         verbose_name = _("Студент (Архив)")
#         verbose_name_plural = _("Студент (Архив)")


class Parent(models.Model):
    """
    Родитель
    """

    kid = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        verbose_name=_("Ребёнок"),
        blank=True,
        null=True,
    )
    name = models.CharField(verbose_name=_("ФИО"), max_length=255)
    work = models.CharField(
        verbose_name=_("Место работы, должность"), max_length=255
    )
    phone = models.CharField(verbose_name=_("Телефон"), max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Родитель")
        verbose_name_plural = _("Родители")


class ResidenceHostel(models.Model):
    """
    Проживающие в общежитии студенты
    """

    student = models.ForeignKey(
        Student,
        verbose_name=_("Студент"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    hostel = models.ForeignKey(
        Hostel,
        verbose_name=_("Общежитие"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    room = models.IntegerField(
        verbose_name=_("Номер комнаты"), blank=True, null=True
    )
    is_family = models.BooleanField(
        default=False, verbose_name=_("Семейная комната"),
    )

    def __str__(self):
        return self.student

    class Meta:
        verbose_name = _("Проживающий в общежитии")
        verbose_name_plural = _("Проживающие в общежитии")
