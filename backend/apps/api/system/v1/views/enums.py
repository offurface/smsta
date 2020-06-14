from rest_framework.views import APIView
from rest_framework.response import Response
from apps.api.other.utils import ChoiceToDictConvertor as converter
from ..serializers import enums
from ...models import (
    FORM_TRAINING,
    PAYMENT_TRAINING,
    TYPE_TRAINING,
    ACTIVE_GROUP,
    DISABILITY_GROUP,
    GENDERS,
)


class BaseChoiceView(APIView):
    """
    Базовый класс для api choices
    """

    objects = None

    def get(self, request):
        objetcs = list(converter.convert(self.objects))
        serializer = enums.ChoiceSerializer(objetcs, many=True)
        return Response(serializer.data)


class FormTrainingListView(BaseChoiceView):
    """
    Форма обучения
    """

    objects = FORM_TRAINING


class PaymentTrainingListView(BaseChoiceView):
    """
    Способ финансирования
    """

    objects = PAYMENT_TRAINING


class TypeTrainingListView(BaseChoiceView):
    """
    Сокращенная
    """

    objects = TYPE_TRAINING


class ActiveGroupListView(BaseChoiceView):
    """
    Актив группы
    """

    objects = ACTIVE_GROUP


class DisabilityGroupListView(BaseChoiceView):
    """
    Группы инвалидности
    """

    objects = DISABILITY_GROUP


class GenderListView(BaseChoiceView):
    """
    Пол
    """

    objects = GENDERS
