from rest_framework import generics
from ..serializers import reference
from ...models import (
    Nationality,
    NativeLanguage,
    Citizenship,
    TrainingDirection,
)


class TrainingDirectionList(generics.ListCreateAPIView):
    """
    Список национальностей
    """

    queryset = TrainingDirection.objects.all()
    serializer_class = reference.TrainingDirectionSerializer

    def perform_create(self, serializer):
        return serializer.save()


class TrainingDirectionDetail(generics.RetrieveUpdateAPIView):
    """
    Подробная информация о национальности
    """

    queryset = TrainingDirection.objects.all()
    serializer_class = reference.TrainingDirectionSerializer


class NationalityList(generics.ListCreateAPIView):
    """
    Список национальностей
    """

    queryset = Nationality.objects.all()
    serializer_class = reference.NationalitySerializer

    def perform_create(self, serializer):
        return serializer.save()


class NationalityDetail(generics.RetrieveUpdateAPIView):
    """
    Подробная информация о национальности
    """

    queryset = Nationality.objects.all()
    serializer_class = reference.NationalitySerializer


class NativeLanguageList(generics.ListCreateAPIView):
    """
    Список языков
    """

    queryset = NativeLanguage.objects.all()
    serializer_class = reference.NativeLanguageSerializer

    def perform_create(self, serializer):
        return serializer.save()


class NativeLanguageDetail(generics.RetrieveUpdateAPIView):
    """
    Подробная информация о языках
    """

    queryset = NativeLanguage.objects.all()
    serializer_class = reference.NativeLanguageSerializer


class CitizenshipList(generics.ListCreateAPIView):
    """
    Список языков
    """

    queryset = Citizenship.objects.all()
    serializer_class = reference.CitizenshipSerializer

    def perform_create(self, serializer):
        return serializer.save()


class CitizenshipDetail(generics.RetrieveUpdateAPIView):
    """
    Подробная информация о языках
    """

    queryset = Citizenship.objects.all()
    serializer_class = reference.CitizenshipSerializer
