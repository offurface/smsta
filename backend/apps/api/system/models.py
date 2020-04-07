from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.api.other.enums import (
    GENDERS,
    FORM_TRAINING,
    DISABILITY_GROUP,
    PAYMENT_TRAINING,
    FORM_TRAINING,
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
        return self.full_name

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

    @property
    def name(self):
        """
        Возвращает название группы
        TODO: Написать свойство возвращающее названия группы
        """
        numbers = ""
        letters = ""
        if self.type_training != TypeTraining.UNABRIDGED:
            letters += "S"
        # ПИZS-341
        return letters + "-" + numbers

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Академическая группа")
        verbose_name_plural = _("Академические группы")


class Student(models.Model):
    """
    Студент
    """

    # TODO: Добавить поля и справочники -
    # Citizenship(Гражданство),
    # Nationality(Национальность),
    # Native language(Родной язык)
    academic_group = models.ForeignKey(
        AcademicGroup,
        on_delete=models.SET_NULL,
        verbose_name="Группа",
        blank=True,
        null=True,
    )
    name = models.CharField(verbose_name=_("Имя"), max_length=30)
    surname = models.CharField(verbose_name=_("Фамилия"), max_length=150)
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
        choices=PAYMENT_TRAINING, verbose_name=_("Форма обучения")
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

    def __str__(self):
        return self.surname + " " + self.name

    class Meta:
        verbose_name = _("Студент")
        verbose_name_plural = _("Студенты")


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


class Hostel(models.Model):
    """
    Общежитие
    """

    name = models.CharField(verbose_name=_("Название"), max_length=255)
    address = models.CharField(verbose_name=_("Адрес"), max_length=255)
    phone = models.CharField(verbose_name=_("Телефон"), max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Общежитие")
        verbose_name_plural = _("Общежития")


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


class VisitHostel(models.Model):
    """
    Журнал посещения общежития
    """

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

    date_time = models.DateTimeField(verbose_name=_("Дата и время проведения"))
    room = models.CharField(verbose_name=_("Аудитория"), max_length=9)
    title = models.CharField(verbose_name=_("Тема"), max_length=255)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = _("Журнал кураторского часа")
        verbose_name_plural = _("Журнал кураторского часа")
