from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["employe_position"] = user.employe_position
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["patronymic"] = user.patronymic
        token["role"] = user.role
        token["phone"] = user.phone
        token["email"] = user.email
        token["isSuperUser"] = user.is_superuser
        token["isStaff"] = user.is_staff

        return token
