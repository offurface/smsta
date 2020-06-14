from rest_framework import serializers
from ...models import (
    Nationality,
    NativeLanguage,
    Citizenship,
    TrainingDirection,
)


class TrainingDirectionSerializer(serializers.ModelSerializer):
    """
    Сериализатор напрвлений обучения
    """

    class Meta:
        model = TrainingDirection
        fields = "__all__"


class CitizenshipSerializer(serializers.ModelSerializer):
    """
    Сериализатор гражданств
    """

    class Meta:
        model = Citizenship
        fields = "__all__"


class NationalitySerializer(serializers.ModelSerializer):
    """
    Сериализатор национальностей
    """

    class Meta:
        model = Nationality
        fields = "__all__"


class NativeLanguageSerializer(serializers.ModelSerializer):
    """
    Сериализатор языков
    """

    class Meta:
        model = NativeLanguage
        fields = "__all__"
