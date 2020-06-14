from rest_framework import generics
from ..serializers import students
from ... import models


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Подробная информация о студенте
    """

    queryset = models.Student.objects.all()
    serializer_class = students.StudentDetailSerializers
