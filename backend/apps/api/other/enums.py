"""Перечисления"""
from enum import Enum, unique
from django.utils.translation import gettext_lazy as _
from etc.choices import ChoicesEnumMixin, get_choices


# @unique
# class DisabilityGroup(ChoicesEnumMixin, Enum):
#     """
#     Роль
#     """

#     FIRST = 1, _("Тютор")
#     SECOND = 2, _("2 группа")


@unique
class Gender(ChoicesEnumMixin, Enum):
    """
    Пол
    """

    FEMALE = 1, _("Женский")
    MALE = 2, _("Мужской")


@unique
class FormTraining(ChoicesEnumMixin, Enum):
    """
    Форма обучения
    """

    INTRAMURAL = 1, _("Очная")
    EXTRAMURAL = 2, _("Заочная")


@unique
class DisabilityGroup(ChoicesEnumMixin, Enum):
    """
    Группы инвалидности
    """

    FIRST = 1, _("1 группа")
    SECOND = 2, _("2 группа")
    THIRD = 3, _("3 группа")


DISABILITY_GROUP = get_choices(DisabilityGroup)
FORM_TRAINING = get_choices(FormTraining)
GENDERS = get_choices(Gender)
