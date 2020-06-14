from rest_framework import generics
from ..serializers import groups
from ... import models


class AcademicGroupList(generics.ListAPIView):
    """
    Список академических групп
    """

    queryset = models.AcademicGroup.objects.all()
    serializer_class = groups.AcademicGroupsDetailSerializers

    def get_queryset(self):
        user = self.request.user
        if user.role == 1:
            return models.AcademicGroup.objects.filter(tutor_id=user.pk)
        else:
            return models.AcademicGroup.objects.all()


class AcademicGroupDetail(generics.RetrieveAPIView):
    """
    Подробная информация об академической группе
    """

    queryset = models.AcademicGroup.objects.all()
    serializer_class = groups.AcademicGroupsDetailSerializers
