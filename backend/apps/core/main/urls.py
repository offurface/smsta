from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("api/", include("apps.core.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    re_path("", views.AppView.as_view(), name="app"),
]
