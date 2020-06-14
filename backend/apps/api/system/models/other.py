from django.db import models
from django.utils.translation import gettext_lazy as _


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


class Citizenship(models.Model):
    """
    Гражданство
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Гражданство")
        verbose_name_plural = _("Гражданства")


class Nationality(models.Model):
    """
    Национальность
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Национальность")
        verbose_name_plural = _("Национальности")


class NativeLanguage(models.Model):
    """
    Родной язык
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Родной язык")
        verbose_name_plural = _("Родные языки")
