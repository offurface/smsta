from rest_framework import serializers
from .. import models


class GroupsSerializers(serializers.ModelSerializer):
    """
    Сериализатор Академических Групп
    """

    class Meta:
        model = models.AcademicGroup
        fields = ["id", "start_date", "department"]


# Create your serializers here.
