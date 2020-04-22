from rest_framework import views
from rest_framework import generics
from . import serializers
from .. import models
from rest_framework.generics import get_object_or_404


class AcademicGroupList(generics.ListAPIView):
    """
    Список академических групп
    """

    queryset = models.AcademicGroup.objects.all()
    serializer_class = serializers.AcademicGroupsSerializers

    def get_queryset(self):
        user = self.request.user
        return models.AcademicGroup.objects.filter()


class AcademicGroupDetail(generics.RetrieveAPIView):
    """
    Аадемических групп
    """

    queryset = models.AcademicGroup.objects.all()
    serializer_class = serializers.AcademicGroupsDetailSerializers
