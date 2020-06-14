from rest_framework import serializers
from ... import models


class AcademicGroupsSerializers(serializers.ModelSerializer):
    """
    Сериализатор Академических Групп
    """

    class Meta:
        model = models.AcademicGroup
        fields = ["pk", "start_date", "department", "name"]


class StudentDetailSerializers(serializers.ModelSerializer):
    """
    Сериализатор студентов
    """

    academic_group = AcademicGroupsSerializers

    class Meta:
        model = models.Student
        fields = "__all__"
