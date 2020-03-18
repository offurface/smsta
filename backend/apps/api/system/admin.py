from django.contrib.admin import register, ModelAdmin, TabularInline
from apps.core.utils.admin import BaseAdminMixin

from .models import Student, Parent, Faculty, Department, AcademicGroup


class ParentInline(TabularInline):
    model = Parent
    extra = 0


@register(Student)
class StudentAdmin(BaseAdminMixin, ModelAdmin):
    list_display = (
        "surname",
        "name",
        "patronymic",
        "series",
        "number",
        "gender",
    )

    inlines = [
        ParentInline,
    ]


class DepartmentInline(TabularInline):
    """
    Инлайновая регистрация кафедры
    """

    model = Department
    extra = 0


@register(Faculty)
class FacultyAdmin(BaseAdminMixin, ModelAdmin):
    """
    Админка факультета
    """

    list_display = (
        "public_id",
        "short_name",
        "full_name",
    )

    inlines = [
        DepartmentInline,
    ]


@register(AcademicGroup)
class FacultyAdmin(BaseAdminMixin, ModelAdmin):
    list_display = ("name",)

