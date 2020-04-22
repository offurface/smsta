from rest_framework import serializers
from .. import models


class DepartmentSerializers(serializers.ModelSerializer):
    """
    Сериализатор кафедр
    """

    class Meta:
        model = models.Department
        fields = ["short_name", "full_name"]


class StudentSerializers(serializers.ModelSerializer):
    """
    Сериализатор студентов
    """

    class Meta:
        model = models.Student
        fields = ["name", "surname", "patronymic", "gender"]


class AcademicGroupsDetailSerializers(serializers.ModelSerializer):
    """
    Сериализатор Академических Групп
    """

    department = DepartmentSerializers()
    students = StudentSerializers(many=True, read_only=True)

    class Meta:
        model = models.AcademicGroup
        fields = ["pk", "start_date", "department", "name", "students"]


class AcademicGroupsSerializers(serializers.ModelSerializer):
    """
    Сериализатор Академических Групп
    """

    class Meta:
        model = models.AcademicGroup
        fields = ["pk", "start_date", "department", "name"]
