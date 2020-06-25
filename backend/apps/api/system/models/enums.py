"""Перечисления"""
from enum import Enum, unique
from django.utils.translation import gettext_lazy as _
from etc.choices import ChoicesEnumMixin, get_choices


@unique
class Gender(ChoicesEnumMixin, Enum):
    """
    Пол
    """

    FEMALE = 1, _("Женский")
    MALE = 2, _("Мужской")


@unique
class DisabilityGroup(ChoicesEnumMixin, Enum):
    """
    Группы инвалидности
    """

    NONE = 0, _("Отсутствует")
    FIRST = 1, _("1 группа")
    SECOND = 2, _("2 группа")
    THIRD = 3, _("3 группа")


@unique
class ActiveGroup(ChoicesEnumMixin, Enum):
    """
    Актив группы
    """

    NONE = 0, _("Отсутствует")
    FIRST = 1, _("Староста")
    SECOND = 2, _("Профгруппорг")


@unique
class Semesters(ChoicesEnumMixin, Enum):
    """
    Семестры
    """

    FIRST = 1, _("I")
    SECOND = 2, _("II")


@unique
class FormTraining(ChoicesEnumMixin, Enum):
    """
    Форма обучения
    """

    INTRAMURAL = 1, _("Очное")
    EXTRAMURAL = 2, _("Заочное")
    INTRAMURAL_EXTRAMURAL = 3, _("Очно-заочное")


@unique
class PaymentTraining(ChoicesEnumMixin, Enum):
    """
    Способ финансирования
    """

    BUDGETARY = 1, _("Бюджетная")
    COMMERCIAL = 2, _("Комерческая")


@unique
class TypeTraining(ChoicesEnumMixin, Enum):
    """
    Форма обучения
    """

    UNABRIDGED = 1, _("Не сокращенная")
    ABRIDGED = 2, _("Сокращенная")


FORM_TRAINING = get_choices(FormTraining)
PAYMENT_TRAINING = get_choices(PaymentTraining)
TYPE_TRAINING = get_choices(TypeTraining)
SEMESTERS = get_choices(Semesters)
ACTIVE_GROUP = get_choices(ActiveGroup)
DISABILITY_GROUP = get_choices(DisabilityGroup)
GENDERS = get_choices(Gender)
