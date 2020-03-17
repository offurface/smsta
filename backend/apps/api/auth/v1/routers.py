from django.urls import path

from rest_framework_simplejwt.views import (
    TokenCookieDeleteView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import TokenObtainPairView

app_name = "auth"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("delete/", TokenCookieDeleteView.as_view(), name="token_delete"),
]
